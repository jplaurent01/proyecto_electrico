from tkinter import *
from tkinter import ttk, filedialog
import numpy
import pandas as pd
import string
import sys
import plot_data
from tkinter import messagebox
import csv
import pandas as pd
from tkinter import filedialog
from tkinter import messagebox as msg
from pandastable import Table
from pathlib import Path
import customtkinter
import os

def show_data(root):
    WIDTH = 780
    HEIGHT = 520
    win = Toplevel(root)
    win.geometry(f"{WIDTH}x{HEIGHT}")
    win.configure(bg="#161E29")
    win.grid_columnconfigure(1, weight=1)
    win.grid_rowconfigure(0, weight=1)

    menubar = Menu(win)
    filemenu = Menu(menubar, tearoff=0)
    #Se destruye ventana actual
    filemenu.add_command(label="Salir", command=win.destroy)

    menubar.add_cascade(label="Menu de opciones", menu=filemenu)

    win.config(menu=menubar)

    win.frame_left = customtkinter.CTkFrame(master=win,
                                                 width=180,
                                                 corner_radius=0)
    win.frame_left.grid(row=0, column=0, sticky="nswe")

    win.frame_right = customtkinter.CTkFrame(master=win)
    win.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

    # ============ frame_left ============

    # configure grid layout (1x11)
    win.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
    win.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
    win.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
    win.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing
    # ============ frame_right ============
    # configure grid layout (3x7)
    win.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
    win.frame_right.rowconfigure(7, weight=10)
    win.frame_right.columnconfigure((0, 1), weight=1)
    win.frame_right.columnconfigure(2, weight=0)

    file_name = ''
	# Creating label widgets
    message_label2 = customtkinter.CTkLabel(master=win.frame_left,
												 text="Convertir archivo a XLS",
												 font=("Roboto Medium", -16))
    message_label2.grid(row=1, column=0, pady=10, padx=10)

	# Buttons
    convert_button = customtkinter.CTkButton(master=win.frame_left,
												text="Convertir a XLS",
												command=lambda:convert_csv_to_xls(win))
    convert_button.grid(row=2, column=0, pady=10, padx=20)

    display_button = customtkinter.CTkButton(master=win.frame_left,
												text="Desplegar XLS",
												command=lambda:display_xls_file(win))
    display_button.grid(row=3, column=0, pady=10, padx=20)


def convert_csv_to_xls(win):
	try:
		frame_leftile_name = filedialog.askopenfilename(initialdir = '/Desktop',
													title = 'Select a CSV file',
													filetypes = (('csv file','*.csv'),
																('csv file','*.csv')))

		df = pd.read_csv(frame_leftile_name)

		# Next - Pandas DF to Excel file on disk
		if(len(df) == 0):
			msg.showinfo('No hay filas seleccionadas', 'CSV no tiene filas')
		else:
			downloads_path = str(Path.home() / "Downloads")
			file_name_string0 = str(os.path.basename(frame_leftile_name))
			file_name_string1 = file_name_string0.split(".csv")
			file_name_string2 = file_name_string1[0]
			fin_path = downloads_path + "/ csvtoxls_"+file_name_string2+".xls"
			# saves in the current directory
			with pd.ExcelWriter(fin_path) as writer:
					df.to_excel(writer,'GFGSheet')
					writer.save()
					msg.showinfo('Archivo Excel creado', 'Archivo Excel creado')

	except FileNotFoundError as e:
			msg.showerror('Error abriendo el archivo', e)

def display_xls_file(win):
	try:
		frame_leftile_name = filedialog.askopenfilename(initialdir = '/Desktop',
													title = 'Select a excel file',
													filetypes = (('excel file','*.xls'),
																('excel file','*.xls')))
		df = pd.read_excel(frame_leftile_name)
		if (len(df)== 0):
			msg.showinfo('No hay registros', 'No hay registros')
		else:
			pass

		# Now display the DF in 'Table' object
		# under'pandastable' module
		frame_left2 = Frame(win.frame_right, height=400, width=500)
		frame_left2.grid(row=0, column=0)
		table = Table(frame_left2, dataframe=df,read_only=True, fill='x',expand=True)
		#table.redraw()
		table.show()

	except FileNotFoundError as e:
		msg.showerror('Error abriendo el archivo',e)
