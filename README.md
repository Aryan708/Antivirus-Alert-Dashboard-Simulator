# Antivirus Alert Dashboard Simulator

## Project Overview

This project simulates an antivirus endpoint alert monitoring system similar to those used in Security Operations Centers (SOC). It generates randomized antivirus alerts from multiple simulated endpoints and displays them in a web dashboard with color-coded severity levels for easier visualization and prioritization of security incidents.

## Features

- Generates simulated antivirus alerts with details such as alert type, severity, status, timestamp, and endpoint.
- Displays alerts in a clean, interactive web dashboard built with Flask.
- Color-codes alerts based on severity levels (Critical, High, Medium, Low).
- Provides a summary of total alerts, counts of critical and new alerts.
- Includes a "Details" button that shows additional alert information via popup.
- Auto-refreshes the dashboard every 15 seconds to simulate real-time updates.

## Technologies Used

- **Python** – Backend scripting and alert generation.
- **Flask** – Micro web framework to serve the dashboard.
- **HTML/CSS and JavaScript** – Frontend visualization and interactivity.
- **JSON** – Storage format for alert data.

## Getting Started

### Prerequisites

- Python 3.6 or higher installed on your system.
- `pip` package manager.

### Installation & Setup

1. Clone the repository:

2. (Optional but recommended) Set up a virtual environment and activate it:
- On Windows:
  ```
  python -m venv venv
  venv\Scripts\activate.bat
  ```
- On macOS/Linux:
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```

3. Install required Python packages:

### Running the Project

1. Generate simulated antivirus alerts by running:
This creates or overwrites `alerts.json` with 15 randomized alert entries.

2. Start the Flask web server:

3. Open your web browser and go to:
http://localhost:5000
You will see a dashboard with color-coded alerts, summary counts, and alert details.

## How It Works

- `generate_alerts.py`: Generates random alerts for endpoints with different types, severities, statuses, and timestamps; saves alerts in `alerts.json`.
- `app.py`: Flask application reads `alerts.json` and renders the data using the `dashboard.html` template.
- `templates/dashboard.html`: HTML template which displays alerts in a table, applies color coding based on severity, and provides "Details" buttons to show alert info in popups.
- The dashboard auto-refreshes every 15 seconds to simulate live alert updates.

## Future Enhancements

- Implement real-time updates with WebSocket or server-sent events to avoid whole page refresh.
- Replace JSON file with a database like SQLite or PostgreSQL for scalability and persistence.
- Enable changing alert status (e.g., acknowledging or resolving alerts) directly from the web dashboard.
- Add filtering and search options to view specific alerts by severity, status, or time.
- Introduce user authentication and role-based access control to secure the dashboard.
- Improve frontend UI with charts, metrics, and better visualization components.

## Project Relevance

This project demonstrates a basic Security Operations Center monitoring approach using endpoint alerts, a critical part of modern enterprise cybersecurity tools like McAfee ePO and Bitdefender GravityZone. It illustrates skills in Python scripting, web development with Flask, cybersecurity concepts, and data visualization.


---

## Contact & Contributions

Feel free to raise issues, submit pull requests, or contact me for improvements and collaborations!

---

Thank you for exploring my Antivirus Alert Dashboard Simulator project
