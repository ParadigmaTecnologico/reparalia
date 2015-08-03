import csv
import requests
import sqlite3 as lite
# Creamos la peticion HTTP con GET:

conn = lite.connect("/home/itirados/Development/reparalia/script-semrush/semrush.db")
curs = conn.cursor()

#company_name =['habitissimo.es','reparalia.es','planreforma.com','tumanitas.com','reformadisimo.es','cerrajerosmadridd24horas.com','hazmeprecio.com','tenders.es','rbtelectricistasmadrid.es','redformas.es','hogar-soluciones.es','hrzfontanerosmadrid.com','3presupuestos.com','servi-madrid24.com','pintorist.es','electricistasmadrid.eu','electricistabarato.es','fontaneros-24horas.eu','ecoelectricistasmadrid.es','hrzelectricistasmadrid.com','cerrajeros-24horas.eu', 'reformador.es']

#Hacemos un backup de la tabla con la consulta api anterior
query_borrado_backup = "delete from semrushKeywordsBackUp"
curs.execute(query_borrado_backup)

#Copiamos info de backup
curs.execute("insert into semrushKeywordsBackUp select * from semrushKeywords")

#Borramos la tabla para volcar los nuevos datos
query_borrado = "delete from semrushKeywords"
curs.execute(query_borrado)

#La lista company_name la sacamos de la tabla DomainNames de la base de datos
company_name = list() 
query = "select * from DomainNames;"

for row in curs.execute(query):
    company_name.append(row[0])

f = open('archivo.csv', 'w')
for domain_name in company_name:
    print(domain_name)
    if domain_name == 'reparalia.es':
        url = "http://api.semrush.com/?type=domain_organic&key=76a7fe266d1a6b662d71821bca1f2093&display_limit=20000&export_columns=Ph,Po,Pp,Pd,Nq,Cp,Ur,Tr,Tc,Co,Nr,Td&domain="+domain_name+"&display_sort=tr_desc&database=es"
    else:
        url = "http://api.semrush.com/?type=domain_organic&key=76a7fe266d1a6b662d71821bca1f2093&display_limit=8000&export_columns=Ph,Po,Pp,Pd,Nq,Cp,Ur,Tr,Tc,Co,Nr,Td&domain="+domain_name+"&display_sort=tr_desc&database=es"
    print(url)
    r = requests.get(url)

    # Imprimimos el resultado si el codigo de estado HTTP es 200 (OK):
    if r.status_code == 200:
#    print r.text

     #   with open('archivo.csv', 'w') as f:
        f.write(r.text)

"""
    f = r.text.split('\n')
    apireader = csv.DictReader(f, delimiter=';', quoting=csv.QUOTE_NONE)
    for row in apireader:
        print(row)
        #print(row['Keyword'], row['Position'])
"""
    # leer el csv y pasarlo a tabla 
f.close()    

files = "archivo.csv"


reader = csv.reader(open(files, 'r'), delimiter=';')
for row in reader:
    to_db = [row[0],row[1],row[2], row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]]
    print(to_db)
    curs.execute("INSERT INTO semrushKeywords (Keyword,Position, PreviousPosition,PositionDifference, SearchVolume,CPC,Url,Traffic,TrafficCost,Competition,NumberResults, Trends) VALUES (?, ?, ?,?,?,?,?,?,?,?,?,?);", to_db)     
conn.commit() 



