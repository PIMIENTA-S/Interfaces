from tkinter import Button, Tk, Frame, Label, Entry

root = Tk()
"""
# Botones
# Los botones como los label tambien se debe especificar en el root


frame = Frame(width="100", height="100")
frame.grid(row=0, column=0)

# los botones tambien tienen tamaño y si no se especifica se ajustara al texto de este

boton1 = Button(root, text="Hola soy un boton").grid(row=1, column=0)

# Para dar ancho y alto a un boton se usa padx y pady respectivamente
# Estado del boton desactivado, atributo stage
boton2 = Button(root, text="Boton con alto y ancho", padx="100", pady="150", state="disabled").grid(row=2, column=0)


def click():
    texto = Label(root, text="Boton precionado...").grid(row=0, column=1)

#caja = Button(root, text="OK", padx="200", pady="100", command=click).grid(row=0, column=0)


# Entry

input = Entry(root)
input.grid(row=0, column=0)

# obtener el valir del input con get()
# placeholder = input.insert(0, "Este es el placeholder")
# tipo de entrada, show = "*" para contraseñas


def submit():
    if (input.get() == ""):
        texto = Label(root, text="No hay nada que enviar").grid(row=1, column=0)
    else:
        texto = Label(root, text="¡Enviado correctamente!").grid(row=1, column=0)



botonEnviar = Button(root, text="Enviar", bg="red", padx=100, pady="25", command=submit).grid(row=2, column=0)

"""

# Formulario de practica

def validate():
    respuestaT = Label(root, text="Iniciando sesion").grid(row=4, columnspan=2)

bienvenida = Label(root, text="Bienvenido a Llega Company S.A.S", padx=100).grid(row=0, columnspan=2)

usuario = Label(root, text="Usuario", padx=10).grid(row=1, column=0)

usuarioInput = Entry(root)
usuarioInput.grid(row=1, column=1)

contraseña = Label(root, text="Contraseña").grid(row=2, column=0)

contraseñaInput = Entry(root)
contraseñaInput.grid(row=2, column=1)

boton = Button(root, text="Ingresar", command=validate).grid(row=3,columnspan=2)




root.mainloop()