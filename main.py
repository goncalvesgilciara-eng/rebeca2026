import pandas as pd
import plotly.express as px
import plotly.io as pio
import streamlit as st

pio.templates.default = 'plotly'

df = pd.read_csv('WHO_time_series.csv')

df['Date_reported'] = pd.to_datetime(df['Date_reported'])

fig1 = px.line(
    df,
    x='Date_reported',
    y='Cumulative_cases',
    color='Country',
    title='Casos Acumulados de Covid-19 - Ano 2020'
)

fig1.update_layout(
    xaxis_title='Data',
    yaxis_title='Casos Acumulados'
)

st.plotly_chart(fig1, use_container_width=True)
