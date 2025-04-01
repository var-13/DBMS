from flask import Blueprint, render_template, redirect, url_for, flash, request, abort
from flask_login import login_required, current_user

from app import db
from app.models import Activity, Trip

activities_bp = Blueprint('activities', __name__)

@activities_bp.route('/')
@login_required
def index():
    """List all activities for the current user."""
    activities = Activity.query.join(Trip).filter(Trip.user_id == current_user.id).all()
    return render_template('activities/index.html', activities=activities) 