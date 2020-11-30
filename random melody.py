import random
from playsound import playsound
import keyboard
import time

path = 'D://Meus Documentos/Desktop/Beats/notes/' #caminho da pasta com as notas
i = 0

def note(x):
    if x == 1:
        playsound(path + 'c.mp3')
        print('c')
    
    if x == 2:
        playsound(path + 'd.mp3')
        print('d')
    
    
    if x == 3:
        playsound(path + 'e.mp3')
        print('e')
    
    
    if x == 4:
        playsound(path + 'f.mp3')
        print('f')
    
    
    if x == 5:
        playsound(path + 'g.mp3')
        print('g')
    
    
    if x == 6:
        playsound(path + 'a.mp3')
        print('a')
    

    if x == 7:
        playsound(path + 'b.mp3')
        print('b')
    

    if x == 8:
        playsound(path + 'c2.mp3')
        print('c')
    

while True:
    
    while i <= 7:
        time.sleep(1)

        note(random.randint(1,8))
        i += 1

    break