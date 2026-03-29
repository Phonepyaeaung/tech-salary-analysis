# Global Tech Salary Analysis

Interactive analysis of 200,000 tech job salary records from 10 countries.

## Project Overview

This project analyzes global tech compensation trends to answer critical questions about skills demand, experience impact, and working conditions in the tech industry.

## Key Questions Answered

1. **Which tech skills pay most?** - C++ and data science frameworks lead
2. **How much does experience matter?** - Lead roles pay 2.25x more than Entry level
3. **Does company size affect salary?** - Minimal impact (Startups ≈ Enterprise)
4. **Which countries pay most?** - Global salaries relatively balanced
5. **Is higher pay linked to satisfaction?** - No correlation found
6. **Gender pay gap?** - Essentially zero across all levels
7. **Remote work impact?** - Remote pays the same as onsite

## Dataset

- **Records:** 180,000 tech job entries
- **Countries:** 10 (France, Canada, Japan, Germany, Netherlands, UK, USA, Australia, India, Brazil)
- **Dimensions:** Skills, salary, experience, company size, remote work, satisfaction, demographics

## Key Findings

### Skills & Salary
- **Top paying skills:** C++ ($137k), TensorFlow ($136k), SQL ($136k)
- **Most in-demand:** React, Docker, JavaScript

### Experience Level
- Entry: $86,348 | Mid: $111,300 | Senior: $152,640 | Lead: $194,485
- **Clear financial incentive for career advancement**

### Company Size
- Enterprise: $135,430 | Startup: $135,799 | Mid-size: $135,723 | SME: $135,346
- **Company size has almost no impact on salary**

### Gender Pay Gap
- Entry: -0.2% | Mid: +0.7% | Senior: +0.9% | Lead: -0.0%
- **Tech industry shows near-zero gender pay gap**

### Salary vs Satisfaction
- Correlation: 0.002 (essentially no relationship)
- **Higher salaries don't lead to higher job satisfaction**

## Technologies Used

- **Python:** Pandas, NumPy, SciPy, Scikit-learn
- **Visualization:** Matplotlib, Seaborn, Plotly
- **Database:** SQLite
- **Dashboard:** Streamlit

## Project Structure
```
├── data/raw/              # Original dataset
├── data/processed/        # Cleaned data
├── src/                   # Python scripts
├── sql/                   # Database queries
├── notebooks/             # Jupyter analysis
├── dashboard/             # Streamlit app
└── reports/               # Findings & charts
```

## How to Run
```bash
# Install dependencies
pip install -r requirements.txt

# Load & clean data
python src/data_loading.py
python src/cleaning.py

# Load to database
python src/load_to_sql.py

# Run analysis
python src/advanced_analysis.py
python src/visualizations.py

# View dashboard
streamlit run dashboard/app.py
```

## Visualizations

7 professional charts analyzing skills, experience, company size, geography, remote work, gender pay gap, and salary vs satisfaction.

## Limitations

- Salary data in multiple currencies (no cost-of-living adjustment)
- Single snapshot in time (not trends)
- May have sampling bias in data collection

## Future Enhancements

- Time-series trends with multi-year data
- Cost-of-living adjustments by country
- Predictive models for salary estimation
- Real-time data updates

## GitHub & Links

- [GitHub Repository](https://github.com/YOUR_USERNAME/tech-salary-analysis)
