###DESARROLLO#
##Hacer un programa que imprima la tabla dell 3:
#'while' imprimiendo Tabla del numero 3
contador = 0
print(' Tabla del numero 3')

#bucle while
while contador <=10:
    print(f'3 X{contador} ==> {contador*3}')
    contador += 1
print('Fin de la tabla')

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

##Hacer un programa que solicite ingreso de contraseña:
#Ingreso de password

password = ''

while password != '12345':
    print('Porfavor ingrese su contraseña')
    password = input()

print('Por fin....!')

##Hacer un programa que valide ingreso nombre Rose:

while True:
    print('Por favor ingrese su nombre: ')
    name = input()
    if name.lower() == 'rose':
        break

print(' Hasta luego !!!!')

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
