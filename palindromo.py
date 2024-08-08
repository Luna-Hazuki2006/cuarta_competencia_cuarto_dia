from unidecode import unidecode

def palindromo(oracion : str):
    for esto in oracion: 
        if not esto.isalpha() or esto.isspace(): 
            oracion = oracion.replace(esto, '')
    for i in range(1, len(oracion) // 2 + 1): 
        primer = oracion[i - 1]
        segundo = oracion[-i]
        if unidecode(primer.lower()) !=  unidecode(segundo.lower()): 
            print(False)
            return 
    print(True)

def main(): 
    oracion = str(input('Escribe la frase que quieres ver si es palíndroma: '))
    palindromo(oracion)

if __name__ == '__main__': 
    main()