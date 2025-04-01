from flask import Blueprint, render_template, redirect, url_for, flash, request, abort
from flask_login import login_required, current_user
from datetime import datetime

from app import db
from app.models import Trip, Destination

trips_bp = Blueprint('trips', __name__)

@trips_bp.route('/')
@login_required
def index():
    """List all trips for the current user."""
    trips = Trip.query.filter_by(user_id=current_user.id).order_by(Trip.start_date).all()
    return render_template('trips/index.html', trips=trips)

@trips_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    """Create a new trip."""
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        start_date = datetime.strptime(request.form.get('start_date'), '%Y-%m-%d').date()
        end_date = datetime.strptime(request.form.get('end_date'), '%Y-%m-%d').date()
        is_public = 'is_public' in request.form
        total_budget = request.form.get('total_budget')
        
        if total_budget:
            total_budget = float(total_budget)
        
        trip = Trip(
            title=title,
            description=description,
            start_date=start_date,
            end_date=end_date,
            is_public=is_public,
            total_budget=total_budget,
            user_id=current_user.id
        )
        
        db.session.add(trip)
        db.session.commit()
        
        flash('Trip created successfully!', 'success')
        return redirect(url_for('trips.view', trip_id=trip.id))
    
    return render_template('trips/create.html')

@trips_bp.route('/<trip_id>')
@login_required
def view(trip_id):
    """View a specific trip."""
    trip = Trip.query.get_or_404(trip_id)
    
    # Check if the user is authorized to view this trip
    if trip.user_id != current_user.id and not trip.is_public:
        abort(403)
    
    return render_template('trips/view.html', trip=trip)

@trips_bp.route('/<trip_id>/edit', methods=['GET', 'POST'])
@login_required
def edit(trip_id):
    """Edit a specific trip."""
    trip = Trip.query.get_or_404(trip_id)
    
    # Check if the user is authorized to edit this trip
    if trip.user_id != current_user.id:
        abort(403)
    
    if request.method == 'POST':
        trip.title = request.form.get('title')
        trip.description = request.form.get('description')
        trip.start_date = datetime.strptime(request.form.get('start_date'), '%Y-%m-%d').date()
        trip.end_date = datetime.strptime(request.form.get('end_date'), '%Y-%m-%d').date()
        trip.is_public = 'is_public' in request.form
        
        total_budget = request.form.get('total_budget')
        if total_budget:
            trip.total_budget = float(total_budget)
        
        db.session.commit()
        
        flash('Trip updated successfully!', 'success')
        return redirect(url_for('trips.view', trip_id=trip.id))
    
    return render_template('trips/edit.html', trip=trip)

@trips_bp.route('/<trip_id>/delete', methods=['POST'])
@login_required
def delete(trip_id):
    """Delete a specific trip."""
    trip = Trip.query.get_or_404(trip_id)
    
    # Check if the user is authorized to delete this trip
    if trip.user_id != current_user.id:
        abort(403)
    
    db.session.delete(trip)
    db.session.commit()
    
    flash('Trip deleted successfully!', 'success')
    return redirect(url_for('trips.index')) 