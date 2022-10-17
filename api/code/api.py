import os
import random

from flask import Flask, json
app = Flask(__name__)

class JSONConstants:
    nameKey = "name"
    priceKey = "price"
    
## starting point intro
@app.route('/', methods = ['GET'])
def hello_world():
    return 'Hello World!'

## random recommend 15 meals from Khao Khan Thai Kitchen
@app.route('/meal_recomm', methods = ['GET'])
def meal_recomm(): 
    meals = [
        ("Thai Fish Cake", "$13.00"),
        ("Thai Samosa", "$13.00"),
        ("Chicken Satay", "$13.95"),
        ("Tom Yum Soup", "$17.00"),
        ("Pineapple Fried Rice", "$17.00"),
        ("Green Curry", "$17.00"),
        ("Pad Thai", "$16.00"),
        ("Khao Moo Krob Cripsy Pork", "$17.00"),
        ("Hor Mok Pla Curry Fish", "$20.00"),
        ("Papaya Salad Thai Style", "$15.00"),
        ("Mango Sticky Rice", "$12.00"),
        ("Thai Ice Tea", "$5.50"),
        ("Strawberry Lemonade", "$3.50"),
        ("Thai Ice Coffee", "$5.50"),
        ("Sparkling Water", "$4.50"),
    ]

    selectedMealIndex = int(random.uniform(0, len(meals)))
    selectedMeal = meals[selectedMealIndex] 

    data = {
        JSONConstants.nameKey: selectedMeal[0],
        JSONConstants.priceKey: selectedMeal[1]
    }
    return app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )

if __name__ == '__main__':
    print("api starting...")
    
    end_point = os.environ.get("END_POINT")
    port = os.environ.get("API_PORT")
    print("end_point: " + end_point)
    print("port: " + port)
    
    ## setting up host and port 
    app.run(host=end_point, port=port, debug=True)
    

# run python api.py runserver 