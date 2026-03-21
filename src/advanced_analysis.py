"""
Advanced analysis: Gender pay gap, education impact, skill correlations.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
import sqlite3

def load_from_sql(db_path='tech_salary.db'):
    """Load data from SQL database"""
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM jobs", conn)
    conn.close()
    return df

def gender_pay_gap_analysis(df):
    """
    Analyze gender pay gap by experience level.
    """
    print("\n" + "="*70)
    print("GENDER PAY GAP ANALYSIS")
    print("="*70)
    
    # Filter for valid genders
    valid_genders = df[df['gender'].isin(['Male', 'Female'])].copy()
    
    # By experience level
    gap_analysis = valid_genders.groupby(['experience_level', 'gender']).agg({
        'salary_local_currency': ['count', 'mean', 'median']
    }).round(0)
    
    gap_analysis.columns = ['count', 'avg_salary', 'median_salary']
    
    print("\nSalary by Gender & Experience Level:")
    print(gap_analysis)
    
    # Calculate gap
    print("\nGender Pay Gap by Experience Level:")
    for exp_level in ['Entry', 'Mid', 'Senior', 'Lead']:
        male_salary = valid_genders[
            (valid_genders['experience_level'] == exp_level) & 
            (valid_genders['gender'] == 'Male')
        ]['salary_local_currency'].median()
        
        female_salary = valid_genders[
            (valid_genders['experience_level'] == exp_level) & 
            (valid_genders['gender'] == 'Female')
        ]['salary_local_currency'].median()
        
        if not np.isnan(male_salary) and not np.isnan(female_salary):
            gap = ((male_salary - female_salary) / female_salary) * 100
            print(f"  {exp_level:10s}: Male ${male_salary:10,.0f} | Female ${female_salary:10,.0f} | Gap: {gap:+.1f}%")

def education_impact_analysis(df):
    """
    Analyze how education level affects salary.
    """
    print("\n" + "="*70)
    print("EDUCATION IMPACT ON SALARY")
    print("="*70)
    
    edu_salary = df[df['education_level'].notna()].groupby('education_level').agg({
        'salary_local_currency': ['count', 'mean', 'median'],
        'years_experience': 'mean'
    }).round(0)
    
    edu_salary.columns = ['job_count', 'avg_salary', 'median_salary', 'avg_years_exp']
    edu_salary = edu_salary.sort_values('median_salary', ascending=False)
    
    print("\n" + edu_salary.to_string())

def skill_salary_correlation(df):
    """
    Analyze top paying skills and their demand.
    """
    print("\n" + "="*70)
    print("TOP SKILLS BY SALARY & DEMAND")
    print("="*70)
    
    skill_analysis = df[df['primary_skill'].notna()].groupby('primary_skill').agg({
        'salary_local_currency': ['count', 'mean', 'median'],
        'job_satisfaction_score': 'mean'
    }).round(0)
    
    skill_analysis.columns = ['job_count', 'avg_salary', 'median_salary', 'avg_satisfaction']
    skill_analysis = skill_analysis.sort_values('median_salary', ascending=False)
    
    print("\nTop 15 Skills by Median Salary:")
    print(skill_analysis.head(15).to_string())
    
    print("\n\nTop 15 Skills by Demand (Job Count):")
    skill_demand = skill_analysis.sort_values('job_count', ascending=False)
    print(skill_demand.head(15).to_string())

def salary_satisfaction_correlation(df):
    """
    Analyze relationship between salary and job satisfaction.
    """
    print("\n" + "="*70)
    print("SALARY VS JOB SATISFACTION")
    print("="*70)
    
    # Remove NaN values
    valid_data = df[
        (df['salary_local_currency'].notna()) & 
        (df['job_satisfaction_score'].notna())
    ].copy()
    
    # Calculate correlation
    correlation, p_value = pearsonr(
        valid_data['salary_local_currency'], 
        valid_data['job_satisfaction_score']
    )
    
    print(f"\nPearson Correlation: {correlation:.3f}")
    print(f"P-value: {p_value:.6f}")
    
    if correlation > 0.1:
        print("→ Weak positive relationship: Higher salary slightly correlates with higher satisfaction")
    elif correlation < -0.1:
        print("→ Weak negative relationship: Higher salary correlates with lower satisfaction")
    else:
        print("→ Almost no relationship between salary and satisfaction")
    
    # Binned analysis
    print("\nSalary vs Satisfaction (Binned):")
    valid_data['salary_bin'] = pd.cut(
        valid_data['salary_local_currency'],
        bins=4,
        labels=['Q1 (Lowest)', 'Q2', 'Q3', 'Q4 (Highest)']
    )
    
    binned = valid_data.groupby('salary_bin').agg({
        'salary_local_currency': ['count', 'mean'],
        'job_satisfaction_score': 'mean'
    }).round(2)
    
    binned.columns = ['count', 'avg_salary', 'avg_satisfaction']
    print(binned)

def company_size_stability_analysis(df):
    """
    Analyze company size vs salary vs satisfaction.
    """
    print("\n" + "="*70)
    print("COMPANY SIZE: SALARY VS SATISFACTION VS HOURS")
    print("="*70)
    
    company_analysis = df[df['company_size'].notna()].groupby('company_size').agg({
        'salary_local_currency': ['count', 'mean', 'median'],
        'job_satisfaction_score': 'mean',
        'work_hours_per_week': 'mean'
    }).round(2)
    
    company_analysis.columns = ['job_count', 'avg_salary', 'median_salary', 'avg_satisfaction', 'avg_hours']
    company_analysis = company_analysis.sort_values('median_salary', ascending=False)
    
    print("\n" + company_analysis.to_string())

def main():
    """
    Run all advanced analyses.
    """
    print("="*70)
    print("WEEK 3: ADVANCED ANALYSIS")
    print("="*70)
    
    # Load data
    df = load_from_sql()
    print(f"\nLoaded {len(df):,} records from database")
    
    # Run analyses
    gender_pay_gap_analysis(df)
    education_impact_analysis(df)
    skill_salary_correlation(df)
    salary_satisfaction_correlation(df)
    company_size_stability_analysis(df)
    
    print("\n" + "="*70)
    print(" Advanced analysis complete!")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()