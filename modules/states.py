import tkinter as tk
states = tk.Tk()

def start(value_rows):
    n_fila, n_columna = 1, 1
    lbl_inst = tk.Label(states, text = "INST")
    lbl_inst.grid(row=n_fila, column=n_columna)

    lbl_i = tk.Label(states, text = "i")
    lbl_i.grid(row=1, column=1)

    lbl_j = tk.Label(states, text = "j")
    lbl_j.grid(row=1, column=2)

    lbl_k = tk.Label(states, text = "k")
    lbl_k.grid(row=1, column=3)
