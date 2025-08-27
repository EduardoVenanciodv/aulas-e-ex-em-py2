for c in range(0 , 5):
    frase = str(input('\033[33mDigite uma frase:\033[m')).lower().replace(" ", "")
    frase1 = frase
    inve = frase[::-1]
    
    if frase1 == inve:
        print('\033[32mPalíndromo\033[m')
    else:
        print('\033[31mNão é Palíndromo\033[m')\
