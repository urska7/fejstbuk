#### poskrbi da se vse zažene (drugace se sploh spletna stran ne nalozi)

import bottle 


#@route('/')
#def vsi_smo_fajni():
#    return "VsI STE TKO FAJNI!!!"

#@route('/kvadriraj/<x>')
#def kvadriraj(x):
#    return str(int(x) ** 2)



@bottle.route('/hello/<name>')
def index(name):
    return bottle.template('<b>Hello {{name}}</b>!', name=name)




bottle.run(host='localhost', port=8080)
