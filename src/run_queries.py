"""
Run analytical SQL queries on the database.
"""

import sqlite3
import pandas as pd

def run_query(conn, query_name, sql_query):
    """
    Run a query and display results.
    """
    print(f"\n{'='*70}")
    print(f"{query_name}")
    print(f"{'='*70}")
    
    try:
        df = pd.read_sql_query(sql_query, conn)
        print(df.to_string(index=False))
        print(f"\n Returned {len(df)} rows")
    except Exception as e:
        print(f"✗ Error: {e}")

def main():
    """
    Main execution.
    """
    print("="*70)
    print("RUNNING ANALYTICAL QUERIES")
    print("="*70)
    
    # Connect to database
    conn = sqlite3.connect('tech_salary.db')
    
    # Query 1: Top skills by salary
    query1 = """
    SELECT 
        primary_skill as skill,
        COUNT(*) as job_count,
        ROUND(AVG(salary_local_currency), 0) as avg_salary,
        ROUND(MIN(salary_local_currency), 0) as min_salary,
        ROUND(MAX(salary_local_currency), 0) as max_salary
    FROM jobs
    WHERE primary_skill IS NOT NULL 
      AND salary_local_currency > 0
    GROUP BY primary_skill
    ORDER BY avg_salary DESC
    LIMIT 10;
    """
    
    run_query(conn, "TOP 10 SKILLS BY AVERAGE SALARY", query1)
    
    # Query 2: Salary by experience level
    query2 = """
    SELECT 
        experience_level,
        COUNT(*) as job_count,
        ROUND(AVG(salary_local_currency), 0) as avg_salary,
        ROUND(MIN(salary_local_currency), 0) as min_salary,
        ROUND(MAX(salary_local_currency), 0) as max_salary
    FROM jobs
    WHERE salary_local_currency > 0
    GROUP BY experience_level
    ORDER BY avg_salary DESC;
    """
    
    run_query(conn, "SALARY BY EXPERIENCE LEVEL", query2)
    
    # Query 3: Salary by company size
    query3 = """
    SELECT 
        company_size,
        COUNT(*) as job_count,
        ROUND(AVG(salary_local_currency), 0) as avg_salary,
        ROUND(AVG(job_satisfaction_score), 2) as avg_satisfaction
    FROM jobs
    WHERE salary_local_currency > 0
    GROUP BY company_size
    ORDER BY avg_salary DESC;
    """
    
    run_query(conn, "SALARY BY COMPANY SIZE", query3)
    
    # Query 4: Top countries by salary
    query4 = """
    SELECT 
        country,
        COUNT(*) as job_count,
        ROUND(AVG(salary_local_currency), 0) as avg_salary,
        ROUND(AVG(job_satisfaction_score), 2) as avg_satisfaction
    FROM jobs
    WHERE salary_local_currency > 0
    GROUP BY country
    ORDER BY avg_salary DESC
    LIMIT 10;
    """
    
    run_query(conn, "TOP 10 COUNTRIES BY SALARY", query4)
    
    # Query 5: Remote work impact
    query5 = """
    SELECT 
        remote_type,
        COUNT(*) as job_count,
        ROUND(AVG(salary_local_currency), 0) as avg_salary,
        ROUND(AVG(work_hours_per_week), 1) as avg_hours
    FROM jobs
    WHERE salary_local_currency > 0
    GROUP BY remote_type
    ORDER BY avg_salary DESC;
    """
    
    run_query(conn, "SALARY BY REMOTE WORK TYPE", query5)
    
    conn.close()
    
    print(f"\n{'='*70}")
    print(" All queries completed successfully!")
    print(f"{'='*70}\n")

if __name__ == "__main__":
    main()