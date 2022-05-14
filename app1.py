from flask import Flask,request,jsonify
from flask_restful import Resource, Api
app = Flask(__name__) 
api = Api(app)
class App(Resource):     
    def get(self): 
        a = request.args.get('a')
        b = request.args.get('b')        
        try: 
            #import pdb; pdb.set_trace()
            if a is not None and b is not None:            
                with open(r"file1.txt", 'r') as fp:
                    x = fp.readlines()[int(a):int(b)]
                    print(x)
            else:
                with open(r"file1.txt", 'r') as fp:
                    x = fp.readlines()
                    print(x)

        except Exception as e:             
            return(                 
                jsonify(                     
                    {                         
                        "message": "unable to process your request. Please try again",
                            "status_code": 500                    
                    }                 
                )             
            ) 
api.add_resource(App,'/task') 
if __name__ == '__main__':     
    app.run(debug=True)
