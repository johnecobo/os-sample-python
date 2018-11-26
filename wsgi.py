from flask import Flask
import requests
import keycloak
application = Flask(__name__)

@application.route("/")
def hello():
    keycloak()
    return getit()

def getit():
    r = requests.get('https://google.com')
    msg = str(r.status_code)
    return msg

def keycloak():
    # Configure client
    keycloak_openid = KeycloakOpenID(server_url="http://localhost:8080/auth/",
    client_id="example_client",
    realm_name="example_realm",
    client_secret_key="secret")
    
    return keycloak_openid
    
if __name__ == "__main__":
    application.run()
