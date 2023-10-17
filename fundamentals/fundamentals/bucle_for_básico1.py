#Básico: imprime todos los números enteros del 0 al 150.
# for v in range(0,150):
#     print(v)
#Múltiplos de cinco: imprime todos los múltiplos de 5 entre 5 y 1,000.
# for v in range(5,1000,5):
#     print(v)
"""Contar, a la manera del Dojo: imprime números enteros del 1 al 100.
Si es divisible por 5, imprime "Coding” en su lugar. Si es divisible por 10,
imprime "Coding Dojo"."""
# for v in range(1,100):
#     if(v % 5 == 0):
#         print("coding")
#         if(v % 10 == 0):
#             print("Coding Dojo")
#         continue
#     else:
#         print(v)
"""
Whoa. Es un gran idiota: agrega los enteros impares del 0 al 500,000, e imprime la suma final.
"""
# sum = 0
# for v in range(0,500000):
#     if(v == 2):
#         sum +=v
#     if(v % 2 != 0):
#         sum += v
# print(sum)
"""
Cuenta regresiva de a 4: imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4.
"""
# for v in range(2018,0,-4):
#     print(v)
"""Contador flexible: establece tres variables: lowNum, highNum, mult.
Comenzando en lowNum y pasando por highNum, imprime solo los enteros que sean múltiplos de mult.
Por ejemplo, si lowNum=2, highNum=9 y mult=3. El bucle debe imprimir 3, 6, 9 (en líneas sucesivas). """
lowNum = 2
highNum = 9
mult = 3
for v in range(lowNum,highNum+1):
    if(v % mult == 0):
        print(v)
