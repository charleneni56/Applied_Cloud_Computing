import os
import json
import requests

from flask import Flask, render_template
app = Flask(__name__)

## starting point intro
@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name
   
@app.route('/', methods = ['GET'])
def mealRecomm():
   api_port = os.environ.get("API_PORT")
   meal_json_string = requests.get("http://api:" + api_port + "/meal_recomm").content
   meal_data = json.loads(meal_json_string)
   # according to Flask's templating setup, have to put the `index.html` inside `/templates` folder
   return render_template("index.html", meal_recommended=meal_data['name'], meal_price=meal_data['price'])

if __name__ == '__main__':
   print("consumer starting...")
   end_point = os.environ.get("END_POINT")
   port = os.environ.get("CONSUMER_PORT")
   print("end_point: " + end_point)
   print("port: " + port)

   app.run(host=end_point, port=port, debug=True)
   