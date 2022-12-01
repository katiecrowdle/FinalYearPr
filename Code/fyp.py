# use flask to connect back end and front 
from flask import Flask, render_template, request
import tweepy
import configparser
import twitter_api

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/', methods=['GET'])
def homepage():
    searched_term = request.form['user_input']
    return "recived: {}".format(searched_term)

if __name__ == "__main__":
    app.run(debug = True )