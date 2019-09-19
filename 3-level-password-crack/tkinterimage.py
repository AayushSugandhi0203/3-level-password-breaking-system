import image_slicer
from PIL import ImageDraw, ImageFont
import cv2
import tkinter as tk
# tk checkbutton frame checkbox entry mainloop listbox menu 
#backgroundcolor command font image width height title 
tiles = image_slicer.slice('C://Users//TCD//Desktop//DP3//x.jpg', 4, save=False)
print(tiles)
#cv2.imshow('lion',C://Users//TCD//Desktop//DP3//x.jpg)

for tile in tiles:
    overlay = ImageDraw.Draw(tile.image)
    overlay.text((5, 5), str(tile.number), (255, 255, 255),
                 ImageFont.load_default())

image_slicer.save_tiles(tiles)
import numpy as np
import PIL
 
img1 = PIL.Image.open('C://Users//TCD//Desktop//DP3//pic1.png')
width, height = img1.size 
img1 = img1.resize((width//4, height//4))
img1.save("img1.png")

img2 = PIL.Image.open('C://Users//TCD//Desktop//DP3//pic2.png')
width, height = img2.size 
img2 = img2.resize((width//4, height//4))
img2.save("img2.png")

img3 = PIL.Image.open('C://Users//TCD//Desktop//DP3//pic3.png')
width, height = img3.size 
img3 = img3.resize((width//4, height//4))
img3.save("img3.png")

img4 = PIL.Image.open('C://Users//TCD//Desktop//DP3//pic4.png')
width, height = img4.size 
img4 = img4.resize((width//4, height//4))
img4.save("img4.png")

list_im = ['img4.png','img2.png','img1.png','img3.png']
imgs    = [ PIL.Image.open(i) for i in list_im ]
# pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )

# save that beautiful picture
imgs_comb = PIL.Image.fromarray( imgs_comb)
imgs_comb.save( 'Trifecta.jpg' ) 
#img = cv2.imre
img2 = PIL.Image.open('Trifecta.jpg')
img = cv2.imread('C://Users//TCD//Desktop//DP3//Trifecta.jpg',1)
cv2.imshow('Attach',img)
print("Now give correct order:")



from tkinter import *
import tkinter.messagebox as box

def dialog1():
    username=entry1.get()
    
    if (username == '4213' ):
        box.showinfo('info','Correct Login')
    else:
        box.showinfo('info','Invalid Login')


window = Tk()
window.title('Level2 password')

frame = Frame(window)

Label1 = Label(window,text = 'Enter Your Answer')
Label1.pack(padx=15,pady= 5)

entry1 = Entry(window,bd =5)
entry1.pack(padx=15, pady=5)








btn = Button(frame, text = 'Check Answer',command = dialog1)


btn.pack(side = RIGHT , padx =5)
frame.pack(padx=100,pady = 19)
window.mainloop()

cv2.waitKey(0)
cv2.destroyAllWindows()
