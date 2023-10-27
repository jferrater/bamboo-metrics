from flask import Flask
from prometheus_client import Counter

app = Flask(__name__)
counter = Counter('my_counter', 'some counters yahoo')


@app.route('/ping')
def ping():
    return 'pong'


if __name__ == '__main__':
    app.run()
