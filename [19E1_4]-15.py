#Escreva uma função em Python que, dado um número PID, imprima o nome do usuário proprietário, o tempo de criação e o uso de memória em KB
import psutil,math,time

def bytes_to_kbyte(pers):
    mem = psutil.virtual_memory()
    return math.ceil(((pers*mem.total)/100)/1000)

#print(psutil.pids()[0])
input = int(input('numero do PID'))
p = psutil.Process(input)

print(p.username())
print(time.ctime(p.create_time()))
print(bytes_to_kbyte(p.memory_percent()),'Kb')