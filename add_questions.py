from tkinter import *
from tkinter import ttk, filedialog, font
import string
import sys
import play
from tkinter import messagebox
import csv
from tkinter import filedialog
from tkinter import messagebox as msg
import customtkinter
import os
import os.path


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
    # ============ Menu ventana principal ============
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

    #Desired_font = font.Font( family = "Roboto Medium", size = 16, weight = "bold")
    #sf= tkFont.Font(family='Helvetica', size=36, weight='bold')
    list_of_lists = []

    check_file = os.path.isfile(r'Dependencies\preguntas.txt')
    print(check_file)
    if check_file == True:
        with open(r'Dependencies\preguntas.txt', 'r') as file:
            fl = file.readlines()
            list_of_lists = [line for line in fl]
            print(list_of_lists)

        if len(list_of_lists) == 0:
            var = ""
        else:
            var = StringVar()
            var.set(list_of_lists)
    else:
        var = ""


    lstbox = Listbox(win.frame_right, listvariable=var, selectmode=MULTIPLE, width=67, height=20, bg = "#3E3F40", fg= "#D1D6DA")
    #lstbox2.grid(column=0, row=0, pady=1, padx=5)
    #lstbox.pack(side = LEFT, fill = BOTH)

    scrollbar = Scrollbar(win.frame_right)
    #scrollbar.pack(side = RIGHT, fill = 'y')
    lstbox.config(yscrollcommand = scrollbar.set)

    scrollbar.config(command = lstbox.yview)

    scrollbar2 = Scrollbar(win.frame_right,  orient = HORIZONTAL)
    #scrollbar2.pack(side = BOTTOM, fill = 'x')
    lstbox.config(xscrollcommand = scrollbar2.set)

    scrollbar2.config(command = lstbox.xview)

    scrollbar2.pack(side = BOTTOM, fill = 'x')
    lstbox.pack(side = LEFT, fill = BOTH)
    scrollbar.pack(side = RIGHT, fill = 'y')

    entry2 = customtkinter.CTkEntry(master=win.frame_left,
                                            width=90,
                                            placeholder_text="Ingrese una pregunta ...")
    entry2.grid(row=0, column=0, columnspan=1, pady=20, padx=20, sticky="we")
    #Se agregan entradas de txto
    label_1 = customtkinter.CTkLabel(master=win.frame_left,
                                                 text="Opciones de la pregunta",
                                                 font=("Roboto Medium", 16))
    label_1.grid(row=1, column=0, columnspan=1, pady=10, padx=10)

    entry_A = customtkinter.CTkEntry(master=win.frame_left,
                                            width=90,
                                            placeholder_text="A")
    entry_A.grid(row=2, column=0, columnspan=1, pady=20, padx=20, sticky="we")

    entry_B = customtkinter.CTkEntry(master=win.frame_left,
                                            width=90,
                                            placeholder_text="B")
    entry_B.grid(row=3, column=0, columnspan=1, pady=20, padx=20, sticky="we")

    entry_C = customtkinter.CTkEntry(master=win.frame_left,
                                            width=90,
                                            placeholder_text="C")
    entry_C.grid(row=4, column=0, columnspan=1, pady=20, padx=20, sticky="we")

    entry_D = customtkinter.CTkEntry(master=win.frame_left,
                                            width=90,
                                            placeholder_text="D")
    entry_D.grid(row=5, column=0, columnspan=1, pady=20, padx=20, sticky="we")


    id_list = ["A","B","C","D"]
    combobox_1 = customtkinter.CTkComboBox(master=win.frame_left,
                                                values=id_list)
    combobox_1.grid(row=6, column=0, columnspan=1, pady=10, padx=20, sticky="we")
    combobox_1.set("Opcion correcta")

    dif_list = ["Facil", "Intermedio", "Dificil"]
    combobox_2 = customtkinter.CTkComboBox(master=win.frame_left,
                                                values=dif_list)
    combobox_2.grid(row=7, column=0, columnspan=1, pady=10, padx=20, sticky="we")
    combobox_2.set("Dificultad")

    # ============ Menu clic derecho ============
    m = Menu(win, tearoff = 0)
    m.add_command(label ="Eliminar", command=lambda:delete_item(lstbox))

    def do_popup(event):
        try:
            m.tk_popup(event.x_root, event.y_root)
        finally:
            m.grab_release()

    win.bind("<Button-3>", do_popup)

    btn = customtkinter.CTkButton(master=win.frame_left,
                                        text="Confirmar",
                                        width=30,
                                        height=25,
                                        #compound="right",
                                        command=lambda:question(entry2.get(), entry_A.get(), entry_B.get(), entry_C.get(), entry_D.get(), combobox_1.get().strip(), combobox_2.get().strip(),lstbox)
                                        )
    btn.grid(row=0, column=8, columnspan=1, padx=20, pady=(20, 10), sticky="ew")


