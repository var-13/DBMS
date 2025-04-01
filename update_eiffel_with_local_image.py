from app import create_app, db
from app.models import Destination
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create app with config
app = create_app('config.Config')

# Define the local path for the Eiffel Tower image
# In a real app, you would upload the image and get a proper URL or file path
# This is a simplified example pointing to a local static file
EIFFEL_IMAGE_PATH = "/static/images/eiffel_tower_reflection.jpg"

# Function to update the Eiffel Tower image
def update_eiffel_tower_with_local_image():
    with app.app_context():
        # Find the Eiffel Tower record
        eiffel = Destination.query.filter_by(name='Eiffel Tower').first()
        
        if not eiffel:
            print("Error: Eiffel Tower destination not found in the database!")
            return False
        
        # Display the current image URL
        print(f"Current image URL: {eiffel.image_url}")
        
        # Update the image URL to point to the local file
        eiffel.image_url = EIFFEL_IMAGE_PATH
        
        # Commit the changes
        db.session.commit()
        
        print(f"Successfully updated Eiffel Tower image to use local file: {EIFFEL_IMAGE_PATH}")
        print("NOTE: For this to work properly, you need to save your Eiffel Tower image with the name 'eiffel_tower_reflection.jpg' in the app/static/images directory.")
        return True

if __name__ == "__main__":
    update_eiffel_tower_with_local_image() 