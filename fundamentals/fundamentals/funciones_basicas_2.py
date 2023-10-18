#1 Cuenta regresiva
def cuenta_regresiva(a):
    lista=[]
    for x in range(0,a+1):
        lista.append(a)
        a-=1
    return lista
    
print(cuenta_regresiva(5))

#2 Imprimir y devolver
def imprimir_y_devolver(a,b):
    print(a)
    return b
print(imprimir_y_devolver(1,2))

#3 Primero más longitud
def primero_mas_longitud(a):
    return a[0]+len(a)
print(primero_mas_longitud([1,2,3,4,5]))

#4 Valores mayores que el segundo
def mayores_que_segundo(a):
    lista =[]
    for x in range(0,len(a)):
        if(len(a)< 2):
            return False
        else:
            if(a[x] > a[1]):
                lista.append(a[x])
    return lista
print(mayores_que_segundo([1,2,3,4,5]))
print(mayores_que_segundo([1]))

#5 Esta longitud, ese valor
def longitud_y_valor(a,b):
    lista=[]
    for x in range(0,a):
        lista.append(b)
    return lista
print(longitud_y_valor(4,7))
print(longitud_y_valor(6,2))