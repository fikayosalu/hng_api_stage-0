#!/usr/bin/python3
import requests
from flask import Flask, jsonify
from datetime import datetime, timezone
from flask_cors import CORS



app = Flask(__name__)
CORS(app)

@app.route('/me', methods=['GET'])
def Info():
  try:
    response = requests.get("https://catfact.ninja/fact", timeout=5)
    data = response.json().get("fact", "Cat facts are unavailable at the moment.")
  except Exception as e:
    print(f"Error fetching cat fact: {e}")
    data = "Cat facts are unavailable at the moment."

  info  = {
    "status": "success",
    "user" : {
      "email" : "fikayosalu@gmail.com",
      "name": "Oluwafikunayomi Emmanuel Salu",
      "stack": "Python/Flask"
    },
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "fact": data
  }
  return jsonify(info), 200

if __name__ == "__main__":
  app.run(debug=True)

