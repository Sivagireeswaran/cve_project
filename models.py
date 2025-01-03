from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cve(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cve_id = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    published_date = db.Column(db.DateTime, nullable=False)
    last_modified = db.Column(db.DateTime, nullable=False)
    cvss_score = db.Column(db.Float, nullable=True)