from flask import Flask
from app.routes import phishing_routes

app = Flask(__name__)
app.register_blueprint(phishing_routes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)