import tkinter as tk

#start the window
window = tk.Tk()
window.title("Scoreboard")
window.geometry("650x500")  # anchoXaltura
window.resizable(False, False)



#function to close the window
def close_program():
    window.destroy()

def obtener_titulos():
    lbl_Inst = tk.Label(window,text='INST')
    lbl_i = tk.Label(window,text='i')
    lbl_j = tk.Label(window,text='j')
    lbl_k = tk.Label(window,text='k')
    lbl_FI = tk.Label(window,text='FI')
    lbl_FO = tk.Label(window,text='FO')
    lbl_EI = tk.Label(window,text='EI')
    lbl_WO = tk.Label(window,text='WO')
    lbl_Inst.grid(row=14, column=0)
    lbl_i.grid(row=14, column=1)
    lbl_j.grid(row=14, column=2)
    lbl_k.grid(row=14, column=3)
    lbl_FI.grid(row=14, column=4)
    lbl_FO.grid(row=14, column=5)
    lbl_EI.grid(row=14, column=6)
    lbl_WO.grid(row=14, column=7)

def obtener_valores_entries():
    obtener_titulos()
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
        

lbl_to_user = tk.Label(window, text = 'Usa en INST: LF - ADDF - MULTF - DIVF - SUBF para tus instrucciones')
lbl_to_user.grid(row=0, column=0, columnspan=5)
lbl_time = tk.Label(window, text = "tiempo")
lbl_time.grid(row=1, column=0)
lbl_inst = tk.Label(window, text = "INST")
lbl_inst.grid(row=1, column=1)
lbl_many = tk.Label(window, text = "¿cuántos?")
lbl_many.grid(row=1, column=2)
lbl_i = tk.Label(window, text = "i")
lbl_i.grid(row=1, column=3)
lbl_j = tk.Label(window, text = "j")
lbl_j.grid(row=1, column=4)
lbl_k = tk.Label(window, text = "k")
lbl_k.grid(row=1, column=5)

arr_timer = []
arr_many = []
arr_inst = []
arr_i = []
arr_j = []
arr_k = []

for i in range(2,8):
    #rows
    
    cj_timer = tk.Entry(window, width=5)
    cj_timer.grid(row=i, column=0)
    arr_timer.append(cj_timer);
    cj_txt_inst = tk.Entry(window, width=5)
    cj_txt_inst.grid(row=i, column=1)
    arr_inst.append(cj_txt_inst);
    cj_many = tk.Entry(window, width=5)
    cj_many.grid(row=i, column=2)
    arr_many.append(cj_many)
    cj_txt_i = tk.Entry(window, width=5)
    cj_txt_i.grid(row=i, column=3)
    arr_i.append(cj_txt_i)
    cj_txt_j = tk.Entry(window, width=5)
    cj_txt_j.grid(row=i, column=4)
    arr_j.append(cj_txt_j)
    cj_txt_k = tk.Entry(window, width=5)
    cj_txt_k.grid(row=i, column=5)
    arr_k.append(cj_txt_k)

# buttons for the nex operation
boton_mostrar = tk.Button(window, text="Next", command=obtener_valores_entries)
boton_mostrar.grid(row=10, column=4)

window.mainloop()
