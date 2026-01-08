import psycopg2
import pandas as pd
from sklearn.ensemble import IsolationForest

# Connect to DB
conn = psycopg2.connect(
    dbname="tesla_ai_db",
    user="postgres",
    password="Mamapipi1234#",  # Your new password
    host="localhost",
    port="5432"
)
df = pd.read_sql("SELECT ride_id, speed_kmh, distance_km, fare_ksh FROM rides", conn)
conn.close()

print(f"Loaded {len(df)} rides for anomaly detection")

# Features for AI
X = df[['speed_kmh', 'distance_km', 'fare_ksh']]

# Train Isolation Forest (detects outliers)
model = IsolationForest(contamination=0.1, random_state=42)  # 10% anomalies
model.fit(X)

# Predict: -1 = anomaly, 1 = normal
df['predicted_anomaly'] = model.predict(X)

# Calculate revenue loss only for anomalies (vectorized!)
df['revenue_loss_ksh'] = df.apply(lambda row: row['fare_ksh'] * 0.2 if row['predicted_anomaly'] == -1 else 0, axis=1)

# Results
anomalies = df[df['predicted_anomaly'] == -1]
print(f"\nDetected {len(anomalies)} anomalous rides (slow/high-loss)")
print(anomalies[['ride_id', 'speed_kmh', 'distance_km', 'fare_ksh', 'revenue_loss_ksh']].head(10))

total_loss = anomalies['revenue_loss_ksh'].sum()
print(f"\nPotential revenue loss from anomalies: KSh {total_loss:.2f}")
print("AI Recommendation: Reroute or incentivize drivers in low-speed zones!")

# Save to predictions table (optional)
conn = psycopg2.connect(dbname="tesla_ai_db", user="denwetende", host="localhost")
cur = conn.cursor()
for _, row in anomalies.iterrows():
    cur.execute("INSERT INTO predictions (ride_id, predicted_anomaly, revenue_loss_ksh) VALUES (%s, %s, %s)",
                (row['ride_id'], 1, row['revenue_loss_ksh']))
conn.commit()
conn.close()
print("Anomalies saved to warehouse!")
