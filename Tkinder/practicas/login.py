from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("Login")
root.geometry("925x500+400+200")
root.resizable(False, False)
root.configure(bg="#fff")

img = PhotoImage(file='Tkinder/practicas/img/image.png')
Label(root, image=img, bg="white").place(x=150, y=100)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

header = Label(frame, text="Sign in", fg="black",bg="white", font=("Comic Sans MS", 23, "bold"))
header.place(x=100, y=5)


# INICIO DE SESION
def signin():
    nombre = user.get()
    contra = code.get()

    if nombre=="llegna" and contra=="1234":
        alfa = Toplevel(root)
        alfa.title("Llegna Company S.A.S.")
        alfa.geometry("925x500+400+200")
        alfa.resizable(False, False)

        Label(alfa, text="PIMIENTA'S", font=("Transformers Movie",100,"bold")).pack(expand=True)

        alfa.mainloop()
    elif nombre != "llegna" and contra!="1234":
        messagebox.showerror("Invalid", "Invalid Username and password")
    
    elif nombre != "llegna" or contra != "1234":
        messagebox.showerror("Invalid", "Invalid Username or password")



# USUARIO -------------------------------

# Funciones
def on_enter(e):
    user.delete(0, END)

def on_leave(e):
    name = user.get()
    if name=="":
        user.insert(0, "username")

user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Comic Sans MS", 11))

user.place(x=30,y=80)
user.insert(0, "username")

#TO:DO
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

# Linea guia

Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)


# CONTRASEÑA ----------------------------

# Funciones
def on_enter1(a):
    code.delete(0, END)

def on_leave1(a):
    password = code.get()
    if password=="":
        code.insert(0, "password")

code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Comic Sans MS", 11))

code.place(x=30,y=150)
code.insert(0, "password")

code.bind('<FocusIn>', on_enter1)
code.bind('<FocusOut>', on_leave1)

# Linea guia

Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

# INGRESAR

Button(frame, width=30, pady=9, text="Sing in", bg="black", fg="white", border=0, command=signin).place(x=65, y=204)

Label(frame, text="© Copyright by Llegna Company", bg="white").place(x=65, y=250)




root.mainloop()