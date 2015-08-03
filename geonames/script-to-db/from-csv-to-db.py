import sqlite3 as lite
import csv

if __name__ == "__main__":
    conn = lite.connect("/home/itirados/Development/reparalia/geonames/script-to-db/geonames.db")
    curs = conn.cursor()

    #curs.execute("CREATE TABLE tablaConsolidada (Keyword char(300), Position integer, PreviousPosition integer,SearchVolume integer,CPC integer,Url char(500),Traffic integer,TrafficCost integer, Competition integer, NumberResults integer, Trends char(100), Timestamp integer, Geo char(10), Relevant char(50));")
    files_list = list()
    company_name_list = list() 
    
    files_list = ['/home/itirados/Development/reparalia/script-semrush/ficherosDatosSemrush/lista223filtradosdeapisemrush.csv']

    for files in files_list:
        reader = csv.reader(open(files, 'r'), delimiter=',')
        print reader
        for row in reader:
	    print row
            to_db = [unicode(row[0], "utf8"), unicode(row[1], "utf8"), unicode(row[2], "utf8"), unicode(row[3], "utf8"), unicode(row[4], "utf8"), unicode(row[5], "utf8"), unicode(row[6], "utf8"), unicode(row[7], "utf8"), unicode(row[8], "utf8"), unicode(row[9], "utf8"), unicode(row[10], "utf8"),unicode(row[11], "utf8"),unicode(row[12], "utf8")]#,unicode(row[13], "utf8")]
            #to_db = [unicode(row[0], "utf8")]
            print to_db
            curs.execute("INSERT INTO semrush223Keywords (Keyword,Position, PreviousPosition,PositionDifference, SearchVolume,CPC,Url,Traffic,TrafficCost,Competition,NumberResults, Trends, Name) VALUES (?, ?, ?,?,?,?,?,?,?,?,?,?,?);", to_db)
            #curs.execute("INSERT INTO keywords223 (Keyword) VALUES (?);", to_db)
        conn.commit()


