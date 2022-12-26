from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return  '<h1 style="text-align: center">Hello, World!</h1>' \
            '<p>This is the paragraph.</p>' \
            '<img src="https://media.giphy.com/media/3oEdv2qNBprY4gDxMk/giphy.gif" width="200>'

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)



if __name__ == "__main__":
    app.run(debug=True)