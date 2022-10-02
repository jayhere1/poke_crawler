from flask import Flask, jsonify, render_template
import json
from db import get_db

app = Flask(__name__)

db = get_db()

mycol = db.get_collection('Pokemon')


@app.route("/all")
def home():
    cursor = mycol.find()
    data = []
    limit = 0
    for doc in cursor:
        limit += 1
        if limit < 20:
            doc['_id'] = str(doc['_id'])
            data.append(doc)
    r = json.dumps(data)
    loaded_r = json.loads(r)
    return render_template('index.html', pokemon_details=loaded_r)


@app.route("/<name>", methods=['GET'])
def get_name(name):
    cursor = mycol.find({"name": name})
    data = []
    for doc in cursor:
        doc['_id'] = str(doc['_id'])
        data.append(doc)
    return jsonify(data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

