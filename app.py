from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/rover")
def rover():
    # Simulated sensor data
    data = {
        "lat": 12.2958 + random.uniform(-0.001, 0.001),
        "lon": 76.6394 + random.uniform(-0.001, 0.001),
        "yaw": random.randint(0, 360),
        "speed": random.uniform(0, 2)
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
