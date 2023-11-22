import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def crear_grafica():
    # Datos de ejemplo
    tiempo = [1, 2, 3, 4, 5]
    ventas = [100, 120, 90, 150, 110]

    # Crear una figura de matplotlib
    fig = Figure(figsize=(5, 4), dpi=100)
    plot = fig.add_subplot(1, 1, 1)
    plot.plot(tiempo, ventas, marker='o', linestyle='-')
    plot.set_xlabel('Tiempo')
    plot.set_ylabel('Ventas')
    plot.set_title('Cantidad Histórica vs Ventas')

    # Crear lienzo de Tkinter para la figura
    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=1, column=0)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cantidad Histórica vs Ventas")

# Crear botón para mostrar la gráfica
boton_grafica = ttk.Button(ventana, text="Mostrar Gráfica", command=crear_grafica)
boton_grafica.grid(row=0, column=0)

# Iniciar el bucle de eventos de la ventana
ventana.mainloop()
