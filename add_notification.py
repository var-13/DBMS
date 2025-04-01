from app import create_app, db
from app.models import User, Notification
from config import DevelopmentConfig
from datetime import datetime

app = create_app(DevelopmentConfig)

with app.app_context():
    # Find the user
    user = User.query.filter_by(username='s').first()
    
    if user:
        print(f"Found user: {user.username}, ID: {user.id}")
        
        # Create a test notification
        notification = Notification(
            title="Welcome to Trip Planner",
            message="Thanks for joining Trip Planner! Start by creating your first trip.",
            notification_type="system",
            icon="fa-bell",
            user_id=user.id
        )
        
        db.session.add(notification)
        db.session.commit()
        
        print(f"Added notification: {notification.title}")
    else:
        print("User 's' not found") 
