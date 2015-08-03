import xlrd
import re

list_geoname2 = []
li = []
with open('gremios.txt') as f:
    li = f.readlines()
list_geoname2 = [x[:-1] for x in li]

#Recorrer el excel y ver si el campo contiene una comunidad de la lista
book = xlrd.open_workbook("in-20150601_keywords-reparalia.xlsx")
sh = book.sheet_by_index(0)

i = 1
from xlrd import open_workbook
from xlutils.copy import copy
wb = copy(book)
ws = wb.get_sheet(0)

gremio_list = ["electricistas","electricista","puerta","puertas","pestillos","pestillo","cerradura","cerraduras","neveras","radiadores","grifo","suelo","tarimas","calderas","vitroceramicas","secadoras","desatascadores","desatascador","desatascar","desatascos","obras","lavavajilla","pergola","toldo","calefacciones","parquets","persiana","aires","electrodomestico","reformados","reformada","reformadas","reforma","reformado","reformar","carpinteras","carpintera","carpintero","carpinteros","carpinterias","cerrajeros","cerrajerias","cerrajero","pinturas","pintar","pintores","pintor","asegurar","aseguradoras","aseguradora","seguro","fontaneria","electricas","lavavajillas","fontaneros","electrica","electrico","electricos","obra","desatasco","nevera","secadora","vitroceramica","caldera","tarima","suelos","grifos","radiador","toldos","pergolas","aire","carpintero"]

gremio_equiv = {'electricistas':'electricidad','electricista':'electricidad','aires':'aire acondicionado','lavavajilla':'electrodomesticos','toldo':'toldos y pergolas','pergola':'toldos y pergolas','pestillos':'cerrajeria','pestillo':'cerrajeria','puertas':'cerrajeria','puerta':'cerrajeria','cerraduras':'cerrajeria','cerradura':'cerrajeria','radiadores':'fontanero','grifo':'fontanero','suelo':'parquet','tarimas':'parquet','calderas':'electrodomesticos','vitroceramicas':'electrodomesticos','secadoras':'electrodomesticos','neveras':'electrodomesticos','desatascadores':'fontanero','desatascador':'fontanero','desatascar':'fontanero','desatascos':'fontanero','obras':'reformas','calefacciones':'calefaccion','parquets':'parquet','persiana':'persianas','electrodomestrico':'electrodomesticos','reformada':'reformas','reformadas':'reformas','reformados':'reformas','reformado':'reformas','reformar':'reformas','reforma':'reformas','carpinteras':'carpinteria','carpintera':'carpinteria','carpinteros':'carpinteria','carpintero':'carpinteria','carpinterias':'carpinteria','cerrajeros':'cerrajeria','cerrajero':'cerrajeria','cerrajerias':'cerrajeria','pinturas':'pintura','pintar':'pintura','pintores':'pintura','pintor':'pintura','asegurar':'seguros','aseguradoras':'seguros','aseguradora':'seguros','seguro':'seguros','electricas':'electricidad','fontaneria':'fontanero','fontaneros':'fontanero','electrica':'electricidad','electrico':'electricidad','electricos':'electricidad','lavavajillas':'electrodomesticos','obra':'reformas','desatasco':'fontanero','nevera':'electrodomesticos','secadora':'electrodomesticos','vitroceramica':'electrodomesticos','caldera':'electrodomesticos','tarima':'parquet','suelos':'albalineria','grifos':'fontanero','radiador':'fontanero','toldos':'toldos y pergolas','pergolas':'toldos y pergolas','aire':'aire acondicionado','carpintero':'carpinteria'}

while (i < sh.nrows):
    keyword = sh.cell_value(rowx=i, colx=0).encode('utf8') 
    
    for comunidad in list_geoname2:
        cadenaAnalizar = sh.cell_value(rowx=i, colx=0).encode('utf8')           
        encontrado = re.search('(^|\s)'+comunidad+'(\s|$)', cadenaAnalizar, re.IGNORECASE)

        if encontrado:
            if comunidad in gremio_list:
                print comunidad
                print "equiv"
                gremio = gremio_equiv[comunidad]
                print gremio
                print "fin"
            else:
                gremio = comunidad
            ws.write(i,13,gremio)
            wb.save('output-20150601_keywords-reparalia.es-domain_organic-es.xls')
                
    i= i+1        
 
#p = re.compile(regexPart1 + re.escape(term) + regexPart2 , re.IGNORECASE)
