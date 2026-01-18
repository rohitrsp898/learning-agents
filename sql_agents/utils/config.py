from pathlib import Path
from dotenv import load_dotenv

def load_environment():
    # Attempt to find .env file in project root (sql_agents) or parent
    # Current file is in sql_agents/utils/
    project_root = Path(__file__).parent.parent
    
    env_path = project_root / '.env'
    if not env_path.exists():
        env_path = project_root.parent / '.env'
        
    load_dotenv(dotenv_path=env_path)
