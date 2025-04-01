from datetime import datetime
import uuid

from app import db

class Weather(db.Model):
    """Weather model for storing weather information for destinations."""
    __tablename__ = 'weather'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    date = db.Column(db.Date, nullable=False)
    temperature_high = db.Column(db.Float, nullable=False)  # in Celsius
    temperature_low = db.Column(db.Float, nullable=False)  # in Celsius
    humidity = db.Column(db.Float)  # percentage
    precipitation = db.Column(db.Float)  # in mm
    wind_speed = db.Column(db.Float)  # in km/h
    wind_direction = db.Column(db.String(10))  # N, NE, E, SE, S, SW, W, NW
    weather_condition = db.Column(db.String(64))  # sunny, cloudy, rainy, etc.
    weather_icon = db.Column(db.String(64))  # icon code from weather API
    uv_index = db.Column(db.Float)
    sunrise = db.Column(db.Time)
    sunset = db.Column(db.Time)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Foreign keys
    destination_id = db.Column(db.String(36), db.ForeignKey('destinations.id', ondelete='CASCADE'), nullable=False)
    
    def __repr__(self):
        return f'<Weather for {self.destination_id} on {self.date}>'
    
    @property
    def temperature_high_fahrenheit(self):
        """Convert temperature from Celsius to Fahrenheit."""
        if self.temperature_high is not None:
            return (self.temperature_high * 9/5) + 32
        return None
    
    @property
    def temperature_low_fahrenheit(self):
        """Convert temperature from Celsius to Fahrenheit."""
        if self.temperature_low is not None:
            return (self.temperature_low * 9/5) + 32
        return None
    
    @property
    def is_rainy(self):
        """Check if weather condition indicates rain."""
        rain_conditions = ['rain', 'drizzle', 'shower', 'thunderstorm']
        if self.weather_condition:
            return any(cond in self.weather_condition.lower() for cond in rain_conditions)
        return False
    
    @property
    def is_sunny(self):
        """Check if weather condition indicates sun."""
        sunny_conditions = ['sun', 'clear', 'fair']
        if self.weather_condition:
            return any(cond in self.weather_condition.lower() for cond in sunny_conditions)
        return False 