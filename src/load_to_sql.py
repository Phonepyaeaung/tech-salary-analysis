"""
Load cleaned data into SQLite database.
"""

import pandas as pd
import sqlite3
import os

def create_database(db_path, schema_path):
    """
    Create SQLite database with schema.
    """
    print(f"Creating database at {db_path}...")
    
    # Connect to database (creates it if doesn't exist)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Read and execute schema
    with open(schema_path, 'r') as f:
        schema = f.read()
    
    # Execute all schema statements
    for statement in schema.split(';'):
        if statement.strip():
            cursor.execute(statement)
    
    conn.commit()
    print(" Database created with schema")
    
    return conn

def load_data_to_sql(df, conn, table_name='jobs'):
    """
    Load cleaned dataframe into SQL table.
    """
    print(f"\nLoading {len(df):,} rows into '{table_name}' table...")
    
    # Load data into SQL
    df.to_sql(table_name, conn, if_exists='append', index=False)
    
    print(f" Data loaded successfully")

def verify_data(conn):
    """
    Verify data was loaded correctly.
    """
    print("\n" + "=" * 70)
    print("VERIFICATION")
    print("=" * 70)
    
    cursor = conn.cursor()
    
    # Count records
    cursor.execute("SELECT COUNT(*) FROM jobs")
    count = cursor.fetchone()[0]
    print(f"\n Total records in database: {count:,}")
    
    # Show sample data
    cursor.execute("SELECT * FROM jobs LIMIT 3")
    columns = [description[0] for description in cursor.description]
    print(f"\n Sample data (first 3 rows):")
    print(f"  Columns: {len(columns)}")
    
    # Show salary stats
    cursor.execute("""
        SELECT 
            COUNT(*) as total,
            ROUND(AVG(salary_local_currency), 0) as avg_salary,
            ROUND(MIN(salary_local_currency), 0) as min_salary,
            ROUND(MAX(salary_local_currency), 0) as max_salary
        FROM jobs
    """)
    stats = cursor.fetchone()
    print(f"\n Salary statistics:")
    print(f"  Average: ${stats[1]:,.0f}")
    print(f"  Range: ${stats[2]:,.0f} - ${stats[3]:,.0f}")
    
    print("\n" + "=" * 70)

def main():
    """
    Main execution.
    """
    print("=" * 70)
    print("LOAD DATA TO SQL")
    print("=" * 70)
    
    # Paths
    db_path = 'tech_salary.db'
    schema_path = 'sql/schema.sql'
    cleaned_data_path = 'data/processed/tech_jobs_cleaned.csv'
    
    # Remove existing database (fresh start)
    if os.path.exists(db_path):
        os.remove(db_path)
        print(f"Removed existing database")
    
    # Create database
    conn = create_database(db_path, schema_path)
    
    # Load cleaned data
    print(f"\nLoading cleaned data from {cleaned_data_path}...")
    df = pd.read_csv(cleaned_data_path)
    print(f" Loaded {len(df):,} rows")
    
    # Load to SQL
    load_data_to_sql(df, conn)
    
    # Verify
    verify_data(conn)
    
    # Close connection
    conn.close()
    
    print(f"\n Database ready at: {db_path}")

if __name__ == "__main__":
    main()