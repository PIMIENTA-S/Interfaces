from tkinter import *
from tkinter.messagebox import *

root = Tk()

root.title("Windows")
root.geometry("300x300")

def ingresar(usuario, contraseña):
    if usuario == "admin" and contraseña == "123":
        ventanaNueva = Toplevel()
        ventanaNueva.title("Llegna Company Secrets")
        ventanaNueva.geometry("300x300")
        cerrar = Button(root, text="Cerrar ventana", command=ventanaNueva.destroy).grid(row=2, column=0)
        control = IntVar()
        opcion1 = Checkbutton(ventanaNueva, text="Opcion 1", variable=control, onvalue=10, offvalue=20)
        opcion1.pack()
        opcion1.deselect()
    else:
        showerror(title="Error 404", message="No esta autorizado")
        

def click():
    ingresoUsuario = usuarioI.get()
    ingresoContra = contraseñaI.get()
    ingresar(ingresoUsuario, ingresoContra)

labelframe = LabelFrame(root, text="Llegna company S.A.S", padx=10, pady=10)
labelframe.grid(row=0, column=0, padx=10, pady=10)

usuario = Label(labelframe, text="Usuario").grid(row=0, column=0)
usuarioI = Entry(labelframe)
usuarioI.grid(row=0, column=1)


contraseña = Label(labelframe, text="Contraseña").grid(row=1, column=0)
contraseñaI = Entry(labelframe, show="*")
contraseñaI.grid(row=1, column=1)

boton = Button(labelframe, text="Ingresar", command=click).grid(row=2, columnspan=2, pady=3)



root.mainloop()