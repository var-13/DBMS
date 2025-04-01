import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app(config_object):
    """Create and configure the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_object)
    
    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    CORS(app)
    
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'
    
    # Register blueprints
    from app.routes.main import main_bp
    from app.routes.auth import auth_bp
    from app.routes.trips import trips_bp
    from app.routes.destinations import destinations_bp
    from app.routes.accommodations import accommodations_bp
    from app.routes.transportation import transportation_bp
    from app.routes.activities import activities_bp
    from app.routes.expenses import expenses_bp
    from app.routes.reviews import reviews_bp
    from app.routes.api import api_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(trips_bp, url_prefix='/trips')
    app.register_blueprint(destinations_bp, url_prefix='/destinations')
    app.register_blueprint(accommodations_bp, url_prefix='/accommodations')
    app.register_blueprint(transportation_bp, url_prefix='/transportation')
    app.register_blueprint(activities_bp, url_prefix='/activities')
    app.register_blueprint(expenses_bp, url_prefix='/expenses')
    app.register_blueprint(reviews_bp, url_prefix='/reviews')
    app.register_blueprint(api_bp, url_prefix='/api')
    
    # Shell context
    @app.shell_context_processor
    def make_shell_context():
        return {'db': db, 'app': app}
    
    return app 