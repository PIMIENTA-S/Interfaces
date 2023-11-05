from tkinter import *

root = Tk()

# Variables de control

enteros = IntVar()
double = DoubleVar()
string = StringVar()
boolean = BooleanVar()

# RadioButton
# Al igual que los label se especifica el root
# atributo value asigna un valor a la opcion seleccionada
 
def actualizar(value):
    selecionada = Label(root, text=value).grid(row=5)

x = IntVar()

titulo = Label(root, text="Seleccione la respuesta corresta").grid(row=0)

pregunta_1 = Radiobutton(root, text="Primera opcion",value=1, variable=x, command=lambda : actualizar(x.get())).grid(row=1)

pregunta_2 = Radiobutton(root, text="Segunda opcion",value=2, variable=x, command=lambda : actualizar(x.get())).grid(row=2)

pregunta_3 = Radiobutton(root, text="Tercera opcion",value=3, variable=x, command=lambda : actualizar(x.get())).grid(row=3)

pregunta_4 = Radiobutton(root, text="Cuarta opcion",value=4, variable=x, command=lambda : actualizar(x.get())).grid(row=4)




root.mainloop()