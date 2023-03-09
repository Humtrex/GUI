from tkinter import *
from tkinter import ttk

class Widgets:
    def __init__(self, raiz): 
        
        raiz.title("Muestra Widgets")

        self.nombre = StringVar()
        self.Apaterno = StringVar()
        self.Amaterno = StringVar()
        self.correo = StringVar()
        self.movil = StringVar()

        mainFrame=ttk.Frame(raiz, padding="5 5 20 10")
        mainFrame.grid(column=0, row=0)
                
        datosFrame = ttk.Frame(mainFrame, padding="5 3 30 10",relief="sunken") 
        datosFrame.grid(column=0, row=0,columnspan=2,rowspan=3)   

        nombreEntry = ttk.Entry(datosFrame, textvariable=self.nombre) 
        nombreEntry.grid(column=1, row=0, sticky=(W,E), columnspan=2)
        ApaternoEntry = ttk.Entry(datosFrame, textvariable=self.Apaterno) 
        ApaternoEntry.grid(column=1, row=1, sticky=(W,E), columnspan=2)
        AmaternoEntry = ttk.Entry(datosFrame, textvariable=self.Amaterno) 
        AmaternoEntry.grid(column=1, row=2, sticky=(W,E), columnspan=2)
        correoEntry = ttk.Entry(datosFrame, textvariable=self.correo) 
        correoEntry.grid(column=1, row=3, sticky=(W,E), columnspan=2)
        movilEntry = ttk.Entry(datosFrame, textvariable=self.movil) 
        movilEntry.grid(column=1, row=4, sticky=(W,E), columnspan=2)        

        ttk.Label(datosFrame, text="Nombre:",padding=(5,10,5,10)).grid(column=0, row=0) 
        ttk.Label(datosFrame, text="A.Paterno: ",padding=(5,10,5,10)).grid(column=0, row=1)
        ttk.Label(datosFrame, text="A.Materno:",padding=(5,10,5,10)).grid(column=0, row=2) 
        ttk.Label(datosFrame, text="Correo: ",padding=(5,10,5,10)).grid(column=0, row=3)
        ttk.Label(datosFrame, text="Movil:",padding=(5,10,5,10)).grid(column=0, row=4) 

        aficionesFrame = ttk.Frame(mainFrame,padding="5 3 15 15",relief="sunken")  
        aficionesFrame.grid(column=0, row=4, columnspan=2)
        ttk.Label(aficionesFrame, text="Aficiones:",padding=(5,5,5,5)).grid(column=0, row=0)
        chkLeer = ttk.Checkbutton(aficionesFrame, text="Leer") 
        chkLeer.grid(column=0, row=2)   
        chkMusica = ttk.Checkbutton(aficionesFrame, text="Musica") 
        chkMusica.grid(column=1, row=2) 
        chkVideojuegos = ttk.Checkbutton(aficionesFrame, text="Videojuegos") 
        chkVideojuegos.grid(column=3, row=2) 

        ocupacionFrame = ttk.Frame(mainFrame,padding="10 10 10 25")
        ocupacionFrame.grid(column=2,row=0, rowspan=3)
        ocupacion = StringVar()
        estudiante=ttk.Radiobutton(ocupacionFrame, text='Esudiante', variable=ocupacion, value ='Estudiante')
        estudiante.grid(column=0,sticky=W)
        empleado=ttk.Radiobutton(ocupacionFrame, text='Empleado', variable=ocupacion, value ='Empleado')
        empleado.grid(column=0,sticky=W)
        desempleado=ttk.Radiobutton(ocupacionFrame, text='Desempleado', variable=ocupacion, value ='Desempleado')
        desempleado.grid(column=0,sticky=W)

        estadoFrame = ttk.Frame(mainFrame,padding="10 10 10 25")
        estadoFrame.grid(column=2,row=4)
        estado = StringVar()
        comboEstados = ttk.Combobox(estadoFrame, textvariable=estado)
        comboEstados.grid()
        comboEstados['values']=("Jalisco","Nayarit","Colima","Michoacan","Estados(32)")

        '''botones=ttk.Frame(mainFrame, padding="5 15 10 5")
        botones.grid(column=0,row=5, columnspan=2)'''
        guardar=ttk.Button(mainFrame,text="Guardar")
        guardar.grid(column=0,row=5, sticky=(W))
        cancelar=ttk.Button(mainFrame,text="Cancelar")
        cancelar.grid(column=1, row=5, sticky=(W))
