try:
    from flask import Flask,request
    from flask_restful import Resource,Api
    from flask_httpauth import HTTPBasicAuth
except Exception as e:
    print("Some modules is missing:{}".format(e))

app = Flask(__name__)
api = Api(app,prefix="/api/v1")
auth = HTTPBasicAuth()

USER_DATA ={
    "admin" : "SuperSecretPwd"
}

@auth.verify_password
def verify(username,password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password

class AuthApi(Resource):
    @auth.login_required
    def get(self):
        return {"Meaning of life is :":42}

api.add_resource(AuthApi,"/private/")

if __name__ == "__main__":
    app.run(debug = True)