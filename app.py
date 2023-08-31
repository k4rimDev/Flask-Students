from flask import Flask


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:example@127.0.0.1:3307/School"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = "9fbc546684f5d7800067528c0b579c06"

from controllers import *
from extensions import *
from models import *


if __name__ == "__main__":
    app.run(port = 8000, debug=True)
