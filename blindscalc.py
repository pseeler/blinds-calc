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
def bb():
    startst = functions.starts()
    BigBa = functions.BBS()
    BigBe = functions.BBE()
    zeite = functions.zeitf()
    levelanz = functions.level()
    bbmulti = functions.bbmult()
    bigbaa = functions.BBSA()
    sbaa = functions.SBSA()
    return "Jeder Spieler bekommt am Anfang %s Chips, die Blinds sind zunächst %s/%s. Nach %s Minuten sollen %s Big Blinds insgesamt übrig bleiben, also nach %s Leveln. BB-Multiplikator: %s. Die Blindstruktur lautet dann folgendermaßen:" % (startst, bigbaa, sbaa, zeite, BigBe, levelanz, bbmulti)

#     v = get(v1)
#     return render(mei.html, v, n)
#
# hahaha
#
# <p> {{v}} Peter! </p>
