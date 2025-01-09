# Job Portal System
A web-based application that connects job seekers with recruiters. The system allows users to post job openings, create user profiles, apply for jobs, and track application statuses.

# Features
Job Listings: View, post, and search for jobs based on criteria like title, location, skills, and salary.
User Profiles: Create and manage user profiles with unique user IDs.
Job Applications: Apply for jobs and track the status of applications.
Search Functionality: Search jobs dynamically using keywords.
Installation
1. Clone the Repository
bash
Copy code
git clone <repository-url>
cd job-portal-system
# 2. Create a Virtual Environment
bash
Copy code
python -m venv venv
# 3. Activate the Virtual Environment
On Windows:
bash
Copy code
.\venv\Scripts\activate
On macOS/Linux:
bash
Copy code
source venv/bin/activate
# 4. Install Dependencies
bash
Copy code
pip install -r requirements.txt
# 5. Initialize the Database
Run the following commands to set up the database:

bash
Copy code
python
>>> from app import db
>>> db.create_all()
>>> exit()
# Usage
1. Run the Flask Application
bash
Copy code
python app.py
2. Open the Application
Visit the application in your browser:

arduino
Copy code
http://127.0.0.1:5000
3. Available Routes
/: Home page
/jobs: View and post jobs
/search: Search for jobs
/users: Create user profiles
/applications: View all job applications and their statuses
Project Structure
csharp
Copy code
job-portal-system/
│
├── Backend/
│   ├── app.py             # Main Flask application
│   ├── models.py          # Database models
│   ├── database.py        # Database initialization
│   ├── requirements.txt   # Python dependencies
│   └── templates/         # HTML templates
│       ├── base.html
│       ├── home.html
│       ├── jobs.html
│       ├── search.html
│       └── users.html
│
├── Frontend/
│   ├── static/
│       ├── css/
│           ├── styles.css  # Custom styles
│
└── README.md               # Project documentation
# Technologies Used
Backend: Flask, Flask-SQLAlchemy
Frontend: HTML, CSS
Database: SQLite
Features in Detail
Job Management

Post new job opportunities with details like title, location, required skills, and salary.
View all available jobs.
User Profiles

Register users with unique IDs, names, and email addresses.
View all registered users.
Job Applications

Allow users to apply for jobs by providing their user ID.
Track the application status (default: "Pending").
Search Functionality

Search jobs by title or skill dynamically.
Contribution
Fork the repository.
Create a feature branch:
bash
Copy code
git checkout -b feature-name
Commit changes:
bash
Copy code
git commit -m "Added new feature"
Push to your branch:
bash
Copy code
git push origin feature-name
Open a pull request.
License
This project is licensed under the MIT License.

