import tkinter as tk

#start the window
window = tk.Tk()
window.title("Scoreboard")
window.geometry("650x500")  # anchoXaltura

#function to close the window
def close_program():
    window.destroy()

def obtener_valores_entries():
    count = 0
    for inst, i, j, k in zip(arr_inst, arr_i, arr_j, arr_k):
        txt_inst = inst.get()
        txt_i = i.get()
        txt_j = j.get()
        txt_k = k.get()


        lbl = tk.Label(window, text=txt_inst)
        lbl.grid(row=15+count, column=0)
        lbl = tk.Label(window, text=txt_i)
        lbl.grid(row=15+count, column=1)
        lbl = tk.Label(window, text=txt_j)
        lbl.grid(row=15+count, column=2)
        lbl = tk.Label(window, text=txt_k)
        lbl.grid(row=15+count, column=3)

        count = count+1
        print(count)
        

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

arr_inst = []
arr_i = []
arr_j = []
arr_k = []

for i in range(2,8):
    #rows
    cj_txt_inst = tk.Entry(window)
    cj_txt_inst.grid(row=i, column=0)
    arr_inst.append(cj_txt_inst);
    cj_txt_i = tk.Entry(window)
    cj_txt_i.grid(row=i, column=1)
    arr_i.append(cj_txt_i)
    cj_txt_j = tk.Entry(window)
    cj_txt_j.grid(row=i, column=2)
    arr_j.append(cj_txt_j)
    cj_txt_k = tk.Entry(window)
    cj_txt_k.grid(row=i, column=3)
    arr_k.append(cj_txt_k)

# buttons to close and nex operation
boton_mostrar = tk.Button(window, text="Ok", command=obtener_valores_entries)
boton_mostrar.grid(row=10, column=0)

boton_ocultar = tk.Button(window, text="Cerrar programa", command=close_program)
boton_ocultar.grid(row=10,column=3)


window.mainloop()
