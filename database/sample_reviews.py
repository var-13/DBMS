"""
Sample reviews data for the Trip Planner application.
Run this script to populate the database with sample reviews.
"""

from datetime import datetime, timedelta
import random
import sys
import os

# Add the parent directory to the path so we can import the app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import db, create_app
from app.models import User, Destination, Accommodation, Transportation, Activity, Review

def create_sample_reviews():
    """Create sample reviews for the application."""
    print("Creating sample reviews...")
    
    # Get existing data
    users = User.query.all()
    destinations = Destination.query.all()
    accommodations = Accommodation.query.all()
    transportations = Transportation.query.all()
    activities = Activity.query.all()
    
    # Check if we have the necessary data
    if not users:
        print("No users found. Please create users first.")
        return
    
    if not destinations and not accommodations and not transportations and not activities:
        print("No reviewable entities found. Please create destinations, accommodations, etc. first.")
        return
    
    # Sample review titles for different entity types
    destination_titles = [
        "Amazing place to visit!",
        "Beautiful scenery and friendly locals",
        "A must-see destination",
        "Exceeded my expectations",
        "Perfect vacation spot",
        "Hidden gem worth discovering",
        "Breathtaking views everywhere",
        "Cultural experience like no other",
        "Unforgettable adventure",
        "Relaxing getaway with stunning landscapes"
    ]
    
    accommodation_titles = [
        "Comfortable stay with great amenities",
        "Excellent service and clean rooms",
        "Perfect location for exploring",
        "Luxurious and worth every penny",
        "Cozy place with friendly staff",
        "Home away from home",
        "Modern facilities and beautiful design",
        "Exceptional value for money",
        "Peaceful retreat with amazing views",
        "Convenient and comfortable accommodation"
    ]
    
    transportation_titles = [
        "Smooth and comfortable journey",
        "On-time and efficient service",
        "Great value for the price",
        "Excellent staff and amenities",
        "Convenient and reliable transportation",
        "Comfortable seats and good service",
        "Hassle-free travel experience",
        "Clean and well-maintained vehicle",
        "Punctual and professional service",
        "Enjoyable journey with great views"
    ]
    
    activity_titles = [
        "Thrilling experience!",
        "Fun for the whole family",
        "Unique and memorable activity",
        "Professional guides and safe equipment",
        "Worth every penny",
        "Highlight of our trip",
        "Exciting adventure with beautiful scenery",
        "Well-organized and enjoyable",
        "Unforgettable experience",
        "Great way to explore the area"
    ]
    
    # Sample review content templates
    review_content_templates = [
        "I {adverb} {verb} my {time} at {entity}. The {aspect1} was {adjective1} and the {aspect2} was {adjective2}. {additional_comment} I would {recommendation} recommend this to {audience}.",
        "Our experience at {entity} was {overall}. {highlight} The {aspect1} was {adjective1}, and we particularly enjoyed the {aspect2}. {additional_comment} {recommendation} for anyone looking for {purpose}.",
        "If you're looking for {purpose}, {entity} is {recommendation_strength}. {highlight} The {aspect1} was {adjective1} and the {aspect2} was {adjective2}. {additional_comment}",
        "{entity} {verb} all my expectations. The {aspect1} was {adjective1} and the {aspect2} was {adjective2}. {highlight} {additional_comment} {recommendation} for {audience}.",
        "My {time} at {entity} was {overall}. {highlight} I found the {aspect1} to be {adjective1} and the {aspect2} was {adjective2}. {additional_comment} {recommendation_strength} worth experiencing."
    ]
    
    # Word banks for template filling
    adverbs = ["absolutely", "thoroughly", "completely", "really", "truly", "genuinely", "totally"]
    verbs = ["enjoyed", "loved", "appreciated", "treasured", "savored", "relished"]
    times = ["time", "stay", "visit", "experience", "trip", "vacation", "journey", "adventure"]
    aspects_destination = ["scenery", "local cuisine", "culture", "architecture", "beaches", "mountains", "weather", "atmosphere", "hospitality", "tourist attractions"]
    aspects_accommodation = ["room", "service", "cleanliness", "location", "breakfast", "staff", "comfort", "facilities", "value", "ambiance"]
    aspects_transportation = ["comfort", "punctuality", "staff", "cleanliness", "seating", "service", "efficiency", "value", "amenities", "booking process"]
    aspects_activity = ["guide", "safety measures", "equipment", "experience", "value", "organization", "scenery", "thrill factor", "instruction", "group size"]
    adjectives_positive = ["excellent", "outstanding", "superb", "amazing", "fantastic", "wonderful", "impressive", "exceptional", "great", "perfect", "delightful", "charming", "beautiful", "stunning", "breathtaking"]
    adjectives_neutral = ["decent", "satisfactory", "adequate", "reasonable", "fair", "acceptable", "standard", "typical", "average", "ordinary"]
    adjectives_negative = ["disappointing", "underwhelming", "mediocre", "subpar", "poor", "lacking", "unsatisfactory", "inadequate", "overpriced", "unimpressive"]
    highlights = [
        "I couldn't have asked for a better experience.",
        "It was the highlight of our trip.",
        "We had an unforgettable time.",
        "The experience exceeded our expectations.",
        "It was worth every penny.",
        "We were blown away by the whole experience.",
        "It made for wonderful memories.",
        "We couldn't have been happier with our choice.",
        "It was exactly what we were looking for.",
        "The experience was truly one-of-a-kind."
    ]
    additional_comments = [
        "The only downside was that we couldn't stay longer.",
        "I wish we had more time to fully enjoy everything it had to offer.",
        "We're already planning our next visit.",
        "I've recommended it to all my friends and family.",
        "It was a bit crowded, but that didn't diminish the experience.",
        "The photos don't do it justice - it's even better in person.",
        "It's a bit pricey, but definitely worth it for the experience.",
        "We were lucky with the weather, which made it even more enjoyable.",
        "It's suitable for all ages and interests.",
        "It's best to visit during the off-season to avoid crowds.",
        "Make sure to bring appropriate clothing and gear.",
        "I'd suggest booking in advance to secure your spot.",
        "Don't miss the opportunity to try the local specialties.",
        "The staff went above and beyond to make our experience special."
    ]
    recommendations = ["definitely", "absolutely", "highly", "strongly", "wholeheartedly", "certainly", "unreservedly"]
    recommendation_strengths = ["an excellent choice", "a perfect option", "a fantastic pick", "a must-visit", "a top choice", "an outstanding option", "a superb selection"]
    audiences = ["families", "couples", "solo travelers", "groups", "adventure seekers", "nature lovers", "culture enthusiasts", "luxury travelers", "budget travelers", "everyone"]
    purposes = ["relaxation", "adventure", "cultural experiences", "family fun", "romantic getaway", "sightseeing", "outdoor activities", "luxury experience", "authentic local experience", "unique experiences"]
    overall_experiences = ["amazing", "wonderful", "fantastic", "excellent", "outstanding", "superb", "incredible", "memorable", "delightful", "remarkable"]
    
    # Sample image URLs
    beach_images = [
        "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
        "https://images.unsplash.com/photo-1519046904884-53103b34b206",
        "https://images.unsplash.com/photo-1520454974749-611b7248ffdb"
    ]
    
    mountain_images = [
        "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b",
        "https://images.unsplash.com/photo-1486870591958-9b9d0d1dda99",
        "https://images.unsplash.com/photo-1486984008208-8880859a4292"
    ]
    
    city_images = [
        "https://images.unsplash.com/photo-1480714378408-67cf0d13bc1b",
        "https://images.unsplash.com/photo-1449824913935-59a10b8d2000",
        "https://images.unsplash.com/photo-1444723121867-7a241cacace9"
    ]
    
    hotel_images = [
        "https://images.unsplash.com/photo-1566073771259-6a8506099945",
        "https://images.unsplash.com/photo-1582719508461-905c673771fd",
        "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa"
    ]
    
    activity_images = [
        "https://images.unsplash.com/photo-1526976668912-1a811878dd37",
        "https://images.unsplash.com/photo-1530866495561-7a0517305f7d",
        "https://images.unsplash.com/photo-1605540436563-5bca919ae766"
    ]
    
    # Create sample reviews
    reviews_to_create = []
    
    # Destination reviews
    for destination in destinations:
        # Determine how many reviews to create for this destination (1-5)
        num_reviews = random.randint(1, 5)
        
        for _ in range(num_reviews):
            user = random.choice(users)
            rating = random.randint(3, 5)  # Mostly positive reviews
            
            # Occasionally add a lower rating for realism
            if random.random() < 0.2:
                rating = random.randint(1, 2)
            
            # Select appropriate adjectives based on rating
            if rating >= 4:
                adjective1 = random.choice(adjectives_positive)
                adjective2 = random.choice(adjectives_positive)
            elif rating == 3:
                adjective1 = random.choice(adjectives_neutral)
                adjective2 = random.choice([*adjectives_neutral, *adjectives_positive])
            else:
                adjective1 = random.choice(adjectives_negative)
                adjective2 = random.choice([*adjectives_negative, *adjectives_neutral])
            
            # Generate review content
            template = random.choice(review_content_templates)
            aspect1 = random.choice(aspects_destination)
            
            # Make sure aspect2 is different from aspect1
            aspect2 = random.choice([a for a in aspects_destination if a != aspect1])
            
            content = template.format(
                adverb=random.choice(adverbs),
                verb=random.choice(verbs),
                time=random.choice(times),
                entity=destination.name,
                aspect1=aspect1,
                aspect2=aspect2,
                adjective1=adjective1,
                adjective2=adjective2,
                highlight=random.choice(highlights),
                additional_comment=random.choice(additional_comments),
                recommendation=random.choice(recommendations) if rating >= 3 else "not",
                recommendation_strength=random.choice(recommendation_strengths) if rating >= 3 else "not the best choice",
                audience=random.choice(audiences),
                purpose=random.choice(purposes),
                overall=random.choice(overall_experiences) if rating >= 3 else "disappointing"
            )
            
            # Determine if this review should have images
            has_images = random.random() < 0.7  # 70% chance of having images
            
            images = None
            if has_images:
                # Choose appropriate image set based on destination category
                if destination.category == 'beach':
                    image_set = beach_images
                elif destination.category == 'mountain':
                    image_set = mountain_images
                elif destination.category == 'city':
                    image_set = city_images
                else:
                    image_set = [*beach_images, *mountain_images, *city_images]
                
                # Select 1-3 random images
                num_images = random.randint(1, min(3, len(image_set)))
                selected_images = random.sample(image_set, num_images)
                images = ','.join(selected_images)
            
            # Create review date (within the last year)
            days_ago = random.randint(0, 365)
            review_date = (datetime.utcnow() - timedelta(days=days_ago)).date()
            
            # Create the review
            review = Review(
                title=random.choice(destination_titles),
                content=content,
                rating=rating,
                review_date=review_date,
                is_public=True,
                images=images,
                user_id=user.id,
                destination_id=destination.id
            )
            
            reviews_to_create.append(review)
    
    # Accommodation reviews (similar pattern)
    for accommodation in accommodations:
        num_reviews = random.randint(0, 3)  # Fewer reviews for accommodations
        
        for _ in range(num_reviews):
            user = random.choice(users)
            rating = random.randint(2, 5)
            
            if rating >= 4:
                adjective1 = random.choice(adjectives_positive)
                adjective2 = random.choice(adjectives_positive)
            elif rating == 3:
                adjective1 = random.choice(adjectives_neutral)
                adjective2 = random.choice([*adjectives_neutral, *adjectives_positive])
            else:
                adjective1 = random.choice(adjectives_negative)
                adjective2 = random.choice([*adjectives_negative, *adjectives_neutral])
            
            template = random.choice(review_content_templates)
            aspect1 = random.choice(aspects_accommodation)
            aspect2 = random.choice([a for a in aspects_accommodation if a != aspect1])
            
            content = template.format(
                adverb=random.choice(adverbs),
                verb=random.choice(verbs),
                time=random.choice(times),
                entity=accommodation.name,
                aspect1=aspect1,
                aspect2=aspect2,
                adjective1=adjective1,
                adjective2=adjective2,
                highlight=random.choice(highlights),
                additional_comment=random.choice(additional_comments),
                recommendation=random.choice(recommendations) if rating >= 3 else "not",
                recommendation_strength=random.choice(recommendation_strengths) if rating >= 3 else "not the best choice",
                audience=random.choice(audiences),
                purpose=random.choice(purposes),
                overall=random.choice(overall_experiences) if rating >= 3 else "disappointing"
            )
            
            has_images = random.random() < 0.5  # 50% chance of having images
            
            images = None
            if has_images:
                num_images = random.randint(1, 2)
                selected_images = random.sample(hotel_images, num_images)
                images = ','.join(selected_images)
            
            days_ago = random.randint(0, 180)  # More recent reviews
            review_date = (datetime.utcnow() - timedelta(days=days_ago)).date()
            
            review = Review(
                title=random.choice(accommodation_titles),
                content=content,
                rating=rating,
                review_date=review_date,
                is_public=True,
                images=images,
                user_id=user.id,
                accommodation_id=accommodation.id
            )
            
            reviews_to_create.append(review)
    
    # Transportation reviews
    for transportation in transportations:
        num_reviews = random.randint(0, 2)  # Even fewer reviews for transportation
        
        for _ in range(num_reviews):
            user = random.choice(users)
            rating = random.randint(2, 5)
            
            if rating >= 4:
                adjective1 = random.choice(adjectives_positive)
                adjective2 = random.choice(adjectives_positive)
            elif rating == 3:
                adjective1 = random.choice(adjectives_neutral)
                adjective2 = random.choice([*adjectives_neutral, *adjectives_positive])
            else:
                adjective1 = random.choice(adjectives_negative)
                adjective2 = random.choice([*adjectives_negative, *adjectives_neutral])
            
            template = random.choice(review_content_templates)
            aspect1 = random.choice(aspects_transportation)
            aspect2 = random.choice([a for a in aspects_transportation if a != aspect1])
            
            content = template.format(
                adverb=random.choice(adverbs),
                verb=random.choice(verbs),
                time=random.choice(times),
                entity=transportation.provider,
                aspect1=aspect1,
                aspect2=aspect2,
                adjective1=adjective1,
                adjective2=adjective2,
                highlight=random.choice(highlights),
                additional_comment=random.choice(additional_comments),
                recommendation=random.choice(recommendations) if rating >= 3 else "not",
                recommendation_strength=random.choice(recommendation_strengths) if rating >= 3 else "not the best choice",
                audience=random.choice(audiences),
                purpose=random.choice(purposes),
                overall=random.choice(overall_experiences) if rating >= 3 else "disappointing"
            )
            
            # Transportation reviews rarely have images
            has_images = random.random() < 0.3
            
            images = None
            if has_images:
                num_images = 1
                selected_images = random.sample([
                    "https://images.unsplash.com/photo-1436491865332-7a61a109cc05",
                    "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957",
                    "https://images.unsplash.com/photo-1517400508447-f8dd518b86db"
                ], num_images)
                images = ','.join(selected_images)
            
            days_ago = random.randint(0, 120)
            review_date = (datetime.utcnow() - timedelta(days=days_ago)).date()
            
            review = Review(
                title=random.choice(transportation_titles),
                content=content,
                rating=rating,
                review_date=review_date,
                is_public=True,
                images=images,
                user_id=user.id,
                transportation_id=transportation.id
            )
            
            reviews_to_create.append(review)
    
    # Activity reviews
    for activity in activities:
        num_reviews = random.randint(0, 3)
        
        for _ in range(num_reviews):
            user = random.choice(users)
            rating = random.randint(3, 5)  # Activities tend to get better reviews
            
            if random.random() < 0.1:
                rating = random.randint(1, 2)
            
            if rating >= 4:
                adjective1 = random.choice(adjectives_positive)
                adjective2 = random.choice(adjectives_positive)
            elif rating == 3:
                adjective1 = random.choice(adjectives_neutral)
                adjective2 = random.choice([*adjectives_neutral, *adjectives_positive])
            else:
                adjective1 = random.choice(adjectives_negative)
                adjective2 = random.choice([*adjectives_negative, *adjectives_neutral])
            
            template = random.choice(review_content_templates)
            aspect1 = random.choice(aspects_activity)
            aspect2 = random.choice([a for a in aspects_activity if a != aspect1])
            
            content = template.format(
                adverb=random.choice(adverbs),
                verb=random.choice(verbs),
                time=random.choice(times),
                entity=activity.name,
                aspect1=aspect1,
                aspect2=aspect2,
                adjective1=adjective1,
                adjective2=adjective2,
                highlight=random.choice(highlights),
                additional_comment=random.choice(additional_comments),
                recommendation=random.choice(recommendations) if rating >= 3 else "not",
                recommendation_strength=random.choice(recommendation_strengths) if rating >= 3 else "not the best choice",
                audience=random.choice(audiences),
                purpose=random.choice(purposes),
                overall=random.choice(overall_experiences) if rating >= 3 else "disappointing"
            )
            
            has_images = random.random() < 0.8  # 80% chance of having images for activities
            
            images = None
            if has_images:
                num_images = random.randint(1, 3)
                selected_images = random.sample(activity_images, num_images)
                images = ','.join(selected_images)
            
            days_ago = random.randint(0, 90)  # More recent reviews
            review_date = (datetime.utcnow() - timedelta(days=days_ago)).date()
            
            review = Review(
                title=random.choice(activity_titles),
                content=content,
                rating=rating,
                review_date=review_date,
                is_public=True,
                images=images,
                user_id=user.id,
                activity_id=activity.id
            )
            
            reviews_to_create.append(review)
    
    # Add all reviews to the database
    db.session.add_all(reviews_to_create)
    db.session.commit()
    
    print(f"Successfully created {len(reviews_to_create)} sample reviews!")

if __name__ == "__main__":
    from config import DevelopmentConfig
    app = create_app(DevelopmentConfig)
    with app.app_context():
        create_sample_reviews() 