import tkinter as tk
import sys
import os
from tkinter import *
from PIL import ImageTk, Image

master = tk.Tk()
master.title('MPS')
master.geometry("700x500+700+500")

#HUSK Å ADDE INFO KNAPP

#code to run the psuedofile
def run():
    os.system('../pseudocode/212projv2.py')

#Logo
image = Image.open("menyferdig.png")
test = ImageTk.PhotoImage(image)
ImageLabel = tk.Label(master, image=test)
ImageLabel.place(x=300,y=10)


#infoKnapp
info = Image.open("Info.png")
resizedImg = info.resize((30, 30), Image.ANTIALIAS)
test2 = ImageTk.PhotoImage(resizedImg)
ImageLabel2 = tk.Label(master, image=test2)
ImageLabel2.place(x=650,y=10)

#These are all the text labels
antall = tk.Label(master, text="Antall", padx=30)
antall.place(x=160,y=85)
antallVal = tk.Label(master, text="""5 stk
2 stk
4 stk
6 stk
2 stk
1 stk
4 stk
1 stk
4 stk
3 stk
2 stk
1 stk
6 stk""")
antallVal.place(x=160, y=120)

vare = tk.Label(master, text="Vare", padx=30)
vare.place(x=250, y=85)
vareVal = tk.Label(master, text="""Potato
Kneipbrød
Pear
Coca-Cola 
Sprite
Pringles
Beef
Steak
Aspargus
Milk
Canned Chickpeas
Brown Cheese
Apple""")
vareVal.place(x=215,y=120)

kode = tk.Label(master, text="Produktkode",padx=30)
kode.place(x=320, y=85)
kodeVal = tk.Label(master, text="""420
91101
5387
500
924
632
911
666
1031
650
404
13
422""")
kodeVal.place(x=360, y=120)

erstatt = tk.Label(master, text="Erstatt", padx=30)
erstatt.place(x=434, y=85)
erstattVal = tk.Label(master, text="""j
j
j
n
n
n
j
j
n
j
j
j
j""")
erstattVal.place(x=460, y=120)

#two buttons, generate document and exit button
generate = Button(master,text="Generate document", borderwidth=2,relief='solid',padx=10,pady=10,
command=run)
generate.place(x=100,y=370)

button_quit = Button(master,text="EXIT",borderwidth=2,relief='solid',padx=10,pady=5,command=master.quit)
button_quit.place(x=530,y=375)

myWidgets = [antall,antallVal,kode,kodeVal,vare,vareVal,erstatt,erstattVal]
 # List of widgets to change colour
for wid in myWidgets:
    wid.configure(bg = "#c0c0c0", padx=45,pady=8)


tk.mainloop()
