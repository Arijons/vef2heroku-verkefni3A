from sys import argv

import bottle
from bottle import*
bottle.debug(True)
# -*- coding: utf-8 -*-

from bottle import Bottle, template, route, run

def thversumma(strengjatala):
    talnalisti=[int(d) for d in strengjatala]
    return sum(talnalisti)





@route('/')
def index():
    info = {'title': 'Welcome Home!',
            'content': 'Hello World'
            }

    return template('kennitölur.tpl', info)


@route('/<kennitala>')
def greet(kennitala='Stranger'):
    return "kennitalan er:" + kennitala + ' þversumma kennitölu er: ' + str(thversumma(kennitala))


@error(404)
def custom404(error):
    return "slá inn rétta route"

bottle.run()

