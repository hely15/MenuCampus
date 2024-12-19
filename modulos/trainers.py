import json
import os
import modulos.menus as menus
import modulos.trainers as funcionesTrainers
import modulos.campers as funcionesCampers



def guardarArchivo(Diccionario,archivo):
    with open (f"./datos/{archivo}.json","w") as salida:
        json.dump(Diccionario, salida)
    return True 

def abrirArchivo(archivo):
    archivo_path = f"./datos/{archivo}.json"
    
    if not os.path.exists(archivo_path):
        print(f"El archivo {archivo_path} no existe.")
        return None 
    with open(archivo_path, "r") as entrada:
        nuevoDiccionario = json.load(entrada)
    return nuevoDiccionario

def getNume(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero   
        except Exception:
            print('Opcion invalida. Ingrese un valor valido: ')

trainersData = abrirArchivo("trainers_database")

    
def ingresarTrainer(trainersData: dict):
    while True:  
        print('Ingrese su ID para continuar: ')
        idIngresdoT = input('<:>')  
        
        if idIngresdoT in trainersData:  
            nombreT = trainersData[idIngresdoT]['nombre']
            print(f'Bienvenido {nombreT}') 
            print(f'Esta es tu informacion: {trainersData[idIngresdoT]}') 
            print(menus.menuTrainers)
            
            op2Trainers = int(input('<:>')) 
            match op2Trainers:
                case 1:
                    funcionesCampers.aggNotas(funcionesCampers.campersData)
                    input('Presione una tecla para continuar...')
                case 2:
                    print('Ingrese el ID del usuario: ')
                    idIngresdo = getNume('<:>')
                    for funcionesCampers.campersData, data in funcionesCampers.campersData.items(): 
                        if idIngresdo in data["estudiantes"]:
                            estudiante = data["estudiantes"][idIngresdo]
                            print(estudiante["notas"])
                            x = input('Presione una tecla para continuar....')
                        return
                    return
                case 3:
                    modulos = funcionesCampers.campersData["p1"]["modulos"]
                    print(modulos)
                    x = input('Presione una tecla para continuar....')
                case 4:
                    trainer2 = trainersData[idIngresdoT]["clasesAsignadas"]
                    print(trainer2)
                    x = input('Presione una tecla para continuar....')
                    
                case _:
                    funcionesCampers.verF(funcionesCampers.mensaje)
        else:
            print("ID no encontrado.")
            continuar = input("¿Deseas intentar de nuevo? (s/n): ")
            if continuar.lower() != 's':
                break  
