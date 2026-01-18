# SQL Agents - Natural Language to SQL Query System

A powerful AI-powered system that converts natural language queries into SQL and executes them against a PostgreSQL database. Built with Pydantic AI, FastAPI, and Google's Gemini model.

## 🌟 Features

- **Natural Language Processing**: Convert plain English questions into SQL queries
- **AI-Powered Agent**: Uses Google's Gemini 2.5 Flash model with Pydantic AI framework
- **Database Schema Understanding**: Automatically fetches and caches database schema for intelligent query generation
- **Web Interface**: Clean, interactive UI for querying your database
- **RESTful API**: FastAPI backend for programmatic access
- **PostgreSQL Integration**: Works with PostgreSQL databases (tested with DVD Rental sample database)
- **pgAdmin Support**: Includes pgAdmin for database management

## 🏗️ Architecture

The project is organized into a modular structure:

```
learning-agents/
├── sql_agents/
│   ├── agent/          # AI agent configuration
│   ├── prompts/        # System prompts for the agent
│   ├── tools/          # Agent tools (list_tables, get_table_schema)
│   ├── utils/          # Utilities (config, database operations)
│   ├── static/         # Frontend UI files
│   └── api.py          # FastAPI application
├── sample_data/        # DVD Rental sample database
├── docker-compose.yml  # PostgreSQL and pgAdmin setup
└── pyproject.toml      # Project dependencies
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- Docker and Docker Compose (for PostgreSQL)
- Google Gemini API key

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd learning-agents
   ```

2. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

3. **Install dependencies using uv**
   ```bash
   uv sync
   ```

4. **Start PostgreSQL and pgAdmin**
   ```bash
   docker-compose up -d
   ```

   This will start:
   - PostgreSQL on `localhost:5432`
     - Username: `root`
     - Password: `root`
     - Database: `root`
   - pgAdmin on `localhost:5050`
     - Email: `admin@admin.com`
     - Password: `root`

5. **Load sample data (optional)**
   
   The project includes the DVD Rental sample database in `sample_data/`. You can restore it using pgAdmin or `pg_restore`:
   ```bash
   pg_restore -U postgres -d dvdrental sample_data/dvdrental.tar
   ```

### Running the Application

Start the FastAPI server:
```bash
uv run uvicorn sql_agents.api:app --reload --host 0.0.0.0 --port 8000
```

Or run directly:
```bash
cd sql_agents   
uv run python api.py
```

The application will be available at:
- Web UI: http://localhost:8000
- API Docs: http://localhost:8000/docs

## 📖 Usage

### Web Interface

1. Open http://localhost:8000 in your browser
2. Type a natural language query (e.g., "Find all rentals made in the last 30 days.")
3. The AI agent will generate and execute the SQL query
4. View the results in a formatted table

### API Endpoint

**POST** `/api/query`

Request body:
```json
{
  "query": "Find the top 10 customers by total payment amount"
}
```

Response:
```json
{
  "sql": "SELECT c.customer_id, c.first_name, c.last_name, SUM(p.amount) as total_amount FROM customer c JOIN payment p ON c.customer_id = p.customer_id GROUP BY c.customer_id ORDER BY total_amount DESC LIMIT 10",
  "data": [...],
  "summary": "Query executed successfully.",
  "error": null
}
```

## 🧪 Example Queries

The `sample_data/questions.md` file contains 100+ example queries organized by category:

- **Basic Retrieval**: "List all films with their title, release year, and rating"
- **Aggregation**: "Find the total number of rentals per customer"
- **Business Analytics**: "Which films have generated the highest total revenue?"
- **Multi-Table Joins**: "List film titles along with their actors' full names"
- **Revenue Analysis**: "Calculate total revenue per month"
- **Advanced Queries**: "Find customers who rented a film but never made a payment"

## 🛠️ Technology Stack

- **Backend**: FastAPI, Uvicorn
- **AI Framework**: Pydantic AI
- **LLM**: Google Gemini 2.5 Flash
- **Database**: PostgreSQL, asyncpg
- **Database Admin**: pgAdmin 4
- **Package Manager**: uv
- **Environment**: python-dotenv
- **Monitoring**: Logfire (optional)

## 🔧 Configuration

### Database Connection

Update the database connection string in `sql_agents/api.py`:

```python
DB_DSN = "postgresql://postgres:root@localhost:5432/dvdrental"
```

### Model Configuration

Change the AI model in `sql_agents/agent/sql_agent.py`:

```python
model = GeminiModel('gemini-2.5-flash')
```

## 📝 Development

### Project Structure

- **Agent**: Configured with system prompts and tools to understand database schema
- **Tools**: 
  - `list_tables`: Lists all available tables in the database
  - `get_table_schema`: Retrieves schema information for specific tables
- **Utils**: Database operations, configuration loading
- **Prompts**: System prompts that guide the agent's behavior

### Adding New Tools

Register new tools in `sql_agents/agent/sql_agent.py`:

```python
sql_agent.tool(your_custom_tool)
```

## 🐛 Troubleshooting

- **Database connection errors**: Ensure PostgreSQL is running via Docker
- **API key errors**: Verify your `GEMINI_API_KEY` is set in `.env`
- **Schema not loading**: Check database permissions and connection string
- **Port conflicts**: Ensure ports 5432, 5050, and 8000 are available

## 📄 License

This project is for learning purposes.


## Commands Reference

```bash
# Install dependencies
uv sync

# Run the application
uv run uvicorn sql_agents.api:app --reload --host 0.0.0.0 --port 8000
```
