from datetime import datetime
import uuid

from app import db

class Activity(db.Model):
    """Activity model for storing activity information."""
    __tablename__ = 'activities'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String(64))  # sightseeing, adventure, cultural, etc.
    start_datetime = db.Column(db.DateTime, nullable=False)
    end_datetime = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(255))
    address = db.Column(db.String(255))
    price = db.Column(db.Float)
    booking_reference = db.Column(db.String(128))
    booking_status = db.Column(db.String(64), default='pending')  # pending, confirmed, cancelled
    contact_info = db.Column(db.String(255))
    website = db.Column(db.String(255))
    image_url = db.Column(db.String(255))
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Foreign keys
    trip_id = db.Column(db.String(36), db.ForeignKey('trips.id', ondelete='CASCADE'), nullable=False)
    destination_id = db.Column(db.String(36), db.ForeignKey('destinations.id'), nullable=False)
    
    def __repr__(self):
        return f'<Activity {self.name} at {self.location}>'
    
    @property
    def duration(self):
        """Calculate activity duration in hours."""
        if self.start_datetime and self.end_datetime:
            delta = self.end_datetime - self.start_datetime
            return delta.total_seconds() / 3600  # Convert to hours
        return 0
    
    @property
    def is_confirmed(self):
        """Check if activity is confirmed."""
        return self.booking_status == 'confirmed'
    
    @property
    def is_free(self):
        """Check if activity is free."""
        return self.price is None or self.price == 0 