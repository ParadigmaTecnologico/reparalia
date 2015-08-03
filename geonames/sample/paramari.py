import re

comunidades = ('Madrid', 'Cataluña', 'Andalucía')

for casilla in casillas:
    encontrado = None
    for comunidad in comunidades:
        if not encontrado:
            encontrado = re.search(comunidad, casilla, re.IGNORECASE)
    if encontrado is not None:
        geo = True
