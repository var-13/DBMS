"""
Database initialization script for Trip Planner application.
This script creates the database schema and populates it with initial data.
"""

import os
import sys
import mysql.connector
from mysql.connector import Error
from getpass import getpass

# Add the parent directory to the path so we can import the app config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import DevelopmentConfig

def create_database(host, user, password, database):
    """Create the database if it doesn't exist."""
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database if it doesn't exist
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
            print(f"Database '{database}' created or already exists.")
            
            # Close connection
            cursor.close()
            connection.close()
            return True
            
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return False

def execute_sql_script(host, user, password, database, sql_file):
    """Execute SQL script to create tables and initial data."""
    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Read SQL script
            with open(sql_file, 'r') as file:
                sql_script = file.read()
            
            # Split script by delimiter to handle triggers
            statements = sql_script.split('DELIMITER //')
            
            if len(statements) > 1:
                # Execute the first part (before DELIMITER //)
                cursor.execute(statements[0])
                connection.commit()
                
                # Handle the trigger definitions
                trigger_section = statements[1].split('DELIMITER ;')[0]
                triggers = trigger_section.split('END //')
                
                for trigger in triggers:
                    if trigger.strip():
                        cursor.execute(trigger + 'END')
                        connection.commit()
                
                # Execute the last part (after DELIMITER ;)
                if len(statements[1].split('DELIMITER ;')) > 1:
                    cursor.execute(statements[1].split('DELIMITER ;')[1])
                    connection.commit()
            else:
                # Execute the entire script if there are no DELIMITER statements
                cursor.execute(sql_script)
                connection.commit()
            
            print("Database schema created successfully.")
            
            # Close connection
            cursor.close()
            connection.close()
            return True
            
    except Error as e:
        print(f"Error while executing SQL script: {e}")
        return False

def main():
    """Main function to initialize the database."""
    # Get database configuration from config
    db_config = DevelopmentConfig.SQLALCHEMY_DATABASE_URI
    
    # Parse database URI
    # Format: mysql://username:password@host:port/database
    db_parts = db_config.replace('mysql://', '').split('@')
    user_pass = db_parts[0].split(':')
    host_db = db_parts[1].split('/')
    
    user = user_pass[0]
    password = user_pass[1] if len(user_pass) > 1 else ''
    host = host_db[0]
    database = host_db[1]
    
    # If password is not in config, prompt for it
    if not password:
        password = getpass("Enter MySQL password: ")
    
    # Create database
    if not create_database(host, user, password, database):
        print("Failed to create database. Exiting.")
        return
    
    # Execute SQL script
    sql_file = os.path.join(os.path.dirname(__file__), 'schema.sql')
    if not os.path.exists(sql_file):
        print(f"SQL file not found: {sql_file}")
        return
    
    if execute_sql_script(host, user, password, database, sql_file):
        print("Database initialization completed successfully.")
    else:
        print("Failed to initialize database schema.")

if __name__ == "__main__":
    main() 