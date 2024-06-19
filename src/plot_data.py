import csv
import sys
import os
import data as dt
from datetime import datetime
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
import tkcalendar
from tkcalendar import Calendar
import data as dt
from datetime import timedelta
from typing import List
import plotly.graph_objs as go
from plotly.offline import plot
import time
from numpy import trapz
import customtkinter
from tkcalendar import *
from functools import partial

n_array = []
i_array = []

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

def win_disp(root):
    #Se configura la ventana
    WIDTH = 780
    HEIGHT = 520
    win = Toplevel(root)
    win.title("Procesador de datos glucosa")
    win.geometry(f"{WIDTH}x{HEIGHT}")
    win.configure(bg="#161E29")
    win.grid_columnconfigure(1, weight=1)
    win.grid_rowconfigure(0, weight=1)

    #Se agrega una barra de menu en la esquina superior izquierda
    menubar = Menu(win)
    filemenu = Menu(menubar, tearoff=0)

    #Se procede a abrir el archivo csv
    buttons0 = []  # list to store the created buttons
    filemenu.add_command(label="Abrir archivo", command=lambda:Onadd(win, buttons0))
    #Se destruye ventana actual
    filemenu.add_command(label="Salir", command=win.destroy)
    menubar.add_cascade(label="Menu de opciones", menu=filemenu)
    win.config(menu=menubar)

    #Configuracion del aspecto estetico de la ventana
    win.frame_left = customtkinter.CTkFrame(master=win,
                                                 width=180,
                                                 corner_radius=0)
    win.frame_left.grid(row=0, column=0, sticky="nswe")
    win.frame_right = customtkinter.CTkFrame(master=win)
    win.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
    win.frame_left.grid_rowconfigure(0, minsize=10)
    win.frame_left.grid_rowconfigure(5, weight=1)
    win.frame_left.grid_rowconfigure(8, minsize=20)
    win.frame_left.grid_rowconfigure(11, minsize=10)
    win.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
    win.frame_right.rowconfigure(7, weight=10)
    win.frame_right.columnconfigure((0, 1), weight=1)
    win.frame_right.columnconfigure(2, weight=0)
    win.frame_info = customtkinter.CTkFrame(master=win.frame_right)
    win.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")
    win.frame_info.rowconfigure(0, weight=1)
    win.frame_info.columnconfigure(0, weight=1)

#Grafica los datos
#Agupa lista en forma de pares ordenados
def grouper(theList, N):
    subList = [theList[n:n+N] for n in range(0, len(theList), N)]
    return subList

#Esta funcion retorna ruta en el directorio donde se encuentra el Archivo
#que se desea abrir
def create_file():
    flag = False
    filetypes = (
        ('text files', '*.csv'),
        ('All files', '*.*')
    )
    # Pide abrir el archivo
    f = fd.askopenfile(filetypes=filetypes)
    try:
        name = os.path.abspath(f.name)
        flag = True
        return flag, name
    except :
        flag = False
        name = ""
        return flag, name #retorna un booleano si se encontro y el nombre.

#Cuando se abre la barra de menu y se presiona abrir archivo se ejecuta este bloque
def Onadd(win, buttons0):
    if len(buttons0) == 0:
        pass
    else:
        # Remueve los botones de los paciente creados
        for b in buttons0:
            b.grid_forget()
    #Variable aux contiene nombre del archivo y booleano
    aux = create_file()
    #Si el archivo existe, ejecuta este bloque
    if aux[0] == True:
        try:
            lst_aux = getname_file(aux[1])
            #Siele archivo se pudo leer, ejecuta
            if lst_aux[2] == True:
                Text_file = aux[1]

                #Se agregan etiquetas y botones de pacientes
                label_1 = customtkinter.CTkLabel(master=win.frame_left,
                                                             text="Cantidad de pacientes",
                                                             font=("Roboto Medium", -16))
                label_1.grid(row=1, column=0, pady=10, padx=10)

                entry = customtkinter.CTkEntry(master=win.frame_left,
                                                        width=90,
                                                        placeholder_text="Ingrese un numero")
                entry.grid(row=3, column=0, columnspan=2, pady=20, padx=20, sticky="we")

                button_1 = customtkinter.CTkButton(master=win.frame_left,
                                                            text="Confirmar",
                                                            command=lambda:show_window(entry.get(), lst_aux, Text_file,win, buttons0))
                button_1.grid(row=4, column=0, pady=10, padx=20)
            else:
                messagebox.showerror(message="Archivo no soportado", title="Advertencia")
        except:
            messagebox.showerror(message="Archivo no soportado", title="Advertencia")
    else :
        messagebox.showerror(message="No se selecciono un archivo", title="Advertencia")
        win.destroy()

#Determina que la fecha inicial sea menor a la fecha final
def greater(test_list):
    n = len(test_list)
    Flag  = True
    for idx in range(1, n):
        if test_list[idx - 1] < test_list[idx]:
            Flag =True
        else:
            Flag =False
            break
    return Flag

