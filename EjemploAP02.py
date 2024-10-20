# EXTRAER TABLAS DE CUALQUIER PÁGINAS WEB CON SOLO EL LINK

import pandas as pd
python = pd.read_html("https://es.wikipedia.org/wiki/Python")

print( len(python) )
print( python[0] )
