import sys
sys.path.insert(0, '.')

from cliente.clientemodbus import ClienteMODBUS
from time import sleep

c = ClienteMODBUS('localhost',502)

# Abre a conexão com o servidor MODBUS
c.connect()

# escrita bit
print("---------- Escrita Bit ----------")
addr = 203
valor = 1
bit_pos = 13
ok = c.escreveBit(int(addr), bool(valor), int(bit_pos))
print(f"Escrita realizada: {valor} no bit {bit_pos-1} do registrador no endereço {addr}. " if ok else "Falha na escrita")
sleep(c._scan_time)

# leitura bits
addr = 203
print(f"Leitura do endereço {addr}: {c.lerBits(int(addr))}")
sleep(c._scan_time)

c._cliente.close()
