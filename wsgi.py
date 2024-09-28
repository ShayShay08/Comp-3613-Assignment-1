import click,pytest,sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User, JobOpening, JobApplication  # Ensure JobOpening and JobApplication are imported
from App.main import create_app
from App.controllers import (create_user, get_all_users_json, get_all_users, initialize)

app = create_app()
migrate = get_migrate(app)

# Initialize the database command
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('Database initialized')

# User Commands
user_cli = AppGroup('user', help='User object commands')

@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli)

# Job Commands
job_cli = AppGroup('job', help='Job commands')

@job_cli.command("create", help="Creates a job opening")
@click.argument("company_id")
@click.argument("job_description")
@click.argument("submission_deadline")
def create_job_command(company_id, job_description, submission_deadline):
    job = JobOpening(company_id=company_id, job_description=job_description, submission_deadline=submission_deadline)
    db.session.add(job)
    db.session.commit()
    print(f"Job created for company {company_id}")

@job_cli.command("list", help="List job openings")
@click.argument("format", default="string")
def list_job_command(format):
    jobs = JobOpening.query.all()
    if format == 'string':
        for job in jobs:
            print(f"Job ID: {job.id}, Company ID: {job.company_id}, Description: {job.job_description}, Deadline: {job.submission_deadline}")
    else:
        print([job.get_json() for job in jobs])

@app.cli.command("apply", help="Apply to a job")
@click.argument("job_id")
@click.argument("applicant_id")
@click.argument("resume")
def apply_to_job_command(job_id, applicant_id, resume):
    application = JobApplication(job_id=job_id, applicant_id=applicant_id, resume=resume)
    db.session.add(application)
    db.session.commit()
    print(f"User {applicant_id} applied to job {job_id}")

@job_cli.command("applicants", help="List applicants for a job")
@click.argument("job_id")
@click.argument("format", default="string")
def view_applicants_command(job_id, format):
    applications = JobApplication.query.filter_by(job_id=job_id).all()
    if format == 'string':
        for app in applications:
            user = User.query.get(app.applicant_id)
            print(f"Applicant ID: {user.id}, Username: {user.username}, Resume: {app.resume}")
    else:
        print([{
            'applicant': User.query.get(app.applicant_id).get_json(),
            'resume': app.resume
        } for app in applications])

app.cli.add_command(job_cli)

# Test Commands
test = AppGroup('test', help='Testing commands')

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))

app.cli.add_command(test)
