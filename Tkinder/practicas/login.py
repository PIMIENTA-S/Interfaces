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

# USUARIO -------------------------------

user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Comic Sans MS", 11))

user.place(x=30,y=80)
user.insert(0, "username")

# Linea guia

Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)


# CONTRASEÑA ----------------------------

user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Comic Sans MS", 11))

user.place(x=30,y=150)
user.insert(0, "password")

# Linea guia

Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

# INGRESAR

Button(frame, width=30, pady=9, text="Sing in", bg="black", fg="white", border=0).place(x=65, y=204)

Label(frame, text="© Copyright by Llegna Company", bg="white").place(x=65, y=250)

root.mainloop()