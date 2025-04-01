# Sample Data for Trip Planner Application

This directory contains scripts to populate your database with sample data for testing and development purposes.

## Available Sample Data Scripts

- `sample_reviews.py`: Generates realistic reviews for destinations, accommodations, transportation, and activities.

## How to Use the Sample Reviews Script

The sample reviews script creates realistic reviews for entities in your database. It uses templates and word banks to generate varied and natural-sounding reviews.

### Prerequisites

Before running the script, make sure you have:

1. Set up your database and run the initial migrations
2. Created at least one user account
3. Added some destinations, accommodations, transportation options, or activities to review

### Running the Script

To populate your database with sample reviews:

```bash
# Navigate to the project root directory
cd /path/to/trip_planer

# Run the sample reviews script
python database/sample_reviews.py
```

### What the Script Does

The script:

1. Retrieves existing users and reviewable entities from your database
2. Generates a varied number of reviews for each entity
3. Creates realistic review content using templates and word banks
4. Assigns appropriate ratings (mostly positive, with some neutral and negative for realism)
5. Adds relevant images to some reviews
6. Sets review dates within the past year
7. Saves all reviews to the database

### Sample Review Features

The generated reviews include:

- Varied titles appropriate to the entity type
- Realistic content with proper grammar and natural language
- Star ratings from 1-5 (weighted toward positive experiences)
- Review dates distributed over the past year
- Images for some reviews (more common for destinations and activities)
- Different writing styles and tones
- Entity-specific details and terminology

### Customization

You can modify the script to:

- Change the distribution of ratings
- Add more templates or word options
- Adjust the frequency of images
- Modify the date range for reviews

## Example Reviews

Here are some examples of the types of reviews the script generates:

### Destination Review Example

**Title:** "Breathtaking views everywhere"  
**Rating:** ★★★★★  
**Content:** "I absolutely loved my time at Santorini. The scenery was stunning and the local cuisine was exceptional. We had an unforgettable time. I'd suggest booking in advance to secure your spot. I would definitely recommend this to couples."

### Accommodation Review Example

**Title:** "Comfortable stay with great amenities"  
**Rating:** ★★★★☆  
**Content:** "Our experience at Grand Hotel was fantastic. It was worth every penny. The room was spacious, and we particularly enjoyed the breakfast. The staff went above and beyond to make our experience special. Highly recommended for anyone looking for a luxury experience."

### Transportation Review Example

**Title:** "On-time and efficient service"  
**Rating:** ★★★☆☆  
**Content:** "My journey with Express Airlines was satisfactory. I found the punctuality to be adequate and the seating was comfortable. It's suitable for all ages and interests. A decent option worth experiencing."

### Activity Review Example

**Title:** "Thrilling experience!"  
**Rating:** ★★★★★  
**Content:** "Scuba diving excursion exceeded all my expectations. The safety measures were excellent and the instruction was outstanding. The experience was truly one-of-a-kind. We're already planning our next visit. Strongly recommended for adventure seekers." 