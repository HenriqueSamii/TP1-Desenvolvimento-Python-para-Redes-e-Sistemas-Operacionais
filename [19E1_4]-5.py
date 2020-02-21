#Escreva um programa que indique se um arquivo existe ou não. Caso exista, indique se é realmente um arquivo ou não.
import os

arquivoInput = input('Nome do arquivo - ')
camingoAbsoluto = os.path.abspath(arquivoInput)

if os.path.exists(camingoAbsoluto):
    if os.path.isfile(camingoAbsoluto):
        print(arquivoInput, 'é um arquivo')
    else:
        print(arquivoInput, 'não é um arquivo')
else:
     print(arquivoInput, 'não existe')