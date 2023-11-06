from tkinter import *

root = Tk()
root.title("frames")

buscador = LabelFrame(root, text="Buscador", padx=3, pady=3)
buscador.grid(row=0, column=0, padx=100, pady=100)

barra = Entry(buscador, text="si?").pack()
boton = Button(buscador, text="Buscar").pack()

# se pueden crear LabelFrame para insertar dentro otros widgets 

# Muy util para tener "cuadernos" dentro de una misma ventana de root
# Cada uno es independiente y se puede agregar padx y pady independientes

root.mainloop()