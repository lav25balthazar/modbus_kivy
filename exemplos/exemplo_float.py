import sys
sys.path.insert(0, '.')

from cliente.clientemodbus import ClienteMODBUS
from time import sleep

c = ClienteMODBUS('localhost',502)

# Abre a conexão com o servidor MODBUS
c.connect()

# faz escrita float
print("---------- Escrita Float ----------")
addr = 502
valor = 16.9
ok = c.escreveFloat(int(addr), float(valor))
print(f"Escrita realizada: {valor} no endereço {addr}. " if ok else "Falha na escrita")
sleep(c._scan_time)

# faz leitura float
print("---------- Leitura Float ----------")
addr = 502
print(f"Leitura: {c.lerFloat(int(addr))} no endereço {addr}.")
sleep(c._scan_time)

c._cliente.close()
