import sqlite3
import pandas as pd

def insert_dataset(dataset_name, category, source, last_updated,
                   record_count, file_size_mb):
    """Insert a new dataset record."""
    conn = connect_database()  # Use existing connection function
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO datasets_metadata
        (dataset_name, category, source, last_updated,
         record_count, file_size_mb)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (dataset_name, category, source, last_updated,
          record_count, file_size_mb))

    conn.commit()
    dataset_id = cursor.lastrowid  # Get the ID of the last inserted row
    conn.close()

    return dataset_id


def get_all_datasets():
    """Return all datasets as a DataFrame."""
    conn = connect_database()  # Use existing connection function
    query = "SELECT * FROM datasets_metadata"  # Store query in a variable for readability
    df = pd.read_sql_query(query, conn)  # Read the results into a DataFrame
    conn.close()
    return df