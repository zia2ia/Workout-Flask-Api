# Workout Tracker API

## Overview
The Workout Tracker API is designed to help users manage their workout routines by storing various workout data such as workout type, name, weight, and reps. This API provides essential CRUD (Create, Read, Update, Delete) functionalities, allowing users to interact with the workout data via a RESTful interface.

The API is built using Flask, a lightweight Python web framework, and SQLite, a serverless, self-contained database engine. The application ensures proper validation for data entries and includes features to enforce limits on workout repetitions and weight.

## Project Structure 
The project is organized with a Flask application that serves as the backend API. The data layer is handled by SQLAlchemy, which provides a powerful Object Relational Mapping (ORM) system, making it easy to interact with the SQLite database. The database stores workout entries with constraints to ensure data integrity.

The project consists of:

1. Application Code: The core logic for handling API requests, validation, and database transactions.
2. Database Models: Definitions for storing workout data and enforcing rules on entries.
3. Validation: Checks to ensure that reps and weight stay within specified bounds.

### API Structure
1. GET Requests: Fetch all workouts or a specific workout by ID.
2. POST Requests: Create new workouts by sending workout details.
3. PUT Requests: Update existing workout data by ID.
4. DELETE Requests: Remove workout entries by ID.

## Setup and Installation
### 1. Prerequisites
Ensure that you have Python installed on your machine. You will also need pip and git to install dependencies, it is also reccomneded you step up a virtual environment before installing this project in order not to add extra installations to your main machine. 

### 2. Installation Steps 
(1) Clone the Repository:
After downloading the project files from the repository and naviagte into the project directory using these commands in the terminal.

* git clone <repository-url>
  
* cd workout-tracker-api

(2) Install Dependencies:
Install the required dependencies (such as Flask and SQLAlchemy) by running:

- pip install -r requirements.txt

(3) Set Up the Database:
Initialize the SQLite database and create the necessary tables by opening a Python shell and running the following commands:
- from application import db
- db.create_all()
- exit()

(4) Set the FLASK_APP Environment Variable:
Set the FLASK_APP environment variable to point to your Flask application, using this command:

- set FLASK_APP=application.py

(5) Optionally, you can also put the flask app into development mode by running:

- set FLASK_ENV=development

(6) Run the Application:
Once the environment variable is set, run the application using:
- flask run

(7) If that run command does not work you can run the app directly by using:

- flask --app application.py run


