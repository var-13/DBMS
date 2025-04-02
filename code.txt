create database trip_planner;
use trip_planner;

-- Create Users table
CREATE TABLE users (
    id VARCHAR(36) PRIMARY KEY,
    username VARCHAR(64) NOT NULL UNIQUE,
    email VARCHAR(120) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(64),
    last_name VARCHAR(64),
    profile_picture VARCHAR(255),
    bio TEXT,
    phone_number VARCHAR(20),
    date_of_birth DATE,
    address VARCHAR(255),
    city VARCHAR(64),
    country VARCHAR(64),
    is_admin BOOLEAN DEFAULT FALSE,
    is_active BOOLEAN DEFAULT TRUE,
    last_login DATETIME,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_username (username),
    INDEX idx_email (email)
);

-- Create Destinations table
CREATE TABLE destinations (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    description TEXT,
    country VARCHAR(64) NOT NULL,
    city VARCHAR(64) NOT NULL,
    address VARCHAR(255),
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8),
    image_url VARCHAR(255),
    category VARCHAR(64),
    popularity INT DEFAULT 0,
    best_time_to_visit VARCHAR(128),
    timezone VARCHAR(64),
    language VARCHAR(64),
    currency VARCHAR(64),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_country_city (country, city),
    INDEX idx_category (category),
    INDEX idx_popularity (popularity)
);

