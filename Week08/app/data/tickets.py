import sqlite3
import pandas as pd


def insert_ticket(ticket_id, priority, status, category, subject,
                  description, created_date, resolved_date,
                  assigned_to):
    """Insert a new IT ticket."""
    conn = connect_database()  # Use existing connection function
    cursor = conn.cursor()

    # SQL query to insert ticket data
    insert_query = """
        INSERT INTO it_tickets
        (ticket_id, priority, status, category, subject,
         description, created_date, resolved_date, assigned_to)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    # Execute the query with parameters
    cursor.execute(insert_query, (ticket_id, priority, status, category, subject,
                                  description, created_date, resolved_date, assigned_to))

    conn.commit()  # Commit the transaction
    ticket_row_id = cursor.lastrowid  # Get the last inserted row ID
    conn.close()  # Close the connection

    return ticket_row_id


def get_all_tickets():
    """Return all tickets as a DataFrame."""
    conn = connect_database()  # Use existing connection function
    query = "SELECT * FROM it_tickets"  # Store the query for readability
    df = pd.read_sql_query(query, conn)  # Execute the query and load results into a DataFrame
    conn.close()  # Close the connection
    return df