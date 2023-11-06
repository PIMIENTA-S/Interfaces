from tkinter import *

root = Tk()

"""
# Cambiar el titulo

root.title("Este es un titulo personalizado")

# cambiar el icono de la ventana

root.iconbitmap("ruta_de_la_imagen.ico")

"""


# Ajedrez

cuadro_0_0 = Frame(bg="white", width="50", height="50")
cuadro_0_0.grid(row=0, column=0)

cuadro_0_1 = Frame(bg="black", width="50", height="50")
cuadro_0_1.grid(row=0, column=1)

cuadro_0_2 = Frame(bg="white", width="50", height="50")
cuadro_0_2.grid(row=0, column=2)

cuadro_0_3 = Frame(bg="black", width="50", height="50")
cuadro_0_3.grid(row=0, column=3)

cuadro_0_4 = Frame(bg="white", width="50", height="50")
cuadro_0_4.grid(row=0, column=4)

cuadro_0_5 = Frame(bg="black", width="50", height="50")
cuadro_0_5.grid(row=0, column=5)

cuadro_0_6 = Frame(bg="white", width="50", height="50")
cuadro_0_6.grid(row=0, column=6)

cuadro_0_7 = Frame(bg="black", width="50", height="50")
cuadro_0_7.grid(row=0, column=7)

# segunda fila

cuadro_1_0 = Frame(bg="black", width="50", height="50")
cuadro_1_0.grid(row=1, column=0)

cuadro_1_1 = Frame(bg="white", width="50", height="50")
cuadro_1_1.grid(row=1, column=1)

cuadro_1_2 = Frame(bg="black", width="50", height="50")
cuadro_1_2.grid(row=1, column=2)

cuadro_1_3 = Frame(bg="white", width="50", height="50")
cuadro_1_3.grid(row=1, column=3)

cuadro_1_4 = Frame(bg="black", width="50", height="50")
cuadro_1_4.grid(row=1, column=4)

cuadro_1_5 = Frame(bg="white", width="50", height="50")
cuadro_1_5.grid(row=1, column=5)

cuadro_1_6 = Frame(bg="black", width="50", height="50")
cuadro_1_6.grid(row=1, column=6)

cuadro_1_7 = Frame(bg="white", width="50", height="50")
cuadro_1_7.grid(row=1, column=7)

# tercera fila

cuadro_2_0 = Frame(bg="white", width="50", height="50")
cuadro_2_0.grid(row=2, column=0)

cuadro_2_1 = Frame(bg="black", width="50", height="50")
cuadro_2_1.grid(row=2, column=1)

cuadro_2_2 = Frame(bg="white", width="50", height="50")
cuadro_2_2.grid(row=2, column=2)

cuadro_2_3 = Frame(bg="black", width="50", height="50")
cuadro_2_3.grid(row=2, column=3)

cuadro_2_4 = Frame(bg="white", width="50", height="50")
cuadro_2_4.grid(row=2, column=4)

cuadro_2_5 = Frame(bg="black", width="50", height="50")
cuadro_2_5.grid(row=2, column=5)

cuadro_2_6 = Frame(bg="white", width="50", height="50")
cuadro_2_6.grid(row=2, column=6)

cuadro_2_7 = Frame(bg="black", width="50", height="50")
cuadro_2_7.grid(row=2, column=7)

# Cuarta fila

cuadro_3_0 = Frame(bg="black", width="50", height="50")
cuadro_3_0.grid(row=3, column=0)

cuadro_3_1 = Frame(bg="white", width="50", height="50")
cuadro_3_1.grid(row=3, column=1)

cuadro_3_2 = Frame(bg="black", width="50", height="50")
cuadro_3_2.grid(row=3, column=2)

cuadro_3_3 = Frame(bg="white", width="50", height="50")
cuadro_3_3.grid(row=3, column=3)

cuadro_3_4 = Frame(bg="black", width="50", height="50")
cuadro_3_4.grid(row=3, column=4)

cuadro_3_5 = Frame(bg="white", width="50", height="50")
cuadro_3_5.grid(row=3, column=5)

cuadro_3_6 = Frame(bg="black", width="50", height="50")
cuadro_3_6.grid(row=3, column=6)

