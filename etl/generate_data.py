import pandas as pd
import random
from datetime import datetime, timedelta

# Nairobi locations
locations = ['Westlands', 'CBD', 'Kilimani', 'Ngong Road', 'Thika Road', 'Juja', 'Embakasi', 'Langata']

# Generate data
data = []
for ride_id in range(1, 501):
    pickup = random.choice(locations)
    dropoff = random.choice([l for l in locations if l != pickup])
    timestamp = datetime.now() - timedelta(days=random.randint(0, 30), hours=random.randint(0, 23))
    distance_km = round(random.uniform(5, 50), 2)
    speed_kmh = round(random.uniform(20, 80), 2)
    fare_ksh = round(distance_km * random.uniform(80, 120), 2)  # Base fare
    driver_id = random.randint(1, 100)
    
    # Simulate anomaly (slow speed = lost revenue)
    anomaly = 1 if speed_kmh < 30 else 0
    
    data.append({
        'ride_id': ride_id,
        'driver_id': driver_id,
        'pickup': pickup,
        'dropoff': dropoff,
        'timestamp': timestamp,
        'distance_km': distance_km,
        'fare_ksh': fare_ksh,
        'speed_kmh': speed_kmh,
        'anomaly': anomaly
    })

# Save to CSV
df = pd.DataFrame(data)
df.to_csv('simulated_tesla_ride_data.csv', index=False)
print("Generated simulated_tesla_ride_data.csv with 500 rides!")
