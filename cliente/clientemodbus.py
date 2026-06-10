from pymodbus.client import ModbusTcpClient
from time import sleep

class ClienteMODBUS():
    """
    Classe Cliente MODBUS usando pymodbus
    """
    def __init__(self, server_ip, porta, scan_time=1):
        """
        Construtor
        """
        self._cliente = ModbusTcpClient(host=server_ip, port=porta)
        self._scan_time = scan_time

    def connect(self):
        self._cliente.connect()

    def close(self):
        self._cliente.close()

    def lerFloat(self, addr):
        resp = self._cliente.read_holding_registers(address=addr, count=2, device_id=1)
        float_value = self._cliente.convert_from_registers(
            resp.registers,
            data_type=self._cliente.DATATYPE.FLOAT32
        )
        if not resp.isError():
            return float_value 

    def escreveFloat(self, addr, valor):
        value = self._cliente.convert_to_registers(
            value = valor, 
            data_type = self._cliente.DATATYPE.FLOAT32
        )
        result = self._cliente.write_registers(addr, value, device_id=1)
        return not result.isError()

    def lerBits(self, addr):
        resp = self._cliente.read_holding_registers(address=addr, count=1, device_id=1)
        bits_lista = self._cliente.convert_from_registers(
            resp.registers, 
            data_type = self._cliente.DATATYPE.BITS
        )
        return bits_lista
    def lerHolding(self, addr):
        resp = self._cliente.read_holding_registers(address=addr, count=1, device_id=1)
        if not resp.isError():
            return resp.registers[0]
    
    def escreverHolding(self, addr, valor):
        resp = self._cliente.write_register(address=addr, value=valor, device_id=1)
        if not resp.isError():
            return resp

    def lerCoil(self, addr):
        resp = self._cliente.read_coils(address=addr, count=1, device_id=1)
        return resp.bits[0]

    def escreveBit(self, addr, valor, bit_pos):
        bits_register = self.lerBits(addr)
        bits_register[bit_pos-1] = bool(valor)
        novo_valor = self._cliente.convert_to_registers(
            value = bits_register, 
            data_type = self._cliente.DATATYPE.BITS
        )  
        resp = self._cliente.write_registers(address=addr, values=novo_valor, device_id=1) 
        return not resp.isError()

    def escreverCoil(self, addr, valor):
        resp = self._cliente.write_coil(address=addr, value=valor, device_id=1)
        return not resp.isError()



    
    

        

        