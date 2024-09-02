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

## Setup

### Prerequisites

- Python 3.x
- MySQL Server
- ChromeDriver (for Selenium)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/dorm-registration-system.git
   cd dorm-registration-system
