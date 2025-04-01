"""
Sample destinations data for the Trip Planner application.
Run this script to populate the database with sample destinations.
"""

import sys
import os

# Add the parent directory to the path so we can import the app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import db, create_app
from app.models import Destination

def create_sample_destinations():
    """Create sample destinations for the application."""
    print("Creating sample destinations...")
    
    # Sample destinations data
    destinations = [
        {
            'name': 'Eiffel Tower',
            'description': 'The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris, France. It is named after the engineer Gustave Eiffel, whose company designed and built the tower.',
            'country': 'France',
            'city': 'Paris',
            'address': 'Champ de Mars, 5 Avenue Anatole France, 75007 Paris',
            'latitude': 48.8584,
            'longitude': 2.2945,
            'image_url': 'https://images.unsplash.com/photo-1543349689-9a4d426bee8e',
            'category': 'city',
            'popularity': 9,
            'best_time_to_visit': 'April to June, September to October',
            'timezone': 'CET',
            'language': 'French',
            'currency': 'Euro'
        },
        {
            'name': 'Santorini',
            'description': 'Santorini is one of the Cyclades islands in the Aegean Sea. It was devastated by a volcanic eruption in the 16th century BC, forever shaping its rugged landscape.',
            'country': 'Greece',
            'city': 'Thira',
            'address': 'Santorini Island, Greece',
            'latitude': 36.3932,
            'longitude': 25.4615,
            'image_url': 'https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff',
            'category': 'beach',
            'popularity': 10,
            'best_time_to_visit': 'April to May, September to October',
            'timezone': 'EET',
            'language': 'Greek',
            'currency': 'Euro'
        },
        {
            'name': 'Grand Canyon',
            'description': 'The Grand Canyon is a steep-sided canyon carved by the Colorado River in Arizona, United States. The Grand Canyon is 277 miles long, up to 18 miles wide and attains a depth of over a mile.',
            'country': 'United States',
            'city': 'Grand Canyon Village',
            'address': 'Grand Canyon National Park, AZ 86023',
            'latitude': 36.0544,
            'longitude': -112.2401,
            'image_url': 'https://images.unsplash.com/photo-1615551043360-33de8b5f410c',
            'category': 'mountain',
            'popularity': 9,
            'best_time_to_visit': 'March to May, September to November',
            'timezone': 'MST',
            'language': 'English',
            'currency': 'USD'
        },
        {
            'name': 'Machu Picchu',
            'description': 'Machu Picchu is an Incan citadel set high in the Andes Mountains in Peru, above the Urubamba River valley. Built in the 15th century and later abandoned, it\'s renowned for its sophisticated dry-stone walls that fuse huge blocks without the use of mortar.',
            'country': 'Peru',
            'city': 'Cusco',
            'address': 'Machu Picchu, Peru',
            'latitude': -13.1631,
            'longitude': -72.5450,
            'image_url': 'https://images.unsplash.com/photo-1526392060635-9d6019884377',
            'category': 'historical',
            'popularity': 10,
            'best_time_to_visit': 'May to September',
            'timezone': 'PET',
            'language': 'Spanish',
            'currency': 'Peruvian Sol'
        },
        {
            'name': 'Bali',
            'description': 'Bali is an Indonesian island known for its forested volcanic mountains, iconic rice paddies, beaches and coral reefs. The island is home to religious sites such as cliffside Uluwatu Temple.',
            'country': 'Indonesia',
            'city': 'Denpasar',
            'address': 'Bali, Indonesia',
            'latitude': -8.3405,
            'longitude': 115.0920,
            'image_url': 'https://images.unsplash.com/photo-1537996194471-e657df975ab4',
            'category': 'beach',
            'popularity': 9,
            'best_time_to_visit': 'April to October',
            'timezone': 'WITA',
            'language': 'Indonesian',
            'currency': 'Indonesian Rupiah'
        },
        {
            'name': 'Kyoto',
            'description': 'Kyoto, once the capital of Japan, is a city on the island of Honshu. It\'s famous for its numerous classical Buddhist temples, as well as gardens, imperial palaces, Shinto shrines and traditional wooden houses.',
            'country': 'Japan',
            'city': 'Kyoto',
            'address': 'Kyoto, Japan',
            'latitude': 35.0116,
            'longitude': 135.7681,
            'image_url': 'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
            'category': 'city',
            'popularity': 8,
            'best_time_to_visit': 'March to May, September to November',
            'timezone': 'JST',
            'language': 'Japanese',
            'currency': 'Japanese Yen'
        },
        {
            'name': 'Swiss Alps',
            'description': 'The Swiss Alps are the portion of the Alps mountain range that lies within Switzerland. Because of their central position within the entire Alpine range, they are also known as the Central Alps.',
            'country': 'Switzerland',
            'city': 'Zermatt',
            'address': 'Swiss Alps, Switzerland',
            'latitude': 46.0207,
            'longitude': 7.7491,
            'image_url': 'https://images.unsplash.com/photo-1531210483974-4f8c1f33fd35',
            'category': 'mountain',
            'popularity': 9,
            'best_time_to_visit': 'June to September for hiking, December to March for skiing',
            'timezone': 'CET',
            'language': 'German, French, Italian, Romansh',
            'currency': 'Swiss Franc'
        },
        {
            'name': 'Great Barrier Reef',
            'description': 'The Great Barrier Reef is the world\'s largest coral reef system composed of over 2,900 individual reefs and 900 islands stretching for over 2,300 kilometres over an area of approximately 344,400 square kilometres.',
            'country': 'Australia',
            'city': 'Cairns',
            'address': 'Great Barrier Reef, Queensland, Australia',
            'latitude': -18.2871,
            'longitude': 147.6992,
            'image_url': 'https://images.unsplash.com/photo-1559592413-7cec4d0cae2b',
            'category': 'beach',
            'popularity': 10,
            'best_time_to_visit': 'June to October',
            'timezone': 'AEST',
            'language': 'English',
            'currency': 'Australian Dollar'
        },
        {
            'name': 'Petra',
            'description': 'Petra is a famous archaeological site in Jordan\'s southwestern desert. Dating to around 300 B.C., it was the capital of the Nabatean Kingdom. Accessed via a narrow canyon called Al Siq, it contains tombs and temples carved into pink sandstone cliffs, earning its nickname, the "Rose City."',
            'country': 'Jordan',
            'city': 'Wadi Musa',
            'address': 'Petra, Jordan',
            'latitude': 30.3285,
            'longitude': 35.4444,
            'image_url': 'https://images.unsplash.com/photo-1563177978-4c5eb2d8ad6c',
            'category': 'historical',
            'popularity': 9,
            'best_time_to_visit': 'March to May, September to November',
            'timezone': 'EET',
            'language': 'Arabic',
            'currency': 'Jordanian Dinar'
        },
        {
            'name': 'Venice',
            'description': 'Venice, the capital of northern Italy\'s Veneto region, is built on more than 100 small islands in a lagoon in the Adriatic Sea. It has no roads, just canals – including the Grand Canal thoroughfare – lined with Renaissance and Gothic palaces.',
            'country': 'Italy',
            'city': 'Venice',
            'address': 'Venice, Metropolitan City of Venice, Italy',
            'latitude': 45.4408,
            'longitude': 12.3155,
            'image_url': 'https://images.unsplash.com/photo-1514890547357-a9ee288728e0',
            'category': 'city',
            'popularity': 9,
            'best_time_to_visit': 'April to June, September to October',
            'timezone': 'CET',
            'language': 'Italian',
            'currency': 'Euro'
        }
    ]
    
    # Create destination objects
    destination_objects = []
    for dest_data in destinations:
        destination = Destination(**dest_data)
        destination_objects.append(destination)
    
    # Add all destinations to the database
    db.session.add_all(destination_objects)
    db.session.commit()
    
    print(f"Successfully created {len(destination_objects)} sample destinations!")

if __name__ == "__main__":
    from config import DevelopmentConfig
    app = create_app(DevelopmentConfig)
    with app.app_context():
        create_sample_destinations() 