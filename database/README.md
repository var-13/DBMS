# Trip Planner Database Setup

This directory contains scripts and SQL files for setting up and managing the Trip Planner database.

## Files

- `schema.sql`: MySQL schema definition for all tables in the Trip Planner application
- `init_db.py`: Python script to initialize the database using the schema
- `sample_destinations.py`: Script to populate the database with sample destinations
- `sample_reviews.py`: Script to populate the database with sample reviews
- `README_SAMPLE_DATA.md`: Documentation for the sample data scripts

## Database Schema

The Trip Planner database consists of the following main tables:

- `users`: User accounts and profile information
- `trips`: Trip plans created by users
- `destinations`: Travel destinations
- `accommodations`: Lodging information for trips
- `transportations`: Travel transportation details
- `activities`: Activities planned for trips
- `itineraries`: Daily plans for trips
- `expenses`: Financial transactions related to trips
- `reviews`: User reviews of destinations, accommodations, etc.
- `notifications`: System notifications for users

## Setting Up the Database

### Prerequisites

- MySQL server installed and running
- Python 3.7 or higher
- Required Python packages: `mysql-connector-python`

### Installation

1. Install required Python packages:

```bash
pip install mysql-connector-python
```

2. Configure database connection:

Make sure your database connection is properly configured in the `config.py` file at the root of the project. The script uses the `DevelopmentConfig` settings.

Example configuration:

```python
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/trip_planner'
```

### Initializing the Database

Run the initialization script to create the database and all tables:

```bash
python database/init_db.py
```

If your database password is not included in the configuration, the script will prompt you to enter it.

## Adding Sample Data

After initializing the database, you can populate it with sample data:

1. Add sample destinations:

```bash
python database/sample_destinations.py
```

2. Add sample reviews (requires destinations and users):

```bash
python database/sample_reviews.py
```

## Database Maintenance

### Backing Up the Database

To create a backup of your database:

```bash
mysqldump -u username -p trip_planner > backup.sql
```

### Restoring from Backup

To restore your database from a backup:

```bash
mysql -u username -p trip_planner < backup.sql
```

## Database Schema Diagram

For a visual representation of the database schema, see the entity-relationship diagram in the project documentation.

## Troubleshooting

- **Connection Issues**: Ensure your MySQL server is running and that the credentials in your config file are correct.
- **Permission Errors**: Make sure the MySQL user has sufficient privileges to create databases and tables.
- **Schema Errors**: If you encounter errors during schema creation, check the MySQL error logs for details. 