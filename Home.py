import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df_sales = pd.read_csv("datasets/vgsales.csv")

st.title("🎮 Video Game Sales")
st.divider()

sales_columns = ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]
sales_ranges = {col: (df_sales[col].min(), df_sales[col].max()) for col in sales_columns}

filters = {}
for col, (min_val, max_val) in sales_ranges.items():
    filters[col] = st.sidebar.slider(f"{col} Filter", min_val, max_val, min_val)

df_filtered = df_sales.copy()
for col, value in filters.items():
    df_filtered = df_filtered[df_filtered[col] >= value]

st.dataframe(df_filtered)

mean_sales = df_filtered[sales_columns].mean()
median_sales = df_filtered[sales_columns].median()
mode_sales = df_filtered[sales_columns].mode().iloc[0]

st.divider()
st.title("📊 Graphics")
fig_bar = px.bar(df_filtered, x="Name", y="Global_Sales", title="Global Sales by Game")
fig_hist = px.histogram(df_filtered, x="Global_Sales", title="Distribution of Global Sales", nbins=30)

st.plotly_chart(fig_bar, use_container_width=True)
st.plotly_chart(fig_hist, use_container_width=True)

st.divider()
st.title("📊 Statistics")

st.subheader("Mean")
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("NA Sales", f"{mean_sales['NA_Sales']:.2f}")
col2.metric("EU Sales", f"{mean_sales['EU_Sales']:.2f}")
col3.metric("JP Sales", f"{mean_sales['JP_Sales']:.2f}")
col4.metric("Other Sales", f"{mean_sales['Other_Sales']:.2f}")
col5.metric("Global Sales", f"{mean_sales['Global_Sales']:.2f}")

st.divider()
st.subheader("Mode")
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("NA Sales", f"{mode_sales['NA_Sales']:.2f}")
col2.metric("EU Sales", f"{mode_sales['EU_Sales']:.2f}")
col3.metric("JP Sales", f"{mode_sales['JP_Sales']:.2f}")
col4.metric("Other Sales", f"{mode_sales['Other_Sales']:.2f}")
col5.metric("Global Sales", f"{mode_sales['Global_Sales']:.2f}")

st.divider()
st.subheader("Median")
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("NA Sales", f"{median_sales['NA_Sales']:.2f}")
col2.metric("EU Sales", f"{median_sales['EU_Sales']:.2f}")
col3.metric("JP Sales", f"{median_sales['JP_Sales']:.2f}")
col4.metric("Other Sales", f"{median_sales['Other_Sales']:.2f}")
col5.metric("Global Sales", f"{median_sales['Global_Sales']:.2f}")
