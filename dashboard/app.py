"""
Streamlit dashboard for Tech Salary Analysis
Interactive exploration of 180k tech job records
"""

import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import plotly.graph_objects as go

# Page config
st.set_page_config(page_title="Tech Salary Analysis", layout="wide")

# Title
st.title(" Global Tech Salary Analysis")
st.markdown("Interactive analysis of 180,000 tech job records")

# Load data from database
@st.cache_data
def load_data():
    conn = sqlite3.connect('tech_salary.db')
    df = pd.read_sql_query("SELECT * FROM jobs", conn)
    conn.close()
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filters")

selected_experience = st.sidebar.multiselect(
    "Experience Level",
    options=df['experience_level'].unique(),
    default=df['experience_level'].unique()
)

selected_country = st.sidebar.multiselect(
    "Country",
    options=df['country'].unique(),
    default=df['country'].unique()
)

selected_skill = st.sidebar.multiselect(
    "Primary Skill",
    options=df['primary_skill'].unique(),
    default=df['primary_skill'].unique()[:5]
)

# Filter data
filtered_df = df[
    (df['experience_level'].isin(selected_experience)) &
    (df['country'].isin(selected_country)) &
    (df['primary_skill'].isin(selected_skill))
]

st.sidebar.markdown(f"**Records shown:** {len(filtered_df):,}")



## Key Metrics

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Average Salary", f"${filtered_df['salary_local_currency'].mean():,.0f}")

with col2:
    st.metric("Median Salary", f"${filtered_df['salary_local_currency'].median():,.0f}")

with col3:
    st.metric("Total Jobs", f"{len(filtered_df):,}")

with col4:
    st.metric("Avg Satisfaction", f"{filtered_df['job_satisfaction_score'].mean():.1f}/5")


## Visualizations

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Skills", "Experience", "Company Size", "Countries", "Remote Work"])

with tab1:
    st.subheader("Salary by Skill")
    skill_data = filtered_df.groupby('primary_skill')['salary_local_currency'].median().sort_values(ascending=False).head(10)
    fig = px.bar(x=skill_data.values, y=skill_data.index, orientation='h', title="Top 10 Skills by Median Salary")
    fig.update_xaxes(title="Median Salary")
    fig.update_yaxes(title="Skill")
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("Salary by Experience Level")
    exp_order = ['Entry', 'Mid', 'Senior', 'Lead']
    exp_data = filtered_df.groupby('experience_level')['salary_local_currency'].median().reindex(exp_order)
    fig = px.bar(x=exp_data.index, y=exp_data.values, title="Salary by Experience Level")
    fig.update_xaxes(title="Experience Level")
    fig.update_yaxes(title="Median Salary")
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.subheader("Salary by Company Size")
    company_data = filtered_df.groupby('company_size')['salary_local_currency'].median().sort_values(ascending=False)
    fig = px.bar(x=company_data.index, y=company_data.values, title="Salary by Company Size")
    fig.update_xaxes(title="Company Size")
    fig.update_yaxes(title="Median Salary")
    st.plotly_chart(fig, use_container_width=True)

with tab4:
    st.subheader("Salary by Country")
    country_data = filtered_df.groupby('country')['salary_local_currency'].median().sort_values(ascending=False)
    fig = px.bar(x=country_data.index, y=country_data.values, title="Salary by Country")
    fig.update_xaxes(title="Country")
    fig.update_yaxes(title="Median Salary")
    st.plotly_chart(fig, use_container_width=True)

with tab5:
    st.subheader("Salary by Remote Work Type")
    remote_data = filtered_df[filtered_df['remote_type'].notna()].groupby('remote_type')['salary_local_currency'].median().sort_values(ascending=False)
    fig = px.bar(x=remote_data.index, y=remote_data.values, title="Salary by Remote Work Type")
    fig.update_xaxes(title="Remote Work Type")
    fig.update_yaxes(title="Median Salary")
    st.plotly_chart(fig, use_container_width=True)


## Data Table

st.subheader("Raw Data")
st.dataframe(filtered_df[['job_title', 'company_size', 'experience_level', 'country', 'salary_local_currency', 'primary_skill', 'remote_type']], use_container_width=True)


## Footer

st.markdown("---")
st.markdown("**About this analysis:** 180,000 tech job records analyzed with Python, SQL, and Streamlit. [View GitHub](https://github.com/YOUR_USERNAME/tech-salary-analysis)")