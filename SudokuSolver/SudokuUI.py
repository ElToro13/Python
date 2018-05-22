import threading
import tkinter as tk
from tkinter import *
from MySudoku import SudokuSolver
import random
import time

root = Tk()
w = 440
h = 450
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

global val
val = ''
global level
level = 0
global colorV
colorV = 'blue'
global colorH
colorH = 'black'
global font
font = 'white'
global buttonbg
buttonbg = 'grey'
label = tk.Label(root, text='').grid(row=0, column=3)


def SelectVal(choice=0):
    gridEasy = ["4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......",
                "52...6.........7.13...........4..8..6......5...........418.........3..2...87.....",
                "6.....8.3.4.7.................5.4.7.3..2.....1.6.......2.....5.....8.6......1....",
                "....7..2.8.......6.1.2.5...9.54....8.........3....85.1...3.2.8.4.......9.7..6....",
                "1...34.8....8..5....4.6..21.18......3..1.2..6......81.52..7.9....6..9....9.64...2",
                "85...24..72......9..4.........1.7..23.5...9...4...........8..7..17..........36.4."]
    gridHard = [".....6....59.....82....8....45........3........6..3.54...325..6.................."]

    gridMeidum = [".6.5.1.9.1...9..539....7....4.8...7.......5.8.817.5.3.....5.2............76..8...",
                  "..5...987.4..5...1..7......2...48....9.1.....6..2.....3..6..2.......9.7.......5..",
                  "3.6.7...........518.........1.4.5...7.....6.....2......2.....4.....8.3.....5.....",
                  "1.....3.8.7.4..............2.3.1...........958.........5.6...7.....8.2...4.......",
                  "6..3.2....4.....1..........7.26............543.........8.15........4.2........7.."]
    global val
    global level
    level = choice
    if level == 0:
        global val
        val = gridEasy[random.randint(0, 5)]
    if level == 1:
        val = gridMeidum[random.randint(0,4)]
    else:
        val = gridHard[0]


def NewValues():
    label = tk.Label(root, text='        ').grid(row=0, column=2)
    global level
    my_thread = threading.Thread(target=SelectVal(level))
    my_thread.start()
    global val
    view = SudokuSolver()
    kk = view.StrToDict(val)
    global colorV
    global colorH
    global buttonbg
    global font
    row = 'ABCDEFGHI'
    digit = '123456789'
    k = 0
    ro = 0
    l = [3, 7]
    m = [4, 8]
    try:
        for i in range(1, 12):

            if i in m:
                for j in range(0, 11):
                    if j in l:

                        button = tk.Button(root, text="", bg=colorV, width=1, height=1)
                        button.grid(row=i, column=j)

                    else:

                        button = tk.Button(root, text=" ", bg=colorV, width=5, height=1)
                        button.grid(row=i, column=j)
            else:

                for j in range(0, 11):
                    if j in l:

                        # tk.Label(self, text=" ", bg="#229954").grid(row=i,column=j)
                        button = tk.Button(root, text=" ", bg=colorH, width=1, height=2)
                        button.grid(row=i, column=j)

                    else:

                        button = tk.Button(root, text=kk[row[ro] + digit[k]], bg=buttonbg, fg=font, width=5, height=2)
                        button.grid(row=i, column=j)
                        k += 1
                ro += 1

            k = 0

    except Exception as e:
        print(e)
    return val


def Sol():
    global val
    global colorV
    global colorH
    global buttonbg
    global font
    label = tk.Label(root, text='Wait.').grid(row=0, column=2)
    start = time.clock()

    prob = SudokuSolver()
    kk = prob.solve(val)
    label = tk.Label(root, text='Done!').grid(row=0, column=2)
    end = time.clock()

    row = 'ABCDEFGHI'
    digit = '123456789'
    k = 0
    ro = 0
    l = [3, 7]
    m = [4, 8]
    try:
        for i in range(1, 12):

            if i in m:
                for j in range(0, 11):
                    if j in l:

                        # tk.Label(self, text=" ", bg="#229954").grid(row=i,column=j)
                        button = tk.Button(root, text="", bg=colorV, width=1, height=1)
                        button.grid(row=i, column=j)

                    else:

                        # tk.Label(self, text=" ", bg="#900C3F").grid(row=i,column=j,ipadx=12)
                        button = tk.Button(root, text=" ", bg=colorV, width=5, height=1)
                        button.grid(row=i, column=j)
            else:

                for j in range(0, 11):
                    if j in l:

                        # tk.Label(self, text=" ", bg="#229954").grid(row=i,column=j)
                        button = tk.Button(root, text=" ", bg=colorH, width=1, height=2)
                        button.grid(row=i, column=j)

                    else:

                        button = tk.Button(root, text=kk[row[ro] + digit[k]], bg=buttonbg, fg=font, width=5, height=2)
                        button.grid(row=i, column=j)
                        k += 1
                ro += 1

            k = 0
        print(float(end - start)*1000)
        labelMin = tk.Label(root, text=str(int(int(end - start) / 60)) + ' M').grid(row=0, column=8)
        labelSec = tk.Label(root, text=str(int(int(end - start) % 60)) + ' S').grid(row=0, column=9)
        labelMili = tk.Label(root, text=str(round(float(end - start), 2)) + ' MS').grid(row=0, column=10)

    except Exception as e:
        print(e)


def Solver():
    my_thread2 = threading.Thread(target=Sol())
    my_thread2.start()


def Theme(foo=0):
    global colorV
    global colorH
    global buttonbg
    global font
    if foo == 0:
        colorV = '#85C1E9'

        colorH = '#A569BD'

        font = '#1C2833'

        buttonbg = '#D0D3D4'

    else:

        colorV = '#273746'

        colorH = '#4A235A'

        font = '#D35400'  # 17202A'

        buttonbg = '#17202A'


menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)

file_menu.add_command(label="Easy", command=lambda: SelectVal(0))
file_menu.add_command(label="Medium", command=lambda: SelectVal(1))
file_menu.add_command(label="Hard", command=lambda: SelectVal(2))
menu_bar.add_cascade(label="File", menu=file_menu)

theme_menu = Menu(menu_bar, tearoff=0)
theme_menu.add_command(label="Dark", command=lambda: Theme(1))
theme_menu.add_command(label="Light", command=lambda: Theme(0))
menu_bar.add_cascade(label="Theme", menu=theme_menu)

root.config(menu=menu_bar)
button = tk.Button(root, text="Sol", bg="#FF5733", width=5, height=1, command=lambda: Solver())
button.grid(row=0, column=0)
button = tk.Button(root, text="New", bg="#FF5733", width=5, height=1, command=lambda: NewValues())
button.grid(row=0, column=1)

root.mainloop()
