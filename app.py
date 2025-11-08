from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Load dataset
DATA_PATH = "livestock_behavior_50000.csv"
df = pd.read_csv(DATA_PATH)

# Convert timestamp to datetime (optional)
if 'timestamp' in df.columns:
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

@app.route('/')
def home():
    animal_ids = df['animal_id'].unique().tolist()
    return render_template('index.html', animal_ids=animal_ids)

@app.route('/details', methods=['POST'])
def details():
    animal_id = request.form.get('animal_id')
    animal_data = df[df['animal_id'] == animal_id]

    if animal_data.empty:
        return render_template('animal_details.html', error=f"No data found for Animal ID: {animal_id}")

    # Sort and get latest record
    animal_data = animal_data.sort_values(by='timestamp', ascending=False)
    latest = animal_data.iloc[0]

    avg_temp = round(animal_data['temperature_c'].mean(), 2)
    avg_hr = round(animal_data['heart_rate_bpm'].mean(), 2)
    anomaly_count = int(animal_data['anomaly'].sum())

    # Health Status logic
    if latest['temperature_c'] > 39.5 or latest['heart_rate_bpm'] > 100 or latest['anomaly'] == 1:
        status = "⚠️ Alert: Unusual Behavior Detected"
        status_class = "alert"
    else:
        status = "✅ Normal"
        status_class = "normal"

    # Generate Temperature Plot
    plt.figure(figsize=(6,3))
    plt.plot(animal_data['timestamp'], animal_data['temperature_c'], color='#00FFFF', linewidth=2)
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.title(f"Temperature Trend - {animal_id}")
    plt.grid(True, alpha=0.3)
    graph_path = f"static/{animal_id}_temp_plot.png"
    plt.tight_layout()
    plt.savefig(graph_path, facecolor='#101820')
    plt.close()

    return render_template(
        'animal_details.html',
        animal_id=animal_id,
        latest=latest,
        avg_temp=avg_temp,
        avg_hr=avg_hr,
        anomaly_count=anomaly_count,
        graph_path=graph_path,
        status=status,
        status_class=status_class
    )

if __name__ == "__main__":
    app.run(debug=True)
