from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user

from app import db
from app.models import Destination

destinations_bp = Blueprint('destinations', __name__)

@destinations_bp.route('/')
def index():
    """List all destinations."""
    destinations = Destination.query.order_by(Destination.popularity.desc()).all()
    return render_template('destinations/index.html', destinations=destinations)

@destinations_bp.route('/<destination_id>')
def view(destination_id):
    """View a specific destination."""
    destination = Destination.query.get_or_404(destination_id)
    return render_template('destinations/view.html', destination=destination) 