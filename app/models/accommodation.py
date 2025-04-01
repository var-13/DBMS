from datetime import datetime
import uuid

from app import db

class Accommodation(db.Model):
    """Accommodation model for storing lodging information."""
    __tablename__ = 'accommodations'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(128), nullable=False)
    type = db.Column(db.String(64), nullable=False)  # hotel, hostel, apartment, etc.
    description = db.Column(db.Text)
    address = db.Column(db.String(255))
    check_in_date = db.Column(db.Date, nullable=False)
    check_out_date = db.Column(db.Date, nullable=False)
    price_per_night = db.Column(db.Float, nullable=False)
    total_price = db.Column(db.Float)
    booking_reference = db.Column(db.String(128))
    booking_status = db.Column(db.String(64), default='pending')  # pending, confirmed, cancelled
    contact_info = db.Column(db.String(255))
    amenities = db.Column(db.Text)  # Comma-separated list or JSON
    rating = db.Column(db.Integer)  # 1-5 stars
    image_url = db.Column(db.String(255))
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Foreign keys
    trip_id = db.Column(db.String(36), db.ForeignKey('trips.id', ondelete='CASCADE'), nullable=False)
    destination_id = db.Column(db.String(36), db.ForeignKey('destinations.id'), nullable=False)
    
    def __repr__(self):
        return f'<Accommodation {self.name} for Trip {self.trip_id}>'
    
    @property
    def duration(self):
        """Calculate accommodation duration in nights."""
        if self.check_in_date and self.check_out_date:
            return (self.check_out_date - self.check_in_date).days
        return 0
    
    @property
    def is_confirmed(self):
        """Check if accommodation is confirmed."""
        return self.booking_status == 'confirmed'
    
    def calculate_total_price(self):
        """Calculate total price based on duration and price per night."""
        if self.price_per_night and self.check_in_date and self.check_out_date:
            self.total_price = self.price_per_night * self.duration
        return self.total_price 