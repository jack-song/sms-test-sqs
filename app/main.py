
from flask import Flask

import boto.sqs
from boto.sqs.message import Message

sqs_conn = boto.sqs.connect_to_region("us-east-1")
sms_q = sqs_conn.create_queue('sms-test', 120)

# the all-important app variable for docker image
app = Flask(__name__)

@app.route("/")
def hello():
	m = Message()
	m.set_body('Oh, Hello World message.')
	sms_q.write(m)
	return "Oh, Hello World"

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True, port=80)
