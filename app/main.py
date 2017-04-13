"""flask app"""
import time

from flask import Flask

import tasks

# app variable must be `app` for nginx-flask docker image
app = Flask(__name__)  #pylint: disable=I0011,C0103

@app.route("/")
def hello():
    """index"""
    tasks.run_test.delay(time.time())
    return "Oh, Hello World"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
