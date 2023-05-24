#Se crea la ventana para la segunda vista
import tkinter as tk
window1 = tk.Tk()

value_spingbox = None

#funcion para ocultar la ventana numero uno.
def hide_window_inicial(window, value):
    global value_spingbox 
    window.withdraw() #método .wothdraw me permite ocultar la ventana
    value_spingbox = int(value)                    
    show_window_table_state_instructions()

# funcion que permite activar la nueva ventana, 
# ocultar la anterior y se activa la vista para la nueva ventana
def show_window_table_state_instructions():
    window1.deiconify() #el método .deiconify me permite mostrar una venatan
    view(value_spingbox)
#funcion para ocultar la ventana numero dos.
def hide_window_table_state_instrucctions():
    window1.withdraw()
#funcion para cerrar el programa
def close_program():
    window1.quit()

#funcion que nos permite poner la misma fila n veces (n = al número que ponga el usuario en la primera ventana)
def fila_cajas(n, r):   
    for i in range(n):
        cj_txt_inst = tk.Entry(window1)
        cj_txt_inst.grid(row=r+i, column=0)

        cj_txt_i = tk.Entry(window1)
        cj_txt_i.grid(row=r+i, column=1)

        cj_txt_j = tk.Entry(window1)
        cj_txt_j.grid(row=r+i, column=2)

        cj_txt_k = tk.Entry(window1)
        cj_txt_k.grid(row=r+i, column=3)      

#función con elementos base y una llamada a la función de fila_cajas
def view(n):
    r = 2
    lbl_to_user = tk.Label(window1, text = 'Usa en INST: LF - ADDF - MULTF - DIVF - SUBF para tus instrucciones')
    lbl_to_user.grid(row=0, column=0, columnspan=3)

    lbl_inst = tk.Label(window1, text = "INST")
    lbl_inst.grid(row=r-1, column=0)

    lbl_i = tk.Label(window1, text = "i")
    lbl_i.grid(row=r-1, column=1)

    lbl_j = tk.Label(window1, text = "j")
    lbl_j.grid(row=r-1, column=2)

    lbl_k = tk.Label(window1, text = "k")
    lbl_k.grid(row=r-1, column=3)
    
    fila_cajas(n,r)

    boton_ocultar = tk.Button(window1, text="Cerrar programa", command=close_program)
    boton_ocultar.grid(row=0,column=4)


    # Iniciar el bucle principal de la aplicación