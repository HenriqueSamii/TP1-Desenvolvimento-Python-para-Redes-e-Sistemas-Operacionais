#Escreva um programa que obtenha um nome de um arquivo texto do usuário e crie um processo, usando o módulo ‘os’, de bloco de notas (notepad) para abri-lo.
import os

inputUser = input("Dejite o texto-")
if os.path.exists(inputUser):
    morada = os.path.abspath(inputUser)
    print(morada)
    os.chdir(morada)
    arrayDir = os.listdir()

    if (os.path.isfile(morada)):
        os.startfile(os.path.split(morada)[1])