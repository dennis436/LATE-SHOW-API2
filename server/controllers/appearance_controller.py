# server/controllers/appearance_controller.py

from flask import Blueprint, request, jsonify
from server.models.appearance import Appearance
from server.models import db

appearance_bp = Blueprint('appearances', __name__)

@appearance_bp.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()

    guest_id = data.get("guest_id")
    episode_id = data.get("episode_id")
    rating = data.get("rating")

    if not guest_id or not episode_id or rating is None:
        return jsonify({"error": "Missing required fields"}), 400

    new_appearance = Appearance(
        guest_id=guest_id,
        episode_id=episode_id,
        rating=rating
    )

    db.session.add(new_appearance)
    db.session.commit()

    return jsonify({
        "id": new_appearance.id,
        "guest_id": new_appearance.guest_id,
        "episode_id": new_appearance.episode_id,
        "rating": new_appearance.rating
    }), 201
