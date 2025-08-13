import plotly.express as px
import pandas as pd

def sales_by_category(df: pd.DataFrame):
    sales_cat = df.groupby("Category")["Sales"].sum().reset_index()
    fig = px.bar(sales_cat, x="Category", y="Sales", title="Vendas por Categoria")
    return fig

def sales_over_time(df: pd.DataFrame):
    sales_time = df.groupby("Month-Year")["Sales"].sum().reset_index()
    fig = px.line(sales_time, x="Month-Year", y="Sales", title="Vendas ao longo do tempo", markers=True)
    return fig

def profit_by_region(df: pd.DataFrame):
    profit_region = df.groupby("Region")["Profit"].sum().reset_index()
    fig = px.bar(profit_region, x="Region", y="Profit", title="Lucro por Região")
    return fig
