from datetime import datetime
import uuid

from app import db

class Itinerary(db.Model):
    """Itinerary model for storing daily trip plans."""
    __tablename__ = 'itineraries'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text)
    date = db.Column(db.Date, nullable=False)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Foreign keys
    trip_id = db.Column(db.String(36), db.ForeignKey('trips.id', ondelete='CASCADE'), nullable=False)
    
    # Relationships
    items = db.relationship('ItineraryItem', backref='itinerary', lazy='dynamic', 
                           cascade='all, delete-orphan', order_by='ItineraryItem.start_time')
    
    def __repr__(self):
        return f'<Itinerary {self.title} for {self.date}>'
    
    @property
    def item_count(self):
        """Count the number of items in the itinerary."""
        return self.items.count()
    
    @property
    def first_item_time(self):
        """Get the start time of the first item."""
        first_item = self.items.order_by(ItineraryItem.start_time).first()
        return first_item.start_time if first_item else None
    
    @property
    def last_item_time(self):
        """Get the end time of the last item."""
        last_item = self.items.order_by(ItineraryItem.end_time.desc()).first()
        return last_item.end_time if last_item else None


class ItineraryItem(db.Model):
    """ItineraryItem model for storing individual activities within an itinerary."""
    __tablename__ = 'itinerary_items'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    location = db.Column(db.String(255))
    item_type = db.Column(db.String(64))  # accommodation, transportation, activity, meal, etc.
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Foreign keys
    itinerary_id = db.Column(db.String(36), db.ForeignKey('itineraries.id', ondelete='CASCADE'), nullable=False)
    accommodation_id = db.Column(db.String(36), db.ForeignKey('accommodations.id'), nullable=True)
    transportation_id = db.Column(db.String(36), db.ForeignKey('transportations.id'), nullable=True)
    activity_id = db.Column(db.String(36), db.ForeignKey('activities.id'), nullable=True)
    
    def __repr__(self):
        return f'<ItineraryItem {self.title} at {self.start_time}>'
    
    @property
    def duration_minutes(self):
        """Calculate duration in minutes."""
        if self.start_time and self.end_time:
            start_minutes = self.start_time.hour * 60 + self.start_time.minute
            end_minutes = self.end_time.hour * 60 + self.end_time.minute
            return end_minutes - start_minutes
        return 0 