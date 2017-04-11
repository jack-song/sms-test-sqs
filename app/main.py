
from flask import Flask

import boto3

import tasks

# the all-important app variable for docker image
app = Flask(__name__)

@app.route("/")
def hello():
	tasks.run_test("oh no id")
	return "Oh, Hello World"

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True, port=80)
