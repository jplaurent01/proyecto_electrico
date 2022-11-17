import csv
import sys
import os
import data as dt
import PIL
from PIL import ImageTk
from PIL import Image
import tkinter
import tkinter.messagebox
import customtkinter
import plot_data
import display_data_ex
import webbrowser

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("Procesador de datos glucosa")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Menu de opciones",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Agregar datos",
                                                command=self.button_event)
        self.button_1.grid(row=2, column=0, pady=10, padx=20)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Pre-visualizar datos",
                                                command=self.button_event_disp)
        self.button_2.grid(row=3, column=0, pady=10, padx=20)


        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Modo de apariencia:")
        self.label_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark", "System"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)


        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

        image = Image.open(r"Dependencies\freestyle.png").resize((500, 100))
        self.bg_image = ImageTk.PhotoImage(image)

        self.image_label_f = tkinter.Label(master=self.frame_info, image=self.bg_image, justify=tkinter.CENTER)
        self.image_label_f.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nwe")
        # ============ frame_info ============

        # configure grid layout (1x1)
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)
        txt = "Información de contacto:\n" + "Correo : josepablo.laurent@gmail.com\n" + "Teléfono : 88060043"
        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_right,
                                                   text= txt ,
                                                   height=250,
                                                   corner_radius=6,  # <- custom corner radius
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.LEFT)
        self.label_info_1.grid(column=0, row=5, sticky="nwe", padx=15, pady=15)

        self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Instrucciones de uso",
                                                command=self.open_url)
        self.button_3.grid(row=4, column=0, pady=10, padx=20)

        #copy_image = dt.load_image(r"Dependencies\copy.png", 20)
        #copy_image = Image.open(r"Dependencies\copia.png").resize((25, 25))
        #self.copy_image = ImageTk.PhotoImage(copy_image)
        #button_cp = tkinter.Button(self, text = '', image = self.copy_image,command=lambda:self.copy_txt(txt),borderwidth=0)
        copy_image = dt.load_image(r"Dependencies\copia.png", 20)
        button_cp = customtkinter.CTkButton(master=self.frame_right,
                                            image=copy_image,
                                            text="",
                                            width =32,
                                            height=32,
                                            border_width=1,
                                            compound="left",
                                            command=lambda:self.copy_txt(txt))
        button_cp.place(relx=0.1, rely=0.46, anchor='e')
        # set default values
        self.optionmenu_1.set("Dark")

    #Se copia texto
    def copy_txt(self, txt):
        #txt = "Información de contacto:\n" + "Correo : josepablo.laurent@gmail.com\n" + "Teléfono : 88060043"
        self.clipboard_clear()
        self.clipboard_append(txt)
        tkinter.messagebox.showinfo(title="", message="El texto ha sido copiado")

    #Grafica los datos
    def button_event(self):
        plot_data.win_disp(self)

#Muestra los datos que se van a graficar, en bruto
    def button_event_disp(self):
        display_data_ex.show_data(self)

#Abre url
    def open_url(self):
        try:
            url = "https://youtu.be/gG0-bhTEabE"
            webbrowser.open_new_tab(url)
        except:
            essagebox.showerror(message="Verifique su conexión a internet", title="Advertencia")


    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
