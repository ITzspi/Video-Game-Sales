import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

df_sales = pd.read_csv("datasets/vgsales.csv")

st.title("🎮 Video Game Details")

st.divider()

game_name = st.sidebar.selectbox("Select a Game", df_sales["Name"].unique())

game = df_sales[df_sales["Name"] == game_name].iloc[0]

st.header(game["Name"])
st.caption(f"**Publisher:** {game['Publisher']} | **Platform:** {game['Platform']} | **Genre:** {game['Genre']}")

st.subheader("Sales Metrics")
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("NA Sales", f"{game['NA_Sales']:.2f}")
col2.metric("EU Sales", f"{game['EU_Sales']:.2f}")
col3.metric("JP Sales", f"{game['JP_Sales']:.2f}")
col4.metric("Other Sales", f"{game['Other_Sales']:.2f}")
col5.metric("Global Sales", f"{game['Global_Sales']:.2f}")

st.divider()

st.subheader("Detailed Metrics")
metrics = {
    "Year": game["Year"],
    "Platform": game["Platform"],
    "Genre": game["Genre"],
    "Publisher": game["Publisher"],
    "Global Sales": game["Global_Sales"],
}
st.table(pd.DataFrame.from_dict(metrics, orient="index", columns=["Value"]))
