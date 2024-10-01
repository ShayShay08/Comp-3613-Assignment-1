from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
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
    

#     class JobApplication(db.Model):
#         id = db.Column(db.Integer, primary_key=True)
#         job_id = db.Column(db.Integer, db.ForeignKey('job_opening.id'), nullable=False)
#         applicant_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#         resume = db.Column(db.String(255), nullable=False)

#     def __init__(self, job_id, applicant_id, resume):
#         self.job_id = job_id
#         self.applicant_id = applicant_id
#         self.resume = resume

#     def get_json(self):
#         return {
#             'id': self.id,
#             'job_id': self.job_id,
#             'applicant_id': self.applicant_id,
#             'resume': self.resume
#         }


# class JobOpening(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     company_id = db.Column(db.Integer, nullable=False)
#     job_description = db.Column(db.String(255), nullable=False)
#     submission_deadline = db.Column(db.DateTime, nullable=False)

#     def __init__(self, company_id, job_description, submission_deadline):
#         self.company_id = company_id
#         self.job_description = job_description
#         self.submission_deadline = submission_deadline

#     def get_json(self):
#         return {
#             'id': self.id,
#             'company_id': self.company_id,
#             'job_description': self.job_description,
#             'submission_deadline': self.submission_deadline
#         }


#class Applicant(db.Model):
#     applicantID = db.Column(db.Integer, primary_key=True)
#     firstName = db.Column(db.String(80), unique=True, nullable=False)
#     lastName = db.Column(db.String(80), unique=True, nullable=False)
#     contact = db.Column(db.Integer, nullable=False)
#     address = db.Column(db.String(120), nullable=False)
#     email = db.Column(db.String(120), nullable=False)
#     username =  db.Column(db.String(20), nullable=False, unique=True)
#     password = db.Column(db.String(120), nullable=False)

    
# class Company(db.Model):
#     companyID = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), unique=True, nullable=False)
#     contact = db.Column(db.Integer, nullable=False)
#     address = db.Column(db.String(120), nullable=False)
#     email = db.Column(db.String(120), nullable=False)
#     username =  db.Column(db.String(20), nullable=False, unique=True)
#     password = db.Column(db.String(120), nullable=False)

       
# class Moderator(db.Model):
#     moderatorID = db.Column(db.Integer, primary_key=True)
#     username =  db.Column(db.String(20), nullable=False, unique=True)
#     password = db.Column(db.String(120), nullable=False)
    
# class JobOpening(db.Model):
#     jobID = db.Column(db.Integer, primary_key=True)
#     companyID = db.Column(db.Integer, unique=True, nullable=False)
#     jobDescription = db.Column(db.String(120), nullable=False)
#     submissionDeadline = db.Column(db.String(120), nullable=False)
#     username =  db.Column(db.String(20), nullable=False, unique=True)
#     password = db.Column(db.String(120), nullable=False)


         