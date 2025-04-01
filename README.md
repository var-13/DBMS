# **Personalized Trip Planner**  

A comprehensive trip planning application with MySQL database integration, Flask backend, and an interactive frontend.

## **Features**  

- ✅ User authentication and profile management  
- ✅ Trip creation and management  
- ✅ Destination browsing and searching  
- ✅ Accommodation booking  
- ✅ Transportation options  
- ✅ Activity planning  
- ✅ Budget tracking  
- ✅ Itinerary generation  
- ✅ Weather information  
- ✅ Travel recommendations  
- ✅ Reviews and ratings  
- ✅ Social sharing  

## **Tech Stack**  

- **Backend**: Flask (Python)  
- **Database**: MySQL  
- **Frontend**: HTML, CSS, JavaScript (with animations)  
- **ORM**: SQLAlchemy  

## **Project Structure**  

```
trip_planner/
├── app/
│   ├── models/         # Database models
│   ├── routes/         # API routes
│   ├── static/         # Static files (CSS, JS, images)
│   ├── templates/      # HTML templates
│   └── utils/          # Utility functions
├── database/           # Database scripts and migrations
├── .env                # Environment variables (not in version control)
├── .gitignore          # Git ignore file
├── config.py           # Application configuration
├── requirements.txt    # Python dependencies
└── run.py              # Application entry point
```

## **Setup Instructions**  

### **Prerequisites**  

- Python 3.8+  
- MySQL 8.0+  
- pip (Python package manager)  

### **Installation**  

1. **Clone the repository:**  
   ```sh
   git clone <repository-url>
   cd trip_planner
   ```

2. **Create and activate a virtual environment:**  
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**  
   ```sh
   pip install -r requirements.txt
   ```

4. **Create a `.env` file in the root directory with the following variables:**  
   ```
   FLASK_APP=run.py
   FLASK_ENV=development
   SECRET_KEY=your_secret_key
   DATABASE_URI=mysql://username:password@localhost/trip_planner
   ```

5. **Initialize the database:**  
   ```sh
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

6. **Run the application:**  
   ```sh
   flask run
   ```

7. **Access the application at:**  
   `http://localhost:5000`  

## **Database Schema**  

The application uses 12 main entities:
- Users  
- Trips  
- Destinations  
- Accommodations  
- Transportation  
- Activities  
- Itineraries  
- Expenses  
- Reviews  
- Preferences  
- Weather  
- Notifications  

## **Contributing**  

We welcome contributions! Feel free to submit issues and pull requests.  

## **License**  

This project is licensed under the MIT License.  

## **Contact**  



