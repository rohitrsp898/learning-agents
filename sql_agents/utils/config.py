from pathlib import Path
from dotenv import load_dotenv
from loguru import logger as log

def load_environment():
    # Attempt to find .env file in project root (sql_agents) or parent
    # Current file is in sql_agents/utils/
    project_root = Path(__file__).parent.parent
    
    env_path = project_root / '.env'
    if not env_path.exists():
        env_path = project_root.parent / '.env'
    
    if env_path.exists():
        load_dotenv(dotenv_path=env_path)
        log.info(f"Environment variables loaded from: {env_path}")
    else:
        log.warning("No .env file found. Environment variables may not be loaded")
