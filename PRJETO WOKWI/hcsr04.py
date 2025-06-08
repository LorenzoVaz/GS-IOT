from machine import Pin, time_pulse_us
from time import sleep_us

class HCSR04:
    def __init__(self, trigger_pin, echo_pin, echo_timeout_us=100000):
        self.trigger = Pin(trigger_pin, Pin.OUT)
        self.echo = Pin(echo_pin, Pin.IN)
        self.echo_timeout_us = echo_timeout_us
        self.trigger.value(0)

    def distance_cm(self):
        # Envia pulso de trigger de 10us
        self.trigger.value(1)
        sleep_us(10)
        self.trigger.value(0)

        try:
            # Espera o pulso do echo, retorna duração em microssegundos
            pulse_time = time_pulse_us(self.echo, 1, self.echo_timeout_us)
            # Calcula distância em cm (velocidade do som / 2)
            distance = (pulse_time / 2) / 29.1
            return distance
        except OSError as ex:
            # Timeout, sem pulso detectado
            return -1