#Crea una ventana que pregunta cuantos rangos se van a crear
def create_window(root,lst_aux, Text_file):
    #Configuracion de la ventana
    WIDTH = 780
    HEIGHT = 520
    win = Toplevel(root)
    win.title("Procesador de datos glucosa")
    win.geometry(f"{WIDTH}x{HEIGHT}")
    win.configure(bg="#161E29")

    #Configuracion del aspecto estetico de la ventana
    win.grid_columnconfigure(1, weight=1)
    win.grid_rowconfigure(0, weight=1)
    win.frame_left = customtkinter.CTkFrame(master=win,
                                                 width=180,
                                                 corner_radius=0)
    win.frame_left.grid(row=0, column=0, sticky="nswe")
    win.frame_right = customtkinter.CTkFrame(master=win)
    win.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
    win.frame_left.grid_rowconfigure(0, minsize=10)
    win.frame_left.grid_rowconfigure(5, weight=1)
    win.frame_left.grid_rowconfigure(8, minsize=20)
    win.frame_left.grid_rowconfigure(11, minsize=10)
    win.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
    win.frame_right.rowconfigure(7, weight=10)
    win.frame_right.columnconfigure((0, 1), weight=1)
    win.frame_right.columnconfigure(2, weight=0)
    win.frame_info = customtkinter.CTkFrame(master=win.frame_right)
    win.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")
    win.frame_info.rowconfigure(0, weight=1)
    win.frame_info.columnconfigure(0, weight=1)

    #Estas lstas almacenan botones y etiquetas que seran borrados cada vez que se actualizan datos de la ventana
    btn_windows = []
    lbl_windows = []
    btn_graph = []
    btn_dwn = []
    lbl_disp = []
    lbl_cp = []
    button_identities = []

    #Se agregan entradas de txto
    label_1 = customtkinter.CTkLabel(master=win.frame_left,
                                                 text="Cantidad de rangos de tiempo del paciente",
                                                 font=("Roboto Medium", -16))
    label_1.grid(row=2, column=0, columnspan=1, pady=10, padx=10)

    entry = customtkinter.CTkEntry(master=win.frame_left,
                                            width=90,
                                            placeholder_text="Ingrese un numero par (Fecha inicial y final)")
    entry.grid(row=3, column=0, columnspan=1, pady=20, padx=20, sticky="we")

    label_2 = customtkinter.CTkLabel(master=win.frame_left,
                                                 text="Nombre del paciente",
                                                 font=("Roboto Medium", -16))
    label_2.grid(row=0, column=0, columnspan=1, pady=10, padx=10)

    entry2 = customtkinter.CTkEntry(master=win.frame_left,
                                            width=90,
                                            placeholder_text="Ingrese un nombre o identificacion")
    entry2.grid(row=1, column=0, columnspan=1, pady=20, padx=20, sticky="we")

    #Se lee el archivo .csv
    lst = dt.read_file(Text_file)
    id_sensor = list(dict.fromkeys(lst[1]))
    combobox_1 = customtkinter.CTkComboBox(master=win.frame_left,
                                                values=id_sensor)
    combobox_1.grid(row=4, column=0, columnspan=1, pady=10, padx=20, sticky="we")
    combobox_1.set("Ingrese numero de identificacion del lector")

    button_1 = customtkinter.CTkButton(master=win.frame_left,
                                                text="Confirmar",
                                                command=lambda:show_dateentry(entry.get(), win,lst_aux,Text_file, entry2.get(), btn_windows, lbl_windows, btn_graph, btn_dwn, lbl_disp, button_identities, combobox_1.get(), lst[1], lbl_cp))
    button_1.grid(row=5, column=0, columnspan=1, pady=10, padx=20)

#Ciclo for crea n cantidad de venatanas adicionales
def show_window(num, lst_aux, Text_file,root, buttons0):
    if len(buttons0) == 0:
        pass
    else:
        # Remueve botones del paciente
        for b in buttons0:
            b.grid_forget()

    if str.isdigit(num) and int(num)> 0:
        paciente_image = dt.load_image(r"Dependencies\pacientes1.png", 20)
        num = int(num)
        if num <= 10:
            for i in range(num):
                pos = i + 1
                texto = "Agregar rangos del paciente #" + " " + str(pos)
                button_1 = customtkinter.CTkButton(master=root.frame_info,
                                                    image=paciente_image,
                                                    text=texto,
                                                    height=32,
                                                    compound="right",
                                                    command=lambda:create_window(root,lst_aux, Text_file))
                button_1.grid(row=pos, column=0, columnspan=2, padx=20, pady=(20, 10), sticky="ew")
                buttons0.append(button_1)
        else:
            messagebox.showerror(message="Debe selecionar un maximo de 10 pacientes, si desea pacientes adicionales puede  volver a selecionar un boton de paciente", title="Advertencia")
    else:
        messagebox.showerror(message="Debe selecionar un valor numerico", title="Advertencia")



def date_and_hour(root, year_imp, month_imp, day_imp, h_imp, m_imp, index,button_identities):
    #Se configura ventana
    import datetime
    ws = Toplevel(root)
    ws.geometry("500x400")
    ws.config(bg="#161E29")
    ws.grid_columnconfigure(1, weight=1)
    ws.grid_rowconfigure(0, weight=1)
    ws.frame_info = customtkinter.CTkFrame(master=ws)
    ws.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")
    hour_string=StringVar(ws.frame_info,str(h_imp))
    min_string=StringVar(ws.frame_info,str(m_imp))
    last_value_sec = ""
    last_value = ""
    f = ('Times', 20)

    def display_msg():
        global n_array
        global i_array
        date = cal.get_date()
        m = min_sb.get()
        h = sec_hour.get()
        date = datetime.datetime.strptime(date,'%m/%d/%y').strftime('%m-%d-%Y')
        date_time =  date.split("-")
        mes = int(date_time[0])
        dia = int(date_time[1])
        ano = int(date_time[2])
        m = int(m)
        h = int(h)
        x = datetime.datetime(ano, mes, dia, m, h)
        total_date = x.strftime("%m-%d-%Y %I:%M %p")
        #Se lmacena la fecha introducida
        n_array.append(total_date)
        i_array.append(index)
        #Se agrea la fecha introducida en el boton de la ventana principal
        bname = (button_identities[index])
        bname.configure(text = total_date)
        ws.destroy()

    #Se configura formato de horas
    if last_value == "59" and min_string.get() == "0":
        hour_string.set(int(hour_string.get())+1 if hour_string.get() !="23" else 0)
        last_value = min_string.get()

    #Configura formato de minutos
    if last_value_sec == "59" and sec_hour.get() == "0":
        min_string.set(int(min_string.get())+1 if min_string.get() !="59" else 0)
    if last_value == "59":
        hour_string.set(int(hour_string.get())+1 if hour_string.get() !="23" else 0)
        last_value_sec = sec_hour.get()

    #Estos frames se crean para posicionar la seleccion de las horas y minutos
    fone = Frame(ws.frame_info)
    ftwo = Frame(ws.frame_info)

    fone.pack(pady=10)
    ftwo.pack(pady=10)

    #Este bloque indica el numero del boton selecionado,para ingresar las fechas de manera ordenada
    if index == 0:
        text010 = "Fecha Inicial # {0}".format(1)
    elif index == 1:
        text010 = "Fecha Final # {0}".format(1)
    elif index == 2:
        text010 = "Fecha Inicial # {0}".format(2)
    elif index == 3:
        text010 = "Fecha Final # {0}".format(2)
    elif index == 4:
        text010 = "Fecha Inicial # {0}".format(3)
    elif index == 5:
        text010 = "Fecha Final # {0}".format(3)
    elif index == 6:
        text010 = "Fecha Inicial # {0}".format(4)
    elif index == 7:
        text010 = "Fecha Final # {0}".format(4)
    elif index == 8:
        text010 = "Fecha Inicial # {0}".format(5)
    elif index == 9:
        text010 = "Fecha Final # {0}".format(5)

    date_frame = customtkinter.CTkLabel(master=ws.frame_info,
                                          text=text010,
                                          font=("Roboto Medium", -20))
    date_frame.pack()

    #Se crea un calendario
    cal = Calendar(
        fone,
        selectmode="day",
        year=year_imp,
        month=month_imp,
        day=day_imp
        )
    cal.pack()

    #Se crea una caja para la seleccion de minutos
    min_sb = Spinbox(
        ftwo,
        from_=0,
        to=23,
        wrap=True,
        textvariable=hour_string,
        width=2,
        state="readonly",
        font=f,
        justify=CENTER
        )
    #Objeto seleccion de horas
    sec_hour = Spinbox(
        ftwo,
        from_=0,
        to=59,
        wrap=True,
        textvariable=min_string,
        font=f,
        state="readonly",
        width=2,
        justify=CENTER
        )

    min_sb.pack(side=LEFT, fill=X, expand=True)
    sec_hour.pack(side=LEFT, fill=X, expand=True)
    msg = customtkinter.CTkLabel(master=ws.frame_info,
                                          text="Hora  Minutos ",
                                          font=("Roboto Medium", -16))
    msg.pack(side=TOP)
    actionBtn = customtkinter.CTkButton(master=ws.frame_info,
                                            text="Confirmar",
                                            command=display_msg)
    actionBtn.pack(pady=10)
    msg_display = customtkinter.CTkLabel(master=ws.frame_info,
                                          text="",
                                          font=("Roboto Medium", -16))
    msg_display.pack(pady=10)

