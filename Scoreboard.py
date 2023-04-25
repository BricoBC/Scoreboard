import tkinter
import ScFunctions as sc

sc.clk

ventana = tkinter.Tk()
ventana.title("Scoreboard")
ventana.geometry("650x500") #anchoXaltura

clk = tkinter.Label(ventana, text=sc.clk)
clk.grid(row= 0,column=0)



ventana.mainloop()