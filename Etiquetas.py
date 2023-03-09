from tkinter import *
from tkinter import ttk

raiz=Tk()
etqTexto = ttk.Label(raiz, text="Etiqueta de solo texto")
etqTexto.grid()

imagen = PhotoImage(file="LadyNagant.png")

etqImagen = ttk.Label(raiz)
etqImagen.grid()
etqImagen['image'] = imagen

etqCombinada=ttk.Label(raiz, text="EtqCombinada",compound="center")
etqCombinada.grid()
etqCombinada['image']=imagen

raiz.mainloop()