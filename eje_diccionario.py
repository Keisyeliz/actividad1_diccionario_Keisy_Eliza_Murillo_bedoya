registro_diccionario = {}
list_pendiente = []

import os
sw = True

def fnt_añadir(diccionario,codigo, nombres,contacto,correo,edad,estracto,sexo,direccion):
    if codigo == '' or nombres == ''  or contacto == '' or correo == '' or edad == '' or estracto=='' or sexo =='' or direccion =='':
        enter = input('Debe diligenciar toda la información solicitada <ENTER>')
    else:
        diccionario[codigo] = {'Nombre': nombres, 'Contacto':contacto,'Correo':correo, 'Edad':edad, 'Estracto':estracto,'Sexo':sexo,'Direccion':direccion}
        enter = input(f'\nLa persona {nombres} ha sido registrada con éxito <ENTER>')

def fnt_selector(op):
    if op == '1':
        os.system('cls')
        codigo = input('Ingrese su codigo:')
        nombres = input('Nombres completos:  ')
        contacto = input('Número de contacto:   ')
        correo = input('Ingrese su correo:  ')
        direccion = input('Ingrese su dirección: ')
        sexo = input('Sexo (M/F):  ')
        if sexo == 'M':
            edad = int(input('Ingrese su edad: '))
            if (edad >= 15 and edad <= 25):
                estracto = input('--Estracto--\n\n1 .1\n2. 2\n-> ')
            else:
                print ('No cuentas con la edad suficiente para realizar el registro <ENTER>')
                list_pendiente.append(contacto)
        elif sexo == 'F':
            edad = int(input('Ingrese su edad: '))
            if (edad >= 20 and edad <= 35):
                estracto = input('--Estracto--\n\n1 .1\n2. 2\n3. 3\n4. 4\n -> ')
            else:
                print ('No cuentas con la edad suficiente para realizar el registro <ENTER>')
                list_pendiente.append(contacto)        
        fnt_añadir(registro_diccionario,codigo, nombres,contacto,correo,edad,estracto,sexo,direccion)




while sw == True:
    os.system('cls')
    opcion = input('1. Registrar\n2. Mostrar\n3. Salir\n- >  ')
    fnt_selector(opcion)

