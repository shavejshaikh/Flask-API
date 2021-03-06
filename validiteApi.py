try:
    from flask import Flask, request
    from flask_restful import Resource,Api
    
    from flask_restful import reqparse

    from flask_limiter.util import get_remote_address
    from flask_limiter import Limiter

except Exception as e:
    print("Some modules is missing {}".format(e))

app = Flask(__name__)
api = Api(app)

limiter = Limiter(app, key_func=get_remote_address)
limiter.init_app(app)

parser  = reqparse.RequestParser()
parser.add_argument("zip",type=str,required=True,help="Please Provide Zip Code")
parser.add_argument("city",type=str,required=True,help="Please Provide City")

class ValidateAPI(Resource):
    def __init__(self):
        self.__zip_code = parser.parse_args().get("zip",None)
        self.__city = parser.parse_args().get("city",None)
        
    def get(self):
        if (len(self.__city) > 2) and (len(self.__zip_code) > 2):
            return {
                "Response":200,
                "Data":parser.parse_args()
                }
        else:
            return {"Response":400}
    

api.add_resource(ValidateAPI,"/weather/")
if __name__ == "__main__":
    app.run(debug= True)