# -*-coding: utf-8-*-
from flask import Flask
app = Flask(__name__)

#from functions import BB
import functions
#from functions import *

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/bb')
def bba():
    BigBa = functions.BBS()
    return "Am Start werden insgesamt  %s Big Blinds benötigt." % (BigBa)

#print "Am Ende sollen insgesamt %s Big Blinds für alle verbliebenen Spieler übrig bleiben." % (gesbbe)

# # bye(v1, v2):
#     v = get(v1)
#     return render(mei.html, v, n)
#
# hahaha
#
# <p> {{v}} Peter! </p>
