import os
from pydantic_ai import Agent
from pydantic_ai.models.gemini import GeminiModel
from loguru import logger as log

from utils.database import DatabaseDeps
from prompts.system_prompts import SYSTEM_PROMPT
from tools.sql_tools import list_tables, get_table_schema
from utils.config import load_environment

# Ensure env vars are loaded
load_environment()

# Define the model
model_name = 'gemini-2.5-flash'
log.info(f"Initializing SQL agent with model: {model_name}")
model = GeminiModel(model_name)

sql_agent = Agent(
    model,
    system_prompt=SYSTEM_PROMPT,
    deps_type=DatabaseDeps,
    retries=3
)

# Register tools
log.info("Registering agent tools: list_tables, get_table_schema")
sql_agent.tool(list_tables)
sql_agent.tool(get_table_schema)
log.info("SQL agent initialized successfully")
# Agent no longer has execute_query tool
