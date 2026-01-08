import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px

st.title("Tesla-Style Kenyan Autonomous Fleet Revenue AI Dashboard 🚕")

conn = psycopg2.connect(
    dbname="tesla_ai_db",
    user="postgres",
    password="Mamapipi1234#",  # Your new password
    host="localhost",
    port="5432"
)
df_rides = pd.read_sql("SELECT * FROM rides", conn)
df_anomalies = pd.read_sql("SELECT * FROM predictions", conn)
conn.close()

st.header("Fleet Ride Summary")
fig_rides = px.bar(df_rides, x='pickup', y='fare_ksh', title="Fares by Pickup Location")
st.plotly_chart(fig_rides)

st.header("AI Anomaly Detection")
st.dataframe(df_anomalies)

total_loss = df_anomalies['revenue_loss_ksh'].sum()
st.success(f"AI prevented potential revenue loss: KSh {total_loss:.2f}")
