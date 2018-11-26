from flask import Flask
import requests
application = Flask(__name__)

@application.route("/")
def hello():
    return getit()

def getit():
    r = requests.get('https://google.com')
    msg = str(r.status_code)
    return msg
    
if __name__ == "__main__":
    application.run()
