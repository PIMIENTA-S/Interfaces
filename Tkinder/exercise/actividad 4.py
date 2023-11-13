from tkinter import *

root = Tk()
root.geometry("260x270")


menus= Menu()
root.config(menu=menus)


menu_colores = Menu(menus)
menus.add_cascade(menu=menu_colores, label="Colores")

menu_colores.add_command(label="Rojo", command=lambda : root.config(background="red"))
menu_colores.add_command(label="Verde", command=lambda : root.config(background="green"))
menu_colores.add_command(label="Azul", command=lambda : root.config(background="blue"))


menu_tamaños = Menu(menus)
menus.add_cascade(menu=menu_tamaños, label="Tamaños")

menu_tamaños.add_command(label="640x480", command=lambda : root.geometry("640x480"))
menu_tamaños.add_command(label="1024x800", command=lambda : root.geometry("1024x800"))



root.mainloop()