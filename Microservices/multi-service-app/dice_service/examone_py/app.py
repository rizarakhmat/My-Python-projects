from flask import Flask, render_template, request, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests
import time
import sys
import random

app = Flask(__name__, instance_relative_config=True)

@app.route('/dice')
def dice():
    k = request.args.get('k', type=int)
    n = request.args.get('n', type=int)
    if k is not None and n is not None:
        if k>0 and n<=6:
            res = []
            for i in range(0,k):
                r = f"{random.randint(1,n)}" # f"{}"-> transform result of func into string; f"result {ran} of {n} dice of {k} faces" 
                res.append(r)
            return make_response(jsonify(s=res), 200)
        else:
            return make_response('Invalid input\n', 400)

def create_app():
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", port=5000)