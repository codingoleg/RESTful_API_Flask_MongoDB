import hashlib
import json

import bson
from bson import ObjectId
from flask import Flask, request

import config
import db.mongo
from utils import invalid_id_error

app = Flask(__name__)
app_client = app.test_client()


@app.route('/create', methods=['POST'])
def create() -> json:
    """
    Creates one document (saves both body и headers). Key order doesn't matter - the hash will be the same.
    Returns:
        JSON with document hash and MongoDB id value.
    """
    # Creates dict, makes hash of it and adds hash to the same dict.
    row = {"headers": dict(request.headers), "body": json.loads(request.data)}
    row["hash"] = hashlib.sha256(json.dumps(row, sort_keys=True).encode()).hexdigest()
    result = db.mongo.collection.insert_one(row)

    return {"hash": row["hash"], "id": str(result.inserted_id)}, 201


@app.route('/read')
def read() -> json:
    """
    Reads one or multiple documents by hash ("h") or one document by id ("id").
    Returns:
        JSON with one/multiple found document(s) or an error.
    """
    if request.args.get('h'):
        found = db.mongo.collection.find(filter={'hash': request.args['h']})
        results = []
        for row in found:
            # Replace ObjectId value with str for json format
            row['_id'] = str(row['_id'])
            results.append(row)
        return results
    elif request.args.get('id'):
        try:
            found = db.mongo.collection.find_one(filter={'_id': ObjectId(request.args['id'])})
            # Replace ObjectId value with str for json format
            found['_id'] = str(found['_id'])
            return {key: value for key, value in found.items()}
        except bson.errors.InvalidId:
            return {"error": invalid_id_error(request.args['id'])}, 400
        except (AttributeError, TypeError):
            return {}
    else:
        return {"error": f'{[key for key in request.args.keys()]} is not a valid argument'}, 400


@app.route('/update', methods=['PUT'])
def update() -> json:
    """
    Updates one or multiple documents by hash ("h") or one document by id ("id").
    Returns:
        JSON with updating info or an error.
    """
    new_data = json.loads(request.data)
    if request.args.get('h'):
        results = db.mongo.collection.update_many(
            filter={'hash': request.args['h']},
            update={'$set': new_data}
        )
    elif request.args.get('id'):
        try:
            results = db.mongo.collection.update_one(
                filter={'_id': ObjectId(request.args['id'])},
                update={'$set': new_data}
            )
        except bson.errors.InvalidId:
            return {"error": invalid_id_error(request.args['id'])}, 400
    else:
        return {"error": f'{[key for key in request.args.keys()]} is not a valid argument'}, 400

    return {
        'acknowledged': results.acknowledged,
        'raw_result': results.raw_result,
        'matched_count': results.matched_count,
        'modified_count': results.modified_count,
        'upserted_id': results.upserted_id
    }


@app.route('/delete', methods=['DELETE'])
def delete() -> json:
    """Deletes one or multiple documents by hash ("h") or one document by id ("id").
    Returns:
        JSON with deletion info or an error.
    """
    if request.args.get('h'):
        results = db.mongo.collection.delete_many(filter={'hash': request.args['h']})
    elif request.args.get('id'):
        try:
            results = db.mongo.collection.delete_one(filter={'_id': ObjectId(request.args['id'])})
        except bson.errors.InvalidId:
            return {"error": invalid_id_error(request.args['id'])}, 400
    else:
        return {"error": f'{[key for key in request.args.keys()]} is not a valid argument'}, 400

    return {
        'acknowledged': results.acknowledged,
        'raw_result': results.raw_result,
        'deleted_count': results.deleted_count
    }


if __name__ == '__main__':
    app.run(host=config.FLASK_HOST, port=config.FLASK_PORT)
