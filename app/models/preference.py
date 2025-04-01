from datetime import datetime
import uuid

from app import db

class Preference(db.Model):
    """Preference model for storing user travel preferences."""
    __tablename__ = 'preferences'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    
    # Travel preferences
    preferred_destinations = db.Column(db.Text)  # Comma-separated list or JSON
    preferred_accommodation_types = db.Column(db.Text)  # Comma-separated list or JSON
    preferred_transportation_types = db.Column(db.Text)  # Comma-separated list or JSON
    preferred_activities = db.Column(db.Text)  # Comma-separated list or JSON
    preferred_cuisines = db.Column(db.Text)  # Comma-separated list or JSON
    
    # Budget preferences
    budget_category = db.Column(db.String(64))  # budget, mid-range, luxury
    max_accommodation_budget = db.Column(db.Float)
    max_transportation_budget = db.Column(db.Float)
    max_activity_budget = db.Column(db.Float)
    max_food_budget = db.Column(db.Float)
    preferred_currency = db.Column(db.String(3), default='USD')
    
    # Accessibility preferences
    accessibility_requirements = db.Column(db.Text)
    dietary_restrictions = db.Column(db.Text)
    
    # Trip preferences
    preferred_trip_duration = db.Column(db.Integer)  # in days
    preferred_travel_seasons = db.Column(db.Text)  # Comma-separated list or JSON
    travel_style = db.Column(db.String(64))  # adventure, relaxation, cultural, etc.
    
    # App preferences
    notification_preferences = db.Column(db.Text)  # JSON with notification settings
    language = db.Column(db.String(5), default='en-US')
    theme = db.Column(db.String(64), default='light')
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Foreign keys
    user_id = db.Column(db.String(36), db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False, unique=True)
    
    def __repr__(self):
        return f'<Preference for User {self.user_id}>'
    
    @property
    def preferred_destinations_list(self):
        """Convert the preferred destinations string to a list."""
        if not self.preferred_destinations:
            return []
        return [dest.strip() for dest in self.preferred_destinations.split(',')]
    
    @property
    def preferred_accommodation_types_list(self):
        """Convert the preferred accommodation types string to a list."""
        if not self.preferred_accommodation_types:
            return []
        return [acc.strip() for acc in self.preferred_accommodation_types.split(',')]
    
    @property
    def preferred_transportation_types_list(self):
        """Convert the preferred transportation types string to a list."""
        if not self.preferred_transportation_types:
            return []
        return [trans.strip() for trans in self.preferred_transportation_types.split(',')]
    
    @property
    def preferred_activities_list(self):
        """Convert the preferred activities string to a list."""
        if not self.preferred_activities:
            return []
        return [act.strip() for act in self.preferred_activities.split(',')]
    
    @property
    def preferred_cuisines_list(self):
        """Convert the preferred cuisines string to a list."""
        if not self.preferred_cuisines:
            return []
        return [cuisine.strip() for cuisine in self.preferred_cuisines.split(',')] 