# INFORMACIÓN DEL DNS SOBRE UNA WEB

import os
import sys

argument = len(sys.argv)

dns = sys.argv[0]
os.system("nslookup " + "8.8.8.8") 
os.system("nslookup " + "1.0.0.1") 