cuadro_3_7 = Frame(bg="white", width="50", height="50")
cuadro_3_7.grid(row=3, column=7)

# quita fila

cuadro_4_0 = Frame(bg="white", width="50", height="50")
cuadro_4_0.grid(row=4, column=0)

cuadro_4_1 = Frame(bg="black", width="50", height="50")
cuadro_4_1.grid(row=4, column=1)

cuadro_4_2 = Frame(bg="white", width="50", height="50")
cuadro_4_2.grid(row=4, column=2)

cuadro_4_3 = Frame(bg="black", width="50", height="50")
cuadro_4_3.grid(row=4, column=3)

cuadro_4_4 = Frame(bg="white", width="50", height="50")
cuadro_4_4.grid(row=4, column=4)

cuadro_4_5 = Frame(bg="black", width="50", height="50")
cuadro_4_5.grid(row=4, column=5)

cuadro_4_6 = Frame(bg="white", width="50", height="50")
cuadro_4_6.grid(row=4, column=6)

cuadro_4_7 = Frame(bg="black", width="50", height="50")
cuadro_4_7.grid(row=4, column=7)

# Sexta fila

cuadro_5_0 = Frame(bg="black", width="50", height="50")
cuadro_5_0.grid(row=5, column=0)

cuadro_5_1 = Frame(bg="white", width="50", height="50")
cuadro_5_1.grid(row=5, column=1)

cuadro_5_2 = Frame(bg="black", width="50", height="50")
cuadro_5_2.grid(row=5, column=2)

cuadro_5_3 = Frame(bg="white", width="50", height="50")
cuadro_5_3.grid(row=5, column=3)

cuadro_5_4 = Frame(bg="black", width="50", height="50")
cuadro_5_4.grid(row=5, column=4)

cuadro_5_5 = Frame(bg="white", width="50", height="50")
cuadro_5_5.grid(row=5, column=5)

cuadro_5_6 = Frame(bg="black", width="50", height="50")
cuadro_5_6.grid(row=5, column=6)

cuadro_5_7 = Frame(bg="white", width="50", height="50")
cuadro_5_7.grid(row=5, column=7)

# septima fila

cuadro_6_0 = Frame(bg="white", width="50", height="50")
cuadro_6_0.grid(row=6, column=0)

cuadro_6_1 = Frame(bg="black", width="50", height="50")
cuadro_6_1.grid(row=6, column=1)

cuadro_6_2 = Frame(bg="white", width="50", height="50")
cuadro_6_2.grid(row=6, column=2)

cuadro_6_3 = Frame(bg="black", width="50", height="50")
cuadro_6_3.grid(row=6, column=3)

cuadro_6_4 = Frame(bg="white", width="50", height="50")
cuadro_6_4.grid(row=6, column=4)

cuadro_6_5 = Frame(bg="black", width="50", height="50")
cuadro_6_5.grid(row=6, column=5)

cuadro_6_6 = Frame(bg="white", width="50", height="50")
cuadro_6_6.grid(row=6, column=6)

cuadro_6_7 = Frame(bg="black", width="50", height="50")
cuadro_6_7.grid(row=6, column=7)

# octava fila

cuadro_7_0 = Frame(bg="black", width="50", height="50")
cuadro_7_0.grid(row=7, column=0)

cuadro_7_1 = Frame(bg="white", width="50", height="50")
cuadro_7_1.grid(row=7, column=1)

cuadro_7_2 = Frame(bg="black", width="50", height="50")
cuadro_7_2.grid(row=7, column=2)

cuadro_7_3 = Frame(bg="white", width="50", height="50")
cuadro_7_3.grid(row=7, column=3)

cuadro_7_4 = Frame(bg="black", width="50", height="50")
cuadro_7_4.grid(row=7, column=4)

cuadro_7_5 = Frame(bg="white", width="50", height="50")
cuadro_7_5.grid(row=7, column=5)

cuadro_7_6 = Frame(bg="black", width="50", height="50")
cuadro_7_6.grid(row=7, column=6)

cuadro_7_7 = Frame(bg="white", width="50", height="50")
cuadro_7_7.grid(row=7, column=7)

root.mainloop()