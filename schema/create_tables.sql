CREATE TABLE rides (
    ride_id SERIAL PRIMARY KEY,
    driver_id INT,
    pickup VARCHAR(100),
    dropoff VARCHAR(100),
    timestamp TIMESTAMP,
    distance_km DECIMAL(5,2),
    fare_ksh DECIMAL(10,2),
    speed_kmh DECIMAL(5,2),
    anomaly INT
);

CREATE TABLE predictions (
    id SERIAL PRIMARY KEY,
    ride_id INT,
    predicted_anomaly INT,
    revenue_loss_ksh DECIMAL(10,2),
    run_date DATE DEFAULT CURRENT_DATE
);
