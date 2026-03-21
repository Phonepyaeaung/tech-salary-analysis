"""
Data loading and initial validation module.

Purpose:
    Load the raw tech salary dataset with minimal processing.
    Validate data structure and identify any immediate issues.
    
Author: Data analyst
Date: January 2026
"""

import pandas as pd
import numpy as np
from datetime import datetime
import os


def load_raw_data(filepath):
    """
    Load raw job salary data from CSV.
    
    Args:
        filepath (str): Path to raw CSV file
        
    Returns:
        pd.DataFrame: Raw data with metadata
        
    Raises:
        FileNotFoundError: If file doesn't exist
        Exception: If file cannot be parsed
    """
    
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    
    print("=" * 70)
    print(f"Loading data from: {filepath}")
    print("=" * 70)
    
    try:
        df = pd.read_csv(filepath)
        print(f"✓ Successfully loaded {len(df):,} rows")
        
    except Exception as e:
        print(f"✗ Error loading file: {e}")
        raise
    
    # Add metadata
    df['data_load_date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    return df


def validate_data(df):
    """
    Validate data structure and identify issues.
    
    Args:
        df (pd.DataFrame): Raw data
        
    Returns:
        dict: Validation report
    """
    
    print("\n" + "=" * 70)
    print("DATA VALIDATION REPORT")
    print("=" * 70)
    
    report = {}
    
    # Basic info
    print(f"\n DATASET SHAPE")
    print(f"  Rows: {len(df):,}")
    print(f"  Columns: {len(df.columns)}")
    report['shape'] = df.shape
    
    # Column overview
    print(f"\n COLUMNS")
    for i, col in enumerate(df.columns, 1):
        dtype = df[col].dtype
        non_null = df[col].notna().sum()
        null_count = df[col].isna().sum()
        null_pct = (null_count / len(df)) * 100
        
        print(f"  {i:2d}. {col:25s} | Type: {str(dtype):10s} | Non-null: {non_null:7,} | Nulls: {null_pct:5.2f}%")
    
    report['columns'] = df.columns.tolist()
    
    # Missing data
    print(f"\n  MISSING DATA")
    missing = df.isnull().sum()
    if missing.sum() == 0:
        print("  ✓ No missing values detected")
        report['missing_data'] = None
    else:
        for col, count in missing[missing > 0].items():
            pct = (count / len(df)) * 100
            print(f"  {col}: {count:,} ({pct:.2f}%)")
        report['missing_data'] = missing[missing > 0].to_dict()
    
    # Numeric columns summary
    print(f"\n NUMERIC COLUMNS SUMMARY")
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) > 0:
        summary = df[numeric_cols].describe().round(2)
        print(summary.to_string())
        report['numeric_summary'] = summary
    else:
        print("  No numeric columns found")
    
    # Categorical columns
    print(f"\n  CATEGORICAL COLUMNS")
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        unique_count = df[col].nunique()
        print(f"\n  {col}: {unique_count} unique values")
        if unique_count <= 10:
            for val, count in df[col].value_counts().items():
                print(f"    - {val}: {count:,}")
        else:
            for val, count in df[col].value_counts().head(5).items():
                print(f"    - {val}: {count:,}")
            print(f"    ... and {unique_count - 5} more")
    
    # Data types
    print(f"\n DATA TYPES")
    print(df.dtypes.to_string())
    
    # First few rows
    print(f"\n📄 SAMPLE DATA (First 3 rows)")
    print(df.head(3).to_string())
    
    print("\n" + "=" * 70)
    
    return report


def save_validation_report(report, output_file='reports/validation_report.txt'):
    """
    Save validation report to file.
    
    Args:
        report (dict): Validation report from validate_data()
        output_file (str): Output file path
    """
    
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    with open(output_file, 'w') as f:
        f.write("DATA VALIDATION REPORT\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 70 + "\n\n")
        
        f.write(f"Dataset Shape: {report['shape']}\n")
        f.write(f"Columns: {len(report['columns'])}\n\n")
        
        if report['missing_data']:
            f.write("Missing Data:\n")
            for col, count in report['missing_data'].items():
                f.write(f"  {col}: {count}\n")
        else:
            f.write("Missing Data: None\n")
    
    print(f"✓ Validation report saved to {output_file}")


def main():
    """
    Main execution: Load and validate data.
    """
    
    # Paths
    raw_file = 'data/raw/tech_jobs_salaries.csv'
    
    # Create directories if needed
    os.makedirs('data/raw', exist_ok=True)
    os.makedirs('data/processed', exist_ok=True)
    os.makedirs('reports', exist_ok=True)
    
    # Load data
    df = load_raw_data(raw_file)
    
    # Validate
    report = validate_data(df)
    
    # Save validation report
    save_validation_report(report)
    
    print(f"\n✓ Data loading complete")
    print(f"✓ Ready for cleaning and analysis")
    
    return df


if __name__ == "__main__":
    df = main()
