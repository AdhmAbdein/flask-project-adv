from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config
from urllib.parse import quote as url_quote

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Define the database model
class UserInput(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<UserInput {self.name}>"

# Initialize database
def init_db():
    with app.app_context():
        db.create_all()

# Routes
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        new_entry = UserInput(name=name, email=email, message=message)
        try:
            db.session.add(new_entry)
            db.session.commit()
            return redirect(url_for("success"))
        except Exception as e:
            db.session.rollback()
            return f"An error occurred: {e}"
    return render_template("form.html")

@app.route("/success")
def success():
    return "Data submitted successfully!"

if __name__ == "__main__":
    init_db()
    app.run(host='0.0.0.0', port=5000)
