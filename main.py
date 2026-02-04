import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Dashboard Covid-19",
    layout="wide"
)

st.title("📊 Dashboard – Casos de Covid-19")
st.markdown("Análise temporal de casos acumulados por país")

@st.cache_data
def load_data():
    df = pd.read_csv("WHO_time_series.csv")
    df["Date_reported"] = pd.to_datetime(df["Date_reported"])
    return df

df = load_data()

st.sidebar.header("Filtros")

lista_paises = sorted(df["Country"].unique())

paises_selecionados = st.sidebar.multiselect(
    "Selecione os países:",
    lista_paises,
    default=lista_paises[:3]
)

if not paises_selecionados:
    st.warning("Selecione pelo menos um país.")
    st.stop()

df_filtrado = df[df["Country"].isin(paises_selecionados)]

fig = px.line(
    df_filtrado,
    x="Date_reported",
    y="Cumulative_cases",
    color="Country",
    labels={
        "Date_reported": "Data",
        "Cumulative_cases": "Casos acumulados",
        "Country": "País"
    }
)

fig.update_layout(
    legend_title_text="País",
    hovermode="x unified"
)

st.plotly_chart(
    fig,
    use_container_width=True,
    key="grafico_covid"
)

with st.expander("📄 Ver dados filtrados"):
    st.dataframe(df_filtrado)
