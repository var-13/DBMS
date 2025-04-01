from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_required, current_user
from datetime import datetime

from app import db
from app.models import Trip, Destination, Review

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Home page route."""
    # Get featured destinations
    featured_destinations = Destination.query.order_by(Destination.popularity.desc()).limit(6).all()
    
    # Get recent reviews
    recent_reviews = Review.query.filter_by(is_public=True).order_by(Review.created_at.desc()).limit(3).all()
    
    # If user is logged in, get their upcoming trips
    upcoming_trips = []
    if current_user.is_authenticated:
        upcoming_trips = Trip.query.filter_by(user_id=current_user.id).order_by(Trip.start_date).limit(3).all()
    
    return render_template('index.html', 
                          featured_destinations=featured_destinations,
                          recent_reviews=recent_reviews,
                          upcoming_trips=upcoming_trips)

@main_bp.route('/about')
def about():
    """About page route."""
    return render_template('about.html')

@main_bp.route('/contact')
def contact():
    """Contact page route."""
    return render_template('contact.html')

@main_bp.route('/privacy')
def privacy():
    """Privacy policy page route."""
    return render_template('privacy.html')

@main_bp.route('/terms')
def terms():
    """Terms of service page route."""
    return render_template('terms.html')

@main_bp.route('/dashboard')
@login_required
def dashboard():
    """User dashboard page route."""
    # Get user's trips
    trips = Trip.query.filter_by(user_id=current_user.id).order_by(Trip.start_date).all()
    
    # Get upcoming trips
    upcoming_trips = [trip for trip in trips if trip.status in ['planning', 'active']]
    
    # Get past trips
    past_trips = [trip for trip in trips if trip.status == 'completed']
    
    # Get user's reviews
    reviews = Review.query.filter_by(user_id=current_user.id).order_by(Review.created_at.desc()).all()
    
    # Get user's notifications
    notifications = current_user.notifications.filter_by(is_dismissed=False).order_by(
        db.desc('is_read'), db.desc('created_at')).limit(5).all()
    
    # Add current datetime for countdown calculations
    now = datetime.now()
    
    return render_template('dashboard.html',
                          upcoming_trips=upcoming_trips,
                          past_trips=past_trips,
                          reviews=reviews,
                          notifications=notifications,
                          now=now) 