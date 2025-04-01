from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user

from app import db
from app.models import Trip, Destination, Weather

api_bp = Blueprint('api', __name__)

@api_bp.route('/trips', methods=['GET'])
@login_required
def get_trips():
    """API endpoint to get user trips."""
    trips = Trip.query.filter_by(user_id=current_user.id).all()
    return jsonify({
        'trips': [
            {
                'id': trip.id,
                'title': trip.title,
                'start_date': trip.start_date.isoformat(),
                'end_date': trip.end_date.isoformat(),
                'status': trip.status
            } for trip in trips
        ]
    }) 