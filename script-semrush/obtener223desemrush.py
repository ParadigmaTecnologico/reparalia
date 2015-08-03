import sqlite3 as lite

if __name__ == "__main__":
    conn = lite.connect("semrush.db")
    curs = conn.cursor()
    curs2 = conn.cursor()
    #curs.execute("CREATE TABLE semrush223Keywords (Keyword char(300), Position integer, PreviousPosition integer,PositionDifference integer, SearchVolume integer,CPC integer,Url char(500),Traffic integer,TrafficCost integer, Competition integer, NumberResults integer, Trends char(100));")

    #Recorremos toda la tabla de semrush con toda la santa api y, las filas que tengan una de las 223 palabras, las pongo en la tabla
    # semrush223keywords que luego usaremos para sacar el informe
   
    query = "select * from keywords223;"
    for row in curs.execute(query):
         keyword = row[0]
#         print keyword +"hola"
         querydos = "select * from semrushKeywords where keyword = \"%s\"" % (row[0])
         print querydos
         for rrow in curs2.execute(querydos):
#             print keyword
             print rrow
             otraquery = "INSERT INTO semrush223Keywords (Keyword,Position, PreviousPosition,PositionDifference, SearchVolume,CPC,Url,Traffic,TrafficCost,Competition,NumberResults, Trends) VALUES (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\");" % (rrow[0],rrow[1],rrow[2],rrow[3],rrow[4],rrow[5],rrow[6],rrow[7],rrow[8],rrow[9],rrow[10],rrow[11])
#             print otraquery
             curs2.execute(otraquery)
             conn.commit() 
    #el conjunto de las dos se hace con un join
    # select * from semrushKeywords join keywords223 where semrushKeywords.Keyword = keywords223.Keyword and semrushKeywords.Keyword = 'electricistas madrid';

