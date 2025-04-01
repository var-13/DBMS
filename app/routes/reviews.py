from flask import Blueprint, render_template, redirect, url_for, flash, request, abort
from flask_login import login_required, current_user
from sqlalchemy import or_

from app import db
from app.models import Review, Destination, Accommodation, Transportation, Activity

reviews_bp = Blueprint('reviews', __name__)

@reviews_bp.route('/')
def index():
    """List all public reviews with optional filtering."""
    # Start with base query
    query = Review.query.filter_by(is_public=True)
    
    # Apply search filter if provided
    search = request.args.get('search', '')
    if search:
        query = query.filter(or_(
            Review.title.ilike(f'%{search}%'),
            Review.content.ilike(f'%{search}%')
        ))
    
    # Apply rating filter if provided
    rating = request.args.get('rating', '')
    if rating and rating.isdigit():
        query = query.filter(Review.rating >= int(rating))
    
    # Apply type filter if provided
    review_type = request.args.get('type', '')
    if review_type == 'destination':
        query = query.filter(Review.destination_id.isnot(None))
    elif review_type == 'accommodation':
        query = query.filter(Review.accommodation_id.isnot(None))
    elif review_type == 'transportation':
        query = query.filter(Review.transportation_id.isnot(None))
    elif review_type == 'activity':
        query = query.filter(Review.activity_id.isnot(None))
    
    # Get the final results ordered by creation date (newest first)
    reviews = query.order_by(Review.created_at.desc()).all()
    
    return render_template('reviews/index.html', reviews=reviews) 