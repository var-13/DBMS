from datetime import datetime
import uuid

from app import db

class Review(db.Model):
    """Review model for storing user reviews of destinations, accommodations, etc."""
    __tablename__ = 'reviews'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String(128), nullable=False)
    content = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # 1-5 stars
    review_date = db.Column(db.Date, default=datetime.utcnow().date)
    is_public = db.Column(db.Boolean, default=True)
    images = db.Column(db.Text)  # Comma-separated list of image URLs or JSON
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Foreign keys
    user_id = db.Column(db.String(36), db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    
    # Optional foreign keys for reviewed entities (only one should be set)
    destination_id = db.Column(db.String(36), db.ForeignKey('destinations.id'), nullable=True)
    accommodation_id = db.Column(db.String(36), db.ForeignKey('accommodations.id'), nullable=True)
    transportation_id = db.Column(db.String(36), db.ForeignKey('transportations.id'), nullable=True)
    activity_id = db.Column(db.String(36), db.ForeignKey('activities.id'), nullable=True)
    
    def __repr__(self):
        return f'<Review {self.title} ({self.rating}/5)>'
    
    @property
    def review_type(self):
        """Determine the type of entity being reviewed."""
        if self.destination_id:
            return 'destination'
        elif self.accommodation_id:
            return 'accommodation'
        elif self.transportation_id:
            return 'transportation'
        elif self.activity_id:
            return 'activity'
        return 'unknown'
    
    @property
    def star_rating(self):
        """Return a string of stars representing the rating."""
        return '★' * self.rating + '☆' * (5 - self.rating)
    
    @property
    def image_list(self):
        """Convert the images string to a list."""
        if not self.images:
            return []
        return [img.strip() for img in self.images.split(',')] 