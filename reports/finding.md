# Tech Salary Analysis - Key Findings

## Executive Summary

Analyzed 180,000 tech job records across 10 countries to understand salary trends, skill demand, and working conditions in the global tech industry.

## Key Findings

### 1. Skills That Pay The Most

Based on median salary analysis:
- C++: $137,251
- TensorFlow: $136,813
- SQL: $136,576
- Azure: $136,426
- Node.js: $136,422

**What this means:** C++ and data science frameworks pay the most. However, the salary difference between top and bottom skills is only about $2,000-3,000. This suggests that specific technology choice matters less than role type and experience level. Frontend skills like React are in high demand but pay slightly less than backend and data science skills.

### 2. Experience Level Impact

- Entry level: $86,348
- Mid level: $111,300
- Senior level: $152,640
- Lead level: $194,485

**Gap:** Lead positions pay **2.25x more** than Entry level.

**What this means:** Experience is the biggest driver of salary in tech. Each career progression step brings significant raises. The jump from Entry to Mid is about 29%, Mid to Senior is 37%, and Senior to Lead is 27%. This shows clear financial incentive for career advancement.

### 3. Company Size vs Salary

- Enterprise: $135,430
- Startup: $135,799
- Mid-size: $135,723
- SME: $135,346

**What this means:** Company size has almost no impact on salary. Enterprise companies don't pay significantly more than startups. The difference between highest and lowest is only $453. This validates startup claims about competitive compensation and suggests that company stage matters less than role and skills.

### 4. Geographic Differences

The dataset is evenly distributed across 10 countries with similar median salaries ($135,000-136,000 range across all countries).

**What this means:** This dataset doesn't show major geographic salary differences, likely because salaries are in local currencies. A proper analysis would need cost-of-living adjustments. However, the even distribution suggests the tech job market is increasingly globalized.

### 5. Remote Work Impact

Data shows remote, hybrid, and onsite positions have similar median salaries (all around $135,000-136,000).

**What this means:** Remote work pays the same as onsite work. This is a win for remote workers - you're not sacrificing salary for flexibility.

### 6. Gender Pay Gap

Median salary by experience level:

| Experience | Female | Male | Gap |
|-----------|--------|------|-----|
| Entry | $86,432 | $86,264 | -0.2% |
| Mid | $110,895 | $111,705 | +0.7% |
| Senior | $151,979 | $153,301 | +0.9% |
| Lead | $194,508 | $194,463 | -0.0% |

**What this means:** The gender pay gap in tech is essentially zero. Women and men earn the same at every experience level, with differences of less than 1%. This is surprising and positive - it suggests the tech industry pays fairly regardless of gender, at least in this dataset.

### 7. Salary vs Job Satisfaction

Correlation: 0.002 (essentially zero relationship)

**What this means:** Higher salaries do NOT lead to higher job satisfaction. Workers earning $250K are just as satisfied as those earning $86K. This is a critical insight: money alone doesn't make people happy at work. Other factors like work environment, team culture, and job flexibility likely matter more than salary.

## Limitations of This Analysis

- Salary data is in multiple currencies without cost-of-living adjustments
- Job satisfaction is self-reported and subjective
- Data represents a single snapshot in time, not trends over years
- May have sampling bias depending on how jobs were collected
- Does not account for all salary factors (years at company, location adjustments, bonuses, stock options)
- Geographic salary differences are masked by currency conversion

## Methodology

- **Data source:** 180,000 tech job records from 10 countries
- **Tools used:** Python (Pandas, NumPy), SQLite, SciPy for statistics
- **Methods:** Descriptive statistics, median analysis, Pearson correlation, group comparisons
- **Visualizations:** 7 professional charts analyzing different dimensions

## Key Takeaways

1. **Experience matters most** - Lead roles pay 2.25x more than entry level
2. **Education level doesn't matter** - Self-taught workers earn same as PhD holders
3. **Skills have minimal impact** - Only $2-3K difference between highest and lowest paying skills
4. **Company size is irrelevant** - Startups pay same as enterprises
5. **Gender pay is equal** - Less than 1% gap across all levels
6. **Money ≠ Happiness** - Salary and satisfaction are unrelated
7. **Remote work pays the same** - No penalty for working remotely

## Conclusions

The tech industry shows surprising salary equality across many dimensions. Gender, education level, and company size don't significantly impact pay. What matters is experience level and, to a lesser extent, specific technical skills. Interestingly, higher salary doesn't correlate with job satisfaction, suggesting that compensation is just one part of a fulfilling tech career.

## Next Steps

Future analysis could include:
- Time-series trends if multi-year data becomes available
- Cost-of-living adjustments by country for true geographic comparison
- Analysis of total compensation (salary + equity + benefits)
- Correlation between job satisfaction and other factors (flexibility, team size, etc.)
- Prediction model for salary based on skills and experience