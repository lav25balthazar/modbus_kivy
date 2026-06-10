import os
os.environ["KIVY_GL_BACKEND"] = "angle_sdl2"

from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.clock import Clock

from clientemodbus import ClienteMODBUS


class MyWidget(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._cliente = None
        self._event = None

    def conectar(self):

        try:
            ip = self.ids.ip_servidor.text
            porta = int(self.ids.porta_servidor.text)
            if self._cliente:
                self._cliente.close()
            self._cliente = ClienteMODBUS(ip, porta)
            self._cliente.connect()

            self.ids.leitura.text = "Conectado"

        except Exception as e:
            self.ids.leitura.text = str(e)

    def addr(self):
        return int(self.ids.endereco_modbus.text)

    def bit(self):
        txt = self.ids.posicao_bit.text.strip()
        return int(txt) if txt else 0

    def is_float(self):
        return self.ids.chk_float.active

    def is_bit(self):
        return self.ids.chk_bit.active

    def is_coil(self):
        return self.ids.chk_coil.active

    def is_holding(self):
        return self.ids.chk_holding.active

    def executar_leitura(self):

        addr = self.addr()

        if self.is_float():
            valor = self._cliente.lerFloat(addr)
        elif self.is_bit():
            valor = self._cliente.lerBits(addr)
        elif self.is_coil():
            valor = self._cliente.lerCoil(addr)
        elif self.is_holding():
            valor = self._cliente.lerHolding(addr)
        else:
            valor = "Config inválida"

        self.ids.leitura.text = str(valor)

    def loop_leitura(self, dt):
        try:
            self.executar_leitura()
        except Exception as e:
            self.ids.leitura.text = str(e)

    def iniciar_loop(self):
        if self._event is None:
            self.executar_leitura()
            self._event = Clock.schedule_interval(self.loop_leitura, 1)
        

    def parar_loop(self):
        if self._event:
            self._event.cancel()
            self._event = None
            self.ids.leitura.text = str('')

    def ler(self):

        if self.ids.leitura_unica.active:
            self.parar_loop()
            self.executar_leitura()

        elif self.ids.leitura_recorrente.active:
            self.iniciar_loop()
        else:
            self.parar_loop()
            self.ids.leitura.text = str("Aguardando...")

    def escrever(self):

        try:
            addr = self.addr()

            if self.is_float():
                valor = float(self.ids.valor_escrita.text)
                self._cliente.escreveFloat(addr, valor)
                self.ids.leitura.text = "FLOAT escrito"
            elif self.is_bit():
                self._cliente.escreveBit(
                    addr,
                    self.ids.valor_escrita.text,
                    self.bit()
                )
                self.ids.leitura.text = "BIT escrito"
            elif self.is_coil():
                self._cliente.escreverCoil(addr, bool(self.ids.valor_escrita.text))
                self.ids.leitura.text = "COIL escrito"
            elif self.is_holding():
                self._cliente.escreverHolding(addr, int(self.ids.valor_escrita.text))
                self.ids.leitura.text = "Holding escrito"

            else:
                self.ids.leitura.text = "Config inválida"

        except Exception as e:
            self.ids.leitura.text = str(e)

    def close_client(self):

        self.parar_loop()

        if self._cliente:
            self._cliente.close()


class Interface(MDApp):

    def build(self):
        return MyWidget()

    def on_stop(self):
        if self.root:
            self.root.close_client()


if __name__ == "__main__":
    Window.size = (1000, 550)
    Interface().run()