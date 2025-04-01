from datetime import datetime, timedelta
import uuid
import random
from dotenv import load_dotenv

# Import app modules
from app import db, create_app
from app.models import Destination, Review, User

# Load environment variables
load_dotenv()

# Create app with config
app = create_app('config.Config')

# Sample destination data
sample_destinations = [
    {
        "name": "Eiffel Tower",
        "description": "The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris, France. It is named after the engineer Gustave Eiffel, whose company designed and built the tower.",
        "country": "France",
        "city": "Paris",
        "address": "Champ de Mars, 5 Avenue Anatole France, 75007 Paris",
        "latitude": 48.8584,
        "longitude": 2.2945,
        "image_url": "https://images.unsplash.com/photo-1543349689-9a4d426bee8e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1101&q=80",
        "category": "historical",
        "popularity": 95,
        "best_time_to_visit": "April to June, September to October",
        "timezone": "Central European Time (CET)",
        "language": "French",
        "currency": "Euro"
    },
    {
        "name": "Grand Canyon",
        "description": "The Grand Canyon is a steep-sided canyon carved by the Colorado River in Arizona, United States. The Grand Canyon is 277 miles long, up to 18 miles wide and attains a depth of over a mile.",
        "country": "United States",
        "city": "Grand Canyon Village",
        "address": "Grand Canyon National Park, AZ 86023",
        "latitude": 36.0544,
        "longitude": -112.2383,
        "image_url": "https://images.unsplash.com/photo-1527333656061-ca7adf608ae1?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1169&q=80",
        "category": "natural",
        "popularity": 90,
        "best_time_to_visit": "March to May, September to November",
        "timezone": "Mountain Standard Time (MST)",
        "language": "English",
        "currency": "US Dollar"
    },
    {
        "name": "Santorini",
        "description": "Santorini is an island in the southern Aegean Sea, about 200 km southeast of Greece's mainland. It is the largest island of a small, circular archipelago, which bears the same name.",
        "country": "Greece",
        "city": "Thira",
        "address": "Santorini, Cyclades, Greece",
        "latitude": 36.3932,
        "longitude": 25.4615,
        "image_url": "https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80",
        "category": "beach",
        "popularity": 85,
        "best_time_to_visit": "April to May, September to October",
        "timezone": "Eastern European Time (EET)",
        "language": "Greek",
        "currency": "Euro"
    },
    {
        "name": "Tokyo Tower",
        "description": "Tokyo Tower is a communications and observation tower in the Shiba-koen district of Minato, Tokyo, Japan. At 333 meters, it is the second-tallest structure in Japan.",
        "country": "Japan",
        "city": "Tokyo",
        "address": "4 Chome-2-8 Shibakoen, Minato City, Tokyo 105-0011, Japan",
        "latitude": 35.6586,
        "longitude": 139.7454,
        "image_url": "https://images.unsplash.com/photo-1536098561742-ca998e48cbcc?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=836&q=80",
        "category": "city",
        "popularity": 80,
        "best_time_to_visit": "March to May, September to November",
        "timezone": "Japan Standard Time (JST)",
        "language": "Japanese",
        "currency": "Yen"
    },
    {
        "name": "Machu Picchu",
        "description": "Machu Picchu is an Incan citadel set high in the Andes Mountains in Peru, above the Urubamba River valley. Built in the 15th century and later abandoned, it's renowned for its sophisticated dry-stone walls that fuse huge blocks without the use of mortar.",
        "country": "Peru",
        "city": "Cusco",
        "address": "Machupicchu District, Peru",
        "latitude": -13.1631,
        "longitude": -72.5450,
        "image_url": "https://images.unsplash.com/photo-1587595431973-160d0d94add1?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1169&q=80",
        "category": "historical",
        "popularity": 88,
        "best_time_to_visit": "May to September",
        "timezone": "Peru Standard Time (PET)",
        "language": "Spanish",
        "currency": "Peruvian Sol"
    },
    {
        "name": "Sydney Opera House",
        "description": "The Sydney Opera House is a multi-venue performing arts center at Sydney Harbour in Sydney, New South Wales, Australia. It is one of the 20th century's most famous and distinctive buildings.",
        "country": "Australia",
        "city": "Sydney",
        "address": "Bennelong Point, Sydney NSW 2000, Australia",
        "latitude": -33.8568,
        "longitude": 151.2153,
        "image_url": "https://images.unsplash.com/photo-1527915676329-fd5ec8a12d4b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1171&q=80",
        "category": "city",
        "popularity": 82,
        "best_time_to_visit": "September to November, March to May",
        "timezone": "Australian Eastern Standard Time (AEST)",
        "language": "English",
        "currency": "Australian Dollar"
    }
]