-- Create Expense Categories table
CREATE TABLE expense_categories (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(64) NOT NULL,
    icon VARCHAR(64),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Create User Preferences table
CREATE TABLE preferences (
    id VARCHAR(36) PRIMARY KEY,
    user_id VARCHAR(36) NOT NULL UNIQUE,
    preferred_destinations TEXT,
    preferred_accommodation_types TEXT,
    preferred_transportation_types TEXT,
    preferred_activities TEXT,
    preferred_cuisines TEXT,
    budget_category VARCHAR(64),
    max_accommodation_budget DECIMAL(10, 2),
    max_transportation_budget DECIMAL(10, 2),
    max_activity_budget DECIMAL(10, 2),
    max_food_budget DECIMAL(10, 2),
    preferred_currency VARCHAR(3) DEFAULT 'USD',
    accessibility_requirements TEXT,
    dietary_restrictions TEXT,
    preferred_trip_duration INT,
    preferred_travel_seasons TEXT,
    travel_style VARCHAR(64),
    notification_preferences TEXT,
    language VARCHAR(5) DEFAULT 'en-US',
    theme VARCHAR(64) DEFAULT 'light',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create Trips table
CREATE TABLE trips (
    id VARCHAR(36) PRIMARY KEY,
    title VARCHAR(128) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    is_public BOOLEAN DEFAULT FALSE,
    status VARCHAR(20) DEFAULT 'planning',
    cover_image VARCHAR(255),
    total_budget DECIMAL(10, 2),
    notes TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    user_id VARCHAR(36) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_user_id (user_id),
    INDEX idx_start_date (start_date),
    INDEX idx_status (status)
);

-- Add check constraint for trip dates
ALTER TABLE trips ADD CONSTRAINT check_dates CHECK (end_date >= start_date);

-- Create Trip-Destinations association table (many-to-many)
CREATE TABLE trip_destinations (
    trip_id VARCHAR(36) NOT NULL,
    destination_id VARCHAR(36) NOT NULL,
    PRIMARY KEY (trip_id, destination_id),
    FOREIGN KEY (trip_id) REFERENCES trips(id) ON DELETE CASCADE,
    FOREIGN KEY (destination_id) REFERENCES destinations(id) ON DELETE CASCADE
);

-- Create Accommodations table
CREATE TABLE accommodations (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    type VARCHAR(64) NOT NULL,
    description TEXT,
    address VARCHAR(255),
    check_in_date DATE NOT NULL,
    check_out_date DATE NOT NULL,
    price_per_night DECIMAL(10, 2) NOT NULL,
    total_price DECIMAL(10, 2),
    booking_reference VARCHAR(128),
    booking_status VARCHAR(64) DEFAULT 'pending',
    contact_info VARCHAR(255),
    amenities TEXT,
    rating INT,
    image_url VARCHAR(255),
    notes TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    trip_id VARCHAR(36) NOT NULL,
    destination_id VARCHAR(36) NOT NULL,
    FOREIGN KEY (trip_id) REFERENCES trips(id) ON DELETE CASCADE,
    FOREIGN KEY (destination_id) REFERENCES destinations(id) ON DELETE CASCADE,
    INDEX idx_trip_id (trip_id)
);

-- Add check constraint for accommodation dates
ALTER TABLE accommodations ADD CONSTRAINT check_accommodation_dates CHECK (check_out_date >= check_in_date);

-- Create Transportations table
CREATE TABLE transportations (
    id VARCHAR(36) PRIMARY KEY,
    type VARCHAR(64) NOT NULL,
    provider VARCHAR(128),
    departure_location VARCHAR(128) NOT NULL,
    arrival_location VARCHAR(128) NOT NULL,
    departure_datetime DATETIME NOT NULL,
    arrival_datetime DATETIME NOT NULL,
    booking_reference VARCHAR(128),
    booking_status VARCHAR(64) DEFAULT 'pending',
    seat_number VARCHAR(64),
    price DECIMAL(10, 2),
    confirmation_email VARCHAR(255),
    notes TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    trip_id VARCHAR(36) NOT NULL,
    FOREIGN KEY (trip_id) REFERENCES trips(id) ON DELETE CASCADE,
    INDEX idx_trip_id (trip_id)
);

-- Add check constraint for transportation dates
ALTER TABLE transportations ADD CONSTRAINT check_transportation_dates CHECK (arrival_datetime >= departure_datetime);

-- Create Activities table
CREATE TABLE activities (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    type VARCHAR(64) NOT NULL,
    description TEXT,
    location VARCHAR(255),
    start_datetime DATETIME NOT NULL,
    end_datetime DATETIME,
    price DECIMAL(10, 2),
    booking_reference VARCHAR(128),
    booking_status VARCHAR(64) DEFAULT 'pending',
    contact_info VARCHAR(255),
    image_url VARCHAR(255),
    notes TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    trip_id VARCHAR(36) NOT NULL,
    destination_id VARCHAR(36) NOT NULL,
    FOREIGN KEY (trip_id) REFERENCES trips(id) ON DELETE CASCADE,
    FOREIGN KEY (destination_id) REFERENCES destinations(id) ON DELETE CASCADE,
    INDEX idx_trip_id (trip_id),
    INDEX idx_activity_type (type)
);

-- Create Itineraries table
CREATE TABLE itineraries (
    id VARCHAR(36) PRIMARY KEY,
    title VARCHAR(128) NOT NULL,
    description TEXT,
    date DATE NOT NULL,
    notes TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    trip_id VARCHAR(36) NOT NULL,
    FOREIGN KEY (trip_id) REFERENCES trips(id) ON DELETE CASCADE,
    INDEX idx_trip_id (trip_id),
    INDEX idx_date (date)
);

-- Create Itinerary Items table
CREATE TABLE itinerary_items (
    id VARCHAR(36) PRIMARY KEY,
    title VARCHAR(128) NOT NULL,
    description TEXT,
    start_time TIME NOT NULL,
    end_time TIME,
    location VARCHAR(255),
    notes TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    itinerary_id VARCHAR(36) NOT NULL,
    accommodation_id VARCHAR(36),
    transportation_id VARCHAR(36),
    activity_id VARCHAR(36),
    FOREIGN KEY (itinerary_id) REFERENCES itineraries(id) ON DELETE CASCADE,
    FOREIGN KEY (accommodation_id) REFERENCES accommodations(id) ON DELETE SET NULL,
    FOREIGN KEY (transportation_id) REFERENCES transportations(id) ON DELETE SET NULL,
    FOREIGN KEY (activity_id) REFERENCES activities(id) ON DELETE SET NULL,
    INDEX idx_itinerary_id (itinerary_id)
);

-- Add check constraint for itinerary item times
ALTER TABLE itinerary_items ADD CONSTRAINT check_item_times CHECK (end_time >= start_time);

-- Create Expenses table
CREATE TABLE expenses (
    id VARCHAR(36) PRIMARY KEY,
    title VARCHAR(128) NOT NULL,
    description TEXT,
    amount DECIMAL(10, 2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'USD',
    date DATE NOT NULL,
    payment_method VARCHAR(64),
    receipt_image VARCHAR(255),
    is_reimbursable BOOLEAN DEFAULT FALSE,
    is_shared BOOLEAN DEFAULT FALSE,
    notes TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    trip_id VARCHAR(36) NOT NULL,
    user_id VARCHAR(36) NOT NULL,
    category_id VARCHAR(36) NOT NULL,
    accommodation_id VARCHAR(36),
    transportation_id VARCHAR(36),
    activity_id VARCHAR(36),
    FOREIGN KEY (trip_id) REFERENCES trips(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES expense_categories(id) ON DELETE RESTRICT,
    FOREIGN KEY (accommodation_id) REFERENCES accommodations(id) ON DELETE SET NULL,
    FOREIGN KEY (transportation_id) REFERENCES transportations(id) ON DELETE SET NULL,
    FOREIGN KEY (activity_id) REFERENCES activities(id) ON DELETE SET NULL,
    INDEX idx_trip_id (trip_id),
    INDEX idx_user_id (user_id),
    INDEX idx_category_id (category_id),
    INDEX idx_date (date)
);

-- Create Reviews table
CREATE TABLE reviews (
    id VARCHAR(36) PRIMARY KEY,
    title VARCHAR(128) NOT NULL,
    content TEXT NOT NULL,
    rating INT NOT NULL,
    review_date DATE DEFAULT (CURRENT_DATE),
    is_public BOOLEAN DEFAULT TRUE,
    images TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    user_id VARCHAR(36) NOT NULL,
    destination_id VARCHAR(36),
    accommodation_id VARCHAR(36),
    transportation_id VARCHAR(36),
    activity_id VARCHAR(36),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (destination_id) REFERENCES destinations(id) ON DELETE SET NULL,
    FOREIGN KEY (accommodation_id) REFERENCES accommodations(id) ON DELETE SET NULL,
    FOREIGN KEY (transportation_id) REFERENCES transportations(id) ON DELETE SET NULL,
    FOREIGN KEY (activity_id) REFERENCES activities(id) ON DELETE SET NULL,
    INDEX idx_user_id (user_id),
    INDEX idx_rating (rating)
);

-- Add check constraints for reviews
ALTER TABLE reviews ADD CONSTRAINT check_rating CHECK (rating BETWEEN 1 AND 5);
ALTER TABLE reviews ADD CONSTRAINT check_review_entity CHECK (
    (destination_id IS NOT NULL AND accommodation_id IS NULL AND transportation_id IS NULL AND activity_id IS NULL) OR
    (destination_id IS NULL AND accommodation_id IS NOT NULL AND transportation_id IS NULL AND activity_id IS NULL) OR
    (destination_id IS NULL AND accommodation_id IS NULL AND transportation_id IS NOT NULL AND activity_id IS NULL) OR
    (destination_id IS NULL AND accommodation_id IS NULL AND transportation_id IS NULL AND activity_id IS NOT NULL)
);

-- Create Notifications table
CREATE TABLE notifications (
    id VARCHAR(36) PRIMARY KEY,
    title VARCHAR(128) NOT NULL,
    message TEXT NOT NULL,
    notification_type VARCHAR(64) NOT NULL,
    is_read BOOLEAN DEFAULT FALSE,
    is_dismissed BOOLEAN DEFAULT FALSE,
    action_url VARCHAR(255),
    icon VARCHAR(64),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    user_id VARCHAR(36) NOT NULL,
    trip_id VARCHAR(36),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (trip_id) REFERENCES trips(id) ON DELETE CASCADE,
    INDEX idx_user_id (user_id),
    INDEX idx_is_read (is_read),
    INDEX idx_is_dismissed (is_dismissed)
);

-- Insert default expense categories
INSERT INTO expense_categories (id, name, icon) VALUES
(UUID(), 'Accommodation', 'fa-hotel'),
(UUID(), 'Transportation', 'fa-plane'),
(UUID(), 'Food & Drinks', 'fa-utensils'),
(UUID(), 'Activities', 'fa-hiking'),
(UUID(), 'Shopping', 'fa-shopping-bag'),
(UUID(), 'Entertainment', 'fa-ticket-alt'),
(UUID(), 'Health & Medical', 'fa-medkit'),
(UUID(), 'Fees & Tips', 'fa-money-bill'),
(UUID(), 'Miscellaneous', 'fa-ellipsis-h');

-- Add triggers to update the updated_at timestamp
DELIMITER //
CREATE TRIGGER update_user_timestamp BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    SET NEW.updated_at = CURRENT_TIMESTAMP;
END //

CREATE TRIGGER update_destination_timestamp BEFORE UPDATE ON destinations
FOR EACH ROW
BEGIN
    SET NEW.updated_at = CURRENT_TIMESTAMP;
END //

CREATE TRIGGER update_expense_category_timestamp BEFORE UPDATE ON expense_categories
FOR EACH ROW
BEGIN
    SET NEW.updated_at = CURRENT_TIMESTAMP;
END //

CREATE TRIGGER update_preference_timestamp BEFORE UPDATE ON preferences
FOR EACH ROW
BEGIN
    SET NEW.updated_at = CURRENT_TIMESTAMP;
END //

CREATE TRIGGER update_trip_timestamp BEFORE UPDATE ON trips
FOR EACH ROW
BEGIN
    SET NEW.updated_at = CURRENT_TIMESTAMP;
END //

CREATE TRIGGER update_accommodation_timestamp BEFORE UPDATE ON accommodations
FOR EACH ROW
BEGIN
    SET NEW.updated_at = CURRENT_TIMESTAMP;
END //

CREATE TRIGGER update_transportation_timestamp BEFORE UPDATE ON transportations
FOR EACH ROW
BEGIN
    SET NEW.updated_at = CURRENT_TIMESTAMP;
END //

CREATE TRIGGER update_activity_timestamp BEFORE UPDATE ON activities
FOR EACH ROW
BEGIN
    SET NEW.updated_at = CURRENT_TIMESTAMP;
END //

CREATE TRIGGER update_itinerary_timestamp BEFORE UPDATE ON itineraries
FOR EACH ROW
BEGIN
    SET NEW.updated_at = CURRENT_TIMESTAMP;
END //

CREATE TRIGGER update_itinerary_item_timestamp BEFORE UPDATE ON itinerary_items
FOR EACH ROW
BEGIN
    SET NEW.updated_at = CURRENT_TIMESTAMP;
END //

CREATE TRIGGER update_expense_timestamp BEFORE UPDATE ON expenses
FOR EACH ROW
BEGIN
    SET NEW.updated_at = CURRENT_TIMESTAMP;
END //

CREATE TRIGGER update_review_timestamp BEFORE UPDATE ON reviews
FOR EACH ROW
BEGIN
    SET NEW.updated_at = CURRENT_TIMESTAMP;
END //

CREATE TRIGGER update_notification_timestamp BEFORE UPDATE ON notifications
FOR EACH ROW
BEGIN
    SET NEW.updated_at = CURRENT_TIMESTAMP;
END //
DELIMITER ; 
