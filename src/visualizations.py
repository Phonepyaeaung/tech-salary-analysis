"""
Create professional visualizations for analysis.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
import os

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 6)

def load_from_sql(db_path='tech_salary.db'):
    """Load data from SQL database"""
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM jobs", conn)
    conn.close()
    return df

def ensure_reports_dir():
    """Create reports directory if it doesn't exist"""
    os.makedirs('reports', exist_ok=True)

def viz_1_skill_salary(df):
    """Top 15 skills by median salary"""
    print("Creating: Skills by Salary visualization...")
    
    skill_salary = df[df['primary_skill'].notna()].groupby('primary_skill')['salary_local_currency'].median().sort_values(ascending=False).head(15)
    
    fig, ax = plt.subplots(figsize=(12, 7))
    skill_salary.plot(kind='barh', ax=ax, color='steelblue')
    ax.set_xlabel('Median Salary (Local Currency)')
    ax.set_ylabel('Skill')
    ax.set_title('Top 15 Skills by Median Salary', fontsize=14, fontweight='bold')
    ax.grid(alpha=0.3, axis='x')
    
    plt.tight_layout()
    plt.savefig('reports/01_skills_salary.png', dpi=300, bbox_inches='tight')
    plt.close()
    print(" Saved: 01_skills_salary.png")

def viz_2_experience_salary(df):
    """Salary by experience level"""
    print("Creating: Experience Level vs Salary visualization...")
    
    exp_order = ['Entry', 'Mid', 'Senior', 'Lead']
    exp_salary = df.groupby('experience_level')['salary_local_currency'].median()
    exp_salary = exp_salary.reindex(exp_order)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
    exp_salary.plot(kind='bar', ax=ax, color=colors)
    ax.set_ylabel('Median Salary (Local Currency)')
    ax.set_xlabel('Experience Level')
    ax.set_title('Median Salary by Experience Level', fontsize=14, fontweight='bold')
    ax.grid(alpha=0.3, axis='y')
    plt.xticks(rotation=45)
    
    # Add value labels
    for i, v in enumerate(exp_salary):
        ax.text(i, v + 5000, f'${v:,.0f}', ha='center', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('reports/02_experience_salary.png', dpi=300, bbox_inches='tight')
    plt.close()
    print(" Saved: 02_experience_salary.png")

def viz_3_company_size(df):
    """Salary by company size"""
    print("Creating: Company Size vs Salary visualization...")
    
    company_salary = df.groupby('company_size')['salary_local_currency'].median().sort_values(ascending=False)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    company_salary.plot(kind='bar', ax=ax, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
    ax.set_ylabel('Median Salary (Local Currency)')
    ax.set_xlabel('Company Size')
    ax.set_title('Median Salary by Company Size', fontsize=14, fontweight='bold')
    ax.grid(alpha=0.3, axis='y')
    plt.xticks(rotation=45)
    
    # Add value labels
    for i, v in enumerate(company_salary):
        ax.text(i, v + 5000, f'${v:,.0f}', ha='center', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('reports/03_company_size_salary.png', dpi=300, bbox_inches='tight')
    plt.close()
    print(" Saved: 03_company_size_salary.png")

def viz_4_country_salary(df):
    """Top countries by salary"""
    print("Creating: Country Salary visualization...")
    
    country_salary = df[df['country'].notna()].groupby('country')['salary_local_currency'].median().sort_values(ascending=False).head(10)
    
    fig, ax = plt.subplots(figsize=(12, 6))
    country_salary.plot(kind='barh', ax=ax, color='steelblue')
    ax.set_xlabel('Median Salary (Local Currency)')
    ax.set_ylabel('Country')
    ax.set_title('Top 10 Countries by Median Salary', fontsize=14, fontweight='bold')
    ax.grid(alpha=0.3, axis='x')
    
    plt.tight_layout()
    plt.savefig('reports/04_country_salary.png', dpi=300, bbox_inches='tight')
    plt.close()
    print(" Saved: 04_country_salary.png")

def viz_5_remote_work(df):
    """Salary by remote work type"""
    print("Creating: Remote Work vs Salary visualization...")
    
    remote_salary = df[df['remote_type'].notna()].groupby('remote_type')['salary_local_currency'].median().sort_values(ascending=False)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    remote_salary.plot(kind='bar', ax=ax, color=['#1f77b4', '#ff7f0e', '#2ca02c'])
    ax.set_ylabel('Median Salary (Local Currency)')
    ax.set_xlabel('Remote Work Type')
    ax.set_title('Median Salary by Remote Work Type', fontsize=14, fontweight='bold')
    ax.grid(alpha=0.3, axis='y')
    plt.xticks(rotation=45)
    
    # Add value labels
    for i, v in enumerate(remote_salary):
        ax.text(i, v + 5000, f'${v:,.0f}', ha='center', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('reports/05_remote_work_salary.png', dpi=300, bbox_inches='tight')
    plt.close()
    print(" Saved: 05_remote_work_salary.png")

def viz_6_gender_gap(df):
    """Gender pay gap by experience level"""
    print("Creating: Gender Pay Gap visualization...")
    
    valid_genders = df[df['gender'].isin(['Male', 'Female'])].copy()
    
    gap_data = valid_genders.groupby(['experience_level', 'gender'])['salary_local_currency'].median().unstack()
    gap_data = gap_data.reindex(['Entry', 'Mid', 'Senior', 'Lead'])
    
    fig, ax = plt.subplots(figsize=(10, 6))
    gap_data.plot(kind='bar', ax=ax, color=['#1f77b4', '#ff7f0e'])
    ax.set_ylabel('Median Salary (Local Currency)')
    ax.set_xlabel('Experience Level')
    ax.set_title('Gender Pay Gap by Experience Level', fontsize=14, fontweight='bold')
    ax.legend(['Female', 'Male'], loc='upper left')
    ax.grid(alpha=0.3, axis='y')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.savefig('reports/06_gender_pay_gap.png', dpi=300, bbox_inches='tight')
    plt.close()
    print(" Saved: 06_gender_pay_gap.png")

def viz_7_satisfaction_salary(df):
    """Salary vs job satisfaction scatter plot"""
    print("Creating: Salary vs Satisfaction visualization...")
    
    valid_data = df[
        (df['salary_local_currency'].notna()) & 
        (df['job_satisfaction_score'].notna())
    ].copy()
    
    # Sample if too many points
    if len(valid_data) > 5000:
        valid_data = valid_data.sample(n=5000, random_state=42)
    
    fig, ax = plt.subplots(figsize=(12, 7))
    scatter = ax.scatter(
        valid_data['salary_local_currency'],
        valid_data['job_satisfaction_score'],
        alpha=0.5,
        s=30,
        c=valid_data['job_satisfaction_score'],
        cmap='viridis'
    )
    
    ax.set_xlabel('Salary (Local Currency)')
    ax.set_ylabel('Job Satisfaction Score')
    ax.set_title('Salary vs Job Satisfaction', fontsize=14, fontweight='bold')
    ax.grid(alpha=0.3)
    
    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label('Satisfaction Score')
    
    plt.tight_layout()
    plt.savefig('reports/07_salary_satisfaction.png', dpi=300, bbox_inches='tight')
    plt.close()
    print(" Saved: 07_salary_satisfaction.png")

def main():
    """Create all visualizations"""
    print("="*70)
    print("CREATING VISUALIZATIONS")
    print("="*70)
    
    # Load data
    df = load_from_sql()
    print(f"\nLoaded {len(df):,} records")
    
    # Ensure reports directory exists
    ensure_reports_dir()
    
    # Create visualizations
    viz_1_skill_salary(df)
    viz_2_experience_salary(df)
    viz_3_company_size(df)
    viz_4_country_salary(df)
    viz_5_remote_work(df)
    viz_6_gender_gap(df)
    viz_7_satisfaction_salary(df)
    
    print("\n" + "="*70)
    print(" All visualizations created in reports/ folder!")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()