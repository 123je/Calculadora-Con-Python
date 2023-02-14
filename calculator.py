from tkinter import *
from tkinter import ttk 
import math # raiz cuadrada
import os
from tkinter.ttk import Style #imagenes dinamicas
from PIL import ImageTk, ImageColor, Image




#titulo y posicion de la calculadora y 

ventana = Tk()
ventana.title("calculadora Amor ❤")
ventana.geometry("+500+200")
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)

#carpeta principal

carpeta_principal = os.path.dirname(__file__)

#carpetas para las imagenes icon y fondo

carpeta_imagenes = os.path.join(carpeta_principal, "imagenes") 

ventana.iconbitmap(os.path.join(carpeta_imagenes, "corazon.ico"))

#imagen de fondo

imagen_amor = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes, "amor.png")).resize((1500, 1248)))
ventana= Label(image = imagen_amor)
ventana.pack()



#renglon en pantalla

text= Entry(ventana, font=("calibri 30"))
text.grid(column=0, row=1, columnspan=4, sticky=(W,E,N,S))


#minimazar o maximizar pantalla

ventana.grid(column=0, row=0, sticky=(W,E,N,S))

ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)
ventana.columnconfigure(2, weight=1)
ventana.columnconfigure(3, weight=1)

ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)
ventana.rowconfigure(2, weight=1)
ventana.rowconfigure(3, weight=1)
ventana.rowconfigure(4, weight=1)
ventana.rowconfigure(5, weight=1)
ventana.rowconfigure(6, weight=1)
ventana.rowconfigure(7, weight=1)



#funcion al dar click y mostrar en pantalla

i=0

def click_boton(valor):
    global i
    text.insert(i, valor) 
    i+= 1


# funcion para borar todo

def borar():
    text.delete(0, END)
    i=0

    
#funcion para las operaciones (+,-,*,/ etc)

 
def resuelve_operacion(operador):
    global i
    logitud_operador = len(operador)
    text.insert(i, operador)
    i+= logitud_operador
    
    
#funcion para borar digito ppr digito
    
def borrar_uno_solo():
    estado_visualizacion = text.get()
    if len(estado_visualizacion):
        nuevo_estado = estado_visualizacion [:-1]
        borar()
        text.insert(0, nuevo_estado)
    else:
        borar()
        text.insert(0, 'error')


#funcion para el igual      
        
def calcular():
    estado_visualizacion = text.get()
    try:
        math_expression =  compile(estado_visualizacion, 'app.py', 'eval')
        result = eval(math_expression)
        borar()
        text.insert(0, result)
    except:
        borar()
        text.insert(0, "Mi Vida Eso Te Da Error :(")
        
        
#estilos para los botones

estilos_botones_numeros = ttk.Style()
estilos_botones_numeros.configure('botones_numeros.TButton', font="Explora 15", Width=5, background="#6D02B2", relief="flat")
estilos_botones_numeros.map('botones_numeros.TButton', foreground=[('active', '#6D02B2')] )

estilos_botones_borrar = ttk.Style()
estilos_botones_borrar.configure('botones_borrar.TButton', font="Explora 15", Width=5, relief="flat", background="#EC0000")
estilos_botones_borrar.map('botones_borrar.TButton', foreground=[('active', '#FF0000')])

estilos_botones_restantes = ttk.Style()
estilos_botones_restantes.configure('botones_restantes.TButton', font="Explora 15", Width=5, relief="flat", background="#0035EB")
estilos_botones_restantes.map('botones_restantes.TButton', foreground=[('active', '#0035EB')] )

#botones de la calculadora 

Button0  = ttk.Button(ventana, style="botones_numeros.TButton", text="0",  command = lambda:click_boton(0))
Button1  = ttk.Button(ventana, style="botones_numeros.TButton", text="1",  command = lambda:click_boton(1))
Button2  = ttk.Button(ventana, style="botones_numeros.TButton", text="2",  command = lambda:click_boton(2))
Button3  = ttk.Button(ventana, style="botones_numeros.TButton", text="3",  command = lambda:click_boton(3))
Button4  = ttk.Button(ventana, style="botones_numeros.TButton", text="4",  command = lambda:click_boton(4))
Button5  = ttk.Button(ventana, style="botones_numeros.TButton", text="5",  command = lambda:click_boton(5))
Button6  = ttk.Button(ventana, style="botones_numeros.TButton", text="6",  command = lambda:click_boton(6))
Button7  = ttk.Button(ventana, style="botones_numeros.TButton", text="7",  command = lambda:click_boton(7))
Button8  = ttk.Button(ventana, style="botones_numeros.TButton", text="8",  command = lambda:click_boton(8))
Button9  = ttk.Button(ventana, style="botones_numeros.TButton", text="9",  command = lambda:click_boton(9))


Button_borrar =         ttk.Button(ventana, text=chr(9003),  style="botones_borrar.TButton", command = lambda:borrar_uno_solo())
Button_borrar_todo =    ttk.Button(ventana, text="c",  style="botones_borrar.TButton", command = lambda: borar())
Button_parentesis1 =    ttk.Button(ventana, text="(",  style="botones_restantes.TButton", command = lambda:resuelve_operacion("("))
Button_parentesis2 =    ttk.Button(ventana, text=")", style="botones_restantes.TButton",  command = lambda:resuelve_operacion(")"))
Button_punto =          ttk.Button(ventana, text=".", style="botones_restantes.TButton",  command = lambda:click_boton("."))

Button_suma =           ttk.Button(ventana, text="+", style="botones_restantes.TButton", command = lambda:resuelve_operacion("+"))
Button_resta =          ttk.Button(ventana, text="-", style="botones_restantes.TButton", command = lambda:resuelve_operacion("-"))
Button_multiplicacion = ttk.Button(ventana, text="x",  style="botones_restantes.TButton", command = lambda:resuelve_operacion("*"))
Button_division =       ttk.Button(ventana, text=chr(247), style="botones_restantes.TButton", command = lambda:resuelve_operacion("/"))


Button_igual = ttk.Button(ventana, text="❤",  style="botones_restantes.TButton", command = lambda:calcular())
Button_raiz_cuadrada = ttk.Button(ventana, text="EXP",  style="botones_restantes.TButton", command = lambda:resuelve_operacion("**"))

#presentacion stylos botones


Button_parentesis1.grid(column=0, row=2, padx=13, pady=13, sticky=(W,E,N,S))
Button_parentesis2.grid(column=1, row=2, padx=13, pady=13, sticky=(W,E,N,S))
Button_borrar_todo.grid(column=2, row=2, padx=15, pady=15, sticky=(W,E,N,S))
Button_borrar.grid(column=3, row=2, padx=13, pady=13, sticky=(W,E,N,S))

Button7.grid(column=0, row=3, padx=13, pady=13, sticky=(W,E,N,S))
Button8.grid(column=1, row=3, padx=13, pady=13, sticky=(W,E,N,S))
Button9.grid(column=2, row=3, padx=13, pady=13,  sticky=(W,E,N,S))
Button_division.grid(column=3, padx=13, pady=13, row=3, sticky=(W,E,N,S))

Button4.grid(column=0, row=4, padx=13, pady=13, sticky=(W,E,N,S))
Button5.grid(column=1, row=4, padx=13, pady=13, sticky=(W,E,N,S))
Button6.grid(column=2, row=4, padx=13, pady=13, sticky=(W,E,N,S))
Button_multiplicacion.grid(column=3, row=4, padx=13, pady=13, sticky=(W,E,N,S))

Button1.grid(column=0, row=5, padx=13, pady=13, sticky=(W,E,N,S))
Button2.grid(column=1, row=5, padx=13, pady=13, sticky=(W,E,N,S))
Button3.grid(column=2, row=5, padx=13, pady=13, sticky=(W,E,N,S))
Button_suma.grid(column=3, row=5, padx=13, pady=13, sticky=(W,E,N,S))

Button0.grid(column=0, row=6, columnspan=2, padx=13, pady=13, sticky=(W,E,N,S))
Button_punto.grid(column=2, row=6, padx=13, pady=13, sticky=(W,E,N,S))
Button_resta.grid(column=3, row=6, padx=13, pady=13, sticky=(W,E,N,S))

Button_igual.grid(column=0, row=7, columnspan=3, padx=13, pady=13, sticky=(W,E,N,S))
Button_raiz_cuadrada.grid(column=3, row=7, padx=13, pady=13, sticky=(W,E,N,S))


#C:\Users\ElFlaco\AppData\Local\Programs\Python\Python311\Scripts\pyinstaller --onefile --icon=.amor.ico calculadora_python.py
ventana.mainloop()

