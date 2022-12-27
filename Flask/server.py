from flask import Flask
import random
import datetime

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

@app.route('guest/<name>')
def guest(name):
    gender_url = f"https://api.genderize.io?none={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data['gender']
        
    age_url = f"https://api.agify.io?none={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data['age']
    
    return render_template("guest.html", person_name=name, gender=gender, age=age)

app.route("/blog/<num>")
def get_blog(num):
    blog_url = f"https://api.npoint.io/5abcca6f4e39b4955965"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)