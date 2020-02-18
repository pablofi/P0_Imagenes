import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
from scipy import ndimage

######Variables Ejercicio 1
img = Image.open('/Users/pablomartineztellez/Desktop/10º/Imagenes/Practicas/Practica0/Imagenes2/1.jpg')
imgE1 = cv2.imread('/Users/pablomartineztellez/Desktop/10º/Imagenes/Practicas/Practica0/Imagenes2/1.jpg')

imgCR = imgE1.copy()
imgCB = imgE1.copy()
imgCG = imgE1.copy()

######Variables Ejercicio 2

imgE2 = cv2.imread('/Users/pablomartineztellez/Desktop/10º/Imagenes/Practicas/Practica0/Imagenes2/retinaRGB.jpg')

######Variables Ejercicio 2

imgE3 = cv2.imread('/Users/pablomartineztellez/Desktop/10º/Imagenes/Practicas/Practica0/Imagenes2/retinaRGB.jpg')

######Variables Ejercicio 2

imgE4 = cv2.imread('/Users/pablomartineztellez/Desktop/10º/Imagenes/Practicas/Practica0/Imagenes2/retinaRGB.jpg')


######Variables Ejercicio 8

imgE8 = cv2.imread('/Users/pablomartineztellez/Desktop/10º/Imagenes/Practicas/Practica0/Imagenes2/cta_scan_index.bmp')

######Variables Ejercicio 9

imgE9 = Image.open('/Users/pablomartineztellez/Desktop/10º/Imagenes/Practicas/Practica0/Imagenes2/mri.jpg')


####################Codigo Ejercicio 1
print("\nFormato de la Imagen:", img.format, "\nModelo de Color:", img.mode, "\nTamaño de la Imagen:", img.size, "\nTipo de datos:", imgE1.dtype)

plt.figure("Ejercicio 1", figsize = (10,5))

###########Imagen Original RGB
plt.subplot(232) #Indicamos la pocsicion de la iagen (nfilas, ncolumnas, casilla)
plt.title('RGB')#Ponemos titulo a la imagen
plt.imshow(cv2.cvtColor(imgE1, cv2.COLOR_BGR2RGB)) #convertimos  la imagen  de BGR a RGB para pode visualizarla en RGB

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

####################Codigo Ejercicio 2.1

imgE2 = cv2.resize(imgE2, (0, 0), None, 1, 1)

imgE2Gr = cv2.cvtColor(imgE2, cv2.COLOR_RGB2GRAY)
gr = np.hstack((imgE2, cv2.cvtColor(imgE2Gr, cv2.COLOR_GRAY2BGR)))
cv2.imshow('RGB a Escala de grises', gr)
cv2.waitKey(0)
cv2.destroyAllWindows()

####################Codigo Ejercicio 2.2

imgE3 = cv2.resize(imgE3, (0, 0), None, 1, 1)

imgE3yuv = cv2.cvtColor(imgE3, cv2.COLOR_RGB2YUV)
yuv = np.hstack((imgE3,cv2.cvtColor(imgE3yuv,cv2.COLOR_YUV2RGB)))
cv2.imshow("RGB a YUV", yuv)
cv2.waitKey(0)
cv2.destroyAllWindows()

####################Codigo Ejercicio 2.3

imgE4 = cv2.resize(imgE4, (0, 0), None, 1, 1)

imgE4hsv = cv2.cvtColor(imgE4, cv2.COLOR_RGB2HSV)
hsv = np.hstack((imgE4,cv2.cvtColor(imgE4hsv,cv2.COLOR_HSV2RGB)))
cv2.imshow("RGB a HSV", hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()


####################Codigo Ejercicio 3



cut = (100, 100, 700, 500)

# Obtener de la imagen original la región de la caja
region = Image.crop(cut)

region.show()
region.size   # Mostrar tamaño de imagen final 600x400

# Guarda la imagen obtenida con el formato JPEG.
#region.save("region.jpg")


####################Codigo Ejercicio 8

cv2.imshow("cta_scan_index.bmp normal", imgE8)

r45 = ndimage.rotate(imgE8, 45)
cv2.imshow("cta_scan_index.bmp 45 grados", r45)

r90 = ndimage.rotate(imgE8, 90)
cv2.imshow("cta_scan_index.bmp 90 grados", r90)

r180 = ndimage.rotate(imgE8, 180)
cv2.imshow("cta_scan_index.bmp 180 grados", r180)

cv2.waitKey(0)
cv2.destroyAllWindows()


####################Codigo Ejercicio 9

imgE9Gr = imgE9.convert('L')
imgE9Gr.show()
imgE9Gr.save('/Users/pablomartineztellez/Desktop/10º/Imagenes/Practicas/Practica0/Imagenes2/mriGris.tiff')











