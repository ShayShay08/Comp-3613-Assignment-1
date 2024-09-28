from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db


class Applicant(db.Model):
    applicantID = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(80), unique=True, nullable=False)
    lastName = db.Column(db.String(80), unique=True, nullable=False)
    contact = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    username =  db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)

    
class Company(db.Model):
    companyID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    contact = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    username =  db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)

       
class Moderator(db.Model):
    moderatorID = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    
class JobOpening(db.Model):
    jobID = db.Column(db.Integer, primary_key=True)
    companyID = db.Column(db.Integer, unique=True, nullable=False)
    jobDescription = db.Column(db.String(120), nullable=False)
    submissionDeadline = db.Column(db.String(120), nullable=False)
    username =  db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)



    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)


        