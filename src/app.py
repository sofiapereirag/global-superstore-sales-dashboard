import streamlit as st
from data_loader import load_data
from plots import sales_by_category, sales_over_time, profit_by_region
from utils import format_currency

# Configuração inicial
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# Título
st.title("Sales Dashboard — Global Superstore")

# Carregar dados
df = load_data("data/processed/superstore.csv")

# Filtros na barra lateral
st.sidebar.header("Filters")
year_filter = st.sidebar.multiselect("Year.Order", sorted(df["Year.Order"].unique()), default=df["Year.Order"].unique())
region_filter = st.sidebar.multiselect("Region", sorted(df["Region"].unique()), default=df["Region"].unique())

# Aplicar filtros
df_filtered = df[(df["Year.Order"].isin(year_filter)) & (df["Region"].isin(region_filter))]

# KPIs
total_sales = df_filtered["Sales"].sum()
total_profit = df_filtered["Profit"].sum()
total_orders = df_filtered["Order.ID"].nunique()

col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", format_currency(total_sales))
col2.metric("Total Profit", format_currency(total_profit))
col3.metric("Total Orders", f"{total_orders:,}".replace(",", "."))

# Gráficos
col4, col5 = st.columns(2)
col4.plotly_chart(sales_by_category(df_filtered), use_container_width=True)
col5.plotly_chart(profit_by_region(df_filtered), use_container_width=True)

st.plotly_chart(sales_over_time(df_filtered), use_container_width=True)

