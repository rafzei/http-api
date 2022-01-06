from flask import Flask, jsonify, request
from prometheus_flask_exporter import PrometheusMetrics
from payload import users

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route("/", methods=['GET'])
def hello_world():
	return "<p>Hello, I'm a simple example app serving http endpoint!<br><br> \
		Get all users: <a href='/api/v1/users/all'>Click to get all users</a> <br> \
		Get specific user by id, example: <a href='/api/v1/users?id=1'>Click to get user id=1</a></p>"

@app.route("/api/v1/users/all", methods=['GET'])
def data():
	return jsonify(users)

@app.route("/api/v1/users", methods=['GET'])
def user_id():
	# Get id from request args
	if 'id' in request.args:
		id = int(request.args['id'])
	else:
			return "Please specify an id. Example: <a href='/api/v1/users?id=1'>/api/v1/users?id=1</a> <br> \
							or <br> \
							display all users: <a href='/api/v1/users/all'>/api/v1/users/all</a>"

	# Empty list for results
	results = []

	for user in users:
			if user['id'] == id:
					results.append(user)

	return jsonify(results)

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, threaded=True)
