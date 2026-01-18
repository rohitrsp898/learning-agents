from typing import List
from pydantic_ai import RunContext
from utils.database import DatabaseDeps


# USing existing context to extract table and schema information
async def list_tables(ctx: RunContext[DatabaseDeps]) -> List[str]:
    """
    List all public tables in the database from the cached schema.
    """
    return list(ctx.deps.schema_cache.keys())

async def get_table_schema(ctx: RunContext[DatabaseDeps], table_name: str) -> str:
    """
    Get the schema (columns and types) for a specific table from the cache.
    
    Args:
        table_name: The name of the table to inspect.
    """
    return ctx.deps.schema_cache.get(table_name, f"No table found named '{table_name}'")
