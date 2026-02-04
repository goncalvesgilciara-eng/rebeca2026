import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout="wide")

st.title("Casos Acumulados de Covid-19")

df = pd.read_csv("WHO_time_series.csv")
df["Date_reported"] = pd.to_datetime(df["Date_reported"])

paises = df["Country"].unique()[:5]
df = df[df["Country"].isin(paises)]

fig = px.line(
    df,
    x="Date_reported",
    y="Cumulative_cases",
    color="Country"
)

with st.container():
    st.plotly_chart(fig, use_container_width=True, key="grafico_covid")
