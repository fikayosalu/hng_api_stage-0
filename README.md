# HNG Backend Task — "Me" Endpoint 🐱

This is a simple Flask API built for the HNG Backend Stage 0 task.  
The API exposes a single endpoint `/me` that returns basic user information, a timestamp, and a random cat fact fetched from an external API.

## 🚀 Features

- Returns user info (email, name, and tech stack)
- Fetches a random cat fact from the [Cat Fact API](https://catfact.ninja/fact)
- Includes a UTC timestamp in ISO format
- Handles API errors gracefully
- Supports CORS (Cross-Origin Resource Sharing)

## 🛠️ Technologies Used

- **Python 3**
- **Flask** — lightweight web framework
- **Flask-CORS** — enables cross-origin requests
- **Requests** — handles external API calls

## 📦 Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/your-username/hng_api_stage-0.git
   cd hng_api_stage-0
   ```
2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install Dependencies**
   ```bash
   pip install flask flask-cors requests
   ```

## ▶ Running the App

1. **Start the server**
   ```bash
   python3 endpoint.py
   ```
2. **Visit the endpoint in your browser**
   ```bash
   http://127.0.0.1:5000/me
   ```
