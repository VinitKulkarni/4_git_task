from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import pymongo

load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')

client = pymongo.MongoClient(MONGO_URI)
db = client.todoListDB
collection = db['todo-collection']

app = Flask(__name__, template_folder='templates')


@app.route('/submittodoitem', methods=['POST'])
def submit():
    form_data = dict(request.json)
    collection.insert_one(form_data)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=9000,debug=True)
