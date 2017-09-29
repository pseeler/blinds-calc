# -*-coding: utf-8-*-
from flask import Flask
app = Flask(__name__)

from bb import BB

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test')
@app.route('/test2')
def bye():
    a = 1 + 2
    return '%s' % (a)

@app.route('/bb')
def bbb():
    BigB = BB()
    # neu = BigB * 7
    return "Die gesamten benötigten Big Blinds sind: %s" % (BigB)


# # bye(v1, v2):
#     v = get(v1)
#     return render(mei.html, v, n)
#
#
#
# <p> {{v}} Peter! </p>
