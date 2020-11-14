from flask import Flask, jsonify, abort, request

app = Flask(__name__)

persons = [
    {
        'id': 1,
        'name': 'Rasputin'
    },
    {
        'id': 2,
        'name': 'Putin'
    },
    {
        'id': 3,
        'name': 'Lenin'
    } 
]

@app.route('/persons/', methods=['GET'])
def get_persons():
    return jsonify({'persons': persons})

@app.route('/persons/', methods=['POST'])
def create_person():
    if not request.json or not 'name' in request.json:
        abort(400)
    person = {
        'id': persons[-1]['id'] + 1,
        'name': request.json['name']
    }
    persons.append(person)
    return jsonify({'person': person}), 201

@app.route('/persons/<int:person_id>/', methods=['PUT'])
def update_person(person_id):
    person = [person for person in persons if person['id'] == person_id]
    if len(person) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if not 'name' in request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) is not unicode:
        abort(400)
    person[0]['name'] = request.json.get('name', person[0]['name'])
    return jsonify({'person': person[0]})

@app.route('/persons/<int:person_id>/', methods=['DELETE'])
def delete_person(person_id):
    person = [person for person in persons if person['id'] == person_id]
    if len(person) == 0:
        abort(404)
    persons.remove(person[0])
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)