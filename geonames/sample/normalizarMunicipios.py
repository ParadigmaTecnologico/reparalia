import unicodedata
def elimina_tildes(s):
   return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))
 
for linea in open('/home/itirados/Development/reparalia/geonames/texto-a-normalizar.txt'):
    u = unicode(linea, "utf-8")
    print elimina_tildes(u[:-1])




