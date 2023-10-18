from flask import Flask 

app = Flask(__name__)

@app.route('/')
def home_page():
     html = """
    <HTML>
    <Body>
    <h1>Home Page</h1>
    <p>Welcome to my simple app!</p>
    <a href='/hello'>Go to hello page </a>
    </body>
    </html>
    """

@app.route('/hello')
def say_hello():
    html = """
    <HTML>
    <Body>
    <h1>Hello!</h1>
    <p>This is the hello page</p>
    </body>
    </html>
    """

@app.route('/goodbye')
def say_bye():
    return "Good BYE"    