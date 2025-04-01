from app import create_app, db
from app.models import Destination
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create app with config
app = create_app('config.Config')

# Define the new image URL with beautiful Eiffel Tower reflection
# This is a high-quality image of the Eiffel Tower with its reflection in water
EIFFEL_IMAGE_URL = "https://images.unsplash.com/photo-1511739001486-6bfe10ce785f?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1887&q=80"

# Function to update the Eiffel Tower image
def update_eiffel_tower_image():
    with app.app_context():
        # Find the Eiffel Tower record
        eiffel = Destination.query.filter_by(name='Eiffel Tower').first()
        
        if not eiffel:
            print("Error: Eiffel Tower destination not found in the database!")
            return False
        
        # Display the current image URL
        print(f"Current image URL: {eiffel.image_url}")
        
        # Update the image URL
        eiffel.image_url = EIFFEL_IMAGE_URL
        
        # Commit the changes
        db.session.commit()
        
        print(f"Successfully updated Eiffel Tower image URL to: {EIFFEL_IMAGE_URL}")
        return True

if __name__ == "__main__":
    update_eiffel_tower_image() 