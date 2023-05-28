masa = 0

masa = float (input('ingrese su indice de masa corporal ->'))
print(f'Su indice de masa corporal es {masa}')

if masa < 15:
    print('Delgadez muy severa')
elif masa <16 and masa >=15:
    print('Delgadez severa')
elif masa <18.5 and masa >=16:
    print('Delgadez')
elif masa <25 and masa >=18.5:
    print('Peso saludable')
elif masa <30 and masa >=25:
    print('Sobrepeso')
elif masa <35 and masa >=30:
    print('Obesidad moderada')
elif masa <40 and masa >=35:
    print('Obesidad severa')
else:
    print('Obesidad muy severa (Obesidad Morvida)')

