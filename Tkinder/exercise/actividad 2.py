from tkinter import *

root = Tk()
root.title("Ventana inicio")
root.geometry("300x200")


# Definimos la funcion que realizara el boton

def click():
    ventana_principal = Tk()
    ventana_principal.title("Ventana principal")
    ventana_principal.geometry("300x200")

    menu = Menu(ventana_principal)
    ventana_principal.config(menu=menu)

    menu_archivo = Menu(menu)
    menu.add_cascade(menu=menu_archivo, label="Archivo")

    menu_archivo.add_command(label="Salir", command=ventana_principal.destroy)




boton_principal = Button(root, text="Ventana principal",command=click).pack(padx=70, pady=70)


root.mainloop()