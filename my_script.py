from flask import Flask, jsonify, render_template
import my_secret # Calling another python script

app = Flask(__name__)

my_job = "Data Scientist"
# calling variables from another python script
my_name = my_secret.username
my_password = my_secret.password

@app.route('/')
def welcome():
    word = "Hello World. My name is " + my_name +". I am a " + my_job + ". My password is " + my_password
    return word

@app.route('/listelement') # Must do this for all functions
def my_list():
    my_list = ["Aina","Aliah"]
    return jsonify(my_list) # this is to return a list (not string)

@app.route('/name/<username>') # dynamic url
def hello(username):
    return 'Hello ' + username + ", You have a great day"

@app.route('/htmlformat')
def index():
    return f'<h1>Hello World! My name is {my_name}</h1> \n <p>This is a paragraph</p>'

@app.route('/multiplehtml')
def listing():
    # Multiple html code
    line1 = "<h1><b>Hello</b> World!</h1>"
    line2 = "<p>If music be the food of love, play on!</p>"
    line3 = "<img src='https://media.giphy.com/media/sWrDT2OqxJ3Fu/giphy.gif'>"
    total = line1+line2+line3
    return total

@app.route('/readhtml')
def read_html():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
