from tkinter import *
from tkinter import ttk

class Login:
    def __init__(self, raiz): 
        
        raiz.title("Inicio de sesion")

        self.usuario = StringVar()
        self.contraseña = StringVar()

        
        mainFrame = ttk.Frame(raiz, padding="10 10 25 25") 
        mainFrame.grid(column=0, row=0) 

        usuarioEntry = ttk.Entry(mainFrame, textvariable=self.usuario) 
        usuarioEntry.grid(column=1, row=0, sticky=(W,E), columnspan=2)
        contraseñaEntry = ttk.Entry(mainFrame, textvariable=self.contraseña) 
        contraseñaEntry.grid(column=1, row=1, sticky=(W,E), columnspan=2)

        ttk.Label(mainFrame, text="Usuario:").grid(column=0, row=0) 
        ttk.Label(mainFrame, text="Contraseña: ",padding=(5,10,5,10)).grid(column=0, row=1)
        

        ttk.Button(mainFrame, text="Ingresar", command=self.ingresar()).grid(column=2, row=3)

        usuarioEntry.focus()

        raiz.bind("<Return>",self.ingresar)

    def ingresar(self, *args):
        print("Boton presionado")
        exisUsuario = self.usuario.get() 
        exisContraseña = self.contraseña.get()
        try:
            print("Iniciaste sesion")
        except ValueError:
            print("No es un dato valido")
            self.usuario.set("")


if __name__ == "__main__":
    print("Este es el archivo principal")
    print("Solo se mostrara esto si es el principal")


