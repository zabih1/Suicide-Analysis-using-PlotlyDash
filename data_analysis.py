import pandas as pd
import plotly.express as px

df = pd.read_csv('suicide Data.csv')

# ---------------------------- Q1 ----------------------------
# Is the suicide rate more prominent in some age categories than others?
age_suicide_rate = df.groupby('age')['suicides_no'].mean().reset_index()
fig_age_suicide = px.pie(
    age_suicide_rate,
    values='suicides_no',
    names='age',
    title="Average Suicide Rate by Age Category",
    template="plotly_dark",
    color_discrete_sequence=px.colors.qualitative.Dark2
)

# ---------------------------- Q2 ----------------------------
# Which countries have the most and the least number of suicides?
country_suicides = df.groupby('country')['suicides_no'].sum().reset_index().sort_values('suicides_no')
most_suicides = country_suicides.tail(10)
least_suicides = country_suicides.head(10)

fig_most_suicides = px.bar(
    most_suicides,
    x='country',
    y='suicides_no',
    title="Top 10 Countries with Most Suicides",
    template="plotly_dark",
    color='country'
)

fig_least_suicides = px.bar(
    least_suicides,
    x='country',
    y='suicides_no',
    title="Top 10 Countries with Least Suicides",
    template="plotly_dark",
    color='country'
)

# ---------------------------- Q3 ----------------------------
# What is the effect of the population on suicide rates?
fig_pop_vs_suicides = px.scatter(
    df,
    x='population',
    y='suicides_no',
    title="Population vs. Number of Suicides",
    template="plotly_dark",
    trendline="ols", 
    hover_data=['country']
)

# ---------------------------- Q4 ----------------------------
# What is the effect of the GDP of a country on suicide rates?
fig_gdp_vs_suicides = px.scatter(
    df,
    x='gdp_per_capita ($)',
    y='suicides_no',
    title="GDP per Capita vs. Suicide Rate",
    template="plotly_dark",
    trendline="ols",
    hover_data=['country']
)

# ---------------------------- Q5 ----------------------------
# What is the trend of suicide rates across all the years?
year_suicide = df.groupby('year')['suicides_no'].sum().reset_index()
fig_year_trend = px.line(
    year_suicide,
    x='year',
    y='suicides_no',
    title="Trend of Suicide Rates Across the Years",
    template="plotly_dark",
    markers=True
)

# ---------------------------- Q6 ----------------------------
# Is there a difference between the suicide rates of men and women?
sex_analysis = df.groupby('sex')['suicides_no'].mean().reset_index()
fig_sex_suicide = px.bar(
    sex_analysis,
    x='sex',
    y='suicides_no',
    title="Average Suicide Rate by Sex",
    template="plotly_dark",
    color='sex'
)

# ---------------------------- Q7 ----------------------------
# Show the Number of Suicides by Generation
generation_suicides = df.groupby('generation')['suicides_no'].sum().reset_index()
fig_generation_suicide = px.bar(
    generation_suicides,
    x='generation',
    y='suicides_no',
    title="Suicides by Generation",
    template="plotly_dark",
    color='generation'
)