def delete_item(lstbox):
    sel = lstbox.curselection()
    print(sel)
    type(sel)
    if len(sel) !=0:
        for index in sel[::-1]:
            lstbox.delete(index)
            with open(r'Dependencies\preguntas.txt', "r+") as f:
                lines = f.readlines()
                del lines[index]  # use linenum - 1 if linenum starts from 1
                f.seek(0)
                f.truncate()
                f.writelines(lines)

    else:
        messagebox.showerror(message="Debe seleccionar un elemento de la lista", title="Advertencia")



def question(pregunta, entry_A, entry_B, entry_C, entry_D, correcta, dificultad, lstbox):
    if len(pregunta) == 0 or len(entry_A) == 0 or len(entry_B) == 0 or len(entry_C) == 0 or len(entry_D) == 0 or len(correcta) == 0 or len(dificultad) == 0 :
        messagebox.showerror(message="Debe llenar todos los espacios", title="Advertencia")

    elif correcta != "A" and correcta !="B" and correcta != "C" and correcta !="D":
        messagebox.showerror(message="Debe ingresar la letra A, B, C o D", title="Advertencia")

    elif dificultad != "Facil" and dificultad != "Intermedio" and dificultad != "Dificil":
        messagebox.showerror(message="Debe ingresar Facil, Intermedio o Dificil", title="Advertencia")

    elif "," in pregunta  or "," in entry_A  or "," in entry_B  or "," in entry_C  or "," in entry_D:
        messagebox.showerror(message="No agregue comas ", title="Advertencia")

    elif len(pregunta) > 78:
        var = str(len(pregunta))
        msm = "La extensión máxima de una pregunta es de 78 caracteres y esta cuenta con: " + var
        messagebox.showerror(message=msm, title="Advertencia")

    elif len(entry_A) > 36:
        var = str(len(entry_A))
        msm = "La extensión máxima de una opcion es de 36 caracteres y esta cuenta con: " + var
        messagebox.showerror(message=msm, title="Advertencia")
    elif len(entry_B) > 36 :
        var = str(len(entry_B))
        msm = "La extensión máxima de una opcion es de 36 caracteres y esta cuenta con: " + var
        messagebox.showerror(message=msm, title="Advertencia")
    elif len(entry_C) > 36:
        var = str(len(entry_C))
        msm = "La extensión máxima de una opcion es de 36 caracteres y esta cuenta con: " + var
        messagebox.showerror(message=msm, title="Advertencia")

    elif len(entry_D) > 36 :
        var = str(len(entry_D))
        msm = "La extensión máxima de una opcion es de 36 caracteres y esta cuenta con: " + var
        messagebox.showerror(message=msm, title="Advertencia")

    else:
        string = str(pregunta + "," + entry_A + "," + entry_B + "," + entry_C + "," + entry_D + "," + correcta + "," + dificultad)
        lstbox.insert("end", string)
        string2 = string + "\n"
        with open(r"Dependencies\preguntas.txt", 'a') as file:
            file.write(string2)
