import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('WHO_time_series.csv')

fig1 = px.line(df, x='Date_reported', y= 'Cumulative_cases', color='Country', title= 'Dados de Covid-19 2020')
fig1.update_layout(xaxis_title='Data', yaxis_title='Casos Acumulados', title_font_size= 30)

st.title("DASHCOVID: Um Dashboard sobre os Dados de COVID-19 - 2020")

st.plotly_chart(fig1, use_container_width=True)
