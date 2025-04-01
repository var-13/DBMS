from datetime import datetime
import uuid

from app import db

class Transportation(db.Model):
    """Transportation model for storing travel information."""
    __tablename__ = 'transportations'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    type = db.Column(db.String(64), nullable=False)  # flight, train, bus, car, ferry, etc.
    provider = db.Column(db.String(128))  # airline, train company, etc.
    departure_location = db.Column(db.String(128), nullable=False)
    arrival_location = db.Column(db.String(128), nullable=False)
    departure_datetime = db.Column(db.DateTime, nullable=False)
    arrival_datetime = db.Column(db.DateTime, nullable=False)
    booking_reference = db.Column(db.String(128))
    booking_status = db.Column(db.String(64), default='pending')  # pending, confirmed, cancelled
    seat_number = db.Column(db.String(64))
    price = db.Column(db.Float)
    confirmation_email = db.Column(db.String(255))
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Foreign keys
    trip_id = db.Column(db.String(36), db.ForeignKey('trips.id', ondelete='CASCADE'), nullable=False)
    
    def __repr__(self):
        return f'<Transportation {self.type} from {self.departure_location} to {self.arrival_location}>'
    
    @property
    def duration(self):
        """Calculate transportation duration in hours."""
        if self.departure_datetime and self.arrival_datetime:
            delta = self.arrival_datetime - self.departure_datetime
            return delta.total_seconds() / 3600  # Convert to hours
        return 0
    
    @property
    def is_confirmed(self):
        """Check if transportation is confirmed."""
        return self.booking_status == 'confirmed'
    
    @property
    def is_international(self):
        """Check if transportation is international (simplified)."""
        # This is a simplified check - in a real app, you'd use a more sophisticated approach
        return self.departure_location.split(',')[-1].strip() != self.arrival_location.split(',')[-1].strip() 