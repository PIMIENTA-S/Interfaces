import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def crear_grafica():
    # Datos de ejemplo
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    # Crear una figura de matplotlib
    fig = Figure(figsize=(5, 4), dpi=100)
    plot = fig.add_subplot(1, 1, 1)
    plot.plot(x, y, label='Datos de ejemplo')
    plot.set_xlabel('Eje X')
    plot.set_ylabel('Eje Y')
    plot.legend()

    # Crear lienzo de Tkinter para la figura
    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=1, column=0)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de Gráfica con Tkinter")

# Crear botón para mostrar la gráfica
boton_grafica = ttk.Button(ventana, text="Mostrar Gráfica", command=crear_grafica)
boton_grafica.grid(row=0, column=0)

# Iniciar el bucle de eventos de la ventana
ventana.mainloop()
