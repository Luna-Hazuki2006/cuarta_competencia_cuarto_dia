from unidecode import unidecode

LISTA = [
    ('A', '·—'), ('B', '—···'), ('C', '—·—·'), 
    ('D', '—··'), ('E', '·'), ('F', '··—·'), 
    ('G', '——·'), ('H', '····'), ('I', '··'), 
    ('J', '·———'), ('K', '—·—'), ('L', '·—··'), 
    ('M', '——'), ('N', '—·'), ('Ñ', '——·——'), 
    ('O', '———'), ('P', '·——·'), ('Q', '——·—'), 
    ('R', '·—·'), ('S', '···'), ('T', '—'), 
    ('U', '··—'), ('V', '···—'), ('W', '·——'), 
    ('X', '—··—'), ('Y', '—·——'), ('Z', '——··'), 
    ('0', '—————'), ('1', '·————'), ('2', '··———'), 
    ('3', '···——'), ('4', '····—'), ('5', '·····'), 
    ('6', '—····'), ('7', '——···'), ('8', '———··'), 
    ('9', '————·'), ('.', '·—·—·—'), (',', '——··——'), 
    ('?', '··——··'), ('"', '·—··—·'), ('/', '—··—·')
]

def morse(oracion : str, tipo : str): 
    traduccion = ''
    if tipo == 'morsear': 
        oracion = oracion.upper()
        oracion = oracion.split(' ')
        for esto in oracion: 
            for letra in esto: 
                if letra != 'Ñ': letra = unidecode(letra)
                traduccion += f'{buscar(letra, tipo)} '
            traduccion += '  '
    elif tipo == 'castellanear': 
        oracion = oracion.replace('‑', '—')
        oracion = oracion.replace('−', '—')
        oracion = oracion.replace('-', '—')
        oracion = oracion.replace('.', '·')
        oracion = oracion.split('  ')
        for esto in oracion: 
            for letra in esto.split(' '): 
                traduccion += f'{buscar(letra, tipo)}'
            traduccion += ' '
    else: 
        print('Chaitos o(*≧▽≦)ツ┏━┓')
        return
    print(traduccion)

def buscar(letra : str, tipo : str):
    primero = 0
    segundo = 0
    if tipo == 'morsear': segundo = 1
    elif tipo == 'castellanear': primero = 1
    for i in range(1, len(LISTA) // 2 + 1): 
        if LISTA[i - 1][primero] == letra: 
            return LISTA[i - 1][segundo]
        elif LISTA[-i][primero] == letra: 
            return LISTA[-i][segundo]
    return ''

def main(): 
    texto = ''
    tipo = str(input('¿Qué tipo de traducción desea?\n(a) Español a morse\n(b) Morse a español\n'))
    if tipo == 'a' or tipo == 'A' or tipo == '(a)' or tipo == '(A)': 
        tipo = 'morsear'
        texto = 'Escriba la oración a traducir: '
    elif tipo == 'b' or tipo == 'B' or tipo == '(b)' or tipo == '(B)': 
        tipo = 'castellanear'
        texto = 'Escriba el códigoo a traducir (un espacio por letra, dos espacios por palabra): '
    else: 
        print('Disculpe esa no es una opción (┬┬﹏┬┬)')
    oracion = str(input(texto))
    morse(oracion, tipo)

if __name__ == '__main__': 
    main()