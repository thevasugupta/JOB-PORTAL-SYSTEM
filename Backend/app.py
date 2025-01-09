from flask import Flask, render_template, request, jsonify, redirect, url_for
from models import db, Job, User, JobApplication
from database import init_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/jobs', methods=['GET', 'POST'])
def jobs():
    if request.method == 'POST':
        # Get form data
        title = request.form['title']
        location = request.form['location']
        skills = request.form['skills']
        salary = request.form['salary']
        
        # Add new job to the database
        new_job = Job(title=title, location=location, skills=skills, salary=salary)
        db.session.add(new_job)
        db.session.commit()
    
    # Fetch all jobs to display
    jobs = Job.query.all()
    return render_template('jobs.html', jobs=jobs)


@app.route('/search', methods=['GET'])
def search():
    criteria = request.args.get('criteria')
    
    # Validate input criteria
    if not criteria:
        # If no criteria provided, return all jobs or an empty list
        jobs = Job.query.all()
        return render_template('search.html', jobs=jobs, message="No search criteria provided. Showing all jobs.")
    
    # Run the query with the validated criteria
    filtered_jobs = Job.query.filter(Job.title.contains(criteria)).all()
    return render_template('search.html', jobs=filtered_jobs, message=None)

# @app.route('/users', methods=['GET', 'POST'])
# def users():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         new_user = User(name=name, email=email)
#         db.session.add(new_user)
#         db.session.commit()
#         return redirect(url_for('users'))
#     users = User.query.all()
#     return render_template('users.html', users=users)

@app.route('/apply/<int:job_id>', methods=['POST'])
def apply(job_id):
    user_id = request.form['user_id']
    new_application = JobApplication(user_id=user_id, job_id=job_id, status='Pending')
    db.session.add(new_application)
    db.session.commit()
    return redirect(url_for('jobs'))

@app.route('/applications', methods=['GET'])
def applications():
    applications = JobApplication.query.all()
    return render_template('applications.html', applications=applications)


@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        # Capture user input
        user_id = request.form['id']
        name = request.form['name']
        email = request.form['email']

        # Save the new user to the database
        new_user = User(id=user_id, name=name, email=email)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('users'))  # Refresh the page after submission

    # Fetch all users to display
    users = User.query.all()
    return render_template('users.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)
