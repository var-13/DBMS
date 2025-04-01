from datetime import datetime
import uuid

from app import db

# Association table for trip destinations (many-to-many)
trip_destinations = db.Table('trip_destinations',
    db.Column('trip_id', db.String(36), db.ForeignKey('trips.id', ondelete='CASCADE'), primary_key=True),
    db.Column('destination_id', db.String(36), db.ForeignKey('destinations.id', ondelete='CASCADE'), primary_key=True)
)

class Trip(db.Model):
    """Trip model for storing trip information."""
    __tablename__ = 'trips'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    is_public = db.Column(db.Boolean, default=False)
    status = db.Column(db.String(20), default='planning')  # planning, active, completed, cancelled
    cover_image = db.Column(db.String(255))
    total_budget = db.Column(db.Float)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Foreign keys
    user_id = db.Column(db.String(36), db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    
    # Relationships
    destinations = db.relationship('Destination', secondary=trip_destinations, backref=db.backref('trips', lazy='dynamic'))
    accommodations = db.relationship('Accommodation', backref='trip', lazy='dynamic', cascade='all, delete-orphan')
    transportations = db.relationship('Transportation', backref='trip', lazy='dynamic', cascade='all, delete-orphan')
    activities = db.relationship('Activity', backref='trip', lazy='dynamic', cascade='all, delete-orphan')
    itineraries = db.relationship('Itinerary', backref='trip', lazy='dynamic', cascade='all, delete-orphan')
    expenses = db.relationship('Expense', backref='trip', lazy='dynamic', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Trip {self.title}>'
    
    @property
    def duration(self):
        """Calculate trip duration in days."""
        if self.start_date and self.end_date:
            return (self.end_date - self.start_date).days + 1
        return 0
    
    @property
    def total_expenses(self):
        """Calculate total expenses for the trip."""
        return sum(expense.amount for expense in self.expenses)
    
    @property
    def budget_remaining(self):
        """Calculate remaining budget."""
        if self.total_budget:
            return self.total_budget - self.total_expenses
        return 0 