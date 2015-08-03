import sqlite3 as lite
import csv

crear_total_txt(domain_name):
    url="http://api.semrush.com/?type=domain_organic&key=76a7fe266d1a6b662d71821bca1f2093&display_limit=10&export_columns=Ph,Po,Pp,Pd,Nq,Cp,Ur,Tr,Tc,Co,Nr,Td&domain="+domain_name+"&display_sort=tr_desc&database=es"

if __name__ == "__main__":
    conn = lite.connect("semrush.db")
    curs = conn.cursor()
    #curs.execute("CREATE TABLE semrushKeywords (Keyword char(300), Position integer, PreviousPosition integer,PositionDifference integer, SearchVolume integer,CPC integer,Url char(500),Traffic integer,TrafficCost integer, Competition integer, NumberResults integer, Trends char(100));")
    files_list = list()
    company_name_list = list() 
    
    files_list = ['ficherosDatosSemrush/cerrajeros-24horas.txt']#,'ficherosDatosSemrush/habitissimo.txt','ficherosDatosSemrush/reparalia.txt','ficherosDatosSemrush/planreforma.txt','ficherosDatosSemrush/tumanitas.txt','ficherosDatosSemrush/reformadisimo.txt','ficherosDatosSemrush/cerrajerosmadridd24horas.txt','ficherosDatosSemrush/hazmeprecio.txt','ficherosDatosSemrush/tenders.txt','ficherosDatosSemrush/hogar-soluciones.txt','ficherosDatosSemrush/redformas.txt','ficherosDatosSemrush/hrzfontanerosmadrid.txt','ficherosDatosSemrush/rbtelectricistasmadrid.txt','ficherosDatosSemrush/3presupuestos.txt','ficherosDatosSemrush','servi-madrid24.txt','ficherosDatosSemrush/pintorist.txt','ficherosDatosSemrush/electricistasmadrid.txt','ficherosDatosSemrush/electricistabarato.txt',
#'ficherosDatosSemrush/fontaneros-24horas.txt','ficherosDatosSemrush/ecoelectricistasmadrid.txt','ficherosDatosSemrush/hrzelectricistasmadrid.txt']

    company_name = ['cerrajeros-24horas']#,'habitissimo','reparalia','planreforma','tumanitas','reformadisimo','cerrajerosmadridd24horas','hazmeprecio',
#'tenders','hogarsoluciones','redformas','hrzfontanerosmadrid','rbtelectricistasmadrid','3presupuestos','servimadrid24',
#'pintorist','electricistasmadrid','electricistabarato','fontaneros-24horas','ecoelectricistasmadrid','hrzelectricistasmadrid']

    i=0
    for files in files_list:
        reader = csv.reader(open(files, 'r'), delimiter=';')
        company_name = company_name[i]
        print reader
        for row in reader:
	    print row
            to_db = [unicode(row[0], "utf8"), unicode(row[1], "utf8"), unicode(row[2], "utf8"), unicode(row[3], "utf8"), unicode(row[4], "utf8"), unicode(row[5], "utf8"), unicode(row[6], "utf8"), unicode(row[7], "utf8"), unicode(row[8], "utf8"), unicode(row[9], "utf8"), unicode(row[10], "utf8"),unicode(row[11], "utf8"), company_name]
            print to_db
            curs.execute("INSERT INTO semrushKeywords (Keyword,Position, PreviousPosition,PositionDifference, SearchVolume,CPC,Url,Traffic,TrafficCost,Competition,NumberResults, Trends, Name) VALUES (?, ?, ?,?,?,?,?,?,?,?,?,?,?);", to_db)
        conn.commit() 
        i = i+1


