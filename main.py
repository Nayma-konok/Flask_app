from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)


app.config["SECRET_KEY"]="myapplication123"   #this guard the app from hackers
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///data.db"
db=SQLAlchemy(app)

class Form(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(20))  # store date as string for simplicity
    occupation = db.Column(db.String(80))

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method=="POST":
        first_name=request.form["first_name"]
        last_name=request.form["last_name"]
        email=request.form["email"]
        Date=request.form["Date"]
        Occupation=request.form["Occupation"]
    return render_template("index.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5001)