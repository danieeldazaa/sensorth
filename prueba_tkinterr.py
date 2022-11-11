from tkinter import *
from tkinter import messagebox
import serialport 
import threading
import prueba_grafica
import db

def crearbase():
    db.crear()

def leer():
    serialport.varcambio=1
    thread = threading.Thread(target=serialport.leer_datos, args=(1, ))
    thread.start()
    miraiz.after(10000, escanear)

def escanear():
    mivariable=serialport.varcambio
    if (mivariable==1):
        leer()
        
def on_closing():
    if messagebox.askokcancel("Salir","¿Deseas cerrar?"):
         miraiz.destroy()
        

def detener():
    serialport.varcambio=0

def graficar():
        prueba_grafica.hacer_grafica()


miraiz=Tk()
miraiz.resizable(1,1)
miraiz.geometry("340x150")
miraiz.iconbitmap('memory.ico')
miraiz.config(bg="lightblue")

miraiz.title("SENSOR DE TEMPERATURA")

miframe = Frame(miraiz)
miframe.config(bg="lightblue")
miframe.pack()

botonleer= Button(miframe, text="MOSTRAR DATOS",bg="#b0b0ff",bd=8, command=leer)
botonleer.grid(row=0, column=0, sticky="e", padx=10, pady=10)


botondejar= Button(miframe, text="DETENER DATOS",bg="#b0b0ff",bd=8, command=detener)
botondejar.grid(row=0, column=1, sticky="e", padx=10, pady=10)


botongrafico=Button(miframe, text="GRAFICA",bg="#b0b0ff",bd=8, command=graficar)
botongrafico.grid(row=1, column=0, sticky="e", padx=10, pady=10)

botoncrearbase=Button(miframe, text="CREAR BASE",bg="#b0b0ff",bd=8, command=crearbase)
botoncrearbase.grid(row=1, column=1, sticky="e", padx=10, pady=10)


miraiz.protocol("WM_DELETE_WINDOW", on_closing)
miraiz.mainloop()
