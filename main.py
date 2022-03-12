from unicodedata import category
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    msg = "Hello World"
    return render_template('index.html', mainmsg = msg)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/calender')
def calender():
    return render_template('event.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route("/registervolunteer",methods=['POST','GET'])
def registervolunteer():
    if request.method == "POST":
        user_name = request.form['name']
        return "hello"+user_name
    else:
        return render_template("registervolunteer.html")

@app.route("/registerorganizer",methods=['POST','GET'])
def registerorganizer():
    if request.method == "POST":
        user_name = request.form['name']
        return "hello"+user_name
    else:
        return render_template("registerorganizer.html")

@app.route('/dashboard')
def dashboard():
    #must add condition to check user type down the line to render correct page
    return render_template('dashboardvolunteer.html')

@app.route("/events")
def displayEvents(text,category):
    return render_template("events.html")

@app.route('/search',methods=['POST','GET'])
def search():
    if request.method == "POST":
        text = request.form['search-text']
        category = request.form['category']
        displayEvents(text,category)
        return render_template("search.html")
    else:
        return render_template("search.html")




if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')