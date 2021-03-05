def vincente(verdetto, utente, nome):
    if verdetto == ('Sasso') and utente == (3):
        print('Hai perso! Mi dispiace! ' + nome)
    if verdetto == ('Sasso') and utente == (2):
        print('Hai vinto! Congratulazioni! ' + nome)
    if verdetto == ('Sasso') and utente == (1):
        print('Pareggio! ' + nome)
    if verdetto == ('Carta') and utente == (1):
        print('Hai perso! Mi dispiace! ' + nome)
    if verdetto == ('Carta') and utente == (3):
        print('Hai vinto! Congratulazioni! ' + nome)
    if verdetto == ('Carta') and utente == (2):
        print('Pareggio! ' + nome)
    if verdetto == ('Forbice') and utente == (1):
        print('Hai vinto! Congratulazioni! ' + nome)
    if verdetto == ('Forbice') and utente == (2):
        print('Hai perso! Mi dispiace! ' + nome)
    if verdetto == ('Forbice') and utente == (3):
        print('Pareggio! ' + nome)