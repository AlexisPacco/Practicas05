```python
###EJEMPLOS
```


```python
##Hacer un programa que busque el numero 2 dentro de una lista de Numeros, si se encuentra, que imprima el indice dentro de la lista:

valores = [5, 1, 9, 2, 7, 4]
encontrado = False
indice = 0
longitud = len(valores)
while not encontrado and indice < longitud:
    valor = valores[indice]
    if valor == 2:
        encontrado = True
    else:
        indice += 1
if encontrado:
    print(f'El numero 2 ha sido encontrado en el indice {indice}')
else:
    print('El numero 2 no se encuentra en la lista de valores')

```

    El numero 2 ha sido encontrado en el indice 3



```python
##Hacer un programa que solicite ingreso de contraseña con intentos limitados:
#Ingreso password
password = ''

#sino tengo contador while True:

cont = 0
while password != '12345':
    cont += 1
    print('Por favor ingrese su contraseña: ')
    password = input()
    if cont == 5:
        print('Finalizo los intentos...!')
        break
if cont != 5:
    print('Por fin...!')

```

    Por favor ingrese su contraseña: 


     12


    Por favor ingrese su contraseña: 


     2341


    Por favor ingrese su contraseña: 


     132


    Por favor ingrese su contraseña: 


     68


    Por favor ingrese su contraseña: 


     64654


    Finalizo los intentos...!



```python
##Imprime la secuencia 3n+1 desde un numero n, terminando cuando llegue a 1:

def seq3np1(n):
    while n != 1:
        print(n, end=", ")
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    print(n, end=".\n")

num = int(input('Ingrese numero de inicio n : ==> '))
seq3np1(num)

```

    Ingrese numero de inicio n : ==>  5


    5, 16, 8, 4, 2, 1.



```python
##Hacer un programa con funcion que cuenta el numero de digitos que son 0 o 5 en un entero prositivo:
#Creamos la funcion
def num_digi(n):
    count = 0
    while n > 0:
        digit = n % 10
        if digit == 0 or digit == 5:
            count = count + 1
        n = n // 10
    return count

#solicitamos numero
num = int(input('Ingrese un numero que contenga los digitos "0" y "5" : ==> '))

#asignamos la cantidad que retorna
cantidad = num_digi(num)

#imprimir resultado
print('\n\n\tLa cantidad de digitos "0" y "5" en el numero ',num,' es: ==>',cantidad)

```

    Ingrese un numero que contenga los digitos "0" y "5" : ==>  1112311511245


    
    
    	La cantidad de digitos "0" y "5" en el numero  1112311511245  es: ==> 2



```python

```
