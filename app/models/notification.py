from datetime import datetime
import uuid

from app import db

class Notification(db.Model):
    """Notification model for storing user notifications."""
    __tablename__ = 'notifications'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String(128), nullable=False)
    message = db.Column(db.Text, nullable=False)
    notification_type = db.Column(db.String(64), nullable=False)  # trip, reminder, system, etc.
    is_read = db.Column(db.Boolean, default=False)
    is_dismissed = db.Column(db.Boolean, default=False)
    action_url = db.Column(db.String(255))  # URL to navigate to when notification is clicked
    icon = db.Column(db.String(64))  # Font Awesome icon name or similar
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Foreign keys
    user_id = db.Column(db.String(36), db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    
    # Optional foreign keys for related entities
    trip_id = db.Column(db.String(36), db.ForeignKey('trips.id'), nullable=True)
    
    def __repr__(self):
        return f'<Notification {self.title} for User {self.user_id}>'
    
    @property
    def is_new(self):
        """Check if notification is new (not read and not dismissed)."""
        return not self.is_read and not self.is_dismissed
    
    @property
    def time_since(self):
        """Calculate time since notification was created."""
        now = datetime.utcnow()
        delta = now - self.created_at
        
        if delta.days > 0:
            return f"{delta.days} days ago"
        elif delta.seconds >= 3600:
            return f"{delta.seconds // 3600} hours ago"
        elif delta.seconds >= 60:
            return f"{delta.seconds // 60} minutes ago"
        else:
            return "Just now"
    
    def mark_as_read(self):
        """Mark notification as read."""
        self.is_read = True
        self.updated_at = datetime.utcnow()
    
    def dismiss(self):
        """Dismiss notification."""
        self.is_dismissed = True
        self.updated_at = datetime.utcnow() 