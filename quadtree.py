from grafica import GraphPro as g
from grafica import GraphPro
from grafos import Graph
import os

from numpy import double
from visionrostros import *
from imagenFase import *
from facestrain import *
from recognizer import *
from sentimientos import *
from faces import *
from quad import *
from os import scandir, getcwd
from os import remove
import cv2
import sys
import re
import os
#import face_recognition
from PIL import Image
#pip install cmake
#pip instal fase_recognition
#pip install scikit_igamge
#pip install twine
#pip install wheel
#install cmake from https://github.com/Kitware/CMake/releases/download/v3.17.2/cmake-3.17.2.zip
#poner cmake en variables de entorno

def quad(image_):
    
        
    #limpieza de imagenes de rostros de pruebas pasadas
    finalizar()
    #Imagenes que se van a analisar
    ruta= "./Imagenes Analizar/"+str(image_)+".jpg"
    

    
    
    imagenAnalizar = cv2.imread(ruta)
    [dataRostros, imagenesRostros] = detectarRostros(imagenAnalizar) 
    
    crearRostros(imagenAnalizar, dataRostros)
    
    verRostosImagen(imagenAnalizar, dataRostros)
    
    
    print("Presencia de rostro OK")
    
    #entrenador de rostros
    trainfaces()

    #Analizar rostros
    resultados=""
    
    resultados = str((reconocedor(ruta))).replace('[', '').replace(']', '').replace('\'', '')
    
    
    print("Rostros en foto "+resultados)

    quad = QuadTree("Detectado")

    g1 = quad.dato

    quad.nuevo_("Cristian", "Daniel", "Alejandro", "Miguel")

    g1_1 = quad.raiz.uno.dato
    g1_2 = quad.raiz.dos.dato
    g1_3 = quad.raiz.tres.dato
    g1_4 = quad.raiz.cuatro.dato

    if(resultados == 'Cristian' or resultados == 'Daniel' or resultados == 'Alejandro' or resultados == 'Miguel'):

        print("Individuo encontrado OK")

        

        analisis_ = emociones_(image_)

    miedo_ = double(analisis_[0])
    felicidad_ = double(analisis_[1])
    neutral_ = double(analisis_[2])
    tristeza_ = double(analisis_[3])

    quad2 = quad.buscar_(resultados)

    gf = quad2.raiz.dato

    quad2.nuevo_("Miedo = "+str(miedo_), "Felicidad = "+str(felicidad_), "Neutral = "+str(neutral_), "Tristeza = "+str(tristeza_))

    

    sentimiento = max(miedo_, felicidad_, neutral_, tristeza_)

    if(quad2.raiz.uno.dato.replace("Miedo = ", "")==str(sentimiento)):

        quad2.raiz.uno.dato = quad2.raizuno.dato+" Final"


    if(quad2.raiz.dos.dato.replace("Felicidad = ", "")==str(sentimiento)):

        quad2.raiz.dos.dato = quad2.raiz.dos.dato+" Final"


    if(quad2.raiz.tres.dato.replace("Neutral = ", "")==str(sentimiento)):

        quad2.raiz.tres.dato = quad2.raiz.tres.dato+" Final"


    if(quad2.raiz.cuatro.dato.replace("Tristeza = ", "")==str(sentimiento)):

        quad2.raiz.cuatro.dato = quad2.raiz.cuatro.dato+" Final"

    g2_1 = quad2.raiz.uno.dato
    g2_2 = quad2.raiz.dos.dato
    g2_3 = quad2.raiz.tres.dato
    g2_4 = quad2.raiz.cuatro.dato

    print("Emocion del rostro OK")

    if(g1_1==gf):
        sources = [g1, g1, g1, g1, g1_1, g1_1, g1_1, g1_1]
        targets = [g1_1, g1_2, g1_3, g1_4, g2_1, g2_2, g2_3, g2_4]
        weights = [5, 5, 5, 5, 5, 5, 5, 5]

    if(g1_2==gf):
        sources = [g1, g1, g1, g1, g1_2, g1_2, g1_2, g1_2]
        targets = [g1_1, g1_2, g1_3, g1_4, g2_1, g2_2, g2_3, g2_4]
        weights = [5, 5, 5, 5, 5, 5, 5, 5]

    if(g1_3==gf):
        sources = [g1, g1, g1, g1, g1_3, g1_3, g1_3, g1_3]
        targets = [g1_1, g1_2, g1_3, g1_4, g2_1, g2_2, g2_3, g2_4]
        weights = [5, 5, 5, 5, 5, 5, 5, 5]

    if(g1_4==gf):
        sources = [g1, g1, g1, g1, g1_4, g1_4, g1_4, g1_4]
        targets = [g1_1, g1_2, g1_3, g1_4, g2_1, g2_2, g2_3, g2_4]
        weights = [5, 5, 5, 5, 5, 5, 5, 5]

    grafo1 = GraphPro(sources, targets, weights, False)


    g = grafo1

    g.print_r()
    g.draw(with_weight=False)
 


    #limpieza de imagenes reciduales
    finalizar()
    
def reajustar(ruta):
    img=Image.open(ruta)
    new_img = img.resize((256,256))
    new_img.save(ruta,'png')
    


def finalizar():
    archivos=ls(".\\")
    ROI_number=0
    for a in archivos:
        if(a=='ROI_{}.png'.format(ROI_number)):
            remove('ROI_{}.png'.format(ROI_number))
            ROI_number+=1


def ls(ruta = getcwd()):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]