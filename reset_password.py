from app import create_app, db
from app.models import User
from config import DevelopmentConfig

app = create_app(DevelopmentConfig)

with app.app_context():
    # Find the user
    user = User.query.filter_by(username='s').first()
    
    if user:
        print(f"Found user: {user.username}, ID: {user.id}")
        
        # Reset password
        user.set_password('password')
        db.session.commit()
        
        print(f"Password reset for user: {user.username}")
    else:
        print("User 's' not found") 