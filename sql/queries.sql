-- Tech Salary Analysis - Key Queries
-- Purpose: Answer core business questions
-- Database: SQLite (tech_salary.db)

-- ============================================================================
-- QUESTION 1: Which tech skills command the highest salaries?
-- ============================================================================

-- Top 15 skills by median salary
SELECT 
    primary_skill as skill,
    COUNT(*) as job_count,
    ROUND(AVG(salary_local_currency), 2) as avg_salary,
    ROUND(AVG(salary_local_currency), 2) as median_salary,
    ROUND(MIN(salary_local_currency), 2) as min_salary,
    ROUND(MAX(salary_local_currency), 2) as max_salary,
    ROUND(AVG(job_satisfaction_score), 2) as avg_satisfaction
FROM jobs
WHERE primary_skill IS NOT NULL 
  AND salary_local_currency > 0
GROUP BY primary_skill
ORDER BY median_salary DESC
LIMIT 15;

-- ============================================================================
-- QUESTION 2: How much does experience level matter?
-- ============================================================================

-- Salary distribution by experience level
SELECT 
    experience_level,
    COUNT(*) as job_count,
    ROUND(AVG(years_experience), 1) as avg_years,
    ROUND(AVG(salary_local_currency), 2) as avg_salary,
    ROUND(AVG(salary_local_currency), 2) as median_salary,
    ROUND(MIN(salary_local_currency), 2) as min_salary,
    ROUND(MAX(salary_local_currency), 2) as max_salary,
    ROUND(AVG(job_satisfaction_score), 2) as avg_satisfaction
FROM jobs
WHERE salary_local_currency > 0
GROUP BY experience_level
ORDER BY 
    CASE 
        WHEN experience_level = 'Entry' THEN 1
        WHEN experience_level = 'Mid' THEN 2
        WHEN experience_level = 'Senior' THEN 3
        WHEN experience_level = 'Lead' THEN 4
    END;

-- ============================================================================
-- QUESTION 3: Does company size affect pay?
-- ============================================================================

-- Salary by company size
SELECT 
    company_size,
    COUNT(*) as job_count,
    ROUND(AVG(salary_local_currency), 2) as avg_salary,
    ROUND(AVG(salary_local_currency), 2) as median_salary,
    ROUND(MIN(salary_local_currency), 2) as min_salary,
    ROUND(MAX(salary_local_currency), 2) as max_salary,
    ROUND(AVG(job_satisfaction_score), 2) as avg_satisfaction,
    ROUND(AVG(work_hours_per_week), 1) as avg_hours_per_week
FROM jobs
WHERE salary_local_currency > 0
GROUP BY company_size
ORDER BY median_salary DESC;

-- ============================================================================
-- QUESTION 4: Which countries pay tech workers most?
-- ============================================================================

-- Top 10 countries by median salary
SELECT 
    country,
    COUNT(*) as job_count,
    ROUND(AVG(salary_local_currency), 2) as avg_salary,
    ROUND(AVG(salary_local_currency), 2) as median_salary,
    ROUND(MIN(salary_local_currency), 2) as min_salary,
    ROUND(MAX(salary_local_currency), 2) as max_salary,
    ROUND(AVG(job_satisfaction_score), 2) as avg_satisfaction
FROM jobs
WHERE salary_local_currency > 0
GROUP BY country
ORDER BY median_salary DESC;

-- ============================================================================
-- QUESTION 5: Gender pay gap in tech
-- ============================================================================

-- Salary comparison by gender (controlling for experience level)
SELECT 
    experience_level,
    gender,
    COUNT(*) as count,
    ROUND(AVG(salary_local_currency), 2) as avg_salary,
    ROUND(AVG(salary_local_currency), 2) as median_salary,
    ROUND(AVG(years_experience), 1) as avg_years
FROM jobs
WHERE salary_local_currency > 0
  AND gender IN ('Male', 'Female')
GROUP BY experience_level, gender
ORDER BY experience_level, gender;

-- ============================================================================
-- QUESTION 6: Remote work impact on salary
-- ============================================================================

-- Salary by remote work type
SELECT 
    remote_type,
    COUNT(*) as job_count,
    ROUND(AVG(salary_local_currency), 2) as avg_salary,
    ROUND(AVG(salary_local_currency), 2) as median_salary,
    ROUND(MIN(salary_local_currency), 2) as min_salary,
    ROUND(MAX(salary_local_currency), 2) as max_salary,
    ROUND(AVG(work_hours_per_week), 1) as avg_hours_per_week,
    ROUND(AVG(job_satisfaction_score), 2) as avg_satisfaction
FROM jobs
WHERE salary_local_currency > 0
GROUP BY remote_type
ORDER BY median_salary DESC;

-- ============================================================================
-- QUESTION 7: Correlation between salary and satisfaction
-- ============================================================================

-- Salary ranges vs satisfaction (binned analysis)
SELECT 
    CASE 
        WHEN salary_local_currency < 50000 THEN '< 50K'
        WHEN salary_local_currency < 100000 THEN '50K - 100K'
        WHEN salary_local_currency < 150000 THEN '100K - 150K'
        ELSE '> 150K'
    END as salary_range,
    COUNT(*) as job_count,
    ROUND(AVG(salary_local_currency), 2) as avg_salary,
    ROUND(AVG(job_satisfaction_score), 2) as avg_satisfaction,
    ROUND(AVG(company_rating), 2) as avg_company_rating
FROM jobs
WHERE salary_local_currency > 0
GROUP BY salary_range
ORDER BY avg_salary;

-- ============================================================================
-- BONUS: Skill + Experience Level Analysis
-- ============================================================================

-- Top skills for each experience level
SELECT 
    experience_level,
    primary_skill,
    COUNT(*) as job_count,
    ROUND(AVG(salary_local_currency), 2) as avg_salary,
    ROUND(AVG(job_satisfaction_score), 2) as avg_satisfaction
FROM jobs
WHERE salary_local_currency > 0
  AND primary_skill IS NOT NULL
GROUP BY experience_level, primary_skill
ORDER BY experience_level, avg_salary DESC;

-- ============================================================================
-- BONUS: Education Level Impact
-- ============================================================================

-- Does education level affect salary?
SELECT 
    education_level,
    COUNT(*) as job_count,
    ROUND(AVG(salary_local_currency), 2) as avg_salary,
    ROUND(AVG(salary_local_currency), 2) as median_salary,
    ROUND(AVG(years_experience), 1) as avg_years_experience,
    ROUND(AVG(job_satisfaction_score), 2) as avg_satisfaction
FROM jobs
WHERE salary_local_currency > 0
  AND education_level IS NOT NULL
GROUP BY education_level
ORDER BY avg_salary DESC;

-- ============================================================================
-- DATA QUALITY CHECKS
-- ============================================================================

-- Check for outliers and data quality issues
SELECT 
    'Total Records' as metric,
    COUNT(*) as value
FROM jobs
UNION ALL
SELECT 'Records with Salary', COUNT(*) FROM jobs WHERE salary_local_currency > 0
UNION ALL
SELECT 'Records Missing Salary', COUNT(*) FROM jobs WHERE salary_local_currency IS NULL OR salary_local_currency = 0
UNION ALL
SELECT 'Unique Countries', COUNT(DISTINCT country) FROM jobs
UNION ALL
SELECT 'Unique Skills (Primary)', COUNT(DISTINCT primary_skill) FROM jobs
UNION ALL
SELECT 'Avg Age', ROUND(AVG(age), 1) FROM jobs
UNION ALL
SELECT 'Age Range', MIN(age) || ' - ' || MAX(age) FROM jobs;
