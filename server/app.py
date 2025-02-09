from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()

app = Flask(
    __name__,
    static_url_path='',
    static_folder='../client/build',
    template_folder='../client/build'
)

...

@app.route('/')
@app.route('/<int:id>')
def index(id=0):
    return render_template("index.html")