# 🚕 Tesla Data Engine Simulation — Kenyan Ride-Hailing 🇰🇪

Simulation of Tesla's famous "Data Engine" for Full Self-Driving, adapted for Kenyan ride-hailing fleet optimization.

## 🎯 Goal
Detect anomalous rides (slow speed = lost revenue) using AI to increase fleet earnings 20-30%.

## 🛠️ Tech Stack
- Python (pandas, scikit-learn)
- PostgreSQL warehouse
- Simulated Nairobi ride data (500 rides)
- Isolation Forest for anomaly detection

## 📊 Features
- Ride data generation (locations, fares, speeds)
- AI detects low-efficiency rides
- Revenue loss calculation
- Ready for Streamlit dashboard & Airflow

## 🚀 Run Locally
1. Clone repo
2. venv: `python3 -m venv venv && source venv/bin/activate`
3. Install: `pip install psycopg2-binary pandas scikit-learn`
4. Setup DB `tesla_ai_db`
5. Run schema: `sudo -u postgres psql -d tesla_ai_db -f schema/create_tables.sql`
6. Generate data: `python etl/generate_data.py`
7. Run AI: `python ai/anomaly_detection.py`

## Sample Output
Detected 48 anomalous rides
Potential revenue loss: KSh 45,230.00
AI Recommendation: Reroute drivers in low-speed zones

Built by **Eden Wetende** — Data Engineer  
January 2026

Inspired by Tesla's FSD data engine — applied to Kenyan mobility!

⭐ Star if you like AI for revenue!
