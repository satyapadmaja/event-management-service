from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    category = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f"Event('{self.title}', '{self.date}', '{self.category}')"