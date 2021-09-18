from tkinter import *
from tkinter import messagebox
import sqlite3


raiz= Tk ()
raiz.title("CRUD - CARGA DE CLIENTES")
#raiz.geometry("400x400")

miFrame= Frame (raiz)
miFrame.pack()
#-------------------funciones de botones--------------------------------------------

RUTA="/Users/macbookpro/Desktop/CRUD/CRUD"

def ConexionBBDD ():
    miConexion=sqlite3.connect ("Usuarios")
    miCursor=miConexion.cursor()
    try:
        miCursor.execute('''
        CREATE TABLE DATOS_USUARIOS (
            CAMPO_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            CAMPO_NOMBRE VARCHAR (50),
            CAMPO_PASSWORD VARCHAR (10),
            CAMPO_APELLIDO VARCHAR (50),
            CAMPO_DIRECCION VARCHAR (50),
            CAMPO_COMENTARIOS VARCHAR (100))
    
        ''')
        messagebox.showinfo ("BBDD", "Base de datos creada exitosamente!")

    except:
        messagebox.showwarning ("OJITO EH!", "La BBDD ya existe!")

def SalirAplicacion():
    Pregunta= messagebox.askquestion ("Salir", "Desesa salir de la aplicación?")
    if Pregunta=="yes":
        raiz.destroy()

def LimpiarCampos():
    miID.set("")
    miNombre.set("")
    miPassword.set("")
    miApellido.set("")
    miDireccion.set("")
    miObservacion.set("")
    

def Crear ():
    miConexion=sqlite3.connect ("Usuarios")
    miCursor=miConexion.cursor()
    miCursor.execute ("INSERT INTO DATOS_USUARIOS VALUES (NULL, '"+ miNombre.get() +
    "', '" + miPassword.get() +
    "', '" + miApellido.get() +
    "', '" + miDireccion.get() +
    "', '" + miObservacion.get() +"') ")
    
    miConexion.commit()
    messagebox.showinfo ("BBDD", "Los registros fueron guardados con exito")

def Leer ():
    miConexion=sqlite3.connect ("Usuarios")
    miCursor=miConexion.cursor()
    miCursor.execute ("SELECT * FROM DATOS_USUARIOS WHERE CAMPO_ID=" + miID.get())
    DataUsuario= miCursor.fetchall()
    for usuario in DataUsuario:
        miID.set (usuario[0])
        miNombre.set (usuario[1])
        miPassword.set (usuario[2])
        miApellido.set (usuario[3])
        miDireccion.set (usuario[4])
        miObservacion.set (usuario[5])
    miConexion.commit()

def Actualizar ():
    miConexion=sqlite3.connect ("Usuarios")
    miCursor=miConexion.cursor()
    miCursor.execute ("UPDATE DATOS_USUARIOS SET CAMPO_NOMBRE='" + miNombre.get() +
        "', CAMPO_PASSWORD='" + miPassword.get() +
        "', CAMPO_APELLIDO='" + miApellido.get() +
        "', CAMPO_DIRECCION='" + miDireccion.get() +
        "', CAMPO_COMENTARIOS='" + miObservacion.get() + 
        "' WHERE CAMPO_ID=" + miID.get())  
    
    miConexion.commit()
    messagebox.showinfo ("BBDD", "Los registros fueron actualizados con exito")

def Eliminar ():
    miConexion=sqlite3.connect ()
    miCursor=miConexion.cursor()
    miCursor.execute ("DELETE FROM DATOS_USUARIOS WHERE CAMPO_ID=" + miID.get())
    miConexion.commit()

    messagebox.showinfo ("BBDD", "El registro ha sido borrado con exito!")




#-------------------MENU--------------------------------------------
miMenu= Menu (raiz)
raiz.config (menu= miMenu, width=300,height=300)

BBDD= Menu (miMenu, tearoff=0)
BBDD.add_command (label="Conectar", command=ConexionBBDD)
BBDD.add_command (label="Salir", command= SalirAplicacion)

Borrar=Menu (miMenu, tearoff=0)
Borrar.add_command (label="Borrar Capmpos", command=LimpiarCampos)

CRUD=Menu (miMenu, tearoff=0)
CRUD.add_command (label="Create", command=Crear)
CRUD.add_command (label="Read", command=Leer)
CRUD.add_command (label="Upgrade", command=Actualizar)
CRUD.add_command (label="Delete", command=Eliminar)

Ayuda=Menu (miMenu, tearoff=0)
Ayuda.add_command (label="Licencia")
Ayuda.add_command (label="Acerca de...")

miMenu.add_cascade(label="BBDD", menu=BBDD)
miMenu.add_cascade(label="Borrar", menu=Borrar)
miMenu.add_cascade(label="CRUD", menu=CRUD)
miMenu.add_cascade(label="Ayuda", menu=Ayuda)

#-------------------CAMPOS--------------------------------------------
miID=StringVar()
miNombre=StringVar()
miPassword=StringVar()
miApellido=StringVar()
miDireccion=StringVar()
miObservacion=StringVar()

ID= Label (miFrame, text="ID: ").grid(row=0, column=0, sticky="w",pady=5)
Nombre= Label (miFrame, text="Nombre: ").grid(row=1, column=0, sticky="w",pady=5)
Password= Label (miFrame, text="Password: ").grid(row=2, column=0, sticky="w",pady=5)
Apellido= Label (miFrame, text="Apellido: ").grid(row=3, column=0, sticky="w",pady=5)
Direccion= Label (miFrame, text="Direccion: ").grid(row=4, column=0, sticky="w",pady=5)
Observaciones= Label (miFrame, text="Observaciones: ").grid(row=5, column=0, sticky="w",pady=5)

Casilla_ID= Entry (miFrame, textvariable=miID).grid(row=0, column=1)
Casilla_Nombre= Entry (miFrame, textvariable=miNombre).grid(row=1, column=1)
Casilla_Password= Entry (miFrame,textvariable=miPassword, show="*").grid(row=2, column=1)
Casilla_Apellido= Entry (miFrame, textvariable=miApellido).grid(row=3, column=1)
Casilla_Direccion= Entry (miFrame, textvariable=miDireccion).grid(row=4, column=1)
Casilla_Observaciones= Entry (miFrame, textvariable=miObservacion).grid(row=5, column=1)

scroll= Scrollbar (miFrame, command= Casilla_Observaciones)
scroll.grid(row=5, column=2, sticky= "nsew")


#-------------------BOTONES--------------------------------------------
Frame2= Frame (raiz)
Frame2.pack()

botonCreate= Button (Frame2, text= "Create",width=8, command=Crear ).grid (row=0, column=0,pady=10)
botonRead= Button (Frame2, text= "Read",width=8, command=Leer ).grid (row=0, column=1,pady=10)
botonUpdate= Button (Frame2, text= "Update",width=8, command=Actualizar ).grid (row=0, column=2,pady=10)
botonDelete= Button (Frame2, text= "Delete",width=8, command=Eliminar ).grid (row=0, column=3, pady=10)




raiz.mainloop()