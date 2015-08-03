import sqlite3 as lite
import math
import numpy
import xlrd
import re
from xlrd import open_workbook
from xlutils.copy import copy

'''

 Seleccionamos la minima posicion para las keywords. Recorremos la consulta y guardamos la info en de las position en una lista
 Con esa lista llamamos a la funcion que calcula desviacion y media
    select Keyword,min(Position),SearchVolume from semrushKeywords group by Keyword;

'''
def get_position_list(query):
    list_position = list() 
    sumSearchVolume = 0
    conn = lite.connect("semrush.db")
    curs = conn.cursor()

    for row in curs.execute(query):
        # Solo vamos a guardar los resultados de position de 1 a 10
        if (row[0] <11): 
	        list_position.append(row[0])
                sumSearchVolume += row[1]

    return list_position,sumSearchVolume

def get_position_list_n20(query):
    list_position = list() 
    conn = lite.connect("semrush.db")
    curs = conn.cursor()

    for row in curs.execute(query):
        # Solo vamos a guardar los resultados de position de 11 a 20
        if (row[0] > 10) & (row[0] < 21): 
	        list_position.append(row[0])

    return list_position

def get_position_list_more20(query):
    list_position = list() 
    conn = lite.connect("semrush.db")
    curs = conn.cursor()

    for row in curs.execute(query):
        # Solo vamos a guardar los resultados de position de 20+
        if (row[0] > 20): 
	        list_position.append(row[0])

    return list_position

# #########################################################################
# Funcion que calcula la desviacion estandar de los elementos de una list
# #########################################################################
def _desest(lista):
   lista2 = []
   A = len(lista)
   suma=0
   varis=0
   if A>1:
       for i in lista:
           suma += i
       p = ((suma+0.0)/(A+0.0))
       for j in range((A)):
           sumat = (lista[j]-p)**2
           lista2.append(sumat)
       for k in lista2:
           varis += k
       vari = varis
       va = math.sqrt((vari+0.0)/(A+0.0))
   else:
       print "Datos insuficientes"
   
   return va

def get_num_position(query):
    conn = lite.connect("semrush.db")
    curs = conn.cursor()
    curs.execute(query)
    data = curs.fetchone()
    return data[0]

def get_previousMonthInfo(queryPreviousMonth):
    conn = lite.connect("semrush.db")
    curs = conn.cursor()
    curs.execute(queryPreviousMonth)
    data = curs.fetchone()
    return data[0], data[1]

def get_sum_searchVolume(query):
    conn = lite.connect("semrush.db")
    curs = conn.cursor()
    curs.execute(query)
    data = curs.fetchone()
    return data[0]

def desviacion_standar(lists, media):
    total = 0
    for i in range(0,len(lists)):
        value = lists[i]
        value = value - media
        value = value**2
        total = total + value
    total = total/(float(len(lists)) - 1)
    return math.sqrt(total)

def get_list_domain_name():
    list_domain_name = list();
    conn = lite.connect("semrush.db")
    curs = conn.cursor()
    query = "select * from DomainNames;"
    for row in curs.execute(query):
        list_domain_name.append(row[1])
    return list_domain_name

def escribirCabeceras(ws):
    ws.write(0,0,'Domain Name')    
    ws.write(0,1,'Search volumen n10')
    ws.write(0,2,'Count n10')
    ws.write(0,3,'Count n20')
    ws.write(0,4,'% var n10+n20 previous month')
    ws.write(0,5,'Count n21+')
    ws.write(0,6,'Media position n10')
    ws.write(0,7,'% var n10 previous month')
    ws.write(0,8,'Desviacion n10')


####################

if __name__ == "__main__":
    
    book = xlrd.open_workbook("ficherosDatosSemrush/filtro-semrush-223-position.xlsx")
    sh = book.sheet_by_index(0)

    wb = copy(book)
    ws = wb.get_sheet(1)

    fila = 1
    #vcdda = (8,8,8,8,9,9,6,6,65,5,3,2,)
    #query = "select Keyword,min(Position),SearchVolume from semrushKeywords group by Keyword limit 223;"
    #list_position = get_position_list(query)
    #desv = _desest(list_position)
    #print "Desviacion estandar: "
    #print desv

    #media = numpy.mean(list_position)
    #print "Media: "
    #print media

    # Esta es la que le da a Ruben
    #otraDesv = desviacion_standar(list_position,media)
    #print "otra desviacion: "
    #print otraDesv

    # Muestra de 1 a 10
    #  domain_name = 'habitissimo'
    #list_domain_name = ["habitissimo","reparalia","planreforma","tumanitas","reformadisimo","cerrajerosmadridd24horas","hazmeprecio","tenders","rbtelectricistasmadrid","redformas","hogar-soluciones","hrzfontanerosmadrid","3presupuestos","servi-madrid24","pintorist","electricistasmadrid","electricistabarato","fontaneros-24horas","ecoelectricistasmadrid","hrzelectricistasmadrid","cerrajeros-24horas","reformador"]
    list_domain_name = get_list_domain_name()

# Pasamos de la talba semrush223keywords y hacemos un join
    # Escribimos las cabeceras
    escribirCabeceras(ws)

   
    #Preparamos tablas de previous Month. Hacemos backup de la tabla actual y borramos tabla actual
   
    con = lite.connect("semrush.db")
    cur = con.cursor()
    cur.execute("insert into previousMonthBackUp select * from previousMonth")
    con.commit() 
   
    #Borramos datos anteriores
    cur.execute("delete from previousMonth")

    for domain_name in list_domain_name:
        print "NOMBRE -------------------"
        print domain_name

        # Escribimos el nombre de dominio en el excel
        ws.write(fila,0,domain_name)

        query_one_ten = "select Position, SearchVolume from semrushKeywords join keywords223 where semrushKeywords.Keyword = keywords223.Keyword and Url like \"%"+domain_name+"%\" group by semrushKeywords.Keyword,Url,Traffic order by SearchVolume desc";
        print query_one_ten
        (list_position_one_ten,sumSearchVolume) = get_position_list(query_one_ten)
        n10 = len(list_position_one_ten)
        print "N10: "
        print n10
        #- Escribimos valor n10 en el excel
        ws.write(fila,2,n10)
               
        # Muestra de 10 a 20
        list_position_ten_twenty = get_position_list_n20(query_one_ten)
        n20 = len(list_position_ten_twenty)
        print "N20: "
        print n20
        #- Escribimos valor n20 en el excel
        ws.write(fila,3,n20)
  
        
        # Muestra de 20 a 223
        list_position_more_twenty = get_position_list_more20(query_one_ten)
        n223 = len(list_position_more_twenty)
        print "N20+ :"
        print n223
        #- Escribimos valor n20+ en el excel
        ws.write(fila,5,n223)
        
        # Media muestra de 1 a 10
        media = numpy.mean(list_position_one_ten)
        print "Media n10: "
        print media
               
        #media = round(media, 1);
        print "Redondeo media"
        print media

       
        
        # Desviacion muestra de 1 a 10
        desv = desviacion_standar(list_position_one_ten,media)
        print "Desviacion n10: "
        print desv
        # Redondeamos la desviacion a un decimal round(f,1) 
        desv = round(desv, 1);
        print desv
  
        # Redondeamos la media a un decimal
        media = round(media, 1) 
        #- Escribimos media del valor n10 en el excel
        ws.write(fila,6,media)
        
        
        #- Escribimos desviacion del valor n10
        ws.write(fila,8,desv)
        
        # Suma de todo el Search Volume
        print "Search Volume n10: "
        print sumSearchVolume
        #- Escribimos suma search volume de la muestra n10
        ws.write(fila,1,sumSearchVolume)
        
        #Actualizamos tabla previousMonth con la suma de n10 y n20 y la media
        query_previousMonth = "INSERT INTO previousMonth VALUES  (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\");" % (domain_name,sumSearchVolume,n10,n20,n223,media,desv);
        print query_previousMonth
        con = lite.connect("semrush.db")
        cur = con.cursor()

        

        #Insertamos datos actuales
        cur.execute(query_previousMonth)
        con.commit() 

        #Obtenemos % var n10+n20 previous month y var n10 previous month
        # Para cada domain name consulto en la tabla previousMonthBackUp los datos que tenia el mes anterior
        queryPreviousMonth = "select n10, n20 from previousMonthBackUp where domainName = \'"+domain_name+"\'"
        previousn10,previousn20 = get_previousMonthInfo(queryPreviousMonth)
        print "PREVIOUS MONTH --- "
        print previousn10
        print previousn20
        # y ya esta. Habria que preguntar a 
        # Incrementamos la fila del excel 
        fila += 1

              
    #Guardamos la copia del excel
    wb.save('ficherosDatosSemrush/informe-semrush-223-position.xlsx')
 

