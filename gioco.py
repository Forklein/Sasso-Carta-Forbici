import time
import random
from vincitore import *

print('Ciao, questo gioco è stato realizzato da Forklein!')
time.sleep(3)
nome= input('Inserisci il tuo nome: ')
print('Ciao '+ nome + ' è il momento di giocare!')
time.sleep(5)
print('-1)Sasso\n-2)Carta\n-3)Forbice')

computer = [
    'Sasso',
    'Carta',
    'Forbice'
]

scelta = True
while scelta == True:
    try:
        utente = int(input('Seleziona la tua scelta: '))        
        if utente == (1):
            print('Hai selezionato Sasso')
            verdetto = random.choice(computer)
            print('Il computer ha selezionato ' + verdetto)
            vincente(verdetto, utente, nome)
            time.sleep(10)
            break
        elif utente == (2):
            print('Hai selezionato Carta')
            verdetto = random.choice(computer)
            print('Il computer ha selezionato ' + verdetto)
            vincente(verdetto, utente, nome)
            time.sleep(10)
            break
        elif utente == (3):
            print('Hai selezionato Forbice')
            verdetto = random.choice(computer)
            print('Il computer ha selezionato ' + verdetto)
            vincente(verdetto, utente, nome)
            time.sleep(10)
            break
        else:
            print('Ehy furbetto ! Riprova !')
            continue
    except ValueError:
        print('Ma cosa stai scrivendo?!')
        continue