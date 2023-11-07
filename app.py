from flask import Flask, jsonify, request
from flask_cors import CORS
from server.gptAccess import ask_ai

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

if __name__ == '__main__':
    app.run()

# prompt input
@app.route('/question', methods=['POST'])
def question():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    query = post_data.get('prompt')
    response_object['query'] = query
    response_object['response'] = ask_ai(query)
    print(response_object)
    return jsonify(response_object)
