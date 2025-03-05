from flask import Flask, render_template
import plotly.graph_objs as go
import pandas as pd
import json

app = Flask(__name__)

# Sample data
data = {
    'Date': pd.date_range(start='2024-03-01', periods=10, freq='D'),
    'Solar Panel Efficiency': [68, 70, 72, 65, 75, 80, 78, 82, 79, 77],
    'Solar Power Generation (kW)': [8.8, 9.0, 9.5, 7.5, 10.2, 10.8, 11.0, 12.0, 11.5, 10.9],
    'Energy Consumption (kWh)': [10, 11, 12, 9, 13, 14, 15, 16, 15, 14],
    'Battery Level': [98, 96, 95, 94, 92, 90, 89, 88, 87, 86],
    'Temperature (°F)': [89.6, 88.5, 87.2, 86.0, 85.5, 84.0, 83.8, 83.5, 83.2, 83.0]
}
df = pd.DataFrame(data)

# Function to generate gauge chart
def create_gauge(value, title, max_range):
    return go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=value,
            title={'text': title},
            gauge={'axis': {'range': [0, max_range]}}
        )
    ).to_json()

@app.route('/')
def index():
    charts = {
        "solar_efficiency": create_gauge(df['Solar Panel Efficiency'].iloc[-1], "Solar Panel Efficiency", 100),
        "solar_power": create_gauge(df['Solar Power Generation (kW)'].iloc[-1], "Solar Power Generation (kW)", 15),
        "energy_consumption": create_gauge(df['Energy Consumption (kWh)'].iloc[-1], "Energy Consumption (kWh)", 20),
        "battery_level": create_gauge(df['Battery Level'].iloc[-1], "Battery Level", 100),
        "temperature": create_gauge(df['Temperature (°F)'].iloc[-1], "Temperature (°F)", 100)
    }
    return render_template('dashboard.html', charts=json.dumps(charts))

if __name__ == '__main__':
    app.run(debug=True)
