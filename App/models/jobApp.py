from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db


class JobApplication(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        job_id = db.Column(db.Integer, db.ForeignKey('job_opening.id'), nullable=False)
        applicant_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
        resume = db.Column(db.String(255), nullable=False)

        def __init__(self, job_id, applicant_id, resume):
            self.job_id = job_id
            self.applicant_id = applicant_id
            self.resume = resume

        def get_json(self):
            return {
                'id': self.id,
                'job_id': self.job_id,
                'applicant_id': self.applicant_id,
                'resume': self.resume
        }


class JobOpening(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, nullable=False)
    job_description = db.Column(db.String(255), nullable=False)
    submission_deadline = db.Column(db.DateTime, nullable=False)

    def __init__(self, company_id, job_description, submission_deadline):
        self.company_id = company_id
        self.job_description = job_description
        self.submission_deadline = submission_deadline

    def get_json(self):
        return {
            'id': self.id,
            'company_id': self.company_id,
            'job_description': self.job_description,
            'submission_deadline': self.submission_deadline
        }
