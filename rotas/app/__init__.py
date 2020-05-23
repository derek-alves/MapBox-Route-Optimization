from flask import request, jsonify
from flask_api import FlaskAPI 
from .algoritmos import *

def create_app(config_name):
    app = FlaskAPI(__name__)
    
    @app.route("/", methods = ["POST"])
    def algoritmos():
        alg = request.json.get("alg")
        coords = request.json.get("coords")
        
        busca =  eval(alg + ".busca")()
        result = eval("busca." + alg)(coords[0],coords[1])
        
        return jsonify(result)
    return app