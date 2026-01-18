from dataclasses import dataclass
from typing import List, Dict, Any
import asyncpg

@dataclass
class DatabaseDeps:
    pool: asyncpg.Pool
    schema_cache: Dict[str, str]

async def fetch_database_schema(pool: asyncpg.Pool) -> Dict[str, str]:
    """
    Fetches the schema for all public tables in the database.
    Returns a dictionary mapping table names to their schema strings.
    """
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
        
        # 2. Get schema for each table
        for table_name in table_names:
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
            
    return schema_cache


async def execute_sql_query(pool: asyncpg.Pool, query: str) -> List[Dict[str, Any]]:
    """
    Executes a SQL query against the database and returns the results as a list of dictionaries.
    """
    if not query or query.strip() == "":
        return []
        
    print(f"DEBUG: Executing SQL: {query}")
    try:
        async with pool.acquire() as conn:
            results = await conn.fetch(query)
            return [dict(r) for r in results]
    except Exception as e:
        print(f"Error executing query: {e}")
        raise e

# Table details
# actor – stores actor data including first name and last name.
# film – stores film data such as title, release year, length, rating, etc.
# film_actor – stores the relationships between films and actors.
# category – stores film’s categories data.
# film_category- stores the relationships between films and categories.
# store – contains the store data including manager staff and address.
# inventory – stores inventory data.
# rental – stores rental data.
# payment – stores customer’s payments.
# staff – stores staff data.
# customer – stores customer data.
# address – stores address data for staff and customers
# city – stores city names.
# country – stores country names.