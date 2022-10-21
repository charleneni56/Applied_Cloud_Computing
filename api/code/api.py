import os
import psycopg2

from flask import Flask, json
app = Flask(__name__)

class JSONConstants:
    nameKey = "name"
    priceKey = "price"
    
## starting point intro
@app.route('/', methods = ['GET'])
def hello_world():
    return 'Hello World!'

@app.route('/meal_recomm')
def recommend_meal():
    conn = psycopg2.connect(database=os.environ.get('POSTGRES_USER'),
                            user=os.environ.get('POSTGRES_USER'),
                            password=os.environ.get('POSTGRES_PASSWORD'),
                            host=os.environ.get('DB_HOST'),
                            port=os.environ.get('DB_PORT'))

    cursor = conn.cursor()
    query = 'SELECT meal_name, meal_price FROM meal_list ORDER BY random() limit 1;'
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    
    selectedMeal = result[0]
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
