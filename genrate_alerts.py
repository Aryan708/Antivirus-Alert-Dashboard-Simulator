
import random
import time
import json
from datetime import datetime

endpoints = ["Host-1", "Host-2", "Host-3", "Host-4"]
alert_types = ["Virus detected", "Suspicious file", "Scan failed", "Unauthorized access"]
severities = ["Low", "Medium", "High", "Critical"]
statuses = ["New", "In Progress", "Resolved"]

alerts = []

for i in range(15):  # Generate 15 fake alerts
    alert = {
        "id": i + 1,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "endpoint": random.choice(endpoints),
        "type": random.choice(alert_types),
        "severity": random.choice(severities),
        "status": random.choice(statuses)
    }
    alerts.append(alert)
    time.sleep(0.1)  # Simulate time delay

with open('alerts.json', 'w') as f:
    json.dump(alerts, f, indent=2)

print("Generated alerts and saved to alerts.json")
