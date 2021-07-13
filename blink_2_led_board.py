#Script para Micropython

#Válido para:
# - Raspberry Pi Pico

#Por José Luis Laica Cornejo
#Gye - Ecu
#2021


import machine
import utime

led_board=machine.Pin(25, machine.Pin.OUT)

while True:
  led_board.on()
  print('Encendido')
  utime.sleep(1)
  print('Apagado')
  led_board.off()
  utime.sleep(1)
