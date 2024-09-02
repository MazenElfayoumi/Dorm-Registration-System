# Dorm Registration System

## Overview

The Dorm Registration System is a web application developed for Galala University to manage student and employee registrations in the university dorms. The system provides functionalities for registering students and employees, searching for records, managing profiles, and handling violations and bookings. The application is built using Flask for the backend, MySQL for the database, and HTML/CSS for the frontend. Selenium is utilized for software testing to ensure smooth operation.

## Technologies Used

- **Backend:** Flask
- **Database:** MySQL
- **Frontend:** HTML, CSS
- **Testing:** Selenium

## Features

- **User Authentication:** Login and session management for users.
- **Student Registration:** Add and view student details.
- **Employee Registration:** Add and view employee details.
- **Search Functionality:** Search for students and employees by various criteria.
- **Profile Management:** View and manage user profiles.
- **Violation Tracking:** Add and search for violations.
- **Booking Management:** Manage room bookings.
- **Medical Conditions & GPA Search:** Search students by medical conditions and GPA.

## Project Structure

- `app.py`: Main application file containing routes and logic.
- `templates/`: Contains HTML templates for different pages.
- `static/`: Contains CSS files and other static resources.
- `tests/`: Contains test scripts using Selenium.
- `database/`: Contains SQL scripts and database schema.

### Prerequisites

- Python 3.x
- MySQL Server
- ChromeDriver (for Selenium)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/dorm-registration-system.git
   cd dorm-registration-system

2. **Clone the Repository**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   
4. **Set Up the Database**
   ```bash
   CREATE DATABASE dorms;
   mysql -u root -p dorms < database/schema.sql 
   ```
5. **Configure the Application**
   ```bash
   - SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:your_password@localhost/dorms'
   ```
6. **Run the Application**
   ```bash
   python app.py
   ```
## Testing

- Selenium is used for testing.
- Ensure ChromeDriver is installed and configured properly.
- Run the Selenium tests from the `tests/` directory to validate the application.

## Screenshots


Include screenshots of the application:

-*Booking Management:** ![login](https://github.com/user-attachments/assets/12643b0c-55ca-4cc5-a2ea-55d061c54200)
- ![register](https://github.com/user-attachments/assets/0c16c20b-708b-454c-8b42-f68f8d350abf)


## ERD Diagram

- ![ERD Diagram](images/erd-diagram.png)

## Contributing

Feel free to submit issues or pull requests. Make sure to follow the coding standards and include tests for new features.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
