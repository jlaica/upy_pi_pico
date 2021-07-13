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
