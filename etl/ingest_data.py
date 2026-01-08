import psycopg2
import pandas as pd

conn = psycopg2.connect(
    dbname="tesla_ai_db",
    user="postgres",
    password="Mamapipi1234#",  # Your new password
    host="localhost",
    port="5432"
)
cur = conn.cursor()

df = pd.read_csv('simulated_tesla_ride_data.csv')

for index, row in df.iterrows():
    cur.execute("""
        INSERT INTO rides (ride_id, driver_id, pickup, dropoff, timestamp, distance_km, fare_ksh, speed_kmh, anomaly)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (row['ride_id'], row['driver_id'], row['pickup'], row['dropoff'], row['timestamp'], row['distance_km'], row['fare_ksh'], row['speed_kmh'], row['anomaly']))

conn.commit()
conn.close()
print("Ingested 500 rides into warehouse!")
