palavra = 'animal'
letra_usu = []
chances = 5
ganhou = False

while True:

    #verificar a palavra
    for letra in palavra:
        if letra.lower() in letra_usu:
            print(letra, end='')
        
        else:
            print(" _ ", end='')
    print(f' : você tem {chances} chances')
    tentativa = input('\nescolha uma letra para advinhar: ')
    letra_usu.append(tentativa.lower())

    #retiram as tentativas
    if tentativa.lower() not in palavra.lower():
        chances -=1 

    ganhou=True
    for  letra in palavra:
        if letra.lower() not in letra_usu:
            ganhou = False

    if chances == 0 or ganhou :
            break

if ganhou:
    print(f'n\nParabéns você ganhou, a palavra era: {palavra}')

else:
    print(f'n\n você perdeu! A palavra era: {palavra}')