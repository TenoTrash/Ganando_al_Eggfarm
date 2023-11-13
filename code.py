# Importamos librerías necesarias
import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse

# Definimos pulsadores a utilizar y los ubicamos en los GPIO correspondientes
btn1_pin = board.GP15
btn2_pin = board.GP16

# Comenzamos la emulación de teclado y mouse
keyboard = Keyboard(usb_hid.devices)
mouse = Mouse(usb_hid.devices)

# Usando el led ya soldado en la placa, lo prendo cuando haya actividad
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT
led.value = False

# Definimos el formato de los botones (por defecto, van a permanecer en 1 o HIGH ya que estan soldados entre el GPIO y GND)
btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.UP

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.UP

# Los efectos de los botones -> al ponerse en 0 o LOW se activa el proceso dentro del if
while True:
    if not(btn1.value):
        print("Botón 1")
        mouse.move(y=600)
        time.sleep(0.1)
        mouse.move(y=-55)
        time.sleep(0.1)
        mouse.move(x=-1)
        time.sleep(0.1)
        mouse.move(x=1)
        click = 500
        while click > 0:
            led.value = True
            mouse.move(x=1)
            mouse.click(Mouse.LEFT_BUTTON)
            mouse.move(x=-1)
            time.sleep(0.02)
            click = click - 1
        led.value = False
    
    if not(btn2.value):
        print("Botón 2")
        mouse.move(y=600)
        time.sleep(0.1)
        mouse.move(y=-55)
        time.sleep(0.1)
        mouse.move(x=-1)
        time.sleep(0.1)
        mouse.move(x=1)
        click = 1500
        while click > 0:
            led.value = True
            mouse.move(x=1)
            mouse.click(Mouse.LEFT_BUTTON)
            mouse.move(x=-1)
            time.sleep(0.02)
            click = click - 1
        led.value = False
        
    time.sleep(0.1)
