from visionrostros import *
from imagenFase import *
from facestrain import *
from recognizer import *
from sentimientos import *
from faces import *
from quadtree import *
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

def main():
    print("Sea Bienvenido al proyecto Quad Emotional Faces Tree")
    print("Que codigo desea probar:")
    print("1. Para el reconocimiento por camara")
    print("2. Para el reconocimiento de imagenes")
    print("3. Sentimientos")
    print("4. Creación Quad Tree")
    op=input()
    if(op=="1"):
        trainfaces()
        print("Para cerrar la camara precionar la tecla q")
        capture()

    if(op=="2"):
        print("Primero deje las imagenes que desea analizar en la carpeta de Imagenes Analizar ")
        print("Desea ver los sub rostros?Y/N")
        opc=input()
        #limpieza de imagenes de rostros de pruebas pasadas
        finalizar()
        #Imagenes que se van a analisar
        ruta= ".\Imagenes Analizar"
        num_archivos= ls(ruta)
        #ver rutas de imagenes 
        '''
        for i in num_archivos:
            print(i)
        '''
        num_img=0
        rutas=[]
        for arc in num_archivos:
            rutaImagen = ".\Imagenes Analizar\\"+arc
            rutas.append(rutaImagen)
            imagenAnalizar = cv2.imread(rutaImagen)
            [dataRostros, imagenesRostros] = detectarRostros(imagenAnalizar) 
            if(opc.upper()=="Y"):
                verSubRostros(imagenesRostros)
            crearRostros(imagenAnalizar, dataRostros)
            
            verRostosImagen(imagenAnalizar, dataRostros)
            num_img+=len(dataRostros)
        rostros=[]
        
        for i in ls(".\\"):
            for n in range(0,num_img):

                if(i=="ROI_{}.png".format(n)):
                    rostros.append(i)
        
        #entrenador de rostros
        trainfaces()

        #Analizar rostros
        resultados=[]
        num_rostros=len(rutas)
        for i in range (0,num_rostros):
            resultados.append(reconocedor(rutas[i]))
        num_resultados=len(resultados)
        num_foto=0
        for i in range(0,num_resultados):
            num_foto+=1
            print("Rostros en foto #"+str(num_foto)+str(resultados[i]))


    

    if(op=="3"):

        print("De la foto de quien quieres saber sus emociones: ")
        persona = input()
        emociones_(persona)


    if(op=="4"):

        print("La foto de quien será analizada y se le creará su QuadTree: ")
        persona = input()
        quad(persona)



    if(op!="1" and op!="2" and op!="3" and op!="4"):
        print("ELIGIO UNA OPCION ERRONEA EL CODIGO SE VOLVERA A EJECUTAR")
        main()


    


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

if __name__ == '__main__':
    main()
    