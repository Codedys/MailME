from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
def send_letter():
    letter= None
    if request.method== "POST":
        letter=request.form.get("text")
    return render_template('index.html',letter=letter)

if __name__ == '__main__':
    app.run(debug=True)
