#esempio di utilizzo della libreria pwntools per interagire con la console di un servizio remoto
from pwn import *

endpoint ="tcp.challs.olicyber.it"
port = 12210

conn = remote(endpoint, port)
print(conn.recvline())   # riceve la prima riga di output
