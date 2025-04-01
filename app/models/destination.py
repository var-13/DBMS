from datetime import datetime
import uuid

from app import db

class Destination(db.Model):
    """Destination model for storing location information."""
    __tablename__ = 'destinations'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text)
    country = db.Column(db.String(64), nullable=False)
    city = db.Column(db.String(64), nullable=False)
    address = db.Column(db.String(255))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    image_url = db.Column(db.String(255))
    category = db.Column(db.String(64))  # e.g., beach, mountain, city, countryside
    popularity = db.Column(db.Integer, default=0)  # 1-10 rating
    best_time_to_visit = db.Column(db.String(128))
    timezone = db.Column(db.String(64))
    language = db.Column(db.String(64))
    currency = db.Column(db.String(64))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    accommodations = db.relationship('Accommodation', backref='destination', lazy='dynamic')
    activities = db.relationship('Activity', backref='destination', lazy='dynamic')
    weather_data = db.relationship('Weather', backref='destination', lazy='dynamic', cascade='all, delete-orphan')
    reviews = db.relationship('Review', backref='destination', lazy='dynamic', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Destination {self.name}, {self.city}, {self.country}>'
    
    @property
    def average_rating(self):
        """Calculate average rating from reviews."""
        reviews = list(self.reviews)
        if not reviews:
            return 0
        return sum(review.rating for review in reviews) / len(reviews)
    
    @property
    def coordinates(self):
        """Return coordinates as a tuple."""
        return (self.latitude, self.longitude) if self.latitude and self.longitude else None 