from flask import Flask
import requests
application = Flask(__name__)

@application.route("/")
def hello():
    return getit()

def getit():
    msg = "golly"
    return msg
    
if __name__ == "__main__":
    application.run()
