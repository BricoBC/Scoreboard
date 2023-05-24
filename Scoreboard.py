import tkinter as tk
import modules.views_two as v_2

window = tk.Tk()
window.title("Scoreboard")
window.geometry("650x500")  # anchoXaltura

lblQuestion = tk.Label(
    window, text="¿Cuántos registros va a tener la tabla en total?")
lblQuestion.grid(row=0, column=0)

spingbox_var = tk.DoubleVar
spinbox = tk.Spinbox(window, width=5, from_=1, to=10, textvariable=spingbox_var)
spinbox.grid(row=0, column=1)

# Creamos un botón para mostrar la ventana
boton_mostrar = tk.Button(window, text="Ok", command=lambda: v_2.hide_window_inicial(window, spinbox.get()))
boton_mostrar.grid(row=0, column=2)

v_2.hide_window_table_state_instrucctions()

window.mainloop()
