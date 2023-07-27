#===========================================================================================================================================================
from tkinter import (ttk, Tk)
from tkinter.ttk import *
#===========================================================================================================================================================
class GUI:
    def __init__(self, master):
        self.master = master
        self.x = 0
        self.TheMainGUI()

    def TheMainGUI(self):
        self.master.geometry('800x150')
        self.master.title('GUI')
        #===========================================================================================================================================================
        self.frame_label = Frame(self.master)
        self.frame_label.pack()
        Label(self.frame_label, text='My Label', font=('Times', 30)).grid(row=0, column=2)
        #===========================================================================================================================================================
        self.frame_menu = Frame(self.master)
        self.frame_menu.pack()
        self.frame_menu.config(padding=(50, 15))
        #===========================================================================================================================================================        #---------------------------------------------------------------------------------------------------------------------------
        self.style = Style()
        self.style.configure('TButton', font=('calibri', 20, 'bold'), borderwidth='4')
        self.style.map('TButton', foreground=[('active', '!disabled', 'green')], background=[('active', 'black')])
        #===========================================================================================================================================================
        self.buttons = Frame(self.master)
        self.buttons.pack()
        #===========================================================================================================================================================
        Button(self.buttons, text="Face_Restoration", command=self.ptn1).grid(row=0, column=0, columnspan=1, padx=5, pady=5)
        Button(self.buttons, text="Full Analysis", command=self.ptn2).grid(row=0, column=1, columnspan=1, padx=5, pady=5)
        Button(self.buttons, text="3D Modeling", command=self.ptn3).grid(row=0, column=2, columnspan=1, padx=5, pady=5)
        Button(self.buttons, text="Cancel", command=self.ptn4).grid(row=0, column=3, columnspan=1, padx=5, pady=5)
    #===========================================================================================================================================================
    def ptn1(self):
        self.x = 1
        self.master.quit()
    def ptn2(self):
        self.x = 2
        self.master.quit()
    def ptn3(self):
        self.x = 3
        self.master.quit()
    def ptn4(self):
        self.master.quit()
    def run(self):
        return self.x

#===========================================================================================================================================================        

# mainWindow = Tk()
# gg = GUI(mainWindow)
# mainWindow.mainloop()
# print(gg.run())
# print(9999)
