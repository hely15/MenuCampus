import json
import os
import modulos.menus as menus


def verF(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero   
        except Exception:
            print('Opcion invalida. Ingrese un valor valido: ')


def guardarArchivo(Diccionario,archivo):
    with open (f"./datos/{archivo}.json","w") as salida:
        json.dump(Diccionario, salida)
    return True 

def abrirArchivo(archivo):
    archivo_path = f"./datos/{archivo}.json"
    
    if not os.path.exists(archivo_path):
        print(f"El archivo {archivo_path} no existe.")
        return None  # Retorna None si no existe el archivo
    
    with open(archivo_path, "r") as entrada:
        nuevoDiccionario = json.load(entrada)
    return nuevoDiccionario

campersData = abrirArchivo("campers_database")
trainersData = abrirArchivo("trainers_database")



## Con esta funcion permitimos que el camper se registre y se guarden sus datos en el archivo campers_database.json
def aggCampers(campersData: dict): 
    nombres = input('Ingrese sus nombres: ').capitalize()
    apellidos = input('Ingrese sus apellidos: ').capitalize()
    numeroDocumento = verF('Ingrese su número de identificación: ')
    direccion = input('Ingrese su dirección: ').capitalize()
    acudiente = input('Ingrese el nombre de su acudiente: ').capitalize()
    telefonoCel = verF('Ingrese su número de teléfono móvil: ')
    telefonoFijo = verF('Ingrese su número de teléfono fijo (si no aplica, coloque 1): ')

    campersData[numeroDocumento] = {
        'nombre': nombres,
        'apellidos': apellidos,
        'numeroDocumento': numeroDocumento,
        'direccion': direccion,
        'acudiente': acudiente,
        'telefonos': {
            'celular': telefonoCel,
            'fijo': telefonoFijo,
            },
        'estado': {
            "En proceso":True,
            "Inscrito": False,
            "Aprobado": False,
            "Denegado": False,
            "Cursando": False,
            "Graduado": False,
            "Expulsado": False,
            "Retirado": False,
        },
        'riesgo': False,
        'horario': '',
        'ruta': '',
         'notas': {
            "modulo1": 0,
            "modulo2": 0,
            "modulo3": 0,
            "modulo4": 0,
            "modulo5": 0
            }
        }

    guardarArchivo(campersData, "campers_database")
    print(f"Usuario agregado con éxito su ID de ingreso es su numero de documento {numeroDocumento}")



## Con esta funcion podemos verificar que el camper esta registrado y darle la bienvenido a la plataforma
def ingresarCamper(campersData: dict):
    print('Ingrese su ID para continuar')
    idIngresdo = input('<:>')
    for campersDataKey, data in campersData.items():
        if "estudiantes" in data and idIngresdo in data["estudiantes"]:
            estudiante = data["estudiantes"][idIngresdo]
            nombre = estudiante["nombre"]
            estado = estudiante["estado"]  
            print(f'Bienvenido {nombre}')
            for estadoKey, value in estado.items():
                if value:  
                    print(f'Tu estado es: {estadoKey}')
                    x = input('Presione una tecla para continuar.......')
                if campersData[idIngresdo]["estado"]["En proceso"] == True:
                    print('Estas en proceso de ingreso al campus espera a que te asignen tu examen.')
                    x = input('Presione una tecla para continuar........')
                    break
                if campersData[idIngresdo]["estado"]["Inscrito"] == True :
                    print('Espera los resultados de tu prueba de ingreso ')
                    x = input('Presione una tecla para continuar........')
                    break
                if campersData[idIngresdo]["estado"]["Aprobado"] == True :
                    print('Ya oficial eres camper espera a que te asignen un grupo :)')
                    x = input('Presione una tecla para continuar........')
                    break
                if campersData[idIngresdo]["estado"]["Denegado"] == True :
                    print('No superastes las pruebas de ingreso sigue estudiando y esfuerzate para la proxima :)')
                    x = input('Presione una tecla para continuar........')
                    break
                if campersData[idIngresdo]["estado"]["Cursando"] == True :
                    while True:
                        print(menus.menuCamper2)
                        opCamper2 = int(input('<:>'))
                        match opCamper2:
                            case 1:
                                print(estudiante)
                                x = input('Presione una tecla para continuar......')
                                return
                            case 2:
                                print(estudiante["notas"])
                                x = input('Presione una tecla para continuar......')
                                return
                            case 3:
                                salon = estudiante.get('salon', 'Información no disponible')
                                ruta = estudiante.get('ruta', 'Información no disponible')
                                horario = estudiante.get('horario', 'Información no disponible')
                                print(f"Salón: {salon}")
                                print(f"Ruta: {ruta}")
                                print(f"Horario: {horario}")
                            case _:
                                print("Opción no válida.")
                                return
                        return  
                if campersData[idIngresdo]["estado"]["Graduado"] == True :
                    print('Bienbenido egresado')
                    x = input('Presione una tecla para continuar........')
                if campersData[idIngresdo]["estado"]["Expulsado"] == True :
                    print('Fuiste expulsado del campus.') 
                    x = input('Presione una tecla para continuar........')
                if campersData[idIngresdo]["estado"]["Retirado"] == True :
                    print('Te restiraste del campus.')
                    x = input('Presione una tecla para continuar........')
            break

                
            
    


def aggGrupo(campersData: dict, trainersData: dict):
    grupo = input('Ingrese el Grupo al cual va agregar el estudiante: ')
    estudiante = input('Ingrese el documento del estudiante para agregarlo: ')
    documento = str(input('Ingrese el documento del trainer encargado de este grupo: '))
    

    if estudiante in campersData and grupo in campersData and documento in trainersData:
        estudiantes = campersData[grupo]["estudiantes"]
        estudiante_data = campersData[estudiante]
        estudiante_data["horario"] = campersData[grupo]["horario"]
        estudiante_data["ruta"] = campersData[grupo]["ruta"]

        if len(estudiantes) < 33:
            if "Inscrito" in campersData[estudiante]["estado"] and campersData[estudiante]["estado"]["Inscrito"]:
                estudiantes[estudiante] = estudiante_data
                #del campersData[estudiante]
                for documento, trainer_info in trainersData.items():
                    if grupo in trainer_info["clasesAsignadas"]:
                        trainer_info["clasesAsignadas"][grupo]["estudiantes"] = int(trainer_info["clasesAsignadas"][grupo]["estudiantes"]) + 1

                        break
                print(f"Estudiante {estudiante} agregado al grupo {grupo}.")
            else:
                print(f"El estudiante no fue asignado al salón {grupo} porque no pasó el filtro inicial.")
        else:
            print(f"El grupo {grupo} ya tiene 33 estudiantes. No se puede agregar más.")
    else:
        print("El estudiante o el grupo no existen en el diccionario.")

    guardarArchivo(campersData, "campers_database")
    guardarArchivo(trainersData, "trainers_database")


def aggNotas(campersData: dict):
    grupo = input('Ingrese el Grupo al cual quiere agregar notas: ')
    estudiante = input('Ingrese el documento del estudiante al que desea colocar notas: ')

    if grupo in campersData and estudiante in campersData[grupo]["estudiantes"]:
        
        estudiante_info = campersData[grupo]["estudiantes"][estudiante]
        print("Datos del estudiante:", estudiante_info)
        print(menus.menuModulos)
        opcionModulos = verF('<:>')
        match opcionModulos:
            case 1:
                teorica = int(input('Ingrese la nota teorica:'))
                practica = int(input('Ingrese la nota practica:'))
                quizes = int(input('Ingrese la nota de los quizes:'))

                teoricaT = teorica * 0.3
                practicaT = practica * 0.6
                quizesT = quizes * 0.1
            
                totalNotas = teoricaT + practicaT + quizesT
                estudiante_info["notas"]["modulo1"] = totalNotas

                print("Notas actualizadas correctamente:", estudiante_info["notas"])
            case 2:
                teorica = int(input('Ingrese la nota teorica:'))
                practica = int(input('Ingrese la nota practica:'))
                quizes = int(input('Ingrese la nota de los quizes:'))

                teoricaT = teorica * 0.3
                practicaT = practica * 0.6
                quizesT = quizes * 0.1
            
                totalNotas = teoricaT + practicaT + quizesT
                estudiante_info["notas"]["modulo1"] = totalNotas

                print("Notas actualizadas correctamente:", estudiante_info["notas"])
            case 3:
                teorica = int(input('Ingrese la nota teorica:'))
                practica = int(input('Ingrese la nota practica:'))
                quizes = int(input('Ingrese la nota de los quizes:'))

                teoricaT = teorica * 0.3
                practicaT = practica * 0.6
                quizesT = quizes * 0.1
            
                totalNotas = teoricaT + practicaT + quizesT
                estudiante_info["notas"]["modulo1"] = totalNotas

                print("Notas actualizadas correctamente:", estudiante_info["notas"])
            case 4:
                teorica = int(input('Ingrese la nota teorica:'))
                practica = int(input('Ingrese la nota practica:'))
                quizes = int(input('Ingrese la nota de los quizes:'))

                teoricaT = teorica * 0.3
                practicaT = practica * 0.6
                quizesT = quizes * 0.1
            
                totalNotas = teoricaT + practicaT + quizesT
                estudiante_info["notas"]["modulo1"] = totalNotas

                print("Notas actualizadas correctamente:", estudiante_info["notas"])
            case 5:
                teorica = int(input('Ingrese la nota teorica:'))
                practica = int(input('Ingrese la nota practica:'))
                quizes = int(input('Ingrese la nota de los quizes:'))

                teoricaT = teorica * 0.3
                practicaT = practica * 0.6
                quizesT = quizes * 0.1
            
                totalNotas = teoricaT + practicaT + quizesT
                estudiante_info["notas"]["modulo1"] = totalNotas

                print("Notas actualizadas correctamente:", estudiante_info["notas"])
            case 6:
                pass
            case _:
                pass
    else:
        print("ID no encontrado.")
        continuar = input("¿Deseas intentar de nuevo? (s/n): ")
        if continuar.lower() != 's':
            pass

   


def subirAdmision(campersData: dict):
    estudiante = input('Ingrese el documento del estudiante al que desea subir notas: ')

    if estudiante in campersData:

        notaTeorica = int(input('Ingrese la nota de la evaluacion teorica: '))
        notaPractica = int(input('Ingrese la nota de la evaluacion practica:  '))

        notasTotal = (notaTeorica * 0.5) + (notaPractica * 0.5)
        if notasTotal > 60:
            campersData[estudiante]['estado']['En proceso'] = False
            campersData[estudiante]['estado']['Inscrito'] = True
            print(f"Notas aprobadas. Total: {notasTotal}")
        else:
            print('La persona no pasó el filtro')
    else:
          print('Estudiante no encontrado')
    guardarArchivo(campersData, "campers_database")
    return subirAdmision




def aggSalonNuevo(campersData, trainersData):
    nombreSalon = input('Ingrese la primera letra del nombre del trainer y su respectiva clase de la jornada: ')
    documento = int(input('Ingrese el documento del profesor: '))

    if documento in trainersData:
        trainer = trainersData[documento]["nombre"]
        ruta = input('Ingrese la ruta del salón: ')
        horario = input('Ingrese el horario de la clase: ')
        salon = input('Ingrese el salón asignado para la clase: ')

        campersData[nombreSalon] = {
            "trainer": trainer,
            "ruta": ruta,
            "horario": horario,
            "salon": salon,
            "modulos": { 
                "modulo1": "Fundamentos de programación (Introducción a la algoritmia, PSeInt y Python",
                "modulo2": "Programación Web (HTML, CSS y Bootstrap)", 
                "modulo3": "Programación formal (Java, JavaScript, C#).", 
                "modulo4": "Bases de datos (Mysql, MongoDb y Postgresql)",
                "modulo5": " Backend (NetCore, Spring Boot, NodeJS y Express)."
            },
            "estudiantes": {}
        }

       
        trainersData[documento]["clasesAsignadas"][nombreSalon] = {
            "ruta": ruta,
            "horario": horario,
            "salon": salon,
            "estudiantes": 0
        }

        print(f"Clase {nombreSalon} asignada al trainer {trainer} correctamente.")

        
        guardarArchivo(campersData, "campers_database")
        guardarArchivo(trainersData, "trainers_database")
    else:
        print("El documento del profesor no existe en la base de datos.")

    






   

