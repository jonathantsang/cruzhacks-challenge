from flask import Flask, make_response, jsonify
from flask import request as fr
from database.UserProfileHandler import UserProfileHandler
from models.UserProfile import UserProfile
import json

app = Flask(__name__)

# create new hacker
@app.route('/hackers', methods=['POST'])
def hacker_insert():
    
    if not (fr.values.get('UserTypeCode') or fr.values.get('Name') or fr.values.get('Street1') or fr.values.get('StateCode'), fr.values.get('ZipCode'), fr.values.get('CountryCode'), fr.values.get('Phone'), fr.values.get('Email'), fr.values.get('BirthDate')):
        response = make_response(jsonify({'result':'Error', 'msg':'One or more required fields is missing'}), 400)
        response.headers['Content-Type'] = 'application/json'
        return response

    handler = UserProfileHandler()
    profile = UserProfile(None, fr.values.get('UserTypeCode'), fr.values.get('Name'), fr.values.get('School'), fr.values.get('Major'), fr.values.get('Street1'), fr.values.get('Street2'), fr.values.get('City'), fr.values.get('StateCode'), fr.values.get('ZipCode'), fr.values.get('CountryCode'), fr.values.get('Phone'), fr.values.get('Email'), fr.values.get('BirthDate'), fr.values.get('ProfileImageUrl'))
    handler.insert(profile)

    response = make_response(jsonify({'result':'Success', 'msg':'OK'}), 201)
    response.headers['Content-Type'] = 'application/json'
    return response

# get hacker info
@app.route('/hackers/<id>', methods=['GET'])
def hacker_get(id):

    handler = UserProfileHandler()
    result = handler.get(id)

    if result is None:
        response = make_response(jsonify({'result':'Error', 'msg':'Hacker does not exist'}), 404)
        response.headers['Content-Type'] = 'application/json'
        return response

    # create UserProfile based off the tuple returned by result
    profile = UserProfile(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9], result[10], result[11], result[12], result[13], result[14])

    response = make_response(jsonify({'result':'Success', 'msg': 'OK', 'val': profile.asdict() }), 200)
    response.headers['Content-Type'] = 'application/json'
    return response

# update info of existing hacker
@app.route('/hackers/<id>', methods=['PUT'])
def hacker_update(id):

    # we don't need to check if the id exists because we assume that this will be
    # handled client-side.

    if not (fr.values.get('UserTypeCode') or fr.values.get('Name') or fr.values.get('Street1') or fr.values.get('StateCode'), fr.values.get('ZipCode'), fr.values.get('CountryCode'), fr.values.get('Phone'), fr.values.get('Email'), fr.values.get('BirthDate')):
        response = make_response(jsonify({'result':'Error', 'msg':'One or more required fields is missing'}), 400)
        response.headers['Content-Type'] = 'application/json'
        return response

    handler = UserProfileHandler()
    profile = UserProfile(id, fr.values.get('UserTypeCode'), fr.values.get('Name'), fr.values.get('School'), fr.values.get('Major'), fr.values.get('Street1'), fr.values.get('Street2'), fr.values.get('City'), fr.values.get('StateCode'), fr.values.get('ZipCode'), fr.values.get('CountryCode'), fr.values.get('Phone'), fr.values.get('Email'), fr.values.get('BirthDate'), fr.values.get('ProfileImageUrl'))
    handler.update(profile)

    response = make_response(jsonify({'result':'Success', 'msg':'OK'}), 200)
    response.headers['Content-Type'] = 'application/json'
    return response    

# delete hacker
@app.route('/hackers/<id>', methods=['DELETE'])
def hacker_delete(id):

    handler = UserProfileHandler()
    handler.delete(id)

    # we don't need to check if the id exists because we assume that this will be
    # handled client-side.

    response = make_response(jsonify({'result':'Success', 'msg':'OK'}), 200)
    response.headers['Content-Type'] = 'application/json'
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)