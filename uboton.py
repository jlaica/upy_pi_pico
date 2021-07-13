#Script para Micropython
#Bucle infinito V1
#Valido para:
# - ESP8266
# - ESP32
# - Raspberry Pi Pico

#Por José Luis Laica Cornejo
#Gye - Ecu
#2021

from machine import Pin #Configuración de pines como entrada
boton = Pin(2, Pin.IN)     

print("Esperando por botón")
while ( boton.value()== 0 ):
    pass

print("Boton fue presionado .. ")
