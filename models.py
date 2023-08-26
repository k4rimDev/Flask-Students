from extensions import db
from datetime import datetime

from sqlalchemy.orm import backref


class Students(db.Model):

    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    surname = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(6), nullable=False)
    status = db.Column(db.String(8), nullable=False)
    image = db.Column(db.Text, nullable=False, default="some image path")
    bio = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return self.name

    def save(self):
        db.session.add(self)
        db.session.commit()

class Blog(db.Model):
    
    __tablename__ = "blog"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(15), nullable=False)
    text = db.Column(db.Text, nullable=False)

    students_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    students = db.relationship("Students", backref=backref("students", uselist=False))
