# server/controllers/guest_controller.py

from flask import Blueprint, request, jsonify
from server.models.guest import Guest
from server.models import db

guest_bp = Blueprint('guests', __name__)

@guest_bp.route('/guests', methods=['POST'])
def create_guest():
    data = request.get_json()

    name = data.get('name')
    occupation = data.get('occupation')

    if not name or not occupation:
        return jsonify({"error": "Missing name or occupation"}), 400

    new_guest = Guest(name=name, occupation=occupation)

    db.session.add(new_guest)
    db.session.commit()

    return jsonify({
        "id": new_guest.id,
        "name": new_guest.name,
        "occupation": new_guest.occupation
    }), 201
