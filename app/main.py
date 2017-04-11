
from flask import Flask

import boto3

sqs = boto3.resource('sqs', region_name="us-east-1")
sms_q = sqs.get_queue_by_name(QueueName='sms-test')

# the all-important app variable for docker image
app = Flask(__name__)

@app.route("/")
def hello():
	reponse = sms_q.send_message(MessageBody="Hello OH")
	return "Oh, Hello World" + response.get('MessageId')

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True, port=80)
