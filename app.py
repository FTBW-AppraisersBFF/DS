# <--- Deps --->
from flask import Flask, render_template, request
from joblib import load
from random import randint
# <--- Deps --->
# (Main)
app = Flask(__name__)
if __name__ == '__main__':
    app.run()
# Pull and predict from a JSON file
@app.route("/input_data", methods=['POST'])
def input_data():
        # Requests:params = dict(
        bathrooms = request.json['bathrooms']
        bedrooms = request.json['bedrooms']
        squarefeet = request.json['squarefeet']
        yearbuilt = request.json['yearbuilt']
        inputs = [bathrooms, bedrooms, squarefeet, yearbuilt]
        # Load the Mc-pickled algorithm:
        pipeline = load('algorithm.sav')
        # Predict:
        estimate = pipeline.predict([inputs])[0]
        # Return Jsonified result as price: "" in the
        #    JSON file.
        return(flask.jsonify(price=estimate))
