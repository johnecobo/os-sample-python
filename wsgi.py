from flask import Flask
import requests
from keycloak import KeycloakOpenID
application = Flask(__name__)

# Configure client
keycloak_openid = KeycloakOpenID(server_url="http://secure-keycloak-pyproject.192.168.64.2.nip.io/auth/",
client_id="jc-client",
realm_name="master",
client_secret_key="secret")
    
@application.route("/")
def hello():
    keycloak1 = keycloak()
    print("well:", keycloak1)
    return getit()

def getit():
    r = requests.get('https://google.com')
    msg = str(r.status_code)
    return msg

def keycloak():
    # Get WellKnow
    config_well_know = keycloak_openid.well_know()
    
    return config_well_know
    
if __name__ == "__main__":
    application.run()
