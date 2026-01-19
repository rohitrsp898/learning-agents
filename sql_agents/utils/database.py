from dataclasses import dataclass
from typing import List, Dict, Any
import asyncpg
from loguru import logger as log

@dataclass
class DatabaseDeps:
    pool: asyncpg.Pool
    schema_cache: Dict[str, str]

async def fetch_database_schema(pool: asyncpg.Pool) -> Dict[str, str]:
    """
    Fetches the schema for all public tables in the database.
    Returns a dictionary mapping table names to their schema strings.
    """
    log.info("Fetching database schema from information_schema...")
    schema_cache = {}
    
    # 1. List tables
    list_query = """
    SELECT table_name 
    FROM information_schema.tables 
    WHERE table_schema = 'public';
    """
    async with pool.acquire() as conn:
        records = await conn.fetch(list_query)
        table_names = [r['table_name'] for r in records]
        log.info(f"Found {len(table_names)} tables in public schema")
        
        # 2. Get schema for each table
        for table_name in table_names:
            log.debug(f"Fetching schema for table: {table_name}")
            schema_query = """
            SELECT column_name, data_type, is_nullable
            FROM information_schema.columns 
            WHERE table_name = $1 AND table_schema = 'public';
            """
            columns = await conn.fetch(schema_query, table_name)
            
            schema_info = f"Schema for table '{table_name}':\n"
            for r in columns:
                schema_info += f"- {r['column_name']} ({r['data_type']}), Nullable: {r['is_nullable']}\n"
            
            schema_cache[table_name] = schema_info
    
    log.info(f"Successfully cached schema for {len(schema_cache)} tables")        
    return schema_cache


async def execute_sql_query(pool: asyncpg.Pool, query: str) -> List[Dict[str, Any]]:
    """
    Executes a SQL query against the database and returns the results as a list of dictionaries.
    """
    if not query or query.strip() == "":
        log.warning("Attempted to execute empty query")
        return []
        
    log.debug(f"Executing SQL: {query}")
    try:
        async with pool.acquire() as conn:
            results = await conn.fetch(query)
            log.debug(f"Query returned {len(results)} rows")
            return [dict(r) for r in results]
    except Exception as e:
        log.error(f"Error executing query: {e}", exc_info=True)
        raise e

