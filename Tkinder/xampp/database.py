import sys
from tkinter import *
import mariadb
from tkinter.messagebox import *

root = Tk()
root.title("database")
root.geometry("400x400")


try:
    conexion = mariadb.connect(
        user="root",
        password="",
        host="127.0.0.1",
        port=3306,
        database="prueba"
    )

    # trabajar con la base de datos
    cursor = conexion.cursor()

except mariadb.Error as error:
    print(f"Error al intentar conectar con la base de datos." + {error})
    sys.exit(1)


# funciones

def crear_tabla():
    try:
        cursor.execute("CREATE TABLE clientes (id INT NOT NULL AUTO_INCREMENT, nombre VARCHAR(32) NOT NULL, apellidos VARCHAR(64) NOT NULL, telefono VARCHAR(9) NOT NULL, direccion VARCHAR(256), PRIMARY KEY(id));")
        conexion.commit()
    except mariadb.Error as error_tabla:
        print(f"Error al crear tabla: {error_tabla}")


def registrar_cliente():
    nombre = usuario_v.get()
    apellidos = apellido_v.get()
    telefono = telefono_v.get()
    direccion = direccion_v.get()
    try:
        cursor.execute("INSERT INTO clientes (nombre, apellidos, telefono, direccion) VALUES (?,?,?,?)", (nombre, apellidos, telefono, direccion))
        conexion.commit()
    except mariadb.Error as errror_registro:
        print(f"Error en el registro: {errror_registro}")
    usuario_v.delete(0, END)
    apellido_v.delete(0, END)
    telefono_v.delete(0, END)
    direccion_v.delete(0, END)
    showinfo(title="Confimacion", message="Se ha registrado correctamente")
    

# interfaz

plantilla = LabelFrame(root, text="Llegna Company S.A.S",width=50, padx=20, pady=20)
plantilla.grid(row=0, columnspan=2, padx=10, pady=10)


usuario = Label(plantilla, text="Usuario", width=20).grid(row=1)
usuario_v = Entry(plantilla, width=30)
usuario_v.grid(row=1, column=1)

apellido = Label(plantilla, text="Apellido", width=20).grid(row=2)
apellido_v = Entry(plantilla, width=30)
apellido_v.grid(row=2, column=1)

telefono = Label(plantilla, text="Telefono", width=20).grid(row=3)
telefono_v = Entry(plantilla, width=30)
telefono_v.grid(row=3, column=1)

direccion = Label(plantilla, text="Direccion", width=20).grid(row=4)
direccion_v = Entry(plantilla, width=30)
direccion_v.grid(row=4, column=1)

registrarse = Button(plantilla, text="Enviar", width=25, command=registrar_cliente).grid(row=5, column=1, pady=20)

root.mainloop()