#Esta ventana permite selecionar los rangos de fechas y ordena su despliegue en pantalla
def show_dateentry(num, win,lst_aux,Text_file, entry2, btn_windows, lbl_windows, btn_graph, btn_dwn, lbl_disp, button_identities, combobox_1, lst_id, lbl_cp):
    contain = []
    entry2 = str(entry2)
    j = 0
    k = 0
    if len(btn_windows) == 0 and len(lbl_windows) == 0 and len(btn_graph) == 0 and len(btn_dwn) == 0 and len(lbl_disp) == 0 and len(lbl_cp) == 0:
        pass
    else:
        # Se remueven etiquetas y botones
        for b in btn_windows:
            b.grid_forget()
        for b in lbl_windows:
            b.grid_forget()
        for b in btn_graph:
            b.grid_forget()
        for b in btn_dwn:
            b.grid_forget()
        for b in lbl_disp:
            b.grid_forget()
        for b in lbl_cp:
            b.place_forget()

    if len(entry2) != 0:
        if len(combobox_1) !=0 and  (combobox_1 in lst_id):
            if str.isdigit(num) and  int(num) >0:
                num = int(num)
                if num <= 10:
                    if num!=0 and (num % 2) == 0:
                        for i in range(num):
                            #Se configura el indice y posicion de los botones
                            pos_col = i
                            pos_col_mas = pos_col + 1
                            pos_col1 = i  - 1
                            pos1 =  2
                            pos2 =  3
                            pos3 = i + 4
                            pos4 = i + 5
                            total_date = ""
                            if (i % 2) == 0:
                                if i == 0:
                                    position = i + 1
                                else:
                                    position = i - j
                                    j +=1
                                rang1 = "Fecha inicial " + str(position)
                                label_1 = customtkinter.CTkLabel(master=win.frame_info,
                                                                text=rang1,
                                                                font=("Roboto Medium", -16))
                                label_1.grid(row=0, column=pos_col, pady=10, padx=10)
                                button_1 = customtkinter.CTkButton(master=win.frame_info,
                                                                            text="Generar fecha inicial # {0}".format(position),
                                                                            command=partial(date_and_hour,win)(lst_aux[0].year, lst_aux[0].month, lst_aux[0].day, 0, 0, i, button_identities))
                                button_1.grid(row=1, column=pos_col, pady=10, padx=10)
                                lbl_windows.append(label_1)
                                btn_windows.append(button_1)
                                button_identities.append(button_1)

                            else:
                                if i == 1:
                                    position = i
                                else:
                                    position = i - 1 - k
                                    k += 1
                                rang2 = "Fecha final " + str(position)
                                label_2 = customtkinter.CTkLabel(master=win.frame_info,
                                                                text=rang2,
                                                                font=("Roboto Medium", -16))
                                label_2.grid(row=2, column=pos_col1, pady=10, padx=10)
                                button_2 = customtkinter.CTkButton(master=win.frame_info,
                                                                            text="Generar fecha final # {0}".format(position),
                                                                            command=partial(date_and_hour,win)(lst_aux[1].year, lst_aux[1].month, lst_aux[1].day, 23, 59, i, button_identities))
                                button_2.grid(row=3, column=pos_col1, pady=10, padx=10)
                                lbl_windows.append(label_2)
                                btn_windows.append(button_2)
                                button_identities.append(button_2)

                        grafico_image = dt.load_image(r"Dependencies\grafico1.png", 20)
                        button_11 = customtkinter.CTkButton(master=win.frame_right,
                                                            image=grafico_image,
                                                            text="Generar grafico",
                                                            height=32,
                                                            compound="right",
                                                            command=lambda:display_data3(Text_file, n_array, entry2, win, num, i_array, btn_dwn, lbl_disp, button_identities, n_array, combobox_1, lbl_cp))
                        button_11.grid(row=5, column=0, columnspan=2, padx=20, pady=(20, 10), sticky="ew")
                        btn_graph.append(button_11)
                    else:
                        messagebox.showerror(message="Selecione un numero par", title="Advertencia")
                else:
                    messagebox.showerror(message="Debe selecionar 6 o menos rangos de fechas", title="Advertencia")

            else:
                messagebox.showerror(message="Debe selecionar un valor numerico", title="Advertencia")
        else:
            messagebox.showerror(message="Debe ingresar la identificacion del sensor", title="Advertencia")
    else:
        messagebox.showerror(message="Ingrese un nombre o identificacion", title="Advertencia")

#Funcion determina si el archivo abierto cumple con el formato deseado
def getname_file(file_name):
    flag= True
    #Lee el archivo y almacena informacion en columnas, crea un dicionario
    lst = dt.read_file(file_name)
    #Si se tienen menos de 19 columns el archivo no se puede leer
    if len(list(lst.keys())) != 19:
        flag= False
    else:
        pass
    date0 = lst[2]
    code = lst[1]
    #Covierto todos los elementos de la columna a formato '%m-%d-%Y %I:%M %p'
    date0s = [datetime.strptime(regex_obtained_str, '%m-%d-%Y %I:%M %p')
                    for regex_obtained_str in date0]
    #Adquiero solo las fechas de la columna
    date0s = (datetime.strftime(i, "%m-%d-%Y") for i in date0s)
    #Elimina Duplicados
    date0s = list(dict.fromkeys(date0s))
    #Ordeno las fechas
    date0s = sorted(date0s)
    last = len(date0s) -1
    min, max = date0s[0], date0s[last]
    min = datetime.strptime(min, '%m-%d-%Y')
    max = datetime.strptime(max, '%m-%d-%Y')
    return min, max, flag #retorna primer y ultima fech del archivo, y si el archivo se pudo leer

#Se copia texto
def copy_txt(root,txt):
    root.clipboard_clear()
    root.clipboard_append(txt)
    messagebox.showinfo(title="", message="El texto ha sido copiado")

#Retorna tiempo paciente esta entre 70 y 140:
#Verificar esta funcion
def range_min_max(min, max, df0, subList, combobox_1, smallest):
    aux_str = []
    df = df0.copy()
    for i in range(len(subList)):
        suma_de_140 = []
        lst_140 = []
        #Se filtran los datos que estan dentro del rango de fechas
        dfh = df[((df['dates'] >= subList[i][0]) & (df['dates'] <= subList[i][1]) & (df["Numero de serie"].str.contains(combobox_1)))]
        #dfh = dfh.dropna(subset=['historial'])
        # Se convierte la columna a elementos de tiempo
        dfh['dates'] = pd.to_datetime(dfh['dates'])
        # cambia las fechas hacia arriba y en una nueva columna
        dfh['dates_shift'] = dfh['dates'].shift(-1)
        #calcular la diferencia
        dfh['time_diff'] = (dfh['dates_shift'] - dfh['dates']) / pd.Timedelta(seconds=1)
        # eliminar la columna temporal
        #del dfh['dates_shift']
        #Para segundos mayores a 86400, es decir un dia, no se tomara en cuenta dicho tiempo
        dfh["Daytime"] = dfh['time_diff']
        dfh.loc[dfh['time_diff']>=86400, 'Daytime'] = 0
        """
        with pd.option_context('display.max_rows', None,
                          'display.max_columns', None,
                           'display.precision', 3,
                           ):
                           print(dfh)
        """
        #Se calcula el tiempo entre 70 y 140 mg/dl
        #Se crean listas a partir de las Series de DataFrame
        hist = list(dfh['historial'].copy())
        delta_range = list(dfh["Daytime"].copy())
        cp_dates = list(dfh["dates"].copy())

        #Basicamente las tres listas tienen la misma extension
        for index in range(len(hist)):
            #El valor del historial ctual de acuerdo con el indice index debe ser menor y mayor a 140
            if pd.isna(hist[index]) == False and ( hist[index] < 70 or hist[index] > 140 ) :
                #Escenario donde el primer elemento de la lista es menor o mayor al rango
                if first_element(hist, hist[index]) == True:
                    pos2 = 0
                    #Si no hay resultados nulos en la columna historial
                    if pd.isna(hist[index + 1]) == False:
                        pos2 = index + 1
                        gluco_2 = hist[pos2]
                        time_2 = delta_range[pos2]
                    #Si hay resultados nulos en la columna historial
                    else:
                        pos22 = index + 2
                        pos2 = index + 1
                        gluco_2 = hist[pos22]
                        time_2 = delta_range[pos2]
                    #Se determina el valor point, para el posterior calculo del tiempo atraves de la pendiente
                    if  hist[index] >= 140 :
                        point = 140
                    else:
                        point = 70
                    #Se obtiene por medio de la pendtiene
                    dif_shift_2 = slope(hist[index],gluco_2,delta_range[index ], point, cp_dates[index+1], gluco_2)
                    #En este caso se otienen dos fechas y se obtiene la cantidad de segundos de la resta
                    if dif_shift_2[2] == True:
                        solv_time_2 = (cp_dates[index + 1] - datetime.fromtimestamp(dif_shift_2[0])).total_seconds()
                    #En este caso se obtien directamente los segundos
                    else:
                        solv_time_2 = dif_shift_2[0]
                    #Si la solucion esta dentro del rango de 70 y 140 se agrega el tiempo a la lista de tiempos
                    if dif_shift_2[1] == True:
                        delta_range[index] = solv_time_2
                    #En caso de que la solucion no este dentro del rango se agrega un cero a la lista de tiempos
                    else:
                        delta_range[index] = 0
                #Escenario donde el ultimo elemento de la lista es menor o mayor al rango
                #Explicacion es la misma que la del if anterior
                elif last_element(hist, hist[index]) == True:
                    pos1 = 0
                    if pd.isna(hist[index - 1]) == False:
                        pos1 = index - 1
                        gluco_1 = hist[pos1]
                        time_1 = delta_range[pos1]
                    else:
                        pos11 = index - 2
                        pos1 = index - 1
                        gluco_1 = hist[pos11]
                        time_1 = delta_range[pos1]

                    if  hist[index] >= 140 :
                        point = 140
                    else:
                        point = 70

                    dif_shift_1 = slope(gluco_1,hist[index],delta_range[index-1], point, cp_dates[index-1], gluco_1)

                    if dif_shift_1[2] == True:
                        solv_time_1 = (datetime.fromtimestamp(dif_shift_1[0]) - cp_dates[index-1]).total_seconds()
                    else:
                        solv_time_1 = dif_shift_1[0]

                    if dif_shift_1[1] == True:
                        delta_range[pos1] = solv_time_1
                    else:
                        delta_range[pos1] = 0

                #Caso donde un valor pivote se encuentra rodeado de un valor inferior o mayor al rango
                else:
                    pos1 = 0
                    pos2 = 0
                    #Se chequea si el elemento de la lista no es un valor nulo, en caso de serlo se salta al siguiete elemento
                    if pd.isna(hist[index - 1]) == False:
                        pos1 = index - 1
                        gluco_1 = hist[pos1]
                        time_1 = delta_range[pos1]
                    else:
                        pos11 = index - 2
                        pos1 = index - 1
                        gluco_1 = hist[pos11]
                        time_1 = delta_range[pos1]
                    if pd.isna(hist[index + 1]) == False:
                        pos2 = index + 1
                        gluco_2 = hist[pos2]
                        time_2 = delta_range[pos2]
                    else:
                        pos22 = index + 2
                        pos2 = index + 1
                        gluco_2 = hist[pos22]
                        time_2 = delta_range[pos2]
                    #Entraan los resultados mayores o menores a 70 y 140 para los valores mayores y menores del indice index
                    if  ( gluco_2 >= 70 or gluco_2 <= 140) and (gluco_1 >= 70 or gluco_1 <= 140) :
                        #Se determina el valor de point para el fututo calculo del tiempo por la pendiente
                        if  hist[index] >= 140 :
                            point = 140
                        else:
                            point = 70
                        #Estas funciones determinan los tiempos por medio de la pendiente
                        dif_shift_1 = slope(gluco_1,hist[index],delta_range[index-1], point, cp_dates[index-1], gluco_1)
                        dif_shift_2 = slope(hist[index],gluco_2,delta_range[index ], point, cp_dates[index+1], gluco_2)
                        #Se reciben deos fechas y se restan y se obtienen los segundos
                        if dif_shift_1[2] == True:
                            solv_time_1 = (datetime.fromtimestamp(dif_shift_1[0]) - cp_dates[index-1]).total_seconds()
                        #Se obtienen solo los segundos
                        else:
                            solv_time_1 = dif_shift_1[0]
                        #Se reciben deos fechas y se restan y se obtienen los segundos
                        if dif_shift_2[2] == True:
                            solv_time_2 = (cp_dates[index + 1] - datetime.fromtimestamp(dif_shift_2[0])).total_seconds()
                        #Se obtienen solo los segundos
                        else:
                            solv_time_2 = dif_shift_2[0]
                        #Se agrega el tiempo por pendiente en la lista
                        if dif_shift_1[1] == True:
                            delta_range[pos1] = solv_time_1
                        #Se agrega un cero cuando el valor del histroia esta por fuera de 70 o 180
                        else:
                            delta_range[pos1] = 0
                        #Se agrega el tiempo por pendiente en la lista
                        if dif_shift_2[1] == True:
                            delta_range[index] = solv_time_2
                        #Se agrega un cero cuando el valor del histroia esta por fuera de 70 o 180
                        else:
                            delta_range[index] = 0

        #Se eliminan los elemntos que no tienen valor
        delta_range = [0 if pd.isna(x) == True else x for x in delta_range]
        #Se calcula el tiempo arriba de 140 mg/dl
        hist_140 = list(dfh['historial'].copy())
        delta_range_140 = list(dfh["Daytime"].copy())
        cp_dates_140 = list(dfh["dates"].copy())
        #Aqui se calcula el tiempo por encima de 140
        #El codigo es el mismo que el del calculo del tiempo entre 70 y 140
        for index in range(len(hist_140)):
            if pd.isna(hist_140[index]) == False and ( hist_140[index] > 140 ) :
                #Primer elemento es mayor a 140 mg/dl
                if first_element(hist_140, hist_140[index]) == True:
                    pos2 = 0
                    if pd.isna(hist_140[index + 1]) == False:
                        pos2 = index + 1
                        gluco_2 = hist_140[pos2]
                        time_2 = delta_range_140[pos2]
                    else:
                        pos22 = index + 2
                        pos2 = index + 1
                        gluco_2 = hist_140[pos22]
                        time_2 = delta_range_140[pos2]

                    if  hist_140[index] >= 140 :
                        point = 140
                    else:
                        pass

                    dif_shift_2 = slope_140(hist_140[index],gluco_2,delta_range_140[index ], point, cp_dates_140[index+1], gluco_2)

                    if dif_shift_2[2] == True:
                        solv_time_2 = (cp_dates[index + 1] - datetime.fromtimestamp(dif_shift_2[0])).total_seconds()
                    else:
                        solv_time_2 = dif_shift_2[0]

                    if dif_shift_2[1] == True:
                        str3 = str(solv_time_2) +","+ str(hist_140[index]) +"-"+ str(gluco_2) + "-" +  str(index) + str(pos2)
                        lst_140.append(str3)
                    else:
                        str4 = str(time_2) +","+ str(hist_140[index]) +"-"+ str(gluco_2) + "-"+ str(index) + str(pos2)
                        lst_140.append(str4)

                #Ultimo elemento es mayor a 140 mg/dl
                elif last_element(hist_140, hist_140[index]) == True:
                    pos1 = 0
                    if pd.isna(hist_140[index - 1]) == False:
                        pos1 = index - 1
                        gluco_1 = hist_140[pos1]
                        time_1 = delta_range_140[pos1]
                    else:
                        pos11 = index - 2
                        pos1 = index - 1
                        gluco_1 = hist_140[pos11]
                        time_1 = delta_range_140[pos1]

                    if  hist_140[index] >= 140 :
                        point = 140
                    else:
                        pass

                    dif_shift_1 = slope_140(gluco_1,hist_140[index],delta_range_140[index-1], point, cp_dates_140[index-1], gluco_1)
                    if dif_shift_1[2] == True:
                        solv_time_1 = (datetime.fromtimestamp(dif_shift_1[0]) - cp_dates[index-1]).total_seconds()
                    else:
                        solv_time_1 = dif_shift_1[0]

                    if dif_shift_1[1] == True:
                        str1 = str(solv_time_1) +","+ str(gluco_1) + "-" + str(hist_140[index]) + "-" + str(pos1) + str(index)
                        lst_140.append(str1)
                    else:
                        str2 = str(time_1) +","+ str(gluco_1) + "-" + str(hist_140[index]) + "-" + str(pos1) + str(index)
                        lst_140.append(str2)

                #Caso donde un valor pivote se encuentra rodeado de un valor inferior o mayor al rango
                else:
                    pos1 = 0
                    pos2 = 0
                    if pd.isna(hist_140[index - 1]) == False:
                        pos1 = index - 1
                        gluco_1 = hist_140[pos1]
                        time_1 = delta_range_140[pos1]
                    else:
                        pos11 = index - 2
                        pos1 = index - 1
                        gluco_1 = hist_140[pos11]
                        time_1 = delta_range_140[pos1]
                    if pd.isna(hist_140[index + 1]) == False:
                        pos2 = index + 1
                        gluco_2 = hist_140[pos2]
                        time_2 = delta_range_140[pos2]
                    else:
                        pos22 = index + 2
                        pos2 = index + 1
                        gluco_2 = hist_140[pos22]
                        time_2 = delta_range_140[pos2]

                    if  ( gluco_2 <= 140) or ( gluco_1 <= 140) :
                        if  hist_140[index] >= 140 :
                            point = 140
                        else:
                            pass

                        dif_shift_1 = slope_140(gluco_1,hist_140[index],delta_range_140[index-1], point, cp_dates_140[index-1], gluco_1)
                        dif_shift_2 = slope_140(hist_140[index],gluco_2,delta_range_140[index ], point, cp_dates_140[index+1], gluco_2)

                        if dif_shift_1[2] == True:
                            solv_aux1 = (datetime.fromtimestamp(dif_shift_1[0]) - cp_dates[index-1]).total_seconds()
                            solv_time_1 = delta_range_140[index-1] - solv_aux1
                        else:
                            solv_time_1 = dif_shift_1[0]

                        if dif_shift_2[2] == True:
                            solv_aux2 = (cp_dates[index + 1] - datetime.fromtimestamp(dif_shift_2[0])).total_seconds()
                            solv_time_2 = delta_range_140[index ] - solv_aux2
                        else:
                            solv_time_2 = dif_shift_2[0]

                        if dif_shift_1[1] == True:
                            str1 = str(solv_time_1) +","+ str(gluco_1) + "-" + str(hist_140[index]) + "-" + str(pos1) + str(index)
                            lst_140.append(str1)
                        else:
                            str2 = str(time_1) +","+ str(gluco_1) + "-" + str(hist_140[index]) + "-" + str(pos1) + str(index)
                            lst_140.append(str2)

                        if dif_shift_2[1] == True:
                            str3 = str(solv_time_2) +","+ str(hist_140[index]) +"-"+ str(gluco_2) + "-" +  str(index) + str(pos2)
                            lst_140.append(str3)
                        else:
                            str4 = str(time_2) +","+ str(hist_140[index]) +"-"+ str(gluco_2) + "-"+ str(index) + str(pos2)
                            lst_140.append(str4)
                    else:
                        pass
            else:
                pass

        lst_140 = [0 if pd.isna(x) == True else x for x in lst_140]
        #Se eliminan los elementos repetidos del la lista
        lst_140 = list(set(lst_140))
        #Se separa el texto de los numeros
        lst_140 =[i.split(',', 1)[0] for i in lst_140]
        #Convierte de string a float
        lst_140 = np.float_(lst_140)
        #Suma todas las diferencias de tiempos
        time_140_70 = delta_range
        time_140 = lst_140
        print("Tiempo entre 70 y 140 ",time_140_70)
        print("Tiempo sobre 140 ",time_140)
        #Se suman todos los segundos de la lista
        delta_time = sum(time_140_70)
        #Se determina el tiempo total
        total_time = dfh['dates'].max() - dfh['dates'].min()
        #Se suman todos los segundos de la lista
        delta_time_max = sum(time_140)
        #Los segundos se transforman a dias, horas, minutos y segundos
        Convertedformat = timedelta(seconds=delta_time)
        Convertedformat_max = timedelta(seconds=delta_time_max)
        #Porcentaje entre 70 y 140
        por_70_140 = (Convertedformat/total_time)*100
        #Porcentaje sobre 140
        por_140 = (Convertedformat_max/total_time)*100
        pppopo = total_time*0.0673
        print(str(pppopo))
        #Se calula el area entre una constante y set de datos
        small_mean = smallest.mean()
        dlt_na_hs = dfh[dfh['historial'].notna()].copy()
        y1 = dlt_na_hs["historial"].to_numpy()
        y2 = np.array([small_mean] * len(y1))
        #https://stackoverflow.com/questions/55182377/find-the-area-between-two-curves-separately-in-numpy
        diff = y1 - y2 # calcula la diferencia
        posPart = np.maximum(diff, 0) #solo mantenga la parte positiva, establezca otros valores en cero
        posArea = str(round(np.trapz(posPart),0))

        position = i + 1
        string = "Rango #{0} del ".format(position) + str(dfh["dates"].min()) + " al "+ str(dfh["dates"].max()) + " : \n" + "Tiempo total: "+ str(total_time) +" (100 %) \n" + " ( 70 - 140 ) [ mg/dL ] : " + str(Convertedformat).split('.')[0] +" (" + str(round(por_70_140, 2)) +" %)\n" + " ( > 140 ) [ mg/dL ] : " + str(Convertedformat_max).split('.')[0] +" (" + str(round(por_140, 2)) + " %)\n" + " area : " + posArea
        aux_str.append(string)
    #Retorna una lista con los tiempos totales y area bajo la curva y la constante
    return aux_str
#Funcion grafica los datos de glucosa vs tiempo
def get_div(plot_x, plot_y, rolling_avg, df_mean, entry2, df0, smallest):
    df_mean_array = [df_mean] * len(plot_x)
    smallest_array = [smallest.mean()] * len(plot_x)
    #Se determina noche
    df = df0.copy()
    df["Daytime"] = np.nan
    df.loc[(df["dates"].dt.hour >= 18) | (df["dates"].dt.hour <= 5), 'Daytime'] = df["historial"]
    #Se grafican diversas curvas
    plot = go.Figure(data=[
    go.Scatter(x = plot_x, y = plot_y, fill = 'tonexty', mode = 'lines+markers', name = 'Historial de glucosa',),
    go.Scatter(x = plot_x, y = rolling_avg, mode = 'lines+markers', name = 'Rolling average',),
    go.Scatter(x = plot_x, y = df_mean_array, mode = 'lines', name = 'Promedio general',),
    go.Scatter(x=plot_x, y=df["Daytime"], line={'color': 'purple'},name = 'Periodo nocturno', connectgaps=False,),
    go.Scatter(x = plot_x, y = smallest_array, mode = 'lines', name = 'Promedio de los 10 menores valores de glucosa',),
    ])

    text0 = entry2 + " registros de datos historicos de glucosa y escaneo de glucosa"
    plot.update_layout(
    title={
        'text': text0,
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    xaxis_title="Tiempo ",
    yaxis_title="Glucosa [mg/dL]",
    legend_title="Datos",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple"
    ))
    plot.show()

#Se comprueba que la lista de fechas este ordenada
def lst_sorted(test_list):
    flag = False
    if(all(test_list[i] <= test_list[i + 1] for i in range(len(test_list)-1))):
        flag = True
    if (flag) :
        return flag
    else :
        return flag

#Se determina que al menos una de las fechas exista dentro del set de datos
def check_dates(date_lst, df_dates):
    flag = True
    df_dates = pd.to_datetime(df_dates).dt.date
    for element in date_lst:
        if ((element[0].date() in list(df_dates) ) == True) and ((element[1].date() in list(df_dates)) == True):
            flag = True
        else:
            flag = False
            break
    return flag

#Se verica que un elemento se el ultimo de una lista
def last_element(urlist, val):
    Flag = False
    urlist_len = len(urlist)-1
    for index, x in enumerate(urlist):
        if index == urlist_len and val == urlist[index]:
            Flag = True
    return Flag

#Se calcula la tiempo para 70 mg/dl < glucosa < 140 mg/dl
def slope(y1,y2,delta_time, point, time_sec,y_sec):
    x_sol = 0
    delta = delta_time
    #Variables de control
    flag = True
    control = True

    #Si el historial de la glucosa es verdadero se suma el valor de tiempo calculado
    #por la pendiente, caso contrario se agrega un cero  de la lista de tiempos.
    if 70 <= y_sec <= 140:
        flag = True
    else:
        flag = False

    #Cunado la diferencia deltiempo en el denominador es distinta de cero
    if delta_time !=0:
        #Se convierte la fecha ingresada a segundos
        time_sec = time.mktime(time_sec.timetuple())
        m = (y2 - y1) / delta
        #Cuando la la pendiente es cero significa que tenmos de valores de glucosa iguales
        #Por tal motivo se sumara el tiempo obtenido sin calcular la pendiente, si y solo si
        #los datos estan entre 70 y  140.
        if m == 0:
            x_sol = y_sec
            control = False
            return x_sol, flag, control

        #Se se calcula el tiempo por medio de la pendiente.
        else:
            control = True
            b = y_sec - m*time_sec
            x_sol = (point - b)/m
            return x_sol, flag, control

#Cunado la diferencia del tiempo en el denominador es  de cero
#Se sumara un cero si flag es True caso contrario se ignora el cero.
    else:
        control = False
        x_sol = 0
        return x_sol, flag, control

#Se calcula la tiempo para glucosa > 140 mg/dl
def slope_140(y1,y2,delta_time, point, time_sec,y_sec):
    x_sol = 0
    delta = delta_time
    #Variables de control
    flag = True
    val = True
    control = True

    #Si el historial de la glucosa es verdadero se suma el valor de tiempo calculado
    #por la pendiente, caso contrario se suma el tiempo  de la lista de tiempos.
    if  y_sec <= 140:
        flag = True
    else:
        flag = False

    #Cunado la diferencia deltiempo en el denominador es distinta de cero
    if delta_time !=0:
        #Se convierte la fecha ingresada a segundos
        time_sec = time.mktime(time_sec.timetuple())
        m = (y2 - y1) / delta
        #Cuando la la pendiente es cero significa que tenmos de valores de glucosa iguales
        #Por tal motivo se sumara el tiempo obtenido sin calcular la pendiente, si y solo si
        #los datos son mayores a 140.
        if m == 0:
            x_sol = y_sec
            control = False
            return x_sol, flag, control

        #Se se calcula el tiempo por medio de la pendiente.
        else:
            control = True
            b = y_sec - m*time_sec
            x_sol = (point - b)/m
            return x_sol, flag, control

#Cunado la diferencia del tiempo en el denominador es  de cero
#Se sumara un cero si flag es True caso contrario se ignora el cero.
    else:
        control = False
        x_sol = 0
        return x_sol, flag, control

#Se determina el primer elemento de una lista
def first_element(urlist, val):
    Flag = False
    urlist_len = 0
    for index, x in enumerate(urlist):
        if index == urlist_len and val == urlist[index]:
            Flag = True
    return Flag

#Esta funcion grafica los datos obtenidos
def display_data3(file_name, contain, entry2, win, num, i_array,btn_dwn, lbl_disp, button_identities, n_array, combobox_1, lbl_cp):
    contain = n_array
    size = len(contain)
    #Conservo los ultimos size elementos
    i_array = i_array[-size:]
    #Creo un dicionario que le asigna a un boton un determinado numero
    dictionary = dict(zip(contain, i_array))
    #Si los botones fueron pulsados se manera desordenada se ordenan de acuerdo a su numero de asignacion
    if greater(list(dictionary.values())) == False:
        dict0 = sorted(dictionary.items(), key=lambda x:x[1])
        dict1 = dict(dict0)
        sorted_list = list(dict1.keys())
        sorted_i = list(dict1.values())
        contain = sorted_list
        i_array = sorted_i
    #Si fueron presionados de manera ordenada se corre el codigo de manera normal
    else:
        contain = list(dictionary.keys())
        i_array = list(dictionary.values())

    #Si los botones estan ordenados de manera secuencia ejecuta
    if lst_sorted(i_array) == True:
        #Si el numero de botones coincide con la cantidad de rangos estipulados por el susuario, ejecuta
        if len(contain) == num:
            name = file_name
            #Se crea un dicionario de todos los datos del archivo
            lst = dt.read_file(name)
            times = []
            times_datetime = []
            times_datetime_aux = []
            #Se obtienen los valores de las entradas de texto
            for element in contain:
                  temp = element
                  times.append(temp)
            #Se convierten las fechas en formato datetime
            in_time  = [datetime.strptime(element, '%m-%d-%Y %I:%M %p') for element in times]
            #out_time  = [datetime.strptime(element, '%m-%d-%Y %H:%M') for element in in_time]
            times_datetime = pd.to_datetime(times, infer_datetime_format=True)
            #Determina si los elementos de la lista son distintos
            value = np.unique(in_time).size == len(in_time)
            if value == True:
                #Cada indice par se agrega una fecha inicial e impar para fecha final
                for i in range(len(times_datetime)):
                    if (i % 2) == 0:
                        t1 = datetime(times_datetime[i].year, times_datetime[i].month, times_datetime[i].day, times_datetime[i].hour, times_datetime[i].minute)
                        times_datetime_aux.append(t1)
                    else:
                        t2 = datetime(times_datetime[i].year, times_datetime[i].month, times_datetime[i].day, times_datetime[i].hour, times_datetime[i].minute)
                        times_datetime_aux.append(t2)
                #Fecha consecutiva es mayor a la fecha anterior
                if greater(in_time) == True:
                    #Corrobora que almenos una fecha exista
                    var = len(times_datetime_aux) - 1
                    date0 = lst[2]
                    gl = lst[4]
                    #En lista date0s se obtienen fechas en formato AM y PM
                    date0s = [datetime.strptime(regex_obtained_str, '%m-%d-%Y %I:%M %p')
                                        for regex_obtained_str in date0]
                    #Por defecto los indices de las columnas del dicionario son numeros, sustituyen por texto
                    lst[2] = date0s
                    lst["dates"] = lst.pop(2)
                    lst["historial"] = lst.pop(4)
                    lst["escaner"] = lst.pop(5)
                    #El dicionario se transforma en un dataframe
                    df = pd.DataFrame(lst)
                    #Columnas del archivo, son 19, estan desordenadas
                    df.columns =["Dispositivo",	"Numero de serie", "Tipo de registro", "Insulina de accion rapida no numerica",	"Insulina de accion rapida (unidades)", "Alimento no numerico",	"Carbohidratos (gramos)", "Carbohidratos (porciones)","Insulina de accion prolongada no numerica", "Insulina de accion prolongada (unidades)","Notas", "Banda de glucosa mg/dL", "Cetona mmol/L", "Insulina para la hora de la comida (unidades)","Insulina de correccion (unidades)", "Insulina de cambio de usuario (unidades)", "dates", "historial", "escaner" ]
                    #Columnas del archivo, ya ordenadas
                    df = df[["Dispositivo",	"Numero de serie", "dates", "Tipo de registro", "historial", "escaner","Insulina de accion rapida no numerica",	"Insulina de accion rapida (unidades)", "Alimento no numerico",	"Carbohidratos (gramos)", "Carbohidratos (porciones)","Insulina de accion prolongada no numerica", "Insulina de accion prolongada (unidades)","Notas", "Banda de glucosa mg/dL", "Cetona mmol/L", "Insulina para la hora de la comida (unidades)","Insulina de correccion (unidades)", "Insulina de cambio de usuario (unidades)"]]
                    #Se ordena todo el dataframe de acuerdo al orden de las fechas
                    df.sort_values(by='dates', inplace=True)
                    #En el dataframe existen 2 columnas, una con valores del escaner automaticos y manual
                    #Se pasan los valores del escaner manual al automatico
                    df['historial'] = np.where(df['historial'] == '', df['escaner'], df['historial'])
                    #Los datos de la glucosa se convierten en numeros
                    df['historial'] = df['historial'].apply(pd.to_numeric)
                    #Los datos de la columna dates se convierten en objetos de tiempo
                    df['dates'] = pd.to_datetime(df['dates'], format = "%m-%d-%Y %I:%M %p")
                    #Se crean pares ordenados de fechas finales e iniciales
                    subList = grouper(times_datetime_aux, 2)
                    #Verifico que las fchas escogidas se encentren dentro de la lista
                    #de fechas cargadas
                    if check_dates(subList, df['dates']) == True:
                        aux_df = []
                        #Se filtran los datos de acuerdo a la fecha inicial, final y codigo del lector, se almacenan en la lista aux_df
                        [aux_df.append(df[(df['dates'] >= subList[index][0]) & (df['dates'] <= subList[index][1]) & (df["Numero de serie"].str.contains(combobox_1))]) for index in range(len(subList)) ]
                        #Se concatenan todos los valores filtrados
                        result = pd.concat(aux_df)
                        #Se eliminan los resultados nulos de la columna historial
                        result = result.dropna(subset=['historial'])
                        #Chequea que el filtro no este vacio
                        if len(result['dates']) != 0:
                            #Creo una copia del filtro, para poder guardar en la computadora
                            go_csv = result.copy()
                            #Se calculan los 10 valores mas pequeuos de la columna
                            smallest = result['historial'].nsmallest(10)
                            #Tiempos entre 70 y 140, y el tiempo por encima de 140
                            sum_time = range_min_max(70, 140, result, subList, combobox_1, smallest)
                            total_lst = sum_time
                            total_display = '\n'.join(total_lst)
                            #Calcula el promedio general
                            df_mean = result['historial'].mean()
                            #Chequear y cambiar nombres, pra conservar datos csv
                            result['rolling_avg'] = result['historial'].rolling(10).mean()
                            #Elimino los valores nulos
                            result['rolling_avg'].dropna(inplace=True)
                            #Los datos de la columna se convierten en numeros
                            result['rolling_avg'] = result['rolling_avg'].apply(pd.to_numeric)
                            #Rinicio los valores de las listas cada vez que presiono el boton de generar grafico
                            contain.clear()
                            n_array.clear()
                            i_array.clear()
                            button_identities.clear()
                            #Grafico los datos de acurdo al filtro
                            plot = get_div(result['dates'], result['historial'], result['rolling_avg'], df_mean, entry2, result, smallest)
                            dwn_image = dt.load_image(r"Dependencies\dwn.png", 20)
                            button_12 = customtkinter.CTkButton(master=win.frame_right,
                                                                image=dwn_image,
                                                                text="Descargar datos",
                                                                height=32,
                                                                compound="right",
                                                                command=lambda:dt.download_csv(go_csv))
                            button_12.grid(row=7, column=0, columnspan=2, padx=20, pady=(20, 10), sticky="ew")
                            btn_dwn.append(button_12)
                            #Creo una etiqueta donde muestro informacion relevante
                            label_info_1 = customtkinter.CTkLabel(master=win.frame_left,
                                                                             text= total_display,
                                                                             height=200,
                                                                             corner_radius=6,  # <- custom corner radius
                                                                             fg_color=("white", "gray38"),  # <- custom tuple-color
                                                                             justify=tk.LEFT)
                            label_info_1.grid(column=0, row=6,  columnspan=1, sticky="nwe", padx=15, pady=15)

                            copy_image = dt.load_image(r"Dependencies\copia.png", 20)
                            button_cp = customtkinter.CTkButton(master=win.frame_left,
                                                                image=copy_image,
                                                                text="",
                                                                width =32,
                                                                height=32,
                                                                border_width=1,
                                                                compound="left",
                                                                command=lambda:copy_txt(win,total_display))
                            button_cp.place(relx=0.05, rely=0.6, anchor='w')
                            lbl_cp.append(button_cp)
                            lbl_disp.append(label_info_1)
                        else:
                            contain.clear()
                            n_array.clear()
                            i_array.clear()
                            button_identities.clear()
                            messagebox.showerror(message="No existe coincidencia entre el codigo del letor y las fechas ingresadas", title="Advertencia")
                    else:
                        n_array.clear()
                        i_array.clear()
                        contain.clear()
                        button_identities.clear()
                        messagebox.showerror(message="Al menos una de las fechas ingresadas no existe dentro de los datos, por favor corregir", title="Advertencia")
                else:
                    n_array.clear()
                    i_array.clear()
                    contain.clear()
                    button_identities.clear()
                    messagebox.showerror(message="Las fechas deben ser mayores a las fechas anteriores", title="Advertencia")
            else:
                n_array.clear()
                i_array.clear()
                contain.clear()
                button_identities.clear()
                messagebox.showerror(message="No selecione fechas repetidas", title="Advertencia")

        else:
            if len(contain) > num:
                n_array.clear()
                i_array.clear()
                contain.clear()
                button_identities.clear()
                messagebox.showerror(message="Debe volver a presionar el boton de confirmar e introducir de nuevo las fechas", title="Advertencia")
            else:
                n_array.clear()
                i_array.clear()
                contain.clear()
                button_identities.clear()
                messagebox.showerror(message="Debe ingresar todas las fechas, para ello presione el boton de confirmar de nuevo", title="Advertencia")

    else:
        n_array.clear()
        i_array.clear()
        contain.clear()
        button_identities.clear()
        messagebox.showerror(message="Selecione de manera ordenada las fechas", title="Advertencia")
