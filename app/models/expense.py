from datetime import datetime
import uuid

from app import db

class ExpenseCategory(db.Model):
    """ExpenseCategory model for categorizing expenses."""
    __tablename__ = 'expense_categories'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(64), nullable=False, unique=True)
    description = db.Column(db.Text)
    icon = db.Column(db.String(64))  # Font Awesome icon name or similar
    color = db.Column(db.String(7))  # Hex color code
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    expenses = db.relationship('Expense', backref='category', lazy='dynamic')
    
    def __repr__(self):
        return f'<ExpenseCategory {self.name}>'


class Expense(db.Model):
    """Expense model for storing financial transactions."""
    __tablename__ = 'expenses'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text)
    amount = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(3), default='USD')  # ISO currency code
    date = db.Column(db.Date, nullable=False)
    payment_method = db.Column(db.String(64))  # cash, credit card, etc.
    receipt_image = db.Column(db.String(255))
    is_reimbursable = db.Column(db.Boolean, default=False)
    is_shared = db.Column(db.Boolean, default=False)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Foreign keys
    trip_id = db.Column(db.String(36), db.ForeignKey('trips.id', ondelete='CASCADE'), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    category_id = db.Column(db.String(36), db.ForeignKey('expense_categories.id'), nullable=False)
    
    # Optional foreign keys for related entities
    accommodation_id = db.Column(db.String(36), db.ForeignKey('accommodations.id'), nullable=True)
    transportation_id = db.Column(db.String(36), db.ForeignKey('transportations.id'), nullable=True)
    activity_id = db.Column(db.String(36), db.ForeignKey('activities.id'), nullable=True)
    
    def __repr__(self):
        return f'<Expense {self.title} ({self.amount} {self.currency})>'
    
    @property
    def formatted_amount(self):
        """Format the amount with currency symbol."""
        currency_symbols = {
            'USD': '$', 'EUR': '€', 'GBP': '£', 'JPY': '¥', 
            'AUD': 'A$', 'CAD': 'C$', 'CHF': 'Fr', 'CNY': '¥'
        }
        symbol = currency_symbols.get(self.currency, self.currency)
        return f"{symbol}{self.amount:.2f}" 