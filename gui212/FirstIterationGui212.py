import tkinter
from tkinter import * 
from PIL import ImageTk, Image


root = Tk()
root.geometry("700x500+700+500")

image = Image.open("menyferdig.png")
test = ImageTk.PhotoImage(image)


ImageLabel = Label(root, image=test)

non_purchased_prod =Label(root, text="Non-purchased Products") 
purchased_prod = Label(root, text="Purchased Products")


Liste1 = Label(root, text="""Potato,420
Beef, 911 [MISSING]
Steak,666
Aspargus, 1301
Milk, 699 [MISSING]
Canned Chickpeas, 42069
Brown cheese, 13""",
borderwidth=2, relief='solid',justify="left", padx=40,pady=70,)



Liste2 = Label(root, text="""Kneibrød,91101
Apple,422 [MISSING]
Pear,5387
Pear, 5387
Bolle, 404 [MISSING]
Coca-cola, 500
Sprite, 924
Pringles, 632"""
, borderwidth=2,relief='solid',padx=50,pady=63)

Generate = Label(root, text="Generate document", borderwidth=2,relief='solid',padx=10,pady=10)

button_quit = Button(root,text="EXIT",borderwidth=2,padx=10,pady=5,command=root.quit)


ImageLabel.place(x=300,y=0)
non_purchased_prod.place(x=185,y=70)
purchased_prod.place(x=450,y=70)
Liste1.place(x=150, y=100)
Liste2.place(x=400, y=100)
Generate.place(x=100, y=400)
button_quit.place(x=500, y=400)


root.mainloop()

