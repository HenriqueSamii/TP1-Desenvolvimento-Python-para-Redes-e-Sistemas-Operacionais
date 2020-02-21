#Escreva um programa que mostre as datas de criação e modificação de cada arquivo em um diretório
import os,time

diretorioInput = input('Caminho do diretório - ')
#camingoAbsoluto = os.path.abspath(diretorioInput)

arrayDir = os.listdir(diretorioInput)

for i in arrayDir:
    if (os.path.isfile(i)):
        print("Arquivo",i,"path absoluto",os.path.abspath(i))
        print("Ultima modificação", time.ctime(os.stat(i).st_mtime))