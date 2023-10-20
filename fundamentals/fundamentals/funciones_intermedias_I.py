# #1 Actualizar valores en diccionarios y listas
# x = [ [5,2,3], [10,8,9] ] 
# estudiantes = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20}]

# #cambiar valor de x desde 10 hasta 15
# def cambiar_valores(a):
#     b=[]
#     # print(a)
#     for x in range(0,len(a)):
#         for y in range(0,len(a[x])):
#             if(x == 1 , y==1):
#                 if(a[x][y] == 10):
#                     a[x][y] = 15
#             # else:
#                 # print(len(a[x]))
#     return a
# print(cambiar_valores(x))

# def cambiar_apellido(a):
#     for i in a:
#         if(i['last_name'] == 'Jordan'):
#             i['last_name'] = 'Bryant'
#     return a
# print(cambiar_apellido(estudiantes))

def cambiar_jugador(lista):
    for i in lista:
        if(lista['fútbol'][0] == 'Messi'):
            lista['fútbol'][0] = 'Andrés'
    return lista
print(cambiar_jugador(directorio_deportes))

# def cambiar_valor(a):
#     for i in a:
#         if(i['y']== 20):
#             i['y'] = 30
#     return i
# print(cambiar_valor(z))

# #2 Iterar a través de una lista de diccionarios

# estudiantes = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
# def iterateDictionary(some_list):
#     for i in some_list:
#         print('first_name','-',i['first_name']+', last_name','-', i['last_name'])
#     return some_list
# iterateDictionary(estudiantes) 

# #3 Obtener valores de una lista de diccionarios
# #Este codigo, utiliza el diccionario del codigo anterior para funcionar

# def iterateDictionary2(key_name,some_list):
#     for i in some_list:
#         print(i.get(key_name))

# iterateDictionary2('first_name',estudiantes) 
# iterateDictionary2('last_name',estudiantes) 
#4 Iterar a través de un diccionarios con valores de lista

dojo ={
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    print(len(some_dict['ubicaciones']),'UBICACIONES')
    for i in range(len(some_dict['ubicaciones'])):
        print(some_dict['ubicaciones'][i])
    print('\t')
    print(len(some_dict['instructores']),'INSTRUCTORES')
    for x in range(len(some_dict['instructores'])):
        print(some_dict['instructores'][x])
printInfo(dojo)
# salida:
''' 
7 UBICACIONES
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
    
8 INSTRUCTORES
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon
'''
