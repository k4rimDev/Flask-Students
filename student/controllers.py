from flask import Blueprint, render_template, request, \
    session

student = Blueprint("student", __name__)

from student.models import Students
from extensions import db

from sqlalchemy import or_


@student.route("/")
def students():
    student_count:int = None
    q:str = None
    session["user"] = "Tech"
    session.permanent = True
    user = session["user"]
    students = Students.query.order_by(Students.name.desc())
    if request.args.get("q"):
        q = request.args.get("q")
        q = "%{q}%".format(q=q)
        students = Students.query.filter(or_(Students.name.like(q), 
                                             Students.surname.like(q), 
                                             Students.bio.like(q), 
                                             Students.id > 24)).all()
        

        student_count = len(students)
        q = q[1:len(q) - 1]
    return render_template("students.html", students=students, 
                                            student_count=student_count, 
                                            q=q, user=user)
    
@student.route("/<int:id>")
def student_detail(id):
    student = db.get_or_404(Students, id)
    
    # student.view_count += 1
    # db.session.commit()
    
    return render_template("student_detail.html", student=student)

@student.route("/create", methods=['GET', 'POST'])
def create_student():

    message: str = None
    user = session.get("user", None)

    if request.method == "POST":
        student = Students(
            name = request.form["name"],
            surname = request.form["surname"],
            gender = request.form["gender"],
            status = request.form["status"],
            bio = request.form["bio"],
            email = request.form["email"],
            password = request.form["password"],
        )
        
        student.save()

        message = "User is created with successfully!"

    return render_template("create_student.html", message = message, user=user)

@student.route("/update/<int:id>", methods=['GET', 'POST'])
def update_student(id):
    student = Students.query.filter_by(id=id)
    message: str = None
    if request.method == "POST":

        # new_student = Students(
            # name = request.form["name"],
            # surname = request.form["surname"],
            # gender = request.form["gender"],
            # status = request.form["status"],
            # bio = request.form["bio"],
        # )
        # new_student.save()

        # student = new_student

        # student.name = request.form["name"]
        # student.surname = request.form["surname"]
        # student.gender = request.form["gender"]
        # student.status = request.form["status"]
        # student.bio = request.form["bio"]

        # student.data = {
        #     "name": request.form["name"],
        #     "surname": request.form["surname"],
        #     "gender": request.form["gender"],
        #     "status": request.form["status"],
        #     "bio": request.form["bio"],
        # }

        Students.query.filter_by(id=id).update(dict(name = request.form["name"], 
                                                    surname = request.form["surname"], 
                                                    gender = request.form["gender"], 
                                                    status = request.form["status"], 
                                                    bio = request.form["bio"],))
        db.session.commit()

        message = "User is updated with successfully!"
        return render_template("update_student.html", student=student, message=message)

    return render_template("update_student.html", student=student[0], message=message)

@student.route("/delete/<int:id>", methods=['GET', 'POST'])
def delete_student(id):
    # Method 1
    # db.session.delete(student)
    # db.session.commit()
    message:str = None

    # Method 2
    if request.method == "POST":
        Students.query.filter_by(id=id).delete()
        db.session.commit()
        message = "User with {id} deleted".format(id=id)
    return render_template("delete.html", message=message)
