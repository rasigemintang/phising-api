from flask import Blueprint, request, jsonify
from app.db import campaigns, track_clicks
import uuid, datetime

phishing_routes = Blueprint('phishing_routes', __name__)

@phishing_routes.route("/create-campaign", methods=["POST"])
def create_campaign():
    data = request.json
    campaign_id = str(uuid.uuid4())
    campaign = {
        "id": campaign_id,
        "name": data.get("name"),
        "targets": data.get("targets", []),
        "created_at": datetime.datetime.utcnow()
    }
    campaigns.append(campaign)
    return jsonify({"message": "Campaign created", "campaign_id": campaign_id})

@phishing_routes.route("/send-email", methods=["POST"])
def send_email():
    data = request.json
    campaign_id = data.get("campaign_id")
    # Simulasi kirim email
    return jsonify({"message": f"Simulated phishing email sent for campaign {campaign_id}"})

@phishing_routes.route("/track-clicks", methods=["GET"])
def track():
    return jsonify(track_clicks)

@phishing_routes.route("/report", methods=["GET"])
def report():
    return jsonify({"campaigns": campaigns, "clicks": track_clicks})
