# ABRIR CUALQUIER PÁGINA WEB

import os
import sys

argument = len(sys.argv)

url = sys.argv[0]

print("url : " , "https://es.wikipedia.org/wiki/Python")
os.system("start chrome  " + "https://es.wikipedia.org/wiki/Python" )
