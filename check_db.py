from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
import logging

# Import app models
from app import db, create_app
from app.models import User, Trip, Notification, Destination, Review

# Set up logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

# Load environment variables
load_dotenv()

# Create app with config
app = create_app('config.Config')

# Use app context
with app.app_context():
    # Get users
    users = User.query.all()
    print(f"Users in database: {len(users)}")
    for user in users:
        print(f"User: {user.username}, ID: {user.id}")
    
    # Get user trips if there are users
    if users:
        user = users[0]  # Use first user for example
        trips = Trip.query.filter_by(user_id=user.id).all()
        print(f"\n{' '*27}Trips: {len(trips)}")
        for trip in trips:
            print(f"    - {trip.title} (Status: {trip.status})")
        
        # Get user notifications
        notifications = Notification.query.filter_by(user_id=user.id).all()
        print(f"\n{' '*27}Notifications: {len(notifications)}")
    
    # Get destinations
    destinations = Destination.query.all()
    print(f"\n{' '*27}Destinations: {len(destinations)}")
    for destination in destinations:
        print(f"    - {destination.name}, {destination.city}, {destination.country}")
    
    # Get reviews
    reviews = Review.query.all()
    print(f"\n{' '*27}Reviews: {len(reviews)}")
    for review in reviews:
        print(f"    - {review.title} ({review.rating}/5) by User ID: {review.user_id}")
        print(f"      Is public: {review.is_public}")
    
    print("\nTotal counts:")
    print(f"Users: {User.query.count()}")
    print(f"Trips: {Trip.query.count()}")
    print(f"Notifications: {Notification.query.count()}")
    print(f"Destinations: {Destination.query.count()}")
    print(f"Reviews: {Review.query.count()}") 