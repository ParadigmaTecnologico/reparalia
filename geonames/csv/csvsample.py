import xlrd
import re

list_geoname2 = []
li = []
with open('normalizados.txt') as f:
    li = f.readlines()
list_geoname2 = [x[:-1] for x in li]

#Recorrer el excel y ver si el campo contiene una comunidad de la lista
book = xlrd.open_workbook("keywords-habitissimo-00.xlsx")
sh = book.sheet_by_index(0)

i = 1
from xlrd import open_workbook
from xlutils.copy import copy
wb = copy(book)
ws = wb.get_sheet(0)

while (i < sh.nrows):
    keyword = sh.cell_value(rowx=i, colx=0).encode('utf8') 
    
    for comunidad in list_geoname2:
        cadenaAnalizar = sh.cell_value(rowx=i, colx=0).encode('utf8')           
        encontrado = re.search('(^|\s)'+comunidad+'(\s|$)', cadenaAnalizar, re.IGNORECASE)

        if encontrado:
            ws.write(i,12,"geo")
            wb.save('output.xls')
                
    i= i+1        
 
#p = re.compile(regexPart1 + re.escape(term) + regexPart2 , re.IGNORECASE)
