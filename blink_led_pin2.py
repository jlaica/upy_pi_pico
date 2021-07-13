#Script para Micropython
#Bucle infinito V1
#Valido para:
# - ESP8266
# - ESP32
# - ESP01
# - Raspberry Pi Pico

#Por José Luis Laica Cornejo
#Gye - Ecu
#2021

import machine
import utime

led_board=machine.Pin(2, machine.Pin.OUT)

while True:
  led_board.value(1)
  print('Encendido')
  utime.sleep(1)
  print('Apagado')
  led_board.value(0)
  utime.sleep(1)
