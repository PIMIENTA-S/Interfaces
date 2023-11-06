from tkinter import *
from tkinter.messagebox import *

root = Tk()
"""
# ALINEACION EN TKINDER

# Alinear a la izquiera (titulo 1)
titulo1 = Label(root, text="Noroeste").pack(anchor=NW)

titulo2 = Label(root, text="Norte").pack(anchor=N)
titulo3 = Label(root, text="Noreste").pack(anchor=NE)
titulo4 = Label(root, text="Oeste").pack(anchor=W)
titulo5 = Label(root, text="Centro").pack(anchor=CENTER)
titulo6 = Label(root, text="Este").pack(anchor=E)
titulo7 = Label(root, text="Sudoeste").pack(anchor=SW)
titulo8 = Label(root, text="Sud").pack(anchor=S)
titulo9 = Label(root, text="Sudeste").pack(anchor=SE)

#   CUADROS DE DIALOGO

# En messagebox tiene atributos titulo y mensage
# existen varios tipo de messagebox 

# Los informativos (showinfo, showwarning, showerror)
def ventanaEmergente():
    showinfo("Aca va el titulo", "Aqui se escribe el mensaje")
    showwarning("no", "Que pasa valemia")
    showerror("chao", "vete de esta monda")

# Los de Pregunta (askquestion, askyesno, askyesnocancel, askretrycancel)
def ventanaPregunta():
    askquestion(message="¿deberia salir a la calle en vez de programar?")


boton = Button(root, text="presionar para aceptar", command=ventanaPregunta, width=75).pack()
"""

def message():
    respuesta = askquestion(title="Pregunta", message="¿Deberia dejar de programar y salir un rato?")
    if respuesta == "no":
        showinfo(title="Respuesta correcta", message="Haz elegido la mejor opcion")
    else:
        retry = askretrycancel(title="Respuesta incorrecta", message="Haz click en reintentar")
        if retry != "cancel":
            message()

# se tiene en cuenta los askquestion devuelven un valor boolean

boton = Button(root, text="ok", command=message, width=50, height=20).grid(row=0)

root.mainloop()