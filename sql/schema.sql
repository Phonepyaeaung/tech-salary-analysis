-- Tech Salary Analysis Database Schema
-- Purpose: Structured storage for tech job salary data analysis

-- Main jobs table
CREATE TABLE IF NOT EXISTS jobs (
    job_id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_title VARCHAR(255) NOT NULL,
    company_size VARCHAR(50) NOT NULL,
    employment_type VARCHAR(50) NOT NULL,
    experience_level VARCHAR(50) NOT NULL,
    years_experience INTEGER,
    education_level VARCHAR(100),
    country VARCHAR(100) NOT NULL,
    salary_local_currency DECIMAL(15, 2),
    currency VARCHAR(10),
    remote_type VARCHAR(50),
    primary_skill VARCHAR(100),
    secondary_skill VARCHAR(100),
    work_hours_per_week INTEGER,
    job_satisfaction_score DECIMAL(3, 1),
    company_rating DECIMAL(3, 1),
    age INTEGER,
    gender VARCHAR(50),
    data_load_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_job_title ON jobs(job_title);
CREATE INDEX IF NOT EXISTS idx_country ON jobs(country);
CREATE INDEX IF NOT EXISTS idx_experience_level ON jobs(experience_level);
CREATE INDEX IF NOT EXISTS idx_primary_skill ON jobs(primary_skill);
CREATE INDEX IF NOT EXISTS idx_company_size ON jobs(company_size);
CREATE INDEX IF NOT EXISTS idx_salary ON jobs(salary_local_currency);