from tkinter import *
from PIL import Image

def resize_imagen(imagen, dimensiones):
    img = Image.open(imagen)
    nueva_imagen = img.resize(dimensiones)
    nueva_imagen.save("logo_redimensionado.png")
    return "logo_redimensionado.png"

def frame_ingreso():
    d = ""
    v = ""
    #nuevo_frame_segun si es ingreso
    miFrame_ingreso = Frame()
    miFrame_ingreso.pack() #meter el frame dentro de la raiz
    miFrame_ingreso.config(bg="lightgreen")
    miFrame_ingreso.config(width="230", height="120")
    miFrame_ingreso.place(x=300, y=170)
    #texto
    descripcion = Label(miFrame_ingreso, text="Descripcion: ", bg="lightgreen")
    descripcion.place(x=20,y=20) #ubica el texto en cualquier lugar con coordenadas

    dato_descripcion = Entry(miFrame_ingreso, textvariable=d)
    dato_descripcion.place(x=95, y=20)

    valor = Label(miFrame_ingreso, text="Valor: ", bg="lightgreen")
    valor.place(x=20,y=50) #ubica el texto en cualquier lugar con coordenadas

    dato_valor = Entry(miFrame_ingreso, textvariable=v)
    dato_valor.place(x=95, y=50)

    buttonForget = Button(miFrame_ingreso,
                          text = 'Enviar',
                          command=lambda: miFrame_ingreso.destroy())
    buttonForget.config(relief="groove")
    buttonForget.config(bd = 2)
    buttonForget.place(x=180, y=90)


def frame_egreso():
    #nuevo_frame_segun si es egreso
    miFrame_egreso = Frame()
    miFrame_egreso.pack() #meter el frame dentro de la raiz
    miFrame_egreso.config(bg="red")
    miFrame_egreso.config(width="230", height="120")
    miFrame_egreso.place(x=300, y=170)
    buttonForget = Button(miFrame_egreso,
                          text = 'Enviar',
                          command=lambda: miFrame_egreso.destroy())
    buttonForget.config(relief="groove")
    buttonForget.config(bd = 2)
    buttonForget.place(x=180, y=90)

def tipo_de_frame(texto):
    if texto == "Ingreso":
        return frame_ingreso()
    elif texto == "Egreso":
        return frame_egreso()
    elif texto == "Fin":
        texto_fin = Label(miFrame, text="ACTUALIZACION FINALIZADA\nPOR FAVOR CIERRA LA VENTANA", bg="gray", font=("Comic Sans MS", 12))
        texto_fin.place(x=245,y=150) #ubica el texto en cualquier lugar con coordenadas

def enviarDatos():
    mensaje =str(cuadroTexto.get())
    tipo_de_frame(mensaje)


raiz = Tk() #Ventana

raiz.title("Controlador de gastos")
#raiz.geometry("650x350") #ancho por defecto
raiz.config(bg="gray")

miFrame = Frame()

miFrame.pack() #meter el frame dentro de la raiz

miFrame.config(bg="gray")
miFrame.config(width="650", height="350")
miFrame.config(bd="40")
miFrame.config(relief="groove")

#Titulo
miLabel = Label(miFrame, text="BIENVENIDO A SU GESTOR DE GASTOS SEBASTIAN", bg="gray", font=("Comic Sans MS", 12))
miLabel.place(x=80,y=5) #ubica el texto en cualquier lugar con coordenadas

#Logo
imagen = resize_imagen("logo_excel.png", (150,150))
logo = PhotoImage(file=imagen)
miLabel2 = Label(miFrame, image=logo, bg="gray", )
miLabel2.place(x=40,y=70)

#Indicar si es un ingreso
tipo_entrada = Label(miFrame, text="Ingrese que dato va a guardar:\n->Ingreso\n->Salida  ", bg="gray",)
tipo_entrada.place(x=200,y=60) #ubica el texto en cualquier lugar con coordenadas

valor = "" #Guarda el dato de la casilla en esta variable
#Cuadro vacio de texto
cuadroTexto = Entry(miFrame, textvariable=valor)
cuadroTexto.place(x=320, y=85)
#Boton_enviar
boton_Envio= Button(miFrame, text="Enviar", command=enviarDatos)
boton_Envio.place(x=450, y=80)




raiz.mainloop() #Ciclo infinito de la Ventana
