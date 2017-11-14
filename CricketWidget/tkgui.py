import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from tkinter import ttk
from pycricbuzz import Cricbuzz
import sys
c = Cricbuzz()


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "CricBuzz")

        self.title_font = tkfont.Font(family='Helvetica', size=8, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Page1, Page2, Page3):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.title_font = tkfont.Font(family='Helvetica', size=15, weight="bold", slant="italic")
        label = tk.Label(self, text="CricBuzz", font=controller.title_font)
        label.pack()
        data = []
        length = c.matches()
        size = len(length)
        
        try:
            iD = length[0]['id']
            src = length[0]['srs']
            mat = length[0]['mchdesc']
            data.append(iD)
            var = str(1) + " : " + " -- " + src +  " " + mat
            button0 = ttk.Button(self, text=var,
                            command=lambda: controller.show_frame("Page1"))
            button0.pack(fill="x")
        except:
            button0 = ttk.Button(self, text="No Matches",
                            command=lambda: controller.show_frame("Page1"))
            button0.pack(fill="x")
        try:
            iD = length[1]['id']
            src = length[1]['srs']
            mat = length[1]['mchdesc']
            data.append(iD)
            var = str(2) + " : " + " -- " + src +  " " + mat
            
            button1 = ttk.Button(self, text=var,
                            command=lambda: controller.show_frame("Page2"))
            button1.pack(fill="x")
        except:
            button1 = ttk.Button(self, text="No Matches",
                            command=lambda: controller.show_frame("Page2"))
            button1.pack(fill="x")
        try:
            iD = length[2]['id']
            src = length[2]['srs']
            mat = length[2]['mchdesc']
            data.append(iD)
            var = str(3) + " : " + " -- " + src +  " " + mat
            
            button2 = ttk.Button(self, text=var,
                            command=lambda: controller.show_frame("Page3"))
            button2.pack(fill="x")
        except:
            button2 = ttk.Button(self, text="No Matches",
                            command=lambda: controller.show_frame("Page3"))
            button2.pack(fill="x")
        try:
            iD = length[3]['id']
            src = length[3]['srs']
            mat = length[3]['mchdesc']
            data.append(iD)
            var = str(4) + " : " + " -- " + src +  " " + mat
            
            button3 = ttk.Button(self, text=var,
                            command=lambda: controller.show_frame("Page4"))
            button3.pack(fill="x")
        except:
            button3 = ttk.Button(self, text="No Matches",
                            command=lambda: controller.show_frame("Page4"))
            button3.pack(fill="x")
        try:
            iD = length[4]['id']
            src = length[4]['srs']
            mat = length[4]['mchdesc']
            data.append(iD)
            var = str(5) + " : " + " -- " + src +  " " + mat
            
            button4 = ttk.Button(self, text=var,
                            command=lambda: controller.show_frame("Page5"))
            button4.pack(fill="x")
        except:
            button4 = ttk.Button(self, text="No Matches",
                            command=lambda: controller.show_frame("Page5"))
            button4.pack(fill="x")
            
    


class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        


class Page2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        
        
class Page3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 3", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

class Page4(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 4", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

class Page5(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 5", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
