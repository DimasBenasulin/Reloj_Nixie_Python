from tkinter import *
from PIL import Image, ImageTk

def mostrarNumero(a=7, b=3, c=7):

    num1 = "nixie_" + str(a) + ".bmp"
    num2 = "nixie_" + str(b) + ".bmp"
    num3 = "nixie_" + str(c) + ".bmp"

    root = Tk()
    root.title("Nixies")
    root.iconbitmap('nixie_ico_1.ico')

    root.geometry('230x114')
    canvas = Canvas(root,width=230,height=114)
    canvas.pack()

    pilImage = Image.open(num1)
    image = ImageTk.PhotoImage(pilImage)
    imagesprite = canvas.create_image(40,60,image=image)
   
    pilImage2 = Image.open(num2)
    image2 = ImageTk.PhotoImage(pilImage2)
    imagesprite2 = canvas.create_image(115,60,image=image2)

    pilImage3 = Image.open(num3)
    image3 = ImageTk.PhotoImage(pilImage3)
    imagesprite3 = canvas.create_image(190,60,image=image3)

    root.mainloop()

# mostrarNumero()



