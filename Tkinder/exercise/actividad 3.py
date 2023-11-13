from tkinter import *

root = Tk()
root.title("Agregar Nombres")
root.geometry("260x270")

def agregar_nombres():
    contenido = nombre_input.get()
    salida.insert(0, contenido)
    nombre_input.delete(0, "end")



nombre = Label(root, text="Nombre:", padx=10, pady=10).grid(row=0, column=1)
nombre_input = Entry(root, width=20)
nombre_input.grid(row=0, column=2)

agregar = Button(root, text="Agregar", command=agregar_nombres).grid(row=0, column=3, padx=8, pady=8)

salida = Listbox(root)
salida.place(x=70, y=60, width=127, height=150)

root.mainloop()