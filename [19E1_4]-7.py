#Escreva um programa que imprima apenas o caminho absoluto de um arquivo com nome relativo. A impressão não deve conter o nome do arquivo, apenas o caminho
import os

arquivoInput = input('Nome do arquivo - ')
camingoAbsoluto = os.path.abspath(arquivoInput)

t = os.path.split(camingoAbsoluto)

print(t[0])