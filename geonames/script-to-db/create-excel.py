import sqlite3 as lite
import xlrd

if __name__ == "__main__":
    f=open("consulta-consolidada.txt","w")
    conn = lite.connect("geonames.db")
    cur = conn.cursor()
    filtro  = 'relevant'
    query = "select Keyword,min(Position),SearchVolume,Relevant from tablaConsolidada where Relevant = %s group by Keyword" % (filtro)
    for row in cur.execute(query):  
        print row
        f.write(row[0])
    f.close()
