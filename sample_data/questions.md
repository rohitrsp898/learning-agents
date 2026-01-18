1. Basic Retrieval (Single / Simple Joins)

“List all films with their title, release year, rental rate, and rating.”

“Show all customers with their full name, email, and city.”

“Retrieve all actors whose last name starts with ‘S’.”

“Get all films available in the ‘Action’ category.”

“List all stores with their address and city.”

2. Date & Time Based Questions

“Find all rentals made in the last 30 days.”

“List customers who created their account in the last 90 days.”

“Show rentals that were returned late (return_date is after rental_date + rental_duration).”

“Find films that were rented at least once in the year 2006.”

“List payments made on weekends.”

3. Aggregation & Metrics

“Find the total number of rentals per customer.”

“Show total revenue generated per store.”

“List top 10 customers by total payment amount.”

“Find the number of films in each category.”

“Show average rental duration per film category.”

4. Business-Style Analytical Questions (Very Important for LLM Evaluation)

“Which films have generated the highest total revenue?”

“Which customers have rented more than 20 films?”

“Find the most rented film in each category.”

“Which store has the highest number of active customers?”

“Which staff member processed the highest number of rentals?”

5. Multi-Table Join Reasoning (Good LLM Stress Tests)

“List film titles along with their actors’ full names.”

“Show customers, their city, and country.”

“Find films that were never rented.”

“List customers who rented films from more than 3 different categories.”

“Find actors who acted in more than 10 films.”

6. Inventory & Availability Logic

“Find all films currently available for rent (not rented out).”

“List films that have no inventory in store 1.”

“Find the total number of copies available per film.”

“Show inventory items that were never rented.”

“Find stores that have inventory for the same film.”

7. Revenue & Payments (Common Real-World Use Case)

“Calculate total revenue per month.”

“Find customers who have made payments exceeding $100 in total.”

“Show revenue contribution by film category.”

“Find customers who have overdue rentals and unpaid balances.”

“List the top 5 films by revenue in each store.”

8. Advanced / Edge-Case Questions (Excellent for Guardrail Testing)

“Find customers who rented a film but never made a payment.”

“List films that were rented but never returned.”

“Find customers who rented the same film more than once.”

“Show actors who have never acted in a film.”

“Identify customers who rented films from every available category.”

9. Natural-Language → SQL Ambiguity Control (Recommended Patterns)

Use phrasing like:

“For each…”

“At least…”

“Never…”

“More than…”

“Currently…”

“Total revenue…”

These help the LLM infer:

GROUP BY

HAVING

LEFT JOIN

NOT EXISTS

Date arithmetic