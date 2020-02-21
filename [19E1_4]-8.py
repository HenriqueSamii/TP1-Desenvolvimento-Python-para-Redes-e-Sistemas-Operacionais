#Escreva um programa que mostre a quantidade de bytes (em KB) de cada arquivo em um diretório.
import os

diretorioInput = input('Caminho do diretório - ')
#camingoAbsoluto = os.path.abspath(diretorioInput)

arrayDir = os.listdir(diretorioInput)

for i in arrayDir:
    if (os.path.isfile(i)):
        print("Arquivo",i,"path absoluto",os.path.abspath(i))
        print("Tamanho em Kilobytes", os.stat(i).st_size/1000)