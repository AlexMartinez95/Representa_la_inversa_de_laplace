import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk
import control as control
import numpy as np

naranja_fuerte_codigo_de_colores='#EEA006'
naranja_claro_codigo_de_colores='#FCEAC7'

def ecuacion_mal_definida():
    tk.messagebox.showinfo(message="Esta combinación de entradas no se pueden representar, por favor verifique los inputs.", title="Error")
    t_error=np.array([0,1,2,3,4,5,6,7])
    y_error=np.zeros(8,)
    fig.add_subplot(111).plot(t_error, y_error)
    canvas.draw()  

def graficado(Y0,s,boton_seleccionado_leído):
    
    fig.clf()
    try:
        if boton_seleccionado_leído=='señal_y_t': 
            t,y=control.impulse_response(Y0)
        if boton_seleccionado_leído=='señal_dy_dt':
             t,y=control.impulse_response(Y0*s)                 
        if boton_seleccionado_leído=='señal_int_y_dt':    
            t,y=control.impulse_response(Y0/s)
        fig.add_subplot(111).plot(t, y)
        canvas.draw()    
    except ValueError:
        ecuacion_mal_definida()
  

def leer_datos_de_la_ventana():
    
    s=control.tf('s') 
    boton_seleccionado_leído=boton_seleccionado_para_leer.get() 
    Y0=eval(input_de_la_ecuación_del_usuario.get())  
    graficado(Y0,s,boton_seleccionado_leído)


ventana = tk.Tk()
ventana.wm_title("Representacion de señales")
ventana.config(width=500, height=200,bg=naranja_claro_codigo_de_colores)

frame_canvas=tk.Frame(ventana)
frame_canvas.grid(row=3, column=0)
fig = Figure(figsize=(5, 4), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=frame_canvas)  
toolbar = NavigationToolbar2Tk(canvas,frame_canvas)
canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=True)
        
frame_parte_de_laplace=tk.Frame(ventana,bg=naranja_claro_codigo_de_colores)
frame_parte_de_laplace.grid(row=0,column=0)

input_de_la_ecuación_del_usuario = ttk.Entry(frame_parte_de_laplace, width=30)
input_de_la_ecuación_del_usuario.insert(0,"(1)/(s**2)")
input_de_la_ecuación_del_usuario.grid(row=1,column=0)

labelSistema=tk.Label(frame_parte_de_laplace,text="Y(s)=L(y(t))",bg=naranja_claro_codigo_de_colores)
labelSistema.grid(row = 0, column =0)

leer_datos_de_la_ventana_boton = tk.Button(frame_parte_de_laplace, text="Ok",command=leer_datos_de_la_ventana,bg=naranja_fuerte_codigo_de_colores)
leer_datos_de_la_ventana_boton.grid(row =1, column = 2, sticky=tk.E)

frameEntradas=tk.Frame(ventana)
frameEntradas.grid(row=1,column=0)

boton_seleccionado_para_leer = tk.StringVar()
boton_seleccionado_para_leer.set(0)

selectorseñal_y_t= tk.Radiobutton(frameEntradas,bg=naranja_claro_codigo_de_colores, text="y(t)", variable=boton_seleccionado_para_leer,value='señal_y_t',command=leer_datos_de_la_ventana)
selectorseñal_dy_dt= tk.Radiobutton(frameEntradas,bg=naranja_claro_codigo_de_colores, text="dy/dt", variable=boton_seleccionado_para_leer,value='señal_dy_dt',command=leer_datos_de_la_ventana)
selectorseñal_int_y_dt=  tk.Radiobutton(frameEntradas,bg=naranja_claro_codigo_de_colores, text="∫ydt", variable=boton_seleccionado_para_leer,value='señal_int_y_dt',command=leer_datos_de_la_ventana)
 
selectorseñal_y_t.grid(row = 0, column =1)
selectorseñal_dy_dt.grid(row = 0, column =2)
selectorseñal_int_y_dt.grid(row = 0, column = 3)

    
        
ventana.mainloop()