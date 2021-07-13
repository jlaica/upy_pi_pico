from machine import Pin
import utime

led_board = led = Pin(25, Pin.OUT)

while True:
  led_board.value(1)
  print('1')
  utime.sleep(1)
  led_board.value(0)
  print('0')
  utime.sleep(1)
