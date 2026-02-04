from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app
@app.route("/index")
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/about")
def index2():
    return render_template('about.html')

if __name__ == ("__main__"):
      app.run()