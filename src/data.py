import csv
import sys
import os
from collections import defaultdict
import numpy
import PIL
from PIL import ImageTk
from PIL import Image
from tkinter.filedialog import asksaveasfilename
import pandas as pd
from tkinter import messagebox
import numpy as np

#PATH = os.path.dirname(os.path.realpath(__file__))

def load_image(path, image_size):
        """ load rectangular image with path relative to PATH """
        #return ImageTk.PhotoImage(Image.open(PATH + path).resize((image_size, image_size)))
        return ImageTk.PhotoImage(Image.open(path).resize((image_size, image_size)))
def read_file(name):
    columns = defaultdict(list)
    word =  "#"
    #with open(r"Z:\ESD Testing Reports\NAMES.TXT", 'r', encoding="ISO-8859-1") as f:
    with open(name, 'r', encoding="ISO-8859-1") as f:
        data = f.readlines()
        final_data_set = data[2:]
        reader = csv.reader(final_data_set, delimiter=',')
        for row in reader:
            for i in range(len(row)):
                columns[i].append(row[i])

    columns = dict(columns)
    return columns

def download_csv(df):
    filename = asksaveasfilename(filetype=[('CSV files', '*.csv')])
    if filename:
        try:
            string = "Datos de glucosa,Generado el," + " " +",Generado por,"+ " "
            df['dates'] = df['dates'].dt.strftime("%m-%d-%Y %I:%M %p")
            column_list = df.columns
            index_array = [[string, column_list[0]]] + [['', f'{column_list[i]}'] for i in np.arange(1,len(column_list))]
            idx = pd.MultiIndex.from_tuples(index_array)
            df.columns = idx
            #df.to_csv(filename, header=False, index=False)
            df.to_csv(filename, index=False)
            messagebox.showinfo(message="Se descargo archivo de manera exitosa", title="Informacion")
        except :
            messagebox.showerror(message="Debe volver a introducir las fechas y presionar el boton de generar grafico para descargar los datos", title="Advertencia")
