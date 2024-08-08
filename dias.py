from datetime import datetime

def dias(inicio : str, final : str): 
    inicio = inicio.split('/')
    final = final.split('/')
    if not verificar(inicio) or not verificar(final): 
        print('Una de las fechas tiene un formato equivocado')
        return
    try: 
        primero = datetime(day=int(inicio[0]), month=int(inicio[1]), year=int(inicio[2]))
        segundo = datetime(day=int(final[0]), month=int(final[1]), year=int(final[2]))
        data = segundo - primero
        dias = data.days
        if dias < 0: dias = dias * -1
        print(f'{dias}')
    except: 
        print('Las fechas no se pueden convertir, disculpe ~(>_<。)＼')
        return

def verificar(lista : list[str]): 
    if len(lista[0]) != 2 or len(lista[1]) != 2 or len(lista[2]) != 4: 
        return False
    for esto in lista: 
        if not esto.isdigit(): return False
    return True

def main(): 
    inicio = str(input('Ingrese la primera fecha (dd/mm/yyyy): '))
    final = str(input('Ingrese la segunda fecha (dd/mm/yyyy): '))
    dias(inicio, final)

if __name__ == '__main__': 
    main()