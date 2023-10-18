from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension 
from stories import story 

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route("/")
def ask_questions():

    prompts = story.prompts 
    return render_template("questions.html", prompts=prompts)

@app.route("/story")
def show_story():

    text = story.generate(request.args)

    return render_template("story.html", text=text)

    <!doctype html>
<html>
<head>
  <title>Madlibs</title>
</head>
<body>
  <h1>Madlibs</h1>
  <form action="/story">
    {% for prompt in prompts %}
      <p>{{ prompt }}:
        <input name="{{ prompt }}">
      </p>
    {% endfor %}
    <button>Submit</button>
  </form>
</body>
</html>

<!doctype html>
<html>
<head>
  <title>Madlibs</title>
</head>
<body>
  <h1>Your Story</h1>
  <p>{{ text }}</p>
</body>
</html>