import tkinter as tk


window = tk.Tk()
window.title("Scoreboard")
window.geometry("650x500")  # anchoXaltura

def close_program():
    window.destroy()

lbl_to_user = tk.Label(window, text = 'Usa en INST: LF - ADDF - MULTF - DIVF - SUBF para tus instrucciones')
lbl_to_user.grid(row=0, column=0, columnspan=3)

lbl_inst = tk.Label(window, text = "INST")
lbl_inst.grid(row=1, column=0)

lbl_i = tk.Label(window, text = "i")
lbl_i.grid(row=1, column=1)

lbl_j = tk.Label(window, text = "j")
lbl_j.grid(row=1, column=2)

lbl_k = tk.Label(window, text = "k")
lbl_k.grid(row=1, column=3)

cj_txt_inst = tk.Entry(window)
cj_txt_inst.grid(row=2, column=0)
cj_txt_i = tk.Entry(window)
cj_txt_i.grid(row=2, column=1)
cj_txt_j = tk.Entry(window)
cj_txt_j.grid(row=2, column=2)
cj_txt_k = tk.Entry(window)
cj_txt_k.grid(row=2, column=3)

cj_txt_inst = tk.Entry(window)
cj_txt_inst.grid(row=3, column=0)
cj_txt_i = tk.Entry(window)
cj_txt_i.grid(row=3, column=1)
cj_txt_j = tk.Entry(window)
cj_txt_j.grid(row=3, column=2)
cj_txt_k = tk.Entry(window)
cj_txt_k.grid(row=3, column=3)

cj_txt_inst = tk.Entry(window)
cj_txt_inst.grid(row=4, column=0)
cj_txt_i = tk.Entry(window)
cj_txt_i.grid(row=4, column=1)
cj_txt_j = tk.Entry(window)
cj_txt_j.grid(row=4, column=2)
cj_txt_k = tk.Entry(window)
cj_txt_k.grid(row=4, column=3)

cj_txt_inst = tk.Entry(window)
cj_txt_inst.grid(row=5, column=0)
cj_txt_i = tk.Entry(window)
cj_txt_i.grid(row=5, column=1)
cj_txt_j = tk.Entry(window)
cj_txt_j.grid(row=5, column=2)
cj_txt_k = tk.Entry(window)
cj_txt_k.grid(row=5, column=3)

cj_txt_inst = tk.Entry(window)
cj_txt_inst.grid(row=6, column=0)
cj_txt_i = tk.Entry(window)
cj_txt_i.grid(row=6, column=1)
cj_txt_j = tk.Entry(window)
cj_txt_j.grid(row=6, column=2)
cj_txt_k = tk.Entry(window)
cj_txt_k.grid(row=6, column=3)

cj_txt_inst = tk.Entry(window)
cj_txt_inst.grid(row=7, column=0)
cj_txt_i = tk.Entry(window)
cj_txt_i.grid(row=7, column=1)
cj_txt_j = tk.Entry(window)
cj_txt_j.grid(row=7, column=2)
cj_txt_k = tk.Entry(window)
cj_txt_k.grid(row=7, column=3)

# Creamos un botón para mostrar la ventana
boton_mostrar = tk.Button(window, text="Ok")
boton_mostrar.grid(row=10, column=0)

boton_ocultar = tk.Button(window, text="Cerrar programa", command=close_program)
boton_ocultar.grid(row=10,column=3)


window.mainloop()
