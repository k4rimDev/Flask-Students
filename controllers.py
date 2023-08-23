from flask import render_template

from app import app
from models import Students


@app.route("/students")
def students():
    students = Students.query.filter_by(status="active")
    return render_template("students.html", students=students)
    

@app.route("/students/<int:id>")
def student_detail(id):
    student = Students.query.get(id)
    return render_template("student_detail.html", student=student)