# Sample review content
sample_review_titles = [
    "Amazing Experience", "Breathtaking Views", "Worth Every Penny",
    "Unforgettable Trip", "A Must-Visit Destination", "Exceeded My Expectations",
    "Beautiful and Peaceful", "Perfect Vacation Spot", "Highly Recommended",
    "Spectacular Beauty"
]

sample_review_content = [
    "I had an amazing time visiting this place. The views were breathtaking and the atmosphere was incredible. Would definitely visit again!",
    "This destination exceeded all my expectations. The natural beauty is unparalleled, and I was able to capture some incredible photos.",
    "One of the best travel experiences I've ever had. The cultural heritage and historical significance made this trip truly special.",
    "I can't recommend this place enough. From the warm hospitality to the stunning scenery, everything was perfect.",
    "A truly magical experience that I'll cherish forever. The local cuisine was delicious, and the people were incredibly friendly.",
    "This destination offers a perfect blend of adventure and relaxation. I was able to explore during the day and unwind in the evening.",
    "An excellent place to disconnect and enjoy nature. The surroundings are pristine and well-preserved.",
    "The historical significance of this location is fascinating. I learned so much about the local culture and traditions.",
    "A photographer's dream! Every corner offers a new perspective and a perfect opportunity for stunning pictures.",
    "I visited with my family and we all had a wonderful time. There's something for everyone at this destination."
]

# Function to add sample data
def add_sample_data():
    with app.app_context():
        # Check if we already have destinations
        existing_destinations = Destination.query.count()
        if existing_destinations > 0:
            print(f"Database already has {existing_destinations} destinations. Skipping destination creation.")
        else:
            # Add destinations
            for destination_data in sample_destinations:
                destination = Destination(
                    id=str(uuid.uuid4()),
                    **destination_data
                )
                db.session.add(destination)
            
            db.session.commit()
            print(f"Added {len(sample_destinations)} sample destinations to the database.")
        
        # Check if we already have reviews
        existing_reviews = Review.query.count()
        if existing_reviews > 0:
            print(f"Database already has {existing_reviews} reviews. Skipping review creation.")
        else:
            # Get first user (for creating reviews)
            user = User.query.first()
            if not user:
                print("No users found in the database. Cannot add reviews.")
                return
            
            # Get all destinations
            destinations = Destination.query.all()
            if not destinations:
                print("No destinations found in the database. Cannot add reviews.")
                return
            
            # Add 2 reviews per destination
            for destination in destinations:
                for _ in range(2):
                    # Create review with random content
                    title = random.choice(sample_review_titles)
                    content = random.choice(sample_review_content)
                    rating = random.randint(3, 5)  # Ratings between 3-5 stars
                    
                    # Random date within the last 6 months
                    days_ago = random.randint(1, 180)
                    review_date = datetime.utcnow() - timedelta(days=days_ago)
                    
                    review = Review(
                        id=str(uuid.uuid4()),
                        title=title,
                        content=content,
                        rating=rating,
                        review_date=review_date.date(),
                        is_public=True,
                        user_id=user.id,
                        destination_id=destination.id
                    )
                    db.session.add(review)
            
            db.session.commit()
            print(f"Added {len(destinations) * 2} sample reviews to the database.")

if __name__ == "__main__":
    add_sample_data() 
