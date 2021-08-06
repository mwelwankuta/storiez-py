# module imports
from flask import Flask
import flask_cors 
from pymongo import MongoClient

# enpoint imports
from endpoints import endpoints

# init app
app = Flask(__name__, static_folder="public")
flask_cors.CORS(app)
app.secret_key = "ghz9czWnbB0pub65_K-02licEiOg"

# database
db_url = 'mongodb://localhost:27017'
collection = MongoClient(db_url)
cursor = collection['storiez']

# endpoints
endpoints(app, cursor)
# endpoints

if __name__ == "__main__":
    app.run(debug=True)
