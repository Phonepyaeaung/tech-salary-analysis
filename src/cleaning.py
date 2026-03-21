"""
Data cleaning and preparation pipeline.
Purpose: Normalize data, handle outliers, prepare for analysis.
"""

import pandas as pd
import numpy as np
from datetime import datetime
import os

def load_data(filepath):
    """Load raw data"""
    print(f"Loading data from {filepath}...")
    df = pd.read_csv(filepath)
    print(f" Loaded {len(df):,} rows")
    return df

def clean_salaries(df):
    """
    Remove extreme outliers from salary data.
    Keep salaries between 5th and 95th percentile.
    """
    print("\nCleaning salaries...")
    
    # Calculate percentiles
    p5 = df['salary_local_currency'].quantile(0.05)
    p95 = df['salary_local_currency'].quantile(0.95)
    
    print(f"  Salary range before: ${df['salary_local_currency'].min():,.0f} - ${df['salary_local_currency'].max():,.0f}")
    
    # Remove extreme outliers
    df_clean = df[(df['salary_local_currency'] >= p5) & (df['salary_local_currency'] <= p95)].copy()
    
    removed = len(df) - len(df_clean)
    print(f"  Removed {removed:,} extreme outliers ({removed/len(df)*100:.1f}%)")
    print(f"  Salary range after: ${df_clean['salary_local_currency'].min():,.0f} - ${df_clean['salary_local_currency'].max():,.0f}")
    
    return df_clean

def standardize_skills(df):
    """
    Clean up skill names for consistency.
    """
    print("\nStandardizing skills...")
    
    # Fill missing skills with 'Unknown'
    df['primary_skill'] = df['primary_skill'].fillna('Unknown')
    df['secondary_skill'] = df['secondary_skill'].fillna('Unknown')
    
    print(f"   Handled missing skills")
    
    return df

def standardize_experience_level(df):
    """
    Ensure experience levels are consistent.
    """
    print("\nStandardizing experience levels...")
    
    valid_levels = ['Entry', 'Mid', 'Senior', 'Lead']
    
    # Check for any unexpected values
    invalid = df[~df['experience_level'].isin(valid_levels)]
    if len(invalid) > 0:
        print(f"  Found {len(invalid)} invalid experience levels - fixing...")
        df = df[df['experience_level'].isin(valid_levels)].copy()
    
    print(f"   Experience levels cleaned")
    
    return df

def remove_duplicates(df):
    """
    Remove exact duplicate rows.
    """
    print("\nChecking for duplicates...")
    
    duplicates = df.duplicated().sum()
    if duplicates > 0:
        print(f"  Found {duplicates} duplicate rows - removing...")
        df = df.drop_duplicates().copy()
    else:
        print(f"   No duplicates found")
    
    return df

def pipeline(input_path, output_path):
    """
    Run full cleaning pipeline.
    """
    print("=" * 70)
    print("DATA CLEANING PIPELINE")
    print("=" * 70)
    
    # Load
    df = load_data(input_path)
    
    # Clean
    df = remove_duplicates(df)
    df = clean_salaries(df)
    df = standardize_skills(df)
    df = standardize_experience_level(df)
    
    # Save cleaned data
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    
    print("\n" + "=" * 70)
    print(f" Cleaning complete!")
    print(f" Cleaned data saved to {output_path}")
    print(f" Final shape: {len(df):,} rows × {len(df.columns)} columns")
    print("=" * 70)
    
    return df

if __name__ == "__main__":
    df_clean = pipeline(
        input_path='data/raw/tech_jobs_salaries.csv',
        output_path='data/processed/tech_jobs_cleaned.csv'
    )