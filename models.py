from extensions import db


class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    surname = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(6), nullable=False)
    status = db.Column(db.String(8), nullable=False)
    image = db.Column(db.Text, nullable=False, server_default="some image path")
    bio = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return self.name

    def save(self):
        db.session.add(self)
        db.session.commit()
