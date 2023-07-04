import csv
import sys
import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
from PIL import Image, ImageTk
import play
import add_questions
import webbrowser
from pygame import mixer
import customtkinter

customtkinter.set_appearance_mode("dark")
count = 0

class App(customtkinter.CTk):
    width = 700
    height = 650

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.title("Quien quiere ser millonario menu")
            self.geometry(f"{self.width}x{self.height}")
            self.resizable(False, False)

            mixer.init()
            self.sound_0 = mixer.Sound(r"Dependencies\intro.ogg")
            self.son_0 = self.sound_0.play()

            # Open and identify the image
            self.image = Image.open("Dependencies/bg_wwm.PNG")

            # Create a copy of the image and store in variable
            self.img_copy = self.image.copy()

            # Define image using PhotoImage function
            self.background_image = ImageTk.PhotoImage(self.image)

            # Create and display the label with the image
            self.background = Label(self, image=self.background_image)
            self.background.place(x=0, y=0, relwidth=1, relheight=1)

            self.button_1 = customtkinter.CTkButton(master=self,
                                                    text="Jugar",
                                                    border_width=0,
                                                    command=self.button_event)
            self.button_1.place(relx=0.5, rely=0.59, anchor=CENTER)

            self.button_2 = customtkinter.CTkButton(master=self,
                                                    text="Agregar preguntas",
                                                    border_width=0,
                                                    command=self.button_event_disp)
            self.button_2.place(relx=0.5, rely=0.65, anchor=CENTER)

            self.button_3 = customtkinter.CTkButton(master=self,
                                                    text="Instrucciones de uso",
                                                    border_width=0,
                                                    command=self.open_url)
            self.button_3.place(relx=0.5, rely=0.71, anchor=CENTER)

            self.protocol("WM_DELETE_WINDOW", self.on_closing)

        except Exception as e:
            text_0 = str(e)
            messagebox.showerror(message=text_0, title="Advertencia")

    def on_closing(self):
        if messagebox.askokcancel("Cerrar", "Desea salir del juego?"):
            try:
                self.son_0.pause()
                #self.quit
                self.destroy()
                #self.quit
                #sys.exit()
            except Exception as e:
                text_0 = str(e)
                messagebox.showerror(message=text_0, title="Advertencia")

    def button_event_disp(self):
        add_questions.show_data(self)

    def button_event(self):
        global count
        count = count + 1
        play.callback(self, count)

    def open_url(self):
        try:
            url = "https://youtu.be/gG0-bhTEabE"
            webbrowser.open_new_tab(url)
        except webbrowser.Error:
            messagebox.showerror(message="Verifique su conexión a internet", title="Advertencia")


if __name__ == "__main__":
    app = App()
    app.mainloop()








"""
import csv
import sys
import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
import customtkinter
from PIL import Image, ImageTk
import customtkinter
import play
import add_questions
import webbrowser
from pygame import mixer
import customtkinter
from PIL import Image
import os

customtkinter.set_appearance_mode("dark")
count = 0


class App(customtkinter.CTk):
    width = 700
    height = 650

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.title("Quien quiere ser millonario menu")
            self.geometry(f"{self.width}x{self.height}")
            self.resizable(False, False)

            mixer.init()
            self.protocol("WM_DELETE_WINDOW", self.on_closing)
            self.sound_0 = mixer.Sound(r"Dependencies\intro.ogg")
            self.son_0 = self.sound_0.play()

            # Open and identify the image
            self.image = Image.open("Dependencies/bg_wwm.PNG")

            # Create a copy of the image and store in variable
            self.img_copy = self.image.copy()

            # Define image using PhotoImage function
            self.background_image = ImageTk.PhotoImage(self.image)

            # Create and display the label with the image
            self.background = Label(self, image=self.background_image)
            #self.background.pack(fill=BOTH,expand=YES)
            self.background.place(x=0, y=0, relwidth = 1, relheight=1)

            #self.button_2 = Button(self, text="BOTTOM")
            self.button_1 = customtkinter.CTkButton(master=self,
                                                    text="Jugar",
                                                    border_width=0,
                                                    command=self.button_event)
            #self.button_1.pack(pady=30)
            self.button_1.place(relx=0.5,rely=0.59, anchor=CENTER)

            self.button_2 = customtkinter.CTkButton(master=self,
                                                    text="Agregar preguntas",
                                                    border_width=0,
                                                    command=self.button_event_disp)
            self.button_2.place(relx=0.5,rely=0.65, anchor=CENTER)

            self.button_3 = customtkinter.CTkButton(master=self,
                                                    text="Instrucciones de uso",
                                                    border_width=0,
                                                    command=self.open_url)
            self.button_3.place(relx=0.5,rely=0.71, anchor=CENTER)

        except Exception as e :
            text_0 = str(e)
            messagebox.showerror(message=text_0, title="Advertencia")



    def on_closing(self, event=0):
        if messagebox.askokcancel("Cerrar", "Dese salir del juego?"):
            try:
                self.son_0.pause()
                self.destroy()
                sys.exit()
            except Exception as e :
                text_0 = str(e)
                messagebox.showerror(message=text_0, title="Advertencia")
                sys.exit()


    def button_event_disp(self):
        add_questions.show_data(self)

    #Grafica los datos
    def button_event(self):
        global count
        count = count + 1
        play.callback(self, count)


#Abre url
    def open_url(self):
        try:
            url = "https://youtu.be/gG0-bhTEabE"
            webbrowser.open_new_tab(url)
        except webbrowser.Error:
            tkinter.messagebox.showerror(message="Verifique su conexión a internet", title="Advertencia")


if __name__ == "__main__":
    app = App()
    app.mainloop()
"""
