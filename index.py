# Ejercicio N° 1

nombre = 0
altura = 0
peso = 0

nombre = input ('Ingrese su Nombre Completo ->')
altura = float (input('Ingrese su altura ->'))
peso = float (input('Ingrese su peso ->'))

imc = float ((peso /(altura*altura)))
#print(imc)

if imc < 15:
    print('Delgadez muy severa')
elif imc <16 and imc >=15:
    print('Delgadez severa')
elif imc <18.5 and imc >=16:
    print('Delgadez')
elif imc <25 and imc >=18.5:
    print('Peso saludable')
elif imc <30 and imc >=25:
    print('Sobrepeso')
elif imc <35 and imc >=30:
    print('Obesidad moderada')
elif imc <40 and imc >=35:
    print('Obesidad severa')
else:
    print('Obesidad muy severa (Obesidad Morvida)')
    
# Ejercicio N° 2

sexo = ''
nombre = ''
edad = 0
altura = 0
band = True

sexo = input('Ingrese su sexo ->')
nombre = input('Ingrese su nombre ->')
edad = int (input('Ingrese su edad ->'))
altura = float(input('Ingrese su altura ->'))
   

if sexo == 'masculino':
        if edad >=18:
            print('Es mayor de edad', end='. ')
            band = False
        if altura >1.80:
            print('Es un hombre alto')
            band = False
elif sexo == 'femenino':
        if edad >=18:
            print('Es mayor de edad', end='. ')
            band = False
        if altura >1.70:
            print('Es una mujer alta')
            band = False              
if band:
    print(nombre)
    