import time
import serial
import tkinter
from tkinter import PhotoImage
from PIL import Image, ImageTk

# Crea la ventana
ventana = tkinter.Tk()
ventana.geometry("450x350")

# Define el puerto serial a usar
arduino = serial.Serial('COM4', 9600)
# Espera dos segundos
time.sleep(2)

# Cargar imágenes y redimensionarlas
imagen_encendido = Image.open("C:\\Users\\EQUIPODAVID\\Desktop\\arduino x python\\encender_y_apagar_led_con_interfaz\\prendido.png")
imagen_apagado = Image.open("C:\\Users\\EQUIPODAVID\\Desktop\\arduino x python\\encender_y_apagar_led_con_interfaz\\apagado.png")

# Redimensionar las imágenes
imagen_encendido = imagen_encendido.resize((100, 100), Image.ANTIALIAS)
imagen_apagado = imagen_apagado.resize((100, 100), Image.ANTIALIAS)

# Convertir las imágenes redimensionadas en objetos PhotoImage
imagen_encendido = ImageTk.PhotoImage(imagen_encendido)
imagen_apagado = ImageTk.PhotoImage(imagen_apagado)

# Método para encender el LED
def encender_led():
    arduino.write(b'1')

# Método para apagar el LED
def apagar_led():
    arduino.write(b'0')

# Crea botones con las imágenes
button1 = tkinter.Button(ventana, text="enciende led", command=encender_led, image=imagen_encendido)
button1.place(x=50, y=150)

button2 = tkinter.Button(ventana, text="apaga led", command=apagar_led, image=imagen_apagado)
button2.place(x=280, y=150)

# Muestra la interfaz
ventana.mainloop()
