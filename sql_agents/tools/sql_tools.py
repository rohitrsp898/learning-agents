from typing import List
from pydantic_ai import RunContext
from utils.database import DatabaseDeps
from loguru import logger as log


# USing existing context to extract table and schema information
async def list_tables(ctx: RunContext[DatabaseDeps]) -> List[str]:
    """
    List all public tables in the database from the cached schema.
    """
    tables = list(ctx.deps.schema_cache.keys())
    log.debug(f"Tool 'list_tables' called. Returning {len(tables)} tables")
    return tables

async def get_table_schema(ctx: RunContext[DatabaseDeps], table_name: str) -> str:
    """
    Get the schema (columns and types) for a specific table from the cache.
    
    Args:
        table_name: The name of the table to inspect.
    """
    log.debug(f"Tool 'get_table_schema' called for table: {table_name}")
    schema = ctx.deps.schema_cache.get(table_name, f"No table found named '{table_name}'")
    return schema

