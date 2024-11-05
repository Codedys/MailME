from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///letters.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Letter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/', methods=["POST","GET"])
def send_letter():
    letters = Letter.query.all()
    letter= None
    if request.method== "POST":
        letter_content = request.form.get("text")
        new_letter = Letter(content=letter_content)
        db.session.add(new_letter)
        db.session.commit()

        letter = letter_content

    return render_template('index.html',letter=letter, letters=letters)

if __name__ == '__main__':
    app.run(debug=True)
