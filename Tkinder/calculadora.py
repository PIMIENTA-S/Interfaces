from tkinter import *

root = Tk()

root.title("Calculadora")
root.iconbitmap("img/icono.ico")
root.resizable(0,0)
root.geometry("320x260")


# Boton pulsado

def click(valor):
    presionado = pantalla.get()
    pantalla.delete(0, END)
    pantalla.insert(0, str(presionado) + str(valor))



# Pantalla

pantalla = Entry(
    width=23,
    bg="black",
    fg="white",
    borderwidth=0,
    font=("arial", 18, 'bold')
)
pantalla.grid(row=0, columnspan=4, padx=4, pady=4)

# Botones

boton1 = Button(
    root,
    text="1",
    bg="white",
    fg="red",
    width=9,
    height=3,
    cursor="hand2",
    borderwidth=0,
    command= lambda : click(1)
).grid(row=1, column=0, padx=1, pady=0)

boton2 = Button(
    root,
    text="2",
    bg="white",
    fg="red",
    width=9,
    height=3,
    cursor="hand2",
    borderwidth=0,
    command= lambda : click(2)
).grid(row=1, column=1, padx=1, pady=1)

boton3 = Button(
    root,
    text="3",
    bg="white",
    fg="red",
    width=9,
    height=3,
    cursor="hand2",
    borderwidth=0,
    command= lambda : click(3)
).grid(row=1, column=2, padx=1, pady=1)

# Segunda fila

boton4 = Button(
    root,
    text="4",
    bg="white",
    fg="red",
    width=9,
    height=3,
    cursor="hand2",
    borderwidth=0,
    command= lambda : click(4)
).grid(row=2, column=0, padx=1, pady=1)

boton5 = Button(
    root,
    text="5",
    bg="white",
    fg="red",
    width=9,
    height=3,
    cursor="hand2",
    borderwidth=0,
    command= lambda : click(5)
).grid(row=2, column=1, padx=1, pady=1)

boton6 = Button(
    root,
    text="6",
    bg="white",
    fg="red",
    width=9,
    height=3,
    cursor="hand2",
    borderwidth=0,
    command= lambda : click(6)
).grid(row=2, column=2, padx=1, pady=1)

# Tercera fila

boton7 = Button(
    root,
    text="7",
    bg="white",
    fg="red",
    width=9,
    height=3,
    cursor="hand2",
    borderwidth=0,
    command= lambda : click(7)
).grid(row=3, column=0, padx=1, pady=1)

boton8 = Button(
    root,
    text="8",
    bg="white",
    fg="red",
    width=9,
    height=3,
    cursor="hand2",
    borderwidth=0,
    command= lambda : click(8)
).grid(row=3, column=1, padx=1, pady=1)

boton9 = Button(
    root,
    text="9",
    bg="white",
    fg="red",
    width=9,
    height=3,
    cursor="hand2",
    borderwidth=0,
    command= lambda : click(9)
).grid(row=3, column=2, padx=1, pady=1)

# Boton cero

boton0 = Button(
    root,
    text="0",
    bg="white",
    fg="red",
    width=9,
    height=3,
    borderwidth=0,
    cursor="hand2",
    command= lambda : click(0)
).grid(row=4, column=1, padx=1, pady=1)

# Boton igual

botonIgual = Button(
    root,
    text="=",
    bg="red",
    fg="white",
    width=9,
    height=3,
    borderwidth=0,
    cursor="hand2"
).grid(row=4, column=0, padx=1, pady=1)

# Boton punto

botonPunto = Button(
    root,
    text=".",
    bg="spring green",
    fg="black",
    width=9,
    height=3,
    borderwidth=0,
    cursor="hand2"
).grid(row=4, column=2, padx=1, pady=1)

# Boton suma

botonSuma = Button(
    root,
    text="+",
    bg="deep sky blue",
    fg="black",
    width=9,
    height=3,
    borderwidth=0,
    cursor="hand2"
).grid(row=1, column=3, padx=1, pady=1)

# Boton resta

botonResta = Button(
    root,
    text="-",
    bg="deep sky blue",
    fg="black",
    width=9,
    height=3,
    borderwidth=0,
    cursor="hand2"
).grid(row=2, column=3, padx=1, pady=1)

# Boton multiplicacion

botonMultiplicacion = Button(
    root,
    text="*",
    bg="deep sky blue",
    fg="black",
    width=9,
    height=3,
    borderwidth=0,
    cursor="hand2"
).grid(row=3, column=3, padx=1, pady=1)

# Boton de division

botonDivision = Button(
    root,
    text="/",
    bg="deep sky blue",
    fg="black",
    width=9,
    height=3,
    borderwidth=0,
    cursor="hand2"
).grid(row=4, column=3, padx=1, pady=1)


root.mainloop()