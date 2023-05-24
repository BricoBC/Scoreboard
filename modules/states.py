import tkinter as tk
from . import views_two as v_2

states = tk.Tk()
states.title("Estados")
states.geometry("600x500")

def hidden():
    states.withdraw()

def start():

    states.deiconify()
    v_2.hide_window()

    n_fila = 1

    lbl_inst = tk.Label(states, text = "INST")
    lbl_inst.grid(row=1, column=0)

    lbl_i = tk.Label(states, text = "i")
    lbl_i.grid(row=1, column=1)

    lbl_j = tk.Label(states, text = "j")
    lbl_j.grid(row=1, column=2)

    lbl_k = tk.Label(states, text = "k")
    lbl_k.grid(row=1, column=3)

    lbl_i = tk.Label(states, text = "FI")
    lbl_i.grid(row=1, column=4)

    lbl_j = tk.Label(states, text = "FO")
    lbl_j.grid(row=1, column=5)

    lbl_k = tk.Label(states, text = "EI")
    lbl_k.grid(row=1, column=6)

    lbl_k = tk.Label(states, text = "WO")
    lbl_k.grid(row=1, column=7)

    
