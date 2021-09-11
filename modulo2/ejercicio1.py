def piramide (altura):
    if 1 <= altura <= 8:
        for i in range(altura):
            print(' ' * (altura - (i+1)) ,'#'* (i+1))
    else:
        print('Proporcione un entero positivo no mayor que 8')

print('Digite la altura de la piramide de altura maximo 8: ')
altura1 = piramide(int(input('height: ')))