import tkinter as tk
from PIL import Image, ImageTk
from collections import defaultdict
import csv
from tkinter import *
import PIL.Image
from tkinter import messagebox
from pygame import mixer
import sys
import copy
from random import shuffle
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
import os



#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
count_50_50 = 0
count_public = 0
count_chance = 0

class Application(Toplevel):

    def __init__(self, questions, count, master = None,*args, **kwargs):
        #tk.Tk.__init__(self, *args, **kwargs)
        super().__init__(master = master, *args, **kwargs)
        try:
            self.id_after = None
            self.protocol("WM_DELETE_WINDOW", self.on_closing)
            mixer.init()
            self.sound_1 = mixer.Sound(r"Dependencies\bg_music1.ogg")
            self.son_1 = self.sound_1.play(-1)
            if count == 0:
                pass
            else:
                global count_50_50, count_public, count_chance
                count_50_50 = 0
                count_public = 0
                count_chance = 0
            WIDTH = 1280
            HEIGHT = 720
            self.title("Juego")
            self.geometry(f"{WIDTH}x{HEIGHT}")
            self.resizable(width=False, height=False)

            self.grid_columnconfigure(0, weight=1)
            self.grid_columnconfigure(1, weight=1)
            self.grid_rowconfigure(0, weight=1)
            self.grid_rowconfigure(1, weight=1)
            self.grid_rowconfigure(2, weight=1)

            #bg = tk.PhotoImage(file = r"quien quiere ser millonario\Dependencies\background.jpg")
            self.image = PIL.Image.open(r"Dependencies\background.jpg")
            self.background_image = ImageTk.PhotoImage(self.image)
            # Show image using label
            self.label1 = tk.Label( self, image = self.background_image)
            self.label1.place(x = 0, y = 0)

            self.frm = tk.Frame(self, bg="#1B2732")
            self.frm.place(relx = 0.07, rely = 0.15)


            self.image_logo = PIL.Image.open(r"Dependencies/LOGO-modified.png")

            # Resize the image using resize() method
            self.resize_image = self.image_logo.resize((250, 250))

            self.img = ImageTk.PhotoImage(self.resize_image)

            self.label_bg = tk.Label(self, image=self.img, bg="#1B2732", highlightthickness = 0, bd = 0)
            self.label_bg.image = self.img
            self.label_bg.place(relx = 0.4, rely = 0.1)

            self.label_trp = tk.Label(self, text= "", bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
            self.label_trp.place(relx = 0.15, rely = 0.1)

            self.puntuation = ["$ 100", "$ 200", "$ 300", "$ 500", "$ 1000", "$ 2000", "$ 4000", "$ 8000", "$ 160 00", "$ 32 000", "$ 64 000", "$ 125 000", "$ 250 000", "$ 500 000", "$ 1000 000"]
            self.puntuation = iter(self.puntuation)

            self.rst = self.oder_lst(questions)
            #self.questions = iter(questions)
            self.questions = iter(self.rst)

            self.img_1 = PhotoImage(file=r"Dependencies\50-50.png")
            self.logo_img_1= Button(self, command=lambda:self.clicked_50_50(self.logo_img_1), image = self.img_1, bg="#1B2732", activebackground="#1B2732", highlightthickness = 0, bd = 0)
            self.logo_img_1.image = self.img_1
            self.logo_img_1.place(relx = 0.65, rely = 0.1)

            self.img_2 = PhotoImage(file=r"Dependencies\asktheaudience.png")
            self.logo_img_2= Button(self, command=lambda:self.clicked_public(self.logo_img_2), image = self.img_2, bg="#1B2732", activebackground="#1B2732", highlightthickness = 0, bd = 0)
            self.logo_img_2.image = self.img_2
            self.logo_img_2.place(relx = 0.71, rely = 0.1)

            self.img_3 = PhotoImage(file=r"Dependencies\switcharoo.png")
            self.logo_img_3= Button(self, command=lambda:self.clicked_chance(self.logo_img_3), image = self.img_3, bg="#1B2732", activebackground="#1B2732", highlightthickness = 0, bd = 0)
            self.logo_img_3.image = self.img_3
            self.logo_img_3.place(relx = 0.77, rely = 0.1)

            self.question_label = tk.Label(self, text= "", bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
            self.question_label.place(relx = 0.32, rely = 0.59)


            self.label_A = tk.Label(self, text= "", bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
            self.label_A.place(relx = 0.25, rely = 0.765)

            self.label_B = tk.Label(self, text= "", bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
            self.label_B.place(relx = 0.25, rely = 0.865)

            self.label_C = tk.Label(self, text= "", bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
            self.label_C.place(relx = 0.57, rely = 0.765)

            self.label_D = tk.Label(self, text= "", bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
            self.label_D.place(relx = 0.57, rely = 0.865)


            self.opt_A = tk.Label(self, text= "A:", bg="#1B2732", fg='#ECEEF1', font=("Arial", 17))
            self.opt_A.place(relx = 0.18, rely = 0.766)

            self.opt_B = tk.Label(self, text= "B:", bg="#1B2732", fg='#ECEEF1', font=("Arial", 17))
            self.opt_B.place(relx = 0.18, rely = 0.866)

            self.opt_C = tk.Label(self, text= "C:", bg="#1B2732", fg='#ECEEF1', font=("Arial", 17))
            self.opt_C.place(relx = 0.54, rely = 0.766)

            self.opt_D = tk.Label(self, text= "D:", bg="#1B2732", fg='#ECEEF1', font=("Arial", 17))
            self.opt_D.place(relx = 0.54, rely = 0.866)


            self.buttons = []
            #self.radbuttons = []
            for y in range(1):

                btn_A = tk.Button(self,text ="123",font=("Arial", 15), bg="#1B2732", activebackground="#1B2732", highlightthickness = 0, bd = 0, height= 1, width=30)
                btn_A.place(relx = 0.20, rely = 0.766)

                btn_B = tk.Button(self, text="123",font=("Arial", 15), bg="#1B2732", activebackground="#1B2732", highlightthickness = 0, bd = 0 , height= 1, width=30)
                btn_B.place(relx = 0.20, rely = 0.866)

                btn_C = tk.Button(self, text="123",font=("Arial", 15), bg="#1B2732", activebackground="#1B2732", highlightthickness = 0, bd = 0 , height= 1, width=30)
                btn_C.place(relx = 0.56, rely = 0.766)

                btn_D = tk.Button(self, text = "123",font=("Arial", 15), bg="#1B2732", fg='#EDEFF1',activebackground="#1B2732", highlightthickness = 0, bd = 0 , height= 1, width=30)
                btn_D.place(relx = 0.56, rely = 0.866)
                self.buttons.append([btn_A, btn_B, btn_C, btn_D])


            self.buttons = sum(self.buttons, [])

            self.buttons[0].bind("<Enter>", self.change_1)
            self.buttons[0].bind("<Leave>", self.change_back_1)

            self.buttons[1].bind("<Enter>", self.change_2)
            self.buttons[1].bind("<Leave>", self.change_back_2)

            self.buttons[2].bind("<Enter>", self.change_3)
            self.buttons[2].bind("<Leave>", self.change_back_3)

            self.buttons[3].bind("<Enter>", self.change_4)
            self.buttons[3].bind("<Leave>", self.change_back_4)
            self.goto_next_question()

        except Exception as e :
            text_0 = str(e)
            messagebox.showerror(message=text_0, title="Advertencia")
            if self.son_1.get_busy() == True:
                self.son_1.pause()

                if self.id_after is not None:
                    self.after_cancel(self.id_after)  # Cancel the scheduled after event
                    self.id_after = None
                else:
                    pass
                self.destroy()
            else:

                if self.id_after is not None:
                    self.after_cancel(self.id_after)  # Cancel the scheduled after event
                    self.id_after = None
                else:
                    pass
                self.destroy()

    def goto_next_question(self):

        self.opt_A.config(bg="#1B2732")
        self.opt_B.config(bg="#1B2732")
        self.opt_C.config(bg="#1B2732")
        self.opt_D.config(bg="#1B2732")

        self.label_A.config(image='', bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
        self.label_B.config(image='', bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
        self.label_C.config(image='', bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
        self.label_D.config(image='', bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))


        path = 'Dependencies/plot.png'
        check_file = os.path.isfile(path)
        if check_file == True:
            self.frm.destroy()
            os.remove(path)
        else:
            pass
        #global count_chance
        global question, tuple_btn_qst, count_50_50

        if count_50_50 == 1:

            self.label_A.config(image='', bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
            self.buttons[0].configure(bg="#1B2732")
            self.label_A.place(relx = 0.25, rely = 0.765)

            self.label_B.config(image='', bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
            self.buttons[1].configure(bg="#1B2732")
            self.label_B.place(relx = 0.25, rely = 0.865)

            self.label_C.config(image='', bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
            self.buttons[2].configure(bg="#1B2732")
            self.label_C.place(relx = 0.57, rely = 0.765)

            self.label_D.config(image='', bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
            self.buttons[3].configure(bg="#1B2732")
            self.label_D.place(relx = 0.57, rely = 0.865)

        else:
            pass

        question = next(self.questions, None)
        puntuation = next(self.puntuation, None)

        if question is None:
            self.son_1.pause()
            if self.id_after is not None:
                self.after_cancel(self.id_after)  # Cancel the scheduled after event
                self.id_after = None
            else:
                pass
            self.destroy()
            return

        shuffle(question["answers"])


        if len(question["text"]) < 20:
            self.question_label.place(relx = 0.42, rely = 0.59)

        elif len(question["text"]) >= 20 and len(question["text"]) <=45:
            self.question_label.place(relx = 0.35, rely = 0.59)

        elif len(question["text"]) > 45 and len(question["text"]) < 54:
            self.question_label.configure(font=("Arial", 24))
            self.question_label.place(relx = 0.22, rely = 0.59)

        elif len(question["text"]) >= 54 and len(question["text"])<= 63:
            self.question_label.configure(font=("Arial", 22))
            self.question_label.place(relx = 0.20, rely = 0.59)

        elif len(question["text"]) > 63 and len(question["text"])<= 72:
            self.question_label.configure(font=("Arial", 19))
            self.question_label.place(relx = 0.17, rely = 0.59)

        elif len(question["text"]) > 72:
            self.question_label.configure(font=("Arial", 16))
            self.question_label.place(relx = 0.2, rely = 0.59)
        else:
            pass



        self.question_label["text"] = question["text"]
        self.label_trp["text"] = puntuation

        index = 0
        #Acomodo la lista de botones para que la respuesta correcta este al final de la lista.
        for element in question["answers"]:
            if "True" in str(element):
                index = question["answers"].index(element)
                break

        element = question["answers"].pop(index)
        new_index = len(question["answers"])
        question["answers"].insert(new_index, element)


        self.copy_list = copy.copy(self.buttons)
        shuffle(self.copy_list)
        tuple_btn_qst = zip(self.copy_list, question["answers"])

        #for button, answer in zip(self.copy_list, question["answers"]):
        for button, answer in tuple_btn_qst:
            button["text"] = answer["text"]
            my_text = button.cget('text')
            button["bg"] = "#1B2732"
            button["fg"]="#EDEFF1"

            if answer["isCorrect"]:
                var = tk.IntVar()
                button["command"] = lambda button=button: [self.on_press(button), var.set(1)]

                button.wait_variable(var)
                print(self.id_after)
                self.id_after = self.after(500, self.goto_next_question)
                #self.after_cancel(self.id_after)
                print(self.id_after)
            else:
                button["command"] = lambda button=button: self.answered_wrong(button)

    def oder_lst(self, questions):

        self.easy = []
        self.mid = []
        self.hard = []

        for sub in questions:
            if ' Facil' in sub["level"] :
                self.easy.append(sub)
            elif ' Intermedio' in sub["level"]:
                self.mid.append(sub)
            else:
                self.hard.append(sub)
        shuffle(self.easy)
        shuffle(self.mid)
        shuffle(self.hard)

        self.questions2 = [self.easy, self.mid, self.hard]
        self.questions2 = sum(self.questions2, [])
        size = len(self.questions2)
        if size > 15:
            size2 = size - 15
            self.questions2 = self.questions2[:-size2]

        else:
            pass

        return self.questions2

    def on_press(self, button):

        sound_2 = mixer.Sound(r"Dependencies\true1.ogg")
        son_2 = sound_2.play()
        button.configure(bg= "#81CE5F")
        self.image = PIL.Image.open(r"Dependencies\correct.png")
        self.resize_image = self.image.resize((424, 60))
        self.pic = ImageTk.PhotoImage(self.resize_image)

        x, y = button.winfo_rootx(), button.winfo_rooty()
        if (x >= 290 and x <= 334)  and y == 664:
            self.label_B.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
            self.label_B.image = self.pic
            self.label_B.place(relx = 0.156, rely = 0.854)
            self.opt_B.config( bg="#81CE5F")

        elif (x >= 751 and x <= 795)  and y ==592:
            self.label_C.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
            self.label_C.image = self.pic
            self.label_C.place(relx = 0.517, rely = 0.755)
            self.opt_C.config( bg="#81CE5F")

        elif (x >= 290 and x <= 334 )  and y ==592:
            self.label_A.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
            self.label_A.image = self.pic
            self.label_A.place(relx = 0.156, rely = 0.756)
            self.opt_A.config( bg="#81CE5F")

        elif (x >= 751 and x <= 795)  and y == 664:
            self.label_D.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
            self.label_D.image = self.pic
            self.label_D.place(relx = 0.517, rely = 0.855)
            self.opt_D.config( bg="#81CE5F")
        else:
            print("No cubre")




    def change_1(self,e):
        self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
        self.resize_image = self.image.resize((424, 60))
        self.pic = ImageTk.PhotoImage(self.resize_image)
        self.label_A.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
        self.label_A.image = self.pic
        self.buttons[0].configure(bg="#D78000")
        self.label_A.place(relx = 0.156, rely = 0.756)
        self.opt_A.configure(bg="#D78000")

    def change_back_1(self,e):

        self.label_A.config(image='', bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
        self.buttons[0].configure(bg="#1B2732")
        self.label_A.place(relx = 0.25, rely = 0.765)
        self.opt_A.configure(bg="#1B2732")

    def change_2(self,e):
        self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
        self.resize_image = self.image.resize((424, 60))
        self.pic = ImageTk.PhotoImage(self.resize_image)
        self.label_B.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
        self.label_B.image = self.pic
        self.buttons[1].configure(bg="#D78000")
        self.label_B.place(relx = 0.156, rely = 0.854)
        self.opt_B.configure(bg="#D78000")

    def change_back_2(self,e):

        self.label_B.config(image='', bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
        self.buttons[1].configure(bg="#1B2732")
        self.label_B.place(relx = 0.25, rely = 0.865)
        self.opt_B.configure(bg="#1B2732")

    def change_3(self,e):
        self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
        self.resize_image = self.image.resize((424, 60))
        self.pic = ImageTk.PhotoImage(self.resize_image)
        self.label_C.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
        self.label_C.image = self.pic
        self.buttons[2].configure(bg="#D78000")
        self.label_C.place(relx = 0.517, rely = 0.755)
        self.opt_C.configure(bg="#D78000")


    def change_back_3(self,e):

        self.label_C.config(image='', bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
        self.buttons[2].configure(bg="#1B2732")
        self.label_C.place(relx = 0.57, rely = 0.765)
        self.opt_C.configure(bg="#1B2732")

    def change_4(self,e):
        self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
        self.resize_image = self.image.resize((424, 60))
        self.pic = ImageTk.PhotoImage(self.resize_image)
        self.label_D.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
        self.label_D.image = self.pic
        self.buttons[3].configure(bg="#D78000")
        self.label_D.place(relx = 0.517, rely = 0.855)
        self.opt_D.configure(bg="#D78000")

    def change_back_4(self,e):

        self.label_D.config(image='', bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
        self.buttons[3].configure(bg="#1B2732")
        self.label_D.place(relx = 0.57, rely = 0.865)
        self.opt_D.configure(bg="#1B2732")


    def answered_wrong(self, button):
        sound_3 = mixer.Sound(r"Dependencies\false1.ogg")
        son_3 = sound_3.play()
        #button["bg"] = "#E35E75"
        button["bg"] = "#c95165"
        self.image = PIL.Image.open(r"Dependencies\incorrect.png")
        self.resize_image = self.image.resize((424, 60))
        self.pic = ImageTk.PhotoImage(self.resize_image)

        x, y = button.winfo_rootx(), button.winfo_rooty()
        if (x >= 290 and x <= 334)  and y == 664:
            self.label_B.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
            self.label_B.image = self.pic
            self.label_B.place(relx = 0.156, rely = 0.854)
            self.opt_B.configure(bg="#c95165")

        elif (x >= 751 and x <= 795)  and y ==592:
            self.label_C.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
            self.label_C.image = self.pic
            self.label_C.place(relx = 0.517, rely = 0.755)
            self.opt_C.configure(bg="#c95165")

        elif (x >= 290 and x <= 334 )  and y ==592:
            self.label_A.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
            self.label_A.image = self.pic
            self.label_A.place(relx = 0.156, rely = 0.756)
            self.opt_A.configure(bg="#c95165")

        elif (x >= 751 and x <= 795)  and y == 664:
            self.label_D.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
            self.label_D.image = self.pic
            self.label_D.place(relx = 0.517, rely = 0.855)
            self.opt_D.configure(bg="#c95165")

        else:
            print("No cubre")

        res = messagebox.askquestion('Pregunta incorrecta', 'Pregunta incorrecta, ¿desea continuar?')
        if res == 'yes':
            pass

        elif res == 'no':
            path = 'Dependencies/plot.png'
            check_file = os.path.isfile(path)
            if check_file == True:
                self.frm.destroy()
                os.remove(path)
            self.son_1.pause()
            if self.id_after is not None:
                self.after_cancel(self.id_after)  # Cancel the scheduled after event
                self.id_after = None
            else:
                pass
            self.destroy()

        else:
            path = 'Dependencies/plot.png'
            check_file = os.path.isfile(path)
            if check_file == True:
                self.frm.destroy()
                os.remove(path)
            self.son_1.pause()
            if self.id_after is not None:
                self.after_cancel(self.id_after)  # Cancel the scheduled after event
                self.id_after = None
            else:
                pass
            self.destroy()


        print("Botton incorrecto")


    def clicked_50_50(self,logo_img_1):

        global count_50_50, question
        count_50_50 +=1
        if count_50_50 <= 1:
            sound_4 = mixer.Sound(r"Dependencies\50-50.ogg")
            son_4 = sound_4.play()
            clickedImage_1 = PhotoImage(file = r"Dependencies\50-50_c.png")
            logo_img_1.config(image = clickedImage_1)
            logo_img_1.image = clickedImage_1

            tup =  zip(self.copy_list, question["answers"])
            tup2 = copy.copy(self.buttons)
            lst_btn = copy.copy(self.buttons)

            index = 0
            t = ""
            for button, answer in tup:
                if answer["isCorrect"]:
                    button.configure(bg="#D78000")
                    if index == 0:
                        #t = tup[1:]
                        start = 1 #start position of slice
                        stop = 3 #end position of slice
                        slice_object = slice(start, stop)
                        t = tup2[slice_object]
                        shuffle(t)
                        if button == t[0]:
                            t = t[1]
                        else:
                            t = t[0]
                        t.configure(bg="#D78000")

                        if button == lst_btn[0]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_A.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_A.image = self.pic
                            self.buttons[0].configure(bg="#D78000")
                            self.label_A.place(relx = 0.156, rely = 0.756)
                            self.opt_A.configure(bg="#D78000")

                        elif button == lst_btn[1]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_B.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_B.image = self.pic
                            self.buttons[1].configure(bg="#D78000")
                            self.label_B.place(relx = 0.156, rely = 0.854)
                            self.opt_B.configure(bg="#D78000")

                        elif button == lst_btn[2]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_C.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_C.image = self.pic
                            self.buttons[2].configure(bg="#D78000")
                            self.label_C.place(relx = 0.517, rely = 0.755)
                            self.opt_C.configure(bg="#D78000")

                        elif button == lst_btn[3]:
                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_D.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_D.image = self.pic
                            self.buttons[3].configure(bg="#D78000")
                            self.label_D.place(relx = 0.517, rely = 0.855)
                            self.opt_D.configure(bg="#D78000")

                        if t == lst_btn[0]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_A.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_A.image = self.pic
                            self.buttons[0].configure(bg="#D78000")
                            self.label_A.place(relx = 0.156, rely = 0.756)
                            self.opt_A.configure(bg="#D78000")

                        elif t == lst_btn[1]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_B.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_B.image = self.pic
                            self.buttons[1].configure(bg="#D78000")
                            self.label_B.place(relx = 0.156, rely = 0.854)
                            self.opt_B.configure(bg="#D78000")

                        elif t == lst_btn[2]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_C.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_C.image = self.pic
                            self.buttons[2].configure(bg="#D78000")
                            self.label_C.place(relx = 0.517, rely = 0.755)
                            self.opt_C.configure(bg="#D78000")

                        elif t == lst_btn[3]:
                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_D.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_D.image = self.pic
                            self.buttons[3].configure(bg="#D78000")
                            self.label_D.place(relx = 0.517, rely = 0.855)
                            self.opt_D.configure(bg="#D78000")

                        break
                    elif index == 1:
                        start = 0 #start position of slice
                        stop = 1 #end position of slice
                        slice_object = slice(start, stop,2)
                        t1 = tup2[slice_object]
                        start = 2 #start position of slice
                        stop = 3 #end position of slice
                        slice_object = slice(start, stop)
                        t2 = tup2[slice_object]
                        t = sum((t1, t2), ())
                        shuffle(t)
                        if button == t[0]:
                            t = t[1]
                        else:
                            t = t[0]
                        t.configure(bg="#D78000")

                        if button == lst_btn[0]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_A.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_A.image = self.pic
                            self.buttons[0].configure(bg="#D78000")
                            self.label_A.place(relx = 0.156, rely = 0.756)
                            self.opt_A.configure(bg="#D78000")

                        elif button == lst_btn[1]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_B.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_B.image = self.pic
                            self.buttons[1].configure(bg="#D78000")
                            self.label_B.place(relx = 0.156, rely = 0.854)
                            self.opt_B.configure(bg="#D78000")

                        elif button == lst_btn[2]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_C.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_C.image = self.pic
                            self.buttons[2].configure(bg="#D78000")
                            self.label_C.place(relx = 0.517, rely = 0.755)
                            self.opt_C.configure(bg="#D78000")

                        elif button == lst_btn[3]:
                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_D.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_D.image = self.pic
                            self.buttons[3].configure(bg="#D78000")
                            self.label_D.place(relx = 0.517, rely = 0.855)
                            self.opt_D.configure(bg="#D78000")

                        if t == lst_btn[0]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_A.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_A.image = self.pic
                            self.buttons[0].configure(bg="#D78000")
                            self.label_A.place(relx = 0.156, rely = 0.756)
                            self.opt_A.configure(bg="#D78000")

                        elif t == lst_btn[1]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_B.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_B.image = self.pic
                            self.buttons[1].configure(bg="#D78000")
                            self.label_B.place(relx = 0.156, rely = 0.854)
                            self.opt_B.configure(bg="#D78000")

                        elif t == lst_btn[2]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_C.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_C.image = self.pic
                            self.buttons[2].configure(bg="#D78000")
                            self.label_C.place(relx = 0.517, rely = 0.755)
                            self.opt_C.configure(bg="#D78000")

                        elif t == lst_btn[3]:
                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_D.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_D.image = self.pic
                            self.buttons[3].configure(bg="#D78000")
                            self.label_D.place(relx = 0.517, rely = 0.855)
                            self.opt_D.configure(bg="#D78000")
                        break
                    elif index == 2:
                        start = 0 #start position of slice
                        stop = 1 #end position of slice
                        slice_object = slice(start, stop)
                        t1 = tup2[slice_object]
                        start = 0 #start position of slice
                        stop = 3 #end position of slice
                        slice_object = slice(start, stop,3)
                        t2 = tup2[slice_object]
                        t = sum((t1, t2), ())
                        shuffle(t)
                        if button == t[0]:
                            t = t[1]
                        else:
                            t = t[0]
                        t.configure(bg="#D78000")

                        if button == lst_btn[0]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_A.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_A.image = self.pic
                            self.buttons[0].configure(bg="#D78000")
                            self.label_A.place(relx = 0.156, rely = 0.756)
                            self.opt_A.configure(bg="#D78000")

                        elif button == lst_btn[1]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_B.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_B.image = self.pic
                            self.buttons[1].configure(bg="#D78000")
                            self.label_B.place(relx = 0.156, rely = 0.854)
                            self.opt_B.configure(bg="#D78000")

                        elif button == lst_btn[2]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_C.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_C.image = self.pic
                            self.buttons[2].configure(bg="#D78000")
                            self.label_C.place(relx = 0.517, rely = 0.755)
                            self.opt_C.configure(bg="#D78000")

                        elif button == lst_btn[3]:
                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_D.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_D.image = self.pic
                            self.buttons[3].configure(bg="#D78000")
                            self.label_D.place(relx = 0.517, rely = 0.855)
                            self.opt_D.configure(bg="#D78000")

                        if t == lst_btn[0]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_A.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_A.image = self.pic
                            self.buttons[0].configure(bg="#D78000")
                            self.label_A.place(relx = 0.156, rely = 0.756)
                            self.opt_A.configure(bg="#D78000")

                        elif t == lst_btn[1]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_B.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_B.image = self.pic
                            self.buttons[1].configure(bg="#D78000")
                            self.label_B.place(relx = 0.156, rely = 0.854)
                            self.opt_B.configure(bg="#D78000")

                        elif t == lst_btn[2]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_C.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_C.image = self.pic
                            self.buttons[2].configure(bg="#D78000")
                            self.label_C.place(relx = 0.517, rely = 0.755)
                            self.opt_C.configure(bg="#D78000")

                        elif t == lst_btn[3]:
                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_D.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_D.image = self.pic
                            self.buttons[3].configure(bg="#D78000")
                            self.label_D.place(relx = 0.517, rely = 0.855)
                            self.opt_D.configure(bg="#D78000")
                        break
                    elif index == 3:
                        start = 0 #start position of slice
                        stop = 2 #end position of slice
                        slice_object = slice(start, stop)
                        t = tup2[slice_object]
                        shuffle(t)
                        if button == t[0]:
                            t = t[1]
                        else:
                            t = t[0]
                        t.configure(bg="#D78000")

                        if button == lst_btn[0]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_A.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_A.image = self.pic
                            self.buttons[0].configure(bg="#D78000")
                            self.label_A.place(relx = 0.156, rely = 0.756)
                            self.opt_A.configure(bg="#D78000")

                        elif button == lst_btn[1]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_B.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_B.image = self.pic
                            self.buttons[1].configure(bg="#D78000")
                            self.label_B.place(relx = 0.156, rely = 0.854)
                            self.opt_B.configure(bg="#D78000")

                        elif button == lst_btn[2]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_C.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_C.image = self.pic
                            self.buttons[2].configure(bg="#D78000")
                            self.label_C.place(relx = 0.517, rely = 0.755)
                            self.opt_C.configure(bg="#D78000")

                        elif button == lst_btn[3]:
                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_D.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_D.image = self.pic
                            self.buttons[3].configure(bg="#D78000")
                            self.label_D.place(relx = 0.517, rely = 0.855)
                            self.opt_D.configure(bg="#D78000")

                        if t == lst_btn[0]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_A.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_A.image = self.pic
                            self.buttons[0].configure(bg="#D78000")
                            self.label_A.place(relx = 0.156, rely = 0.756)
                            self.opt_A.configure(bg="#D78000")

                        elif t == lst_btn[1]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_B.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_B.image = self.pic
                            self.buttons[1].configure(bg="#D78000")
                            self.label_B.place(relx = 0.156, rely = 0.854)
                            self.opt_B.configure(bg="#D78000")

                        elif t == lst_btn[2]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_C.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_C.image = self.pic
                            self.buttons[2].configure(bg="#D78000")
                            self.label_C.place(relx = 0.517, rely = 0.755)
                            self.opt_C.configure(bg="#D78000")

                        elif t == lst_btn[3]:
                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_D.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_D.image = self.pic
                            self.buttons[3].configure(bg="#D78000")
                            self.label_D.place(relx = 0.517, rely = 0.855)
                            self.opt_D.configure(bg="#D78000")
                        break
                else:
                    pass

                index+=1

        else:
            messagebox.showerror(message="Ya utilizo comodin", title="Advertencia")



    def clicked_public(self,logo_img_2): # without event because I use `command=` instead of `bind`
        global count_public, question
        count_public+=1
        if count_public <= 1:
            sound_5 = mixer.Sound(r"Dependencies\asktheaudience.ogg")
            son_5 = sound_5.play()
            clickedImage_2 = PhotoImage(file = r"Dependencies\asktheaudience_c.png")
            logo_img_2.config(image = clickedImage_2)
            logo_img_2.image = clickedImage_2
            self.plot(question)
        else:
            messagebox.showerror(message="Ya utilizo este comodin", title="Advertencia")


    def clicked_chance(self, logo_img_3): # without event because I use `command=` instead of `bind`
        global count_chance, count_50_50, count_public
        count_chance+=1

        if count_50_50 == 1:

            self.label_A.config(image='', bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
            self.buttons[0].configure(bg="#1B2732")
            self.label_A.place(relx = 0.25, rely = 0.765)
            self.opt_A.configure(bg="#1B2732")

            self.label_B.config(image='', bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
            self.buttons[1].configure(bg="#1B2732")
            self.label_B.place(relx = 0.25, rely = 0.865)
            self.opt_B.configure(bg="#1B2732")

            self.label_C.config(image='', bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
            self.buttons[2].configure(bg="#1B2732")
            self.label_C.place(relx = 0.57, rely = 0.765)
            self.opt_C.configure(bg="#1B2732")

            self.label_D.config(image='', bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
            self.buttons[3].configure(bg="#1B2732")
            self.label_D.place(relx = 0.57, rely = 0.865)
            self.opt_D.configure(bg="#1B2732")

        else:
            pass

        if count_public == 1:
            path = 'Dependencies/plot.png'
            check_file = os.path.isfile(path)
            if check_file == True:
                self.frm.destroy()
                os.remove(path)
            else:
                self.frm.destroy()

        else:
            pass

        if count_chance <= 1:

            sound_6 = mixer.Sound(r"Dependencies\switcharoo.ogg")
            son_6 = sound_6.play()
            clickedImage_3 = PhotoImage(file = r"Dependencies\switcharoo_c.png")
            logo_img_3.config(image = clickedImage_3)
            logo_img_3.image = clickedImage_3


            global question
            global tuple_btn_qst
            #puntuation = next(self.puntuation, None)

            var = {
            "text": "Cual es la primer sonda espacial en llegar a marte?",
            "answers": [
                {
                    "text": "Viking 2",
                    "isCorrect": False
                },
                {
                    "text": "Voyager 1",
                    "isCorrect": False
                },
                {
                    "text": "Juno",
                    "isCorrect": False
                },
                {
                    "text": "Viking 1",
                    "isCorrect": True
                }
            ],
            "level": "Dificil",
            "Correct": "D"
        }

            #itertools.chain(self.questions, var)
            self.rst.append(var)

            question = next(self.questions, None)
            shuffle(question["answers"])

            if len(question["text"]) < 20:
                self.question_label.place(relx = 0.42, rely = 0.59)

            elif len(question["text"]) >= 20 and len(question["text"]) <=45:
                self.question_label.place(relx = 0.35, rely = 0.59)

            elif len(question["text"]) > 45 and len(question["text"]) < 54:
                self.question_label.configure(font=("Arial", 24))
                self.question_label.place(relx = 0.22, rely = 0.59)

            elif len(question["text"]) >= 54 and len(question["text"])<= 63:
                self.question_label.configure(font=("Arial", 22))
                self.question_label.place(relx = 0.20, rely = 0.59)

            elif len(question["text"]) > 63 and len(question["text"])<= 72:
                self.question_label.configure(font=("Arial", 19))
                self.question_label.place(relx = 0.17, rely = 0.59)

            elif len(question["text"]) > 72:
                self.question_label.configure(font=("Arial", 16))
                self.question_label.place(relx = 0.2, rely = 0.59)
            else:
                pass

            self.question_label["text"] = question["text"]

            index = 0
            #Acomodo la lista de botones para que la respuesta correcta este al final de la lista.
            for element in question["answers"]:
                if "True" in str(element):
                    index = question["answers"].index(element)
                    break

            element = question["answers"].pop(index)
            new_index = len(question["answers"])
            question["answers"].insert(new_index, element)


            self.copy_list = copy.copy(self.buttons)
            shuffle(self.copy_list)
            tuple_btn_qst = zip(self.copy_list, question["answers"])

            #for button, answer in zip(self.copy_list, question["answers"]):
            for button, answer in tuple_btn_qst:
                button["text"] = answer["text"]
                my_text = button.cget('text')
                button["bg"] = "#1B2732"
                button["fg"]="#EDEFF1"

                if answer["isCorrect"]:
                    var = tk.IntVar()
                    button["command"] = lambda button=button: [self.on_press(button), var.set(1)]
                    button.wait_variable(var)
                    print(self.id_after)
                    self.id_after = self.after(500, self.goto_next_question)
                    #self.after_cancel(self.id_after)
                    print(self.id_after)

                else:
                    button["command"] = lambda button=button: self.answered_wrong(button)
        else:
            messagebox.showerror(message="Ya utilizo este comodin", title="Advertencia")

    def plot(self, question):

        opt = ["A", "B", "C", "D"]
        prb = [75, 8.33, 8.33, 8.33]
        shuffle(prb)
        result = zip(opt, prb)
        data = dict(result)
        courses = list(data.keys())
        values = list(data.values())

        self.fig = Figure(figsize = (4, 3),dpi = 100, facecolor="#1B2732")
        self.plot1 = self.fig.add_subplot(111)
        self.plot1.bar(courses, values, color ='#006CCE',width = 0.4)
        self.plot1.set(ylabel = "(%)")
        self.plot1.spines['bottom'].set_color('#dcdee0')
        self.plot1.spines['top'].set_color('#dcdee0')
        self.plot1.xaxis.label.set_color('#dcdee0')
        self.plot1.tick_params(axis='x', colors='#dcdee0')
        self.plot1.yaxis.label.set_color('#dcdee0')
        self.plot1.tick_params(axis='y', colors='#dcdee0')
        self.plot1.set_facecolor("#1B2732")
        self.fig.savefig('Dependencies\plot.png')

        path = 'Dependencies/plot.png'
        check_file = os.path.isfile(path)
        if check_file == True:
            self.image_prb = PIL.Image.open("Dependencies\plot.png")

            # Resize the image using resize() method
            self.resize_image_prb = self.image_prb.resize((300, 300))

            self.img_prb = ImageTk.PhotoImage(self.resize_image_prb)

            self.label_bg_prb = tk.Label(self.frm, image=self.img_prb, bg="#1B2732", highlightthickness = 0, bd = 0)
            self.label_bg_prb.image = self.img_prb
            self.label_bg_prb.pack()
            print("Estoy aqui")
        else:
            print("No se genero imagen")

    def on_closing(self, event=0):
        if messagebox.askokcancel("Eliminar", "Desea eliminar la sesion?"):
            path = 'Dependencies/plot.png'
            check_file = os.path.isfile(path)
            if check_file == True:
                self.frm.destroy()
                os.remove(path)
            else:
                pass
            self.son_1.pause()

            if self.id_after is not None:
                self.after_cancel(self.id_after)  # Cancel the scheduled after event
                self.id_after = None
            else:
                pass
            self.destroy()


def main(root, count):
    filename = r"Dependencies\preguntas.txt"
    columns = defaultdict(list)
    count_line = 0

    with open(filename, 'r', encoding="latin1" ) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            count_line+=1
            for i in range(len(row)):
                columns[i].append(row[i])

    if count_line >= 15:
        columns = dict(columns)
        QST = []
        for i in range(len(columns[0])):
            if columns[5][i].replace(" ", "") == "A":
                var = {
                "text": str(columns[0][i]),
                "answers": [
                    {
                        "text": str(columns[1][i]),
                        "isCorrect": True
                    },
                    {
                        "text": str(columns[2][i]),
                        "isCorrect": False
                    },
                    {
                        "text": str(columns[3][i]),
                        "isCorrect": False
                    },
                    {
                        "text": str(columns[4][i]),
                        "isCorrect": False
                    }
                ],
                "level": str(columns[6][i]),
                "Correct": str(columns[5][i])
            }
                QST.append(var)

            elif columns[5][i].replace(" ", "") == "B":
                var = {
                "text": str(columns[0][i]),
                "answers": [
                    {
                        "text": str(columns[1][i]),
                        "isCorrect": False
                    },
                    {
                        "text": str(columns[2][i]),
                        "isCorrect": True
                    },
                    {
                        "text": str(columns[3][i]),
                        "isCorrect": False
                    },
                    {
                        "text": str(columns[4][i]),
                        "isCorrect": False
                    }
                ],
                "level": str(columns[6][i]),
                "Correct": str(columns[5][i])
            }
                QST.append(var)

            elif columns[5][i].replace(" ", "") == "C":
                var = {
                "text": str(columns[0][i]),
                "answers": [
                    {
                        "text": str(columns[1][i]),
                        "isCorrect": False
                    },
                    {
                        "text": str(columns[2][i]),
                        "isCorrect": False
                    },
                    {
                        "text": str(columns[3][i]),
                        "isCorrect": True
                    },
                    {
                        "text": str(columns[4][i]),
                        "isCorrect": False
                    }
                ],
                "level": str(columns[6][i]),
                "Correct": str(columns[5][i])
            }
                QST.append(var)

            elif columns[5][i].replace(" ", "") == "D":
                var = {
                "text": str(columns[0][i]),
                "answers": [
                    {
                        "text": str(columns[1][i]),
                        "isCorrect": False
                    },
                    {
                        "text": str(columns[2][i]),
                        "isCorrect": False
                    },
                    {
                        "text": str(columns[3][i]),
                        "isCorrect": False
                    },
                    {
                        "text": str(columns[4][i]),
                        "isCorrect": True
                    }
                ],
                "level": str(columns[6][i]),
                "Correct": str(columns[5][i])
            }
                QST.append(var)
            else:
                print("EXCEPCION")


        application = Application(QST,count, root)
        application.mainloop()

        return 0
    else:
        messagebox.showerror(message="Debe existir un minimo de 15 preguntas para poder jugar", title="Advertencia")

#if __name__ == "__main__":
def callback(root, count):
    import sys
    sys.exit(main(root, count))


"""
import tkinter as tk
from PIL import Image, ImageTk
from collections import defaultdict
import csv
from tkinter import *
import PIL.Image
from tkinter import messagebox
from pygame import mixer
import sys
import copy
from random import shuffle
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
import os



#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
count_50_50 = 0
count_public = 0
count_chance = 0

class Application(Toplevel):

    def __init__(self, questions, count, master = None,*args, **kwargs):
        #tk.Tk.__init__(self, *args, **kwargs)
        super().__init__(master = master, *args, **kwargs)
        try:
            self.id_after = None
            self.protocol("WM_DELETE_WINDOW", self.on_closing)
            mixer.init()
            self.sound_1 = mixer.Sound(r"Dependencies\bg_music1.ogg")
            self.son_1 = self.sound_1.play(-1)
            if count == 0:
                pass
            else:
                global count_50_50, count_public, count_chance
                count_50_50 = 0
                count_public = 0
                count_chance = 0
            WIDTH = 1280
            HEIGHT = 720
            self.title("Juego")
            self.geometry(f"{WIDTH}x{HEIGHT}")
            self.resizable(width=False, height=False)

            self.grid_columnconfigure(0, weight=1)
            self.grid_columnconfigure(1, weight=1)
            self.grid_rowconfigure(0, weight=1)
            self.grid_rowconfigure(1, weight=1)
            self.grid_rowconfigure(2, weight=1)

            #bg = tk.PhotoImage(file = r"quien quiere ser millonario\Dependencies\background.jpg")
            self.image = PIL.Image.open(r"Dependencies\background.jpg")
            self.background_image = ImageTk.PhotoImage(self.image)
            # Show image using label
            self.label1 = tk.Label( self, image = self.background_image)
            self.label1.place(x = 0, y = 0)

            self.frm = tk.Frame(self, bg="#1B2732")
            self.frm.place(relx = 0.07, rely = 0.15)


            self.image_logo = PIL.Image.open(r"Dependencies/LOGO-modified.png")

            # Resize the image using resize() method
            self.resize_image = self.image_logo.resize((250, 250))

            self.img = ImageTk.PhotoImage(self.resize_image)

            self.label_bg = tk.Label(self, image=self.img, bg="#1B2732", highlightthickness = 0, bd = 0)
            self.label_bg.image = self.img
            self.label_bg.place(relx = 0.4, rely = 0.1)

            self.label_trp = tk.Label(self, text= "", bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
            self.label_trp.place(relx = 0.15, rely = 0.1)

            self.puntuation = ["$ 100", "$ 200", "$ 300", "$ 500", "$ 1000", "$ 2000", "$ 4000", "$ 8000", "$ 160 00", "$ 32 000", "$ 64 000", "$ 125 000", "$ 250 000", "$ 500 000", "$ 1000 000"]
            self.puntuation = iter(self.puntuation)

            self.rst = self.oder_lst(questions)
            #self.questions = iter(questions)
            self.questions = iter(self.rst)

            self.img_1 = PhotoImage(file=r"Dependencies\50-50.png")
            self.logo_img_1= Button(self, command=lambda:self.clicked_50_50(self.logo_img_1), image = self.img_1, bg="#1B2732", activebackground="#1B2732", highlightthickness = 0, bd = 0)
            self.logo_img_1.image = self.img_1
            self.logo_img_1.place(relx = 0.65, rely = 0.1)

            self.img_2 = PhotoImage(file=r"Dependencies\asktheaudience.png")
            self.logo_img_2= Button(self, command=lambda:self.clicked_public(self.logo_img_2), image = self.img_2, bg="#1B2732", activebackground="#1B2732", highlightthickness = 0, bd = 0)
            self.logo_img_2.image = self.img_2
            self.logo_img_2.place(relx = 0.71, rely = 0.1)

            self.img_3 = PhotoImage(file=r"Dependencies\switcharoo.png")
            self.logo_img_3= Button(self, command=lambda:self.clicked_chance(self.logo_img_3), image = self.img_3, bg="#1B2732", activebackground="#1B2732", highlightthickness = 0, bd = 0)
            self.logo_img_3.image = self.img_3
            self.logo_img_3.place(relx = 0.77, rely = 0.1)

            self.question_label = tk.Label(self, text= "", bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
            self.question_label.place(relx = 0.32, rely = 0.59)


            self.label_A = tk.Label(self, text= "", bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
            self.label_A.place(relx = 0.25, rely = 0.765)

            self.label_B = tk.Label(self, text= "", bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
            self.label_B.place(relx = 0.25, rely = 0.865)

            self.label_C = tk.Label(self, text= "", bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
            self.label_C.place(relx = 0.57, rely = 0.765)

            self.label_D = tk.Label(self, text= "", bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
            self.label_D.place(relx = 0.57, rely = 0.865)


            self.opt_A = tk.Label(self, text= "A:", bg="#1B2732", fg='#ECEEF1', font=("Arial", 17))
            self.opt_A.place(relx = 0.18, rely = 0.766)

            self.opt_B = tk.Label(self, text= "B:", bg="#1B2732", fg='#ECEEF1', font=("Arial", 17))
            self.opt_B.place(relx = 0.18, rely = 0.866)

            self.opt_C = tk.Label(self, text= "C:", bg="#1B2732", fg='#ECEEF1', font=("Arial", 17))
            self.opt_C.place(relx = 0.54, rely = 0.766)

            self.opt_D = tk.Label(self, text= "D:", bg="#1B2732", fg='#ECEEF1', font=("Arial", 17))
            self.opt_D.place(relx = 0.54, rely = 0.866)


            self.buttons = []
            #self.radbuttons = []
            for y in range(1):

                btn_A = tk.Button(self,text ="123",font=("Arial", 15), bg="#1B2732", activebackground="#1B2732", highlightthickness = 0, bd = 0, height= 1, width=30)
                btn_A.place(relx = 0.20, rely = 0.766)

                btn_B = tk.Button(self, text="123",font=("Arial", 15), bg="#1B2732", activebackground="#1B2732", highlightthickness = 0, bd = 0 , height= 1, width=30)
                btn_B.place(relx = 0.20, rely = 0.866)

                btn_C = tk.Button(self, text="123",font=("Arial", 15), bg="#1B2732", activebackground="#1B2732", highlightthickness = 0, bd = 0 , height= 1, width=30)
                btn_C.place(relx = 0.56, rely = 0.766)

                btn_D = tk.Button(self, text = "123",font=("Arial", 15), bg="#1B2732", fg='#EDEFF1',activebackground="#1B2732", highlightthickness = 0, bd = 0 , height= 1, width=30)
                btn_D.place(relx = 0.56, rely = 0.866)
                self.buttons.append([btn_A, btn_B, btn_C, btn_D])


            self.buttons = sum(self.buttons, [])

            self.buttons[0].bind("<Enter>", self.change_1)
            self.buttons[0].bind("<Leave>", self.change_back_1)

            self.buttons[1].bind("<Enter>", self.change_2)
            self.buttons[1].bind("<Leave>", self.change_back_2)

            self.buttons[2].bind("<Enter>", self.change_3)
            self.buttons[2].bind("<Leave>", self.change_back_3)

            self.buttons[3].bind("<Enter>", self.change_4)
            self.buttons[3].bind("<Leave>", self.change_back_4)
            self.goto_next_question()

        except Exception as e :
            text_0 = str(e)
            messagebox.showerror(message=text_0, title="Advertencia")
            if self.son_1.get_busy() == True:
                self.son_1.pause()

                if self.id_after is not None:
                    self.after_cancel(self.id_after)  # Cancel the scheduled after event
                    self.id_after = None
                else:
                    pass
                self.destroy()
            else:

                if self.id_after is not None:
                    self.after_cancel(self.id_after)  # Cancel the scheduled after event
                    self.id_after = None
                else:
                    pass
                self.destroy()

    def goto_next_question(self):

        self.opt_A.config(bg="#1B2732")
        self.opt_B.config(bg="#1B2732")
        self.opt_C.config(bg="#1B2732")
        self.opt_D.config(bg="#1B2732")

        self.label_A.config(image='', bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
        self.label_B.config(image='', bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
        self.label_C.config(image='', bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
        self.label_D.config(image='', bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))


        path = 'Dependencies/plot.png'
        check_file = os.path.isfile(path)
        if check_file == True:
            self.frm.destroy()
            os.remove(path)
        else:
            pass
        #global count_chance
        global question, tuple_btn_qst, count_50_50

        if count_50_50 == 1:

            self.label_A.config(image='', bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
            self.buttons[0].configure(bg="#1B2732")
            self.label_A.place(relx = 0.25, rely = 0.765)

            self.label_B.config(image='', bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
            self.buttons[1].configure(bg="#1B2732")
            self.label_B.place(relx = 0.25, rely = 0.865)

            self.label_C.config(image='', bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
            self.buttons[2].configure(bg="#1B2732")
            self.label_C.place(relx = 0.57, rely = 0.765)

            self.label_D.config(image='', bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
            self.buttons[3].configure(bg="#1B2732")
            self.label_D.place(relx = 0.57, rely = 0.865)

        else:
            pass

        question = next(self.questions, None)
        puntuation = next(self.puntuation, None)

        if question is None:
            self.son_1.pause()
            if self.id_after is not None:
                self.after_cancel(self.id_after)  # Cancel the scheduled after event
                self.id_after = None
            else:
                pass
            self.destroy()
            return

        shuffle(question["answers"])


        if len(question["text"]) < 20:
            self.question_label.place(relx = 0.42, rely = 0.59)

        elif len(question["text"]) >= 20 and len(question["text"]) <=45:
            self.question_label.place(relx = 0.35, rely = 0.59)

        elif len(question["text"]) > 45 and len(question["text"]) < 54:
            self.question_label.configure(font=("Arial", 24))
            self.question_label.place(relx = 0.22, rely = 0.59)

        elif len(question["text"]) >= 54 and len(question["text"])<= 63:
            self.question_label.configure(font=("Arial", 22))
            self.question_label.place(relx = 0.20, rely = 0.59)

        elif len(question["text"]) > 63 and len(question["text"])<= 72:
            self.question_label.configure(font=("Arial", 19))
            self.question_label.place(relx = 0.17, rely = 0.59)

        elif len(question["text"]) > 72:
            self.question_label.configure(font=("Arial", 16))
            self.question_label.place(relx = 0.2, rely = 0.59)
        else:
            pass



        self.question_label["text"] = question["text"]
        self.label_trp["text"] = puntuation

        index = 0
        #Acomodo la lista de botones para que la respuesta correcta este al final de la lista.
        for element in question["answers"]:
            if "True" in str(element):
                index = question["answers"].index(element)
                break

        element = question["answers"].pop(index)
        new_index = len(question["answers"])
        question["answers"].insert(new_index, element)


        self.copy_list = copy.copy(self.buttons)
        shuffle(self.copy_list)
        tuple_btn_qst = zip(self.copy_list, question["answers"])

        #for button, answer in zip(self.copy_list, question["answers"]):
        for button, answer in tuple_btn_qst:
            button["text"] = answer["text"]
            my_text = button.cget('text')
            button["bg"] = "#1B2732"
            button["fg"]="#EDEFF1"

            if answer["isCorrect"]:
                var = tk.IntVar()
                button["command"] = lambda button=button: [self.on_press(button), var.set(1)]

                button.wait_variable(var)
                print(self.id_after)
                self.id_after = self.after(500, self.goto_next_question)
                print(self.id_after)
            else:
                button["command"] = lambda button=button: self.answered_wrong(button)

    def oder_lst(self, questions):

        self.easy = []
        self.mid = []
        self.hard = []

        for sub in questions:
            if ' Facil' in sub["level"] :
                self.easy.append(sub)
            elif ' Intermedio' in sub["level"]:
                self.mid.append(sub)
            else:
                self.hard.append(sub)
        shuffle(self.easy)
        shuffle(self.mid)
        shuffle(self.hard)

        self.questions2 = [self.easy, self.mid, self.hard]
        self.questions2 = sum(self.questions2, [])
        size = len(self.questions2)
        if size > 15:
            size2 = size - 15
            self.questions2 = self.questions2[:-size2]

        else:
            pass

        return self.questions2

    def on_press(self, button):

        sound_2 = mixer.Sound(r"Dependencies\true1.ogg")
        son_2 = sound_2.play()
        button.configure(bg= "#81CE5F")
        self.image = PIL.Image.open(r"Dependencies\correct.png")
        self.resize_image = self.image.resize((424, 60))
        self.pic = ImageTk.PhotoImage(self.resize_image)

        x, y = button.winfo_rootx(), button.winfo_rooty()
        if (x >= 290 and x <= 334)  and y == 664:
            self.label_B.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
            self.label_B.image = self.pic
            self.label_B.place(relx = 0.156, rely = 0.854)
            self.opt_B.config( bg="#81CE5F")

        elif (x >= 751 and x <= 795)  and y ==592:
            self.label_C.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
            self.label_C.image = self.pic
            self.label_C.place(relx = 0.517, rely = 0.755)
            self.opt_C.config( bg="#81CE5F")

        elif (x >= 290 and x <= 334 )  and y ==592:
            self.label_A.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
            self.label_A.image = self.pic
            self.label_A.place(relx = 0.156, rely = 0.756)
            self.opt_A.config( bg="#81CE5F")

        elif (x >= 751 and x <= 795)  and y == 664:
            self.label_D.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
            self.label_D.image = self.pic
            self.label_D.place(relx = 0.517, rely = 0.855)
            self.opt_D.config( bg="#81CE5F")
        else:
            print("No cubre")




    def change_1(self,e):
        self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
        self.resize_image = self.image.resize((424, 60))
        self.pic = ImageTk.PhotoImage(self.resize_image)
        self.label_A.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
        self.label_A.image = self.pic
        self.buttons[0].configure(bg="#D78000")
        self.label_A.place(relx = 0.156, rely = 0.756)
        self.opt_A.configure(bg="#D78000")

    def change_back_1(self,e):

        self.label_A.config(image='', bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
        self.buttons[0].configure(bg="#1B2732")
        self.label_A.place(relx = 0.25, rely = 0.765)
        self.opt_A.configure(bg="#1B2732")

    def change_2(self,e):
        self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
        self.resize_image = self.image.resize((424, 60))
        self.pic = ImageTk.PhotoImage(self.resize_image)
        self.label_B.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
        self.label_B.image = self.pic
        self.buttons[1].configure(bg="#D78000")
        self.label_B.place(relx = 0.156, rely = 0.854)
        self.opt_B.configure(bg="#D78000")

    def change_back_2(self,e):

        self.label_B.config(image='', bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
        self.buttons[1].configure(bg="#1B2732")
        self.label_B.place(relx = 0.25, rely = 0.865)
        self.opt_B.configure(bg="#1B2732")

    def change_3(self,e):
        self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
        self.resize_image = self.image.resize((424, 60))
        self.pic = ImageTk.PhotoImage(self.resize_image)
        self.label_C.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
        self.label_C.image = self.pic
        self.buttons[2].configure(bg="#D78000")
        self.label_C.place(relx = 0.517, rely = 0.755)
        self.opt_C.configure(bg="#D78000")


    def change_back_3(self,e):

        self.label_C.config(image='', bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
        self.buttons[2].configure(bg="#1B2732")
        self.label_C.place(relx = 0.57, rely = 0.765)
        self.opt_C.configure(bg="#1B2732")

    def change_4(self,e):
        self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
        self.resize_image = self.image.resize((424, 60))
        self.pic = ImageTk.PhotoImage(self.resize_image)
        self.label_D.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
        self.label_D.image = self.pic
        self.buttons[3].configure(bg="#D78000")
        self.label_D.place(relx = 0.517, rely = 0.855)
        self.opt_D.configure(bg="#D78000")

    def change_back_4(self,e):

        self.label_D.config(image='', bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
        self.buttons[3].configure(bg="#1B2732")
        self.label_D.place(relx = 0.57, rely = 0.865)
        self.opt_D.configure(bg="#1B2732")


    def answered_wrong(self, button):
        sound_3 = mixer.Sound(r"Dependencies\false1.ogg")
        son_3 = sound_3.play()
        #button["bg"] = "#E35E75"
        button["bg"] = "#c95165"
        self.image = PIL.Image.open(r"Dependencies\incorrect.png")
        self.resize_image = self.image.resize((424, 60))
        self.pic = ImageTk.PhotoImage(self.resize_image)

        x, y = button.winfo_rootx(), button.winfo_rooty()
        if (x >= 290 and x <= 334)  and y == 664:
            self.label_B.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
            self.label_B.image = self.pic
            self.label_B.place(relx = 0.156, rely = 0.854)
            self.opt_B.configure(bg="#c95165")

        elif (x >= 751 and x <= 795)  and y ==592:
            self.label_C.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
            self.label_C.image = self.pic
            self.label_C.place(relx = 0.517, rely = 0.755)
            self.opt_C.configure(bg="#c95165")

        elif (x >= 290 and x <= 334 )  and y ==592:
            self.label_A.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
            self.label_A.image = self.pic
            self.label_A.place(relx = 0.156, rely = 0.756)
            self.opt_A.configure(bg="#c95165")

        elif (x >= 751 and x <= 795)  and y == 664:
            self.label_D.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
            self.label_D.image = self.pic
            self.label_D.place(relx = 0.517, rely = 0.855)
            self.opt_D.configure(bg="#c95165")

        else:
            print("No cubre")

        res = messagebox.askquestion('Pregunta incorrecta', 'Pregunta incorrecta, ¿desea continuar?')
        if res == 'yes':
            pass

        elif res == 'no':
            path = 'Dependencies/plot.png'
            check_file = os.path.isfile(path)
            if check_file == True:
                self.frm.destroy()
                os.remove(path)
            self.son_1.pause()
            if self.id_after is not None:
                self.after_cancel(self.id_after)  # Cancel the scheduled after event
                self.id_after = None
            else:
                pass
            self.destroy()

        else:
            path = 'Dependencies/plot.png'
            check_file = os.path.isfile(path)
            if check_file == True:
                self.frm.destroy()
                os.remove(path)
            self.son_1.pause()
            if self.id_after is not None:
                self.after_cancel(self.id_after)  # Cancel the scheduled after event
                self.id_after = None
            else:
                pass
            self.destroy()


        print("Botton incorrecto")


    def clicked_50_50(self,logo_img_1):

        global count_50_50, question
        count_50_50 +=1
        if count_50_50 <= 1:
            sound_4 = mixer.Sound(r"Dependencies\50-50.ogg")
            son_4 = sound_4.play()
            clickedImage_1 = PhotoImage(file = r"Dependencies\50-50_c.png")
            logo_img_1.config(image = clickedImage_1)
            logo_img_1.image = clickedImage_1

            tup =  zip(self.copy_list, question["answers"])
            tup2 = copy.copy(self.buttons)
            lst_btn = copy.copy(self.buttons)

            index = 0
            t = ""
            for button, answer in tup:
                if answer["isCorrect"]:
                    button.configure(bg="#D78000")
                    if index == 0:
                        #t = tup[1:]
                        start = 1 #start position of slice
                        stop = 3 #end position of slice
                        slice_object = slice(start, stop)
                        t = tup2[slice_object]
                        shuffle(t)
                        if button == t[0]:
                            t = t[1]
                        else:
                            t = t[0]
                        t.configure(bg="#D78000")

                        if button == lst_btn[0]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_A.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_A.image = self.pic
                            self.buttons[0].configure(bg="#D78000")
                            self.label_A.place(relx = 0.156, rely = 0.756)
                            self.opt_A.configure(bg="#D78000")

                        elif button == lst_btn[1]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_B.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_B.image = self.pic
                            self.buttons[1].configure(bg="#D78000")
                            self.label_B.place(relx = 0.156, rely = 0.854)
                            self.opt_B.configure(bg="#D78000")

                        elif button == lst_btn[2]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_C.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_C.image = self.pic
                            self.buttons[2].configure(bg="#D78000")
                            self.label_C.place(relx = 0.517, rely = 0.755)
                            self.opt_C.configure(bg="#D78000")

                        elif button == lst_btn[3]:
                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_D.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_D.image = self.pic
                            self.buttons[3].configure(bg="#D78000")
                            self.label_D.place(relx = 0.517, rely = 0.855)
                            self.opt_D.configure(bg="#D78000")

                        if t == lst_btn[0]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_A.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_A.image = self.pic
                            self.buttons[0].configure(bg="#D78000")
                            self.label_A.place(relx = 0.156, rely = 0.756)
                            self.opt_A.configure(bg="#D78000")

                        elif t == lst_btn[1]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_B.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_B.image = self.pic
                            self.buttons[1].configure(bg="#D78000")
                            self.label_B.place(relx = 0.156, rely = 0.854)
                            self.opt_B.configure(bg="#D78000")

                        elif t == lst_btn[2]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_C.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_C.image = self.pic
                            self.buttons[2].configure(bg="#D78000")
                            self.label_C.place(relx = 0.517, rely = 0.755)
                            self.opt_C.configure(bg="#D78000")

                        elif t == lst_btn[3]:
                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_D.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_D.image = self.pic
                            self.buttons[3].configure(bg="#D78000")
                            self.label_D.place(relx = 0.517, rely = 0.855)
                            self.opt_D.configure(bg="#D78000")

                        break
                    elif index == 1:
                        start = 0 #start position of slice
                        stop = 1 #end position of slice
                        slice_object = slice(start, stop,2)
                        t1 = tup2[slice_object]
                        start = 2 #start position of slice
                        stop = 3 #end position of slice
                        slice_object = slice(start, stop)
                        t2 = tup2[slice_object]
                        t = sum((t1, t2), ())
                        shuffle(t)
                        if button == t[0]:
                            t = t[1]
                        else:
                            t = t[0]
                        t.configure(bg="#D78000")

                        if button == lst_btn[0]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_A.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_A.image = self.pic
                            self.buttons[0].configure(bg="#D78000")
                            self.label_A.place(relx = 0.156, rely = 0.756)
                            self.opt_A.configure(bg="#D78000")

                        elif button == lst_btn[1]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_B.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_B.image = self.pic
                            self.buttons[1].configure(bg="#D78000")
                            self.label_B.place(relx = 0.156, rely = 0.854)
                            self.opt_B.configure(bg="#D78000")

                        elif button == lst_btn[2]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_C.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_C.image = self.pic
                            self.buttons[2].configure(bg="#D78000")
                            self.label_C.place(relx = 0.517, rely = 0.755)
                            self.opt_C.configure(bg="#D78000")

                        elif button == lst_btn[3]:
                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_D.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_D.image = self.pic
                            self.buttons[3].configure(bg="#D78000")
                            self.label_D.place(relx = 0.517, rely = 0.855)
                            self.opt_D.configure(bg="#D78000")

                        if t == lst_btn[0]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_A.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_A.image = self.pic
                            self.buttons[0].configure(bg="#D78000")
                            self.label_A.place(relx = 0.156, rely = 0.756)
                            self.opt_A.configure(bg="#D78000")

                        elif t == lst_btn[1]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_B.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_B.image = self.pic
                            self.buttons[1].configure(bg="#D78000")
                            self.label_B.place(relx = 0.156, rely = 0.854)
                            self.opt_B.configure(bg="#D78000")

                        elif t == lst_btn[2]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_C.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_C.image = self.pic
                            self.buttons[2].configure(bg="#D78000")
                            self.label_C.place(relx = 0.517, rely = 0.755)
                            self.opt_C.configure(bg="#D78000")

                        elif t == lst_btn[3]:
                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_D.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_D.image = self.pic
                            self.buttons[3].configure(bg="#D78000")
                            self.label_D.place(relx = 0.517, rely = 0.855)
                            self.opt_D.configure(bg="#D78000")
                        break
                    elif index == 2:
                        start = 0 #start position of slice
                        stop = 1 #end position of slice
                        slice_object = slice(start, stop)
                        t1 = tup2[slice_object]
                        start = 0 #start position of slice
                        stop = 3 #end position of slice
                        slice_object = slice(start, stop,3)
                        t2 = tup2[slice_object]
                        t = sum((t1, t2), ())
                        shuffle(t)
                        if button == t[0]:
                            t = t[1]
                        else:
                            t = t[0]
                        t.configure(bg="#D78000")

                        if button == lst_btn[0]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_A.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_A.image = self.pic
                            self.buttons[0].configure(bg="#D78000")
                            self.label_A.place(relx = 0.156, rely = 0.756)
                            self.opt_A.configure(bg="#D78000")

                        elif button == lst_btn[1]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_B.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_B.image = self.pic
                            self.buttons[1].configure(bg="#D78000")
                            self.label_B.place(relx = 0.156, rely = 0.854)
                            self.opt_B.configure(bg="#D78000")

                        elif button == lst_btn[2]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_C.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_C.image = self.pic
                            self.buttons[2].configure(bg="#D78000")
                            self.label_C.place(relx = 0.517, rely = 0.755)
                            self.opt_C.configure(bg="#D78000")

                        elif button == lst_btn[3]:
                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_D.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_D.image = self.pic
                            self.buttons[3].configure(bg="#D78000")
                            self.label_D.place(relx = 0.517, rely = 0.855)
                            self.opt_D.configure(bg="#D78000")

                        if t == lst_btn[0]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_A.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_A.image = self.pic
                            self.buttons[0].configure(bg="#D78000")
                            self.label_A.place(relx = 0.156, rely = 0.756)
                            self.opt_A.configure(bg="#D78000")

                        elif t == lst_btn[1]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_B.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_B.image = self.pic
                            self.buttons[1].configure(bg="#D78000")
                            self.label_B.place(relx = 0.156, rely = 0.854)
                            self.opt_B.configure(bg="#D78000")

                        elif t == lst_btn[2]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_C.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_C.image = self.pic
                            self.buttons[2].configure(bg="#D78000")
                            self.label_C.place(relx = 0.517, rely = 0.755)
                            self.opt_C.configure(bg="#D78000")

                        elif t == lst_btn[3]:
                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_D.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_D.image = self.pic
                            self.buttons[3].configure(bg="#D78000")
                            self.label_D.place(relx = 0.517, rely = 0.855)
                            self.opt_D.configure(bg="#D78000")
                        break
                    elif index == 3:
                        start = 0 #start position of slice
                        stop = 2 #end position of slice
                        slice_object = slice(start, stop)
                        t = tup2[slice_object]
                        shuffle(t)
                        if button == t[0]:
                            t = t[1]
                        else:
                            t = t[0]
                        t.configure(bg="#D78000")

                        if button == lst_btn[0]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_A.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_A.image = self.pic
                            self.buttons[0].configure(bg="#D78000")
                            self.label_A.place(relx = 0.156, rely = 0.756)
                            self.opt_A.configure(bg="#D78000")

                        elif button == lst_btn[1]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_B.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_B.image = self.pic
                            self.buttons[1].configure(bg="#D78000")
                            self.label_B.place(relx = 0.156, rely = 0.854)
                            self.opt_B.configure(bg="#D78000")

                        elif button == lst_btn[2]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_C.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_C.image = self.pic
                            self.buttons[2].configure(bg="#D78000")
                            self.label_C.place(relx = 0.517, rely = 0.755)
                            self.opt_C.configure(bg="#D78000")

                        elif button == lst_btn[3]:
                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_D.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_D.image = self.pic
                            self.buttons[3].configure(bg="#D78000")
                            self.label_D.place(relx = 0.517, rely = 0.855)
                            self.opt_D.configure(bg="#D78000")

                        if t == lst_btn[0]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_A.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_A.image = self.pic
                            self.buttons[0].configure(bg="#D78000")
                            self.label_A.place(relx = 0.156, rely = 0.756)
                            self.opt_A.configure(bg="#D78000")

                        elif t == lst_btn[1]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_B.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_B.image = self.pic
                            self.buttons[1].configure(bg="#D78000")
                            self.label_B.place(relx = 0.156, rely = 0.854)
                            self.opt_B.configure(bg="#D78000")

                        elif t == lst_btn[2]:

                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_C.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_C.image = self.pic
                            self.buttons[2].configure(bg="#D78000")
                            self.label_C.place(relx = 0.517, rely = 0.755)
                            self.opt_C.configure(bg="#D78000")

                        elif t == lst_btn[3]:
                            self.image = PIL.Image.open(r"Dependencies\answer_hover.png")
                            self.resize_image = self.image.resize((424, 60))
                            self.pic = ImageTk.PhotoImage(self.resize_image)
                            self.label_D.config(image = self.pic, bg="#1B2732", highlightthickness = 0, bd = 0)
                            self.label_D.image = self.pic
                            self.buttons[3].configure(bg="#D78000")
                            self.label_D.place(relx = 0.517, rely = 0.855)
                            self.opt_D.configure(bg="#D78000")
                        break
                else:
                    pass

                index+=1

        else:
            messagebox.showerror(message="Ya utilizo comodin", title="Advertencia")



    def clicked_public(self,logo_img_2): # without event because I use `command=` instead of `bind`
        global count_public, question
        count_public+=1
        if count_public <= 1:
            sound_5 = mixer.Sound(r"Dependencies\asktheaudience.ogg")
            son_5 = sound_5.play()
            clickedImage_2 = PhotoImage(file = r"Dependencies\asktheaudience_c.png")
            logo_img_2.config(image = clickedImage_2)
            logo_img_2.image = clickedImage_2
            self.plot(question)
        else:
            messagebox.showerror(message="Ya utilizo este comodin", title="Advertencia")


    def clicked_chance(self, logo_img_3): # without event because I use `command=` instead of `bind`
        global count_chance, count_50_50, count_public
        count_chance+=1

        if count_50_50 == 1:

            self.label_A.config(image='', bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
            self.buttons[0].configure(bg="#1B2732")
            self.label_A.place(relx = 0.25, rely = 0.765)
            self.opt_A.configure(bg="#1B2732")

            self.label_B.config(image='', bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
            self.buttons[1].configure(bg="#1B2732")
            self.label_B.place(relx = 0.25, rely = 0.865)
            self.opt_B.configure(bg="#1B2732")

            self.label_C.config(image='', bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
            self.buttons[2].configure(bg="#1B2732")
            self.label_C.place(relx = 0.57, rely = 0.765)
            self.opt_C.configure(bg="#1B2732")

            self.label_D.config(image='', bg="#1B2732", fg='#ECEEF1', font=("Arial", 25))
            self.buttons[3].configure(bg="#1B2732")
            self.label_D.place(relx = 0.57, rely = 0.865)
            self.opt_D.configure(bg="#1B2732")

        else:
            pass

        if count_public == 1:
            path = 'Dependencies/plot.png'
            check_file = os.path.isfile(path)
            if check_file == True:
                self.frm.destroy()
                os.remove(path)
            else:
                self.frm.destroy()

        else:
            pass

        if count_chance <= 1:

            sound_6 = mixer.Sound(r"Dependencies\switcharoo.ogg")
            son_6 = sound_6.play()
            clickedImage_3 = PhotoImage(file = r"Dependencies\switcharoo_c.png")
            logo_img_3.config(image = clickedImage_3)
            logo_img_3.image = clickedImage_3


            global question
            global tuple_btn_qst
            #puntuation = next(self.puntuation, None)

            var = {
            "text": "Cual es la primer sonda espacial en llegar a marte?",
            "answers": [
                {
                    "text": "Viking 2",
                    "isCorrect": False
                },
                {
                    "text": "Voyager 1",
                    "isCorrect": False
                },
                {
                    "text": "Juno",
                    "isCorrect": False
                },
                {
                    "text": "Viking 1",
                    "isCorrect": True
                }
            ],
            "level": "Dificil",
            "Correct": "D"
        }

            #itertools.chain(self.questions, var)
            self.rst.append(var)

            question = next(self.questions, None)
            shuffle(question["answers"])

            if len(question["text"]) < 20:
                self.question_label.place(relx = 0.42, rely = 0.59)

            elif len(question["text"]) >= 20 and len(question["text"]) <=45:
                self.question_label.place(relx = 0.35, rely = 0.59)

            elif len(question["text"]) > 45 and len(question["text"]) < 54:
                self.question_label.configure(font=("Arial", 24))
                self.question_label.place(relx = 0.22, rely = 0.59)

            elif len(question["text"]) >= 54 and len(question["text"])<= 63:
                self.question_label.configure(font=("Arial", 22))
                self.question_label.place(relx = 0.20, rely = 0.59)

            elif len(question["text"]) > 63 and len(question["text"])<= 72:
                self.question_label.configure(font=("Arial", 19))
                self.question_label.place(relx = 0.17, rely = 0.59)

            elif len(question["text"]) > 72:
                self.question_label.configure(font=("Arial", 16))
                self.question_label.place(relx = 0.2, rely = 0.59)
            else:
                pass

            self.question_label["text"] = question["text"]

            index = 0
            #Acomodo la lista de botones para que la respuesta correcta este al final de la lista.
            for element in question["answers"]:
                if "True" in str(element):
                    index = question["answers"].index(element)
                    break

            element = question["answers"].pop(index)
            new_index = len(question["answers"])
            question["answers"].insert(new_index, element)


            self.copy_list = copy.copy(self.buttons)
            shuffle(self.copy_list)
            tuple_btn_qst = zip(self.copy_list, question["answers"])

            #for button, answer in zip(self.copy_list, question["answers"]):
            for button, answer in tuple_btn_qst:
                button["text"] = answer["text"]
                my_text = button.cget('text')
                button["bg"] = "#1B2732"
                button["fg"]="#EDEFF1"

                if answer["isCorrect"]:
                    var = tk.IntVar()
                    button["command"] = lambda button=button: [self.on_press(button), var.set(1)]
                    button.wait_variable(var)
                    print(self.id_after)
                    self.id_after = self.after(500, self.goto_next_question)
                    print(self.id_after)

                else:
                    button["command"] = lambda button=button: self.answered_wrong(button)
        else:
            messagebox.showerror(message="Ya utilizo este comodin", title="Advertencia")

    def plot(self, question):

        opt = ["A", "B", "C", "D"]
        prb = [75, 8.33, 8.33, 8.33]
        shuffle(prb)
        result = zip(opt, prb)
        data = dict(result)
        courses = list(data.keys())
        values = list(data.values())

        self.fig = Figure(figsize = (4, 3),dpi = 100, facecolor="#1B2732")
        self.plot1 = self.fig.add_subplot(111)
        self.plot1.bar(courses, values, color ='#006CCE',width = 0.4)
        self.plot1.set(ylabel = "(%)")
        self.plot1.spines['bottom'].set_color('#dcdee0')
        self.plot1.spines['top'].set_color('#dcdee0')
        self.plot1.xaxis.label.set_color('#dcdee0')
        self.plot1.tick_params(axis='x', colors='#dcdee0')
        self.plot1.yaxis.label.set_color('#dcdee0')
        self.plot1.tick_params(axis='y', colors='#dcdee0')
        self.plot1.set_facecolor("#1B2732")
        self.fig.savefig('Dependencies\plot.png')

        path = 'Dependencies/plot.png'
        check_file = os.path.isfile(path)
        if check_file == True:
            self.image_prb = PIL.Image.open("Dependencies\plot.png")

            # Resize the image using resize() method
            self.resize_image_prb = self.image_prb.resize((300, 300))

            self.img_prb = ImageTk.PhotoImage(self.resize_image_prb)

            self.label_bg_prb = tk.Label(self.frm, image=self.img_prb, bg="#1B2732", highlightthickness = 0, bd = 0)
            self.label_bg_prb.image = self.img_prb
            self.label_bg_prb.pack()
            print("Estoy aqui")
        else:
            print("No se genero imagen")

    def on_closing(self, event=0):
        if messagebox.askokcancel("Eliminar", "Desea eliminar la sesion?"):
            path = 'Dependencies/plot.png'
            check_file = os.path.isfile(path)
            if check_file == True:
                self.frm.destroy()
                os.remove(path)
            else:
                pass
            self.son_1.pause()
            if self.id_after is not None:
                self.after_cancel(self.id_after)  # Cancel the scheduled after event
                self.id_after = None
            else:
                pass
            self.destroy()


def main(root, count):
    filename = r"Dependencies\preguntas.txt"
    columns = defaultdict(list)
    count_line = 0

    with open(filename, 'r', encoding="latin1" ) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            count_line+=1
            for i in range(len(row)):
                columns[i].append(row[i])

    if count_line >= 15:
        columns = dict(columns)
        QST = []
        for i in range(len(columns[0])):
            if columns[5][i].replace(" ", "") == "A":
                var = {
                "text": str(columns[0][i]),
                "answers": [
                    {
                        "text": str(columns[1][i]),
                        "isCorrect": True
                    },
                    {
                        "text": str(columns[2][i]),
                        "isCorrect": False
                    },
                    {
                        "text": str(columns[3][i]),
                        "isCorrect": False
                    },
                    {
                        "text": str(columns[4][i]),
                        "isCorrect": False
                    }
                ],
                "level": str(columns[6][i]),
                "Correct": str(columns[5][i])
            }
                QST.append(var)

            elif columns[5][i].replace(" ", "") == "B":
                var = {
                "text": str(columns[0][i]),
                "answers": [
                    {
                        "text": str(columns[1][i]),
                        "isCorrect": False
                    },
                    {
                        "text": str(columns[2][i]),
                        "isCorrect": True
                    },
                    {
                        "text": str(columns[3][i]),
                        "isCorrect": False
                    },
                    {
                        "text": str(columns[4][i]),
                        "isCorrect": False
                    }
                ],
                "level": str(columns[6][i]),
                "Correct": str(columns[5][i])
            }
                QST.append(var)

            elif columns[5][i].replace(" ", "") == "C":
                var = {
                "text": str(columns[0][i]),
                "answers": [
                    {
                        "text": str(columns[1][i]),
                        "isCorrect": False
                    },
                    {
                        "text": str(columns[2][i]),
                        "isCorrect": False
                    },
                    {
                        "text": str(columns[3][i]),
                        "isCorrect": True
                    },
                    {
                        "text": str(columns[4][i]),
                        "isCorrect": False
                    }
                ],
                "level": str(columns[6][i]),
                "Correct": str(columns[5][i])
            }
                QST.append(var)

            elif columns[5][i].replace(" ", "") == "D":
                var = {
                "text": str(columns[0][i]),
                "answers": [
                    {
                        "text": str(columns[1][i]),
                        "isCorrect": False
                    },
                    {
                        "text": str(columns[2][i]),
                        "isCorrect": False
                    },
                    {
                        "text": str(columns[3][i]),
                        "isCorrect": False
                    },
                    {
                        "text": str(columns[4][i]),
                        "isCorrect": True
                    }
                ],
                "level": str(columns[6][i]),
                "Correct": str(columns[5][i])
            }
                QST.append(var)
            else:
                print("EXCEPCION")


        application = Application(QST,count, root)
        application.mainloop()

        return 0
    else:
        messagebox.showerror(message="Debe existir un minimo de 15 preguntas para poder jugar", title="Advertencia")

#if __name__ == "__main__":
def callback(root, count):
    import sys
    sys.exit(main(root, count))
"""
