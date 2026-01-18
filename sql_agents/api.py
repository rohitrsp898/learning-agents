from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import asyncpg
import os
from contextlib import asynccontextmanager
from typing import List, Dict, Any, Optional
import re

from utils.config import load_environment
from utils.database import DatabaseDeps, fetch_database_schema, execute_sql_query
from agent.sql_agent import sql_agent

load_environment()

# Global state for the app
class AppState:
    pool: asyncpg.Pool = None
    schema_cache: Dict[str, str] = {}

state = AppState()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup DONT USE THIS IN PRODUCTION
    # DB_DSN = "postgresql://root:root@localhost:5432/root"
    DB_DSN = "postgresql://postgres:root@localhost:5432/dvdrental"
    try:
        state.pool = await asyncpg.create_pool(DB_DSN)
        print("Connected to database.")
        state.schema_cache = await fetch_database_schema(state.pool)
        print("Schema fetched.")
    except Exception as e:
        print(f"Startup failed: {e}")
        
    yield
    
    # Shutdown
    if state.pool:
        await state.pool.close()
        print("Database connection closed.")

app = FastAPI(lifespan=lifespan)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    sql: Optional[str] = None
    data: Optional[List[Dict[str, Any]]] = None
    summary: str
    error: Optional[str] = None

def clean_sql(sql_text: str) -> str:
    """Clean markdown formatting from SQL"""
    cleaned = sql_text.strip()
    # Remove ```sql ... ``` or ``` ... ```
    cleaned = re.sub(r'```sql\s*', '', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'```\s*', '', cleaned)
    return cleaned.strip()

@app.post("/api/query", response_model=QueryResponse)
async def process_query(request: QueryRequest):
    if not state.pool:
         raise HTTPException(status_code=500, detail="Database not connected")

    # Create dependencies
    deps = DatabaseDeps(pool=state.pool, schema_cache=state.schema_cache)
    
    try:
        # Run the agent to generate SQL
        result = await sql_agent.run(request.query, deps=deps)
        generated_text = result.output
        
        # Check if it looks like an error
        if generated_text.startswith("ERROR:"):
             return QueryResponse(summary=generated_text)

        sql_query = clean_sql(generated_text)
        print(f"Agent generated SQL: {sql_query}")
        
        # Execute the SQL
        data = await execute_sql_query(state.pool, sql_query)
        # print(data)
        return QueryResponse(
            sql=sql_query,
            data=data,
            summary="Query executed successfully."
        )

    except Exception as e:
        print(f"Error processing query: {e}")
        return QueryResponse(
            summary="An error occurred while processing your request.",
            error=str(e)
        )

@app.get("/")
async def root():
    from fastapi.responses import FileResponse
    return FileResponse('static/index.html')



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
