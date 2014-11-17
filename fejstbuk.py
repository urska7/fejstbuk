#### poskrbi da se vse zažene (drugace se sploh spletna stran ne nalozi)

import bottle 
import sqlite3

#@route('/')
#def vsi_smo_fajni():
#    return "VsI STE TKO FAJNI!!!"

#@route('/kvadriraj/<x>')
#def kvadriraj(x):
#    return str(int(x) ** 2)

bottle.debug(True)
datoteka_baze = "knjiga_obrazov.sqlite"

###################################################################

## ne naredi format na select stavku!!!!!!

@bottle.route('/prijatelji/<id>')
@bottle.view('prijatelji')
def prijatelji(id):
    c = baza.cursor()
    c.execute("""SELECT ime, priimek FROM osebe WHERE id = ?""", [id])
    oseba = c.fetchone()
    if oseba is None:
        c.close()
        return {'obstaja': False}
    else:
        (ime, priimek) = oseba
        c.execute(
            """SELECT osebe.ime, osebe.priimek
                FROM osebe JOIN prijateljstva ON osebe.id = prijateljstva.drugi
                WHERE prijateljstva.prvi = ?""", [id])
        prijatelji = c.fetchall()
        c.close()
        return {
            'obstaja': True,
            'ime': ime,
            'priimek': priimek,
            'prijatelji': prijatelji
            }
    

###################################################################

#priklopimo se na bazo
baza = sqlite3.connect(datoteka_baze, isolation_level=None)
bottle.run(host='localhost', port=8080)

##    """SELECT osebe.ime, osebe.priimek FROM
##       osebe JOIN prijateljstva ON
##       osebe.id = prijateljstva.drugi
##       WHERE prijateljstva.prvi = 2
##    """

##seznam_imen = ", ".join(i + " " + p for (i, p) in c.fetchall())
