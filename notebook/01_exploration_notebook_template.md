# Week 1: Data Exploration & Initial Analysis

## Objective
Load the tech salary dataset, understand its structure, and identify key patterns.
This notebook will be converted to Jupyter format.

## Import Libraries

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 6)
```

## 1. Load & Validate Data

```python
# Load the dataset
df = pd.read_csv('../data/raw/tech_jobs_salaries.csv')

print("=" * 70)
print("DATASET OVERVIEW")
print("=" * 70)
print(f"\n✓ Shape: {df.shape[0]:,} rows × {df.shape[1]} columns")
print(f"\n✓ Columns:\n{df.columns.tolist()}")
print(f"\n✓ Data Types:\n{df.dtypes}")
print(f"\n✓ First 3 rows:")
print(df.head(3))
```

## 2. Data Quality Check

```python
# Missing data
print("\n" + "=" * 70)
print("MISSING DATA")
print("=" * 70)
missing = df.isnull().sum()
if missing.sum() == 0:
    print("✓ No missing values found!")
else:
    print(missing[missing > 0])

# Duplicates
print(f"\n✓ Duplicate rows: {df.duplicated().sum()}")
```

## 3. Numeric Summary

```python
print("\n" + "=" * 70)
print("NUMERIC SUMMARY")
print("=" * 70)
print(df.describe())
```

## 4. Categorical Overview

```python
print("\n" + "=" * 70)
print("CATEGORICAL COLUMNS")
print("=" * 70)

# Experience Level
print("\nExperience Level Distribution:")
print(df['experience_level'].value_counts())

# Company Size
print("\nCompany Size Distribution:")
print(df['company_size'].value_counts())

# Countries
print("\nTop 10 Countries:")
print(df['country'].value_counts().head(10))

# Primary Skills
print("\nTop 15 Primary Skills:")
print(df['primary_skill'].value_counts().head(15))

# Remote Type
print("\nRemote Work Type:")
print(df['remote_type'].value_counts())

# Gender
print("\nGender Distribution:")
print(df['gender'].value_counts())
```

## 5. Salary Analysis

```python
print("\n" + "=" * 70)
print("SALARY DISTRIBUTION")
print("=" * 70)

# Basic stats
print(f"\nSalary Range: ${df['salary_local_currency'].min():,.0f} to ${df['salary_local_currency'].max():,.0f}")
print(f"Mean Salary: ${df['salary_local_currency'].mean():,.0f}")
print(f"Median Salary: ${df['salary_local_currency'].median():,.0f}")
print(f"Std Dev: ${df['salary_local_currency'].std():,.0f}")

# Check for outliers
q1 = df['salary_local_currency'].quantile(0.25)
q3 = df['salary_local_currency'].quantile(0.75)
iqr = q3 - q1
outliers = df[(df['salary_local_currency'] < q1 - 1.5*iqr) | (df['salary_local_currency'] > q3 + 1.5*iqr)]
print(f"\nPotential outliers: {len(outliers)} records ({len(outliers)/len(df)*100:.2f}%)")

# Distribution visualization
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Histogram
axes[0].hist(df['salary_local_currency'], bins=50, color='steelblue', edgecolor='black')
axes[0].set_xlabel('Salary (Local Currency)')
axes[0].set_ylabel('Frequency')
axes[0].set_title('Salary Distribution (Histogram)')
axes[0].grid(alpha=0.3)

# Box plot
df.boxplot(column='salary_local_currency', ax=axes[1])
axes[1].set_ylabel('Salary (Local Currency)')
axes[1].set_title('Salary Distribution (Box Plot)')
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.savefig('../reports/01_salary_distribution.png', dpi=300, bbox_inches='tight')
plt.show()
```

## 6. Quick Insights - Skills & Salary

```python
# Average salary by skill
skill_salary = df.groupby('primary_skill').agg({
    'salary_local_currency': ['count', 'mean', 'median']
}).round(0)

skill_salary.columns = ['job_count', 'avg_salary', 'median_salary']
skill_salary = skill_salary.sort_values('median_salary', ascending=False)

print("\n" + "=" * 70)
print("SALARY BY SKILL (Top 10)")
print("=" * 70)
print(skill_salary.head(10))

# Visualization
fig, ax = plt.subplots(figsize=(12, 6))
top_10_skills = skill_salary.head(10)
ax.barh(top_10_skills.index, top_10_skills['median_salary'], color='steelblue')
ax.set_xlabel('Median Salary (Local Currency)')
ax.set_title('Top 10 Skills by Median Salary')
ax.grid(alpha=0.3, axis='x')

for i, v in enumerate(top_10_skills['median_salary']):
    ax.text(v + 5000, i, f'${v:,.0f}', va='center')

plt.tight_layout()
plt.savefig('../reports/02_skills_salary.png', dpi=300, bbox_inches='tight')
plt.show()
```

## 7. Experience Level & Salary

```python
# Salary by experience level
exp_salary = df.groupby('experience_level').agg({
    'salary_local_currency': ['count', 'mean', 'median'],
    'years_experience': 'mean'
}).round(0)

exp_salary.columns = ['job_count', 'avg_salary', 'median_salary', 'avg_years']
experience_order = ['Entry', 'Mid', 'Senior', 'Lead']
exp_salary = exp_salary.reindex(experience_order)

print("\n" + "=" * 70)
print("SALARY BY EXPERIENCE LEVEL")
print("=" * 70)
print(exp_salary)

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Salary by experience
axes[0].bar(exp_salary.index, exp_salary['median_salary'], color='steelblue', edgecolor='black')
axes[0].set_ylabel('Median Salary (Local Currency)')
axes[0].set_xlabel('Experience Level')
axes[0].set_title('Median Salary by Experience Level')
axes[0].grid(alpha=0.3, axis='y')

for i, (idx, row) in enumerate(exp_salary.iterrows()):
    axes[0].text(i, row['median_salary'] + 5000, f"${row['median_salary']:,.0f}", ha='center')

# Years of experience by level
axes[1].bar(exp_salary.index, exp_salary['avg_years'], color='coral', edgecolor='black')
axes[1].set_ylabel('Average Years of Experience')
axes[1].set_xlabel('Experience Level')
axes[1].set_title('Avg Experience Years by Level')
axes[1].grid(alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('../reports/03_experience_salary.png', dpi=300, bbox_inches='tight')
plt.show()
```

## 8. Company Size & Salary

```python
# Salary by company size
company_salary = df.groupby('company_size').agg({
    'salary_local_currency': ['count', 'mean', 'median'],
    'job_satisfaction_score': 'mean'
}).round(0)

company_salary.columns = ['job_count', 'avg_salary', 'median_salary', 'avg_satisfaction']
company_salary = company_salary.sort_values('median_salary', ascending=False)

print("\n" + "=" * 70)
print("SALARY BY COMPANY SIZE")
print("=" * 70)
print(company_salary)

# Visualization
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(company_salary.index, company_salary['median_salary'], color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
ax.set_ylabel('Median Salary (Local Currency)')
ax.set_xlabel('Company Size')
ax.set_title('Median Salary by Company Size')
ax.grid(alpha=0.3, axis='y')

for i, (idx, row) in enumerate(company_salary.iterrows()):
    ax.text(i, row['median_salary'] + 5000, f"${row['median_salary']:,.0f}", ha='center')

plt.tight_layout()
plt.savefig('../reports/04_company_size_salary.png', dpi=300, bbox_inches='tight')
plt.show()
```

## 9. Geographic Analysis

```python
# Salary by country
country_salary = df.groupby('country').agg({
    'salary_local_currency': ['count', 'mean', 'median'],
    'job_satisfaction_score': 'mean'
}).round(0)

country_salary.columns = ['job_count', 'avg_salary', 'median_salary', 'avg_satisfaction']
country_salary = country_salary.sort_values('median_salary', ascending=False)

print("\n" + "=" * 70)
print("SALARY BY COUNTRY")
print("=" * 70)
print(country_salary)

# Visualization
fig, ax = plt.subplots(figsize=(12, 6))
ax.barh(country_salary.index, country_salary['median_salary'], color='steelblue')
ax.set_xlabel('Median Salary (Local Currency)')
ax.set_title('Median Salary by Country')
ax.grid(alpha=0.3, axis='x')

for i, v in enumerate(country_salary['median_salary']):
    ax.text(v + 50000, i, f'${v:,.0f}', va='center')

plt.tight_layout()
plt.savefig('../reports/05_country_salary.png', dpi=300, bbox_inches='tight')
plt.show()
```

## 10. Key Findings Summary

```python
print("\n" + "=" * 70)
print("KEY FINDINGS FROM WEEK 1 EXPLORATION")
print("=" * 70)

# Finding 1: Top skill
top_skill = skill_salary.index[0]
top_skill_salary = skill_salary.iloc[0]['median_salary']
print(f"\n1. Highest-paying skill: {top_skill} (${top_skill_salary:,.0f} median)")

# Finding 2: Experience impact
entry_salary = exp_salary.loc['Entry', 'median_salary']
lead_salary = exp_salary.loc['Lead', 'median_salary']
increase = ((lead_salary - entry_salary) / entry_salary) * 100
print(f"\n2. Entry → Lead salary increase: {increase:.1f}% (${entry_salary:,.0f} → ${lead_salary:,.0f})")

# Finding 3: Company size
best_company = company_salary.index[0]
best_salary = company_salary.iloc[0]['median_salary']
print(f"\n3. Best-paying company size: {best_company} (${best_salary:,.0f})")

# Finding 4: Best country
best_country = country_salary.index[0]
best_country_salary = country_salary.iloc[0]['median_salary']
print(f"\n4. Highest-paying country: {best_country} (${best_country_salary:,.0f})")

# Finding 5: Satisfaction correlation
satisfaction_corr = df['salary_local_currency'].corr(df['job_satisfaction_score'])
print(f"\n5. Salary-satisfaction correlation: {satisfaction_corr:.3f} (weak positive)")

print("\n" + "=" * 70)
```

## Notes for Next Weeks

- Week 2: Data cleaning (handle outliers, normalize currencies)
- Week 3: SQL transformations and deeper aggregations
- Week 4: Advanced analysis (gender pay gap, education impact)
- Week 5: Insights report and documentation
- Week 6: Build Streamlit dashboard
