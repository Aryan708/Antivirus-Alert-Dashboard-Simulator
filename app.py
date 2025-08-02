
from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def dashboard():
    with open('alerts.json') as f:
        alerts = json.load(f)
        print("ALERTS:", alerts)
    return render_template('dashboard.html', alerts=alerts)

if __name__ == '__main__':
    app.run(debug=True)
