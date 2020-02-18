import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

img = Image.open('/Users/pablomartineztellez/Desktop/10º/Imagenes/Practicas/Practica0/Imagenes2/retinaRGB.jpg')
img1 = cv2.imread('/Users/pablomartineztellez/Desktop/10º/Imagenes/Practicas/Practica0/Imagenes2/retinaRGB.jpg')

imgCR = img1.copy()
imgCB = img1.copy()
imgCG = img1.copy()


print("\normato de la Imagen:", img.format, "\nModelo de Color:", img.mode, "\nTamaño de la Imagen:", img.size, "\nTipo de datos:", img1.dtype)

plt.figure("Ejercicio 1", figsize = (10,5))
plt.subplot(232)
plt.title('RGB')
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)) #convertimos  la imagen  de BGR a RGB para pode visualizarla en RGB

############Canal Rojo
imgCR[:,:,0] = 0 #capa 0 (Azul) le pasamos 0 para quitarla
imgCR[:,:,1] = 0 #capa 1 (Verde) le pasamos 0 para quitarla
plt.subplot(234)
plt.title("Canal Rojo")
plt.imshow(cv2.cvtColor(imgCR, cv2.COLOR_BGR2RGB))


############Canal Verde
imgCG[:,:,0] = 0 #capa 0 (Azul) le pasamos 0 para quitarla
imgCG[:,:,2] = 0 #capa 2 (Rojo) le pasamos 0 para quitarla
plt.subplot(235)
plt.title("Canal Verde")
plt.imshow(cv2.cvtColor(imgCG, cv2.COLOR_BGR2RGB))

############Canal Azul
imgCB[:,:,1] = 0 #capa 0 (Verde) le pasamos 0 para quitarla
imgCB[:,:,2] = 0 #capa 2 (Rojo) le pasamos 0 para quitarla
plt.subplot(236)
plt.title("Canal Azul")
plt.imshow(cv2.cvtColor(imgCB, cv2.COLOR_BGR2RGB))
plt.show()






