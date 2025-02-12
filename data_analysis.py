import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('suicide Data.csv')

# ----------------------------------------------------- Q1 ---------------------------------
# Is the suicide rate more prominent in some age categories than others?
age_suicide_rate = df.groupby('age')['suicides_no'].mean().sort_values().reset_index()

fig_age_suicide = px.bar(
    age_suicide_rate,
    x='age',
    y='suicides_no',
    title='Average Number of Suicides by Age Category',
    labels={'age': 'Age Category', 'suicides_no': 'Average Suicides'},
    color='age',
    text='suicides_no'
)
fig_age_suicide.update_traces(textposition='outside')
fig_age_suicide.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
    xaxis=dict(title='Age Category', tickfont=dict(color='white')),
    yaxis=dict(title='Average Number of Suicides', tickfont=dict(color='white'))
)

# ----------------------------------------------------- Q2 ---------------------------------
# Which countries have the most and the least number of suicides?
country_suicides = df.groupby('country')['suicides_no'].sum().sort_values().reset_index()

fig_country_suicide = px.bar(
    country_suicides,
    x='country',
    y='suicides_no',
    title='Total Suicides by Country (Ascending Order)',
    labels={'country': 'Country', 'suicides_no': 'Total Suicides'},
    color='country',
    text='suicides_no'
)
fig_country_suicide.update_traces(textposition='outside')
fig_country_suicide.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
    xaxis=dict(title='Country', tickfont=dict(color='white')),
    yaxis=dict(title='Total Suicides', tickfont=dict(color='white'))
)

# ----------------------------------------------------- Q3 ---------------------------------
# Show the Number of Suicides by Generation
generation_suicides = df.groupby('generation')['suicides_no'].sum().reset_index()

fig_generation_suicide = px.bar(
    generation_suicides,
    x='generation',
    y='suicides_no',
    title='Total Suicides by Generation',
    labels={'generation': 'Generation', 'suicides_no': 'Total Suicides'},
    color='generation',
    text='suicides_no'
)
fig_generation_suicide.update_traces(textposition='outside')
fig_generation_suicide.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
    xaxis=dict(title='Generation', tickfont=dict(color='white')),
    yaxis=dict(title='Total Suicides', tickfont=dict(color='white'))
)
