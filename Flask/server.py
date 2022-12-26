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
    return render_template('index.html')

# @app.route("/username/<name>/<int:number>")
# def greet(name, number):
#     return f"Hello there {name}!, you are {number} years old."

if __name__ == "__main__":
    app.run()