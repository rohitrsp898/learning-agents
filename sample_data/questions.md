# DVD Rental Database - Sample Questions

This document contains a comprehensive set of natural language queries designed to test the SQL Agent's ability to generate accurate SQL queries across various complexity levels.

# Table Details

- "actor – stores actor data including first name and last name."
- "film – stores film data such as title, release year, length, rating, etc."
- "film_actor – stores the relationships between films and actors."
- "category – stores film’s categories data."
- "film_category- stores the relationships between films and categories."
- "store – contains the store data including manager staff and address."
- "inventory – stores inventory data."
- "rental – stores rental data."
- "payment – stores customer’s payments."
- "staff – stores staff data."
- "customer – stores customer data."
- "address – stores address data for staff and customers"
- "city – stores city names."
- "country – stores country names."

## 1. Basic Retrieval (Single / Simple Joins)

Simple queries that involve one or two tables with straightforward joins.

- "List all films with their title, release year, rental rate, and rating."
- "Show all customers with their full name, email, and city."
- "Retrieve all actors whose last name starts with 'S'."
- "Get all films available in the 'Action' category."
- "List all stores with their address and city."

## 2. Date & Time Based Questions

Queries involving date/time filtering and calculations.

- "Find all rentals made in the last 30 days."
- "List customers who created their account in the last 90 days."
- "Show rentals that were returned late (return_date is after rental_date + rental_duration)."
- "Find films that were rented at least once in the year 2006."
- "List payments made on weekends."

## 3. Aggregation & Metrics

Queries using aggregate functions like COUNT, SUM, AVG, etc.

- "Find the total number of rentals per customer."
- "Show total revenue generated per store."
- "List top 10 customers by total payment amount."
- "Find the number of films in each category."
- "Show average rental duration per film category."

## 4. Business-Style Analytical Questions

**Very Important for LLM Evaluation** - These queries simulate real business intelligence questions.

- "Which films have generated the highest total revenue?"
- "Which customers have rented more than 20 films?"
- "Find the most rented film in each category."
- "Which store has the highest number of active customers?"
- "Which staff member processed the highest number of rentals?"

## 5. Multi-Table Join Reasoning

**Good LLM Stress Tests** - Complex queries requiring multiple table joins and logical reasoning.

- "List film titles along with their actors’ full names."
- "Show customers, their city, and country."
- "Find films that were never rented."
- "List customers who rented films from more than 3 different categories."
- "Find actors who acted in more than 10 films."

## 6. Inventory & Availability Logic

Queries related to inventory management and availability tracking.

- "Find all films currently available for rent (not rented out)."
- "List films that have no inventory in store 1."
- "Find the total number of copies available per film."
- "Show inventory items that were never rented."
- "Find stores that have inventory for the same film."

## 7. Revenue & Payments

**Common Real-World Use Case** - Financial and payment-related queries.

- "Calculate total revenue per month."
- "Find customers who have made payments exceeding $100 in total."
- "Show revenue contribution by film category."
- "Find customers who have overdue rentals and unpaid balances."
- "List the top 5 films by revenue in each store."

## 8. Advanced / Edge-Case Questions

**Excellent for Guardrail Testing** - Complex edge cases that test the agent's robustness.

- "Find customers who rented a film but never made a payment."
- "List films that were rented but never returned."
- "Find customers who rented the same film more than once."
- "Show actors who have never acted in a film."
- "Identify customers who rented films from every available category."

## 9. Natural-Language → SQL Ambiguity Control

### Recommended Patterns

Use specific phrasing to help the LLM generate accurate SQL:

- **"For each…"** → Indicates `GROUP BY`
- **"At least…"** → Indicates `HAVING` with comparison
- **"Never…"** → Indicates `NOT EXISTS` or `LEFT JOIN` with `NULL` check
- **"More than…"** → Indicates `HAVING` with `>` operator
- **"Currently…"** → Indicates filtering for active/current state
- **"Total revenue…"** → Indicates `SUM()` aggregate function

### SQL Patterns These Help Infer

These natural language patterns help the LLM understand when to use:

- `GROUP BY` - For aggregating data by categories
- `HAVING` - For filtering aggregated results
- `LEFT JOIN` - For finding missing relationships
- `NOT EXISTS` - For negation queries
- **Date arithmetic** - For time-based calculations

## Usage Tips

1. **Start Simple**: Begin with Basic Retrieval queries to verify the agent works correctly
2. **Progress Gradually**: Move to more complex queries as confidence builds
3. **Test Edge Cases**: Use Advanced queries to ensure robust error handling
4. **Validate Results**: Cross-check results using pgAdmin or direct SQL queries
5. **Monitor Performance**: Track which query types the agent handles best

## Query Categories Summary

| Category | Complexity | Count | Primary SQL Features |
|----------|-----------|-------|---------------------|
| Basic Retrieval | ⭐ | 5 | SELECT, JOIN |
| Date & Time | ⭐⭐ | 5 | Date functions, filtering |
| Aggregation | ⭐⭐ | 5 | COUNT, SUM, AVG, GROUP BY |
| Business Analytics | ⭐⭐⭐ | 5 | Complex aggregations, ranking |
| Multi-Table Joins | ⭐⭐⭐⭐ | 5 | Multiple JOINs, subqueries |
| Inventory Logic | ⭐⭐⭐ | 5 | NOT EXISTS, availability checks |
| Revenue & Payments | ⭐⭐⭐ | 5 | Financial calculations |
| Advanced/Edge Cases | ⭐⭐⭐⭐⭐ | 5 | Complex logic, edge cases |

---

**Total Questions**: 40+ queries covering all major SQL patterns and business scenarios.