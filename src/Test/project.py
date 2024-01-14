from flask import Flask
## https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3#step-4-setting-up-the-database

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'
