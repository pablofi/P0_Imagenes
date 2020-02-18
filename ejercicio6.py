####Ejrcico 3
"""from PIL import Image

im = Image.open(r'/Users/pablomartineztellez/Desktop/10º/Imagenes/Practicas/Practica0/Imagenes2/corte1.jpg')
imE3c = im.copy()
width, height = imE3c.size

left = width - 245    #X arriba
top = height -250   #Y arriba
right =  width
bottom = height

im1 = imE3c.crop((left, top, right, bottom))

im1.show()
im.show()
"""


import cv2
import numpy as np
bgr = np.zeros((200,800,3),dtype=np.uint8)

bgr[:100, :200] = (255,0,0) #azul
bgr[:100, 200:400] = (0,255,0) #Verde
bgr[:100, 400:600] = (0,0,255) #Rojo
bgr[:100, 600:800] = (0,255,255) #amarillo
bgr[100:200, :200] = (255,0,255)# Magenta
bgr[100:200, 200:400] = (255,255,0)# cyan
bgr[100:200, 400:600] = (255,255,255)#Blanco
bgr[100:200, 600:800] = (0)#Negro

cv2.imshow('Paleta de Colores RGB',bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()