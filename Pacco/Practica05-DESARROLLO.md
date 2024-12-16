```python
###DESARROLLO
```


```python
##Estructura Iterativa - Bucle 'while'
while <condicion>:
    <codigo>
    <codigo>
    ........................
```


```python
##Hacer un programa que imprima la tabla dell 3:
#'while' imprimiendo Tabla del numero 3
contador = 0
print(' Tabla del numero 3')

#bucle while
while contador <=10:
    print(f'3 X{contador} ==> {contador*3}')
    contador += 1
print('Fin de la tabla')

```

     Tabla del numero 3
    3 X0 ==> 0
    3 X1 ==> 3
    3 X2 ==> 6
    3 X3 ==> 9
    3 X4 ==> 12
    3 X5 ==> 15
    3 X6 ==> 18
    3 X7 ==> 21
    3 X8 ==> 24
    3 X9 ==> 27
    3 X10 ==> 30
    Fin de la tabla



```python
##Hacer un programa que repita una frase las veces que se desee, use funciones
#frase a repetir
frase = "Debo escribir mi propio codigo y comentario"
#contador
cont = 0

#funcion recibe n veces
def repetir(n,cont):
    while cont < n:
        print(frase)
        cont +=1

num = int(input('Ingrese el numero de veces a repetir la frase: '))
print('\n\n')

#llamar a la funcion
repetir(num,cont)

```

    Ingrese el numero de veces a repetir la frase:  5


    
    
    
    Debo escribir mi propio codigo y comentario
    Debo escribir mi propio codigo y comentario
    Debo escribir mi propio codigo y comentario
    Debo escribir mi propio codigo y comentario
    Debo escribir mi propio codigo y comentario



```python
##Hacer un programa que solicite ingreso de contraseña:
#Ingreso de password

password = ''

while password != '12345':
    print('Porfavor ingrese su contraseña')
    password = input()

print('Por fin....!')

```

    Porfavor ingrese su contraseña


     12


    Porfavor ingrese su contraseña


     12


    Porfavor ingrese su contraseña


     12345


    Por fin....!



```python
##Hacer un programa que valide ingreso nombre Rose:

while True:
    print('Por favor ingrese su nombre: ')
    name = input()
    if name.lower() == 'rose':
        break

print(' Hasta luego !!!!')

```

    Por favor ingrese su nombre: 


     asd


    Por favor ingrese su nombre: 


     asd


    Por favor ingrese su nombre: 


     ROSE


     Hasta luego !!!!



```python
##Hacer un programa que valide nombre y contraseña de dos listas respectivamente:
#lista de nombre y numeros
nombre = ['juan','pedro','luis','fatima','vladi']
contra = ['1234','4321','abcd','dcba','4567']

#while

while True:
    name = input('Ingrese su nombre: ')
    if name not in nombre:
        continue
    print(f'\nHola {name.title()}, por favor ingresa tu contraseña: ')
    password = input()
    if password in contra:
        print('\nBienvenido a su cuenta Bancaria')
        break
    else:
        print('\n Acceso Negado')
        break


```

    Ingrese su nombre:  luisito
    Ingrese su nombre:  fatima


    
    Hola Fatima, por favor ingresa tu contraseña: 


     1325


    
     Acceso Negado



```python

```
