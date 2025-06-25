# server/controllers/episode_controller.py

from flask import Blueprint, request, jsonify
from server.models.episode import Episode
from server.models import db

episode_bp = Blueprint('episodes', __name__)

@episode_bp.route('/episodes', methods=['POST'])
def create_episode():
    data = request.get_json()

    title = data.get('title')
    air_date = data.get('air_date')

    if not title or not air_date:
        return jsonify({"error": "Missing title or air_date"}), 400

    new_episode = Episode(title=title, air_date=air_date)

    db.session.add(new_episode)
    db.session.commit()

    return jsonify({
        "id": new_episode.id,
        "title": new_episode.title,
        "air_date": new_episode.air_date
    }), 201
