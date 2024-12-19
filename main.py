import modulos.menus as menus
import modulos.trainers as funcionesTrainers
import modulos.campers as funcionesCampers





if __name__ == '__main__':
    while(True):
        print(menus.aviso)
        print(menus.menu1)
        opMenu1 = int(input('<:>'))
        match opMenu1:
            case 1:
                    print(menus.menuEntrar)
                    opMenuEntrar = int(input('<:>'))
                    match opMenuEntrar:
                        case 1:
                            funcionesCampers.aggCampers(funcionesCampers.campersData)
                            x = input('Presione una tecla.......')
                        case 2:
                            funcionesCampers.ingresarCamper(funcionesCampers.campersData)
                        case 3:
                            pass
                        case _:
                            funcionesCampers.verF(funcionesCampers.mensaje)
                
            case 2:
                funcionesTrainers.ingresarTrainer(funcionesTrainers.trainersData)
            case 3:
                while True:
                    print(menus.menusCoordinador)
                    opMenucordinador = funcionesCampers.verF('<:>')   
                    match opMenucordinador:
                        case 1:
                            funcionesCampers.aggSalonNuevo(funcionesCampers.campersData, funcionesCampers.trainersData)
                            x = input('Presione un tecla para continuar......')
                        case 2:
                            funcionesCampers.aggGrupo(funcionesCampers.campersData, funcionesCampers.trainersData)
                        case 3: 
                            funcionesCampers.subirAdmision(funcionesCampers.campersData)
                        case 4:
                            break
                        case _:
                            funcionesCampers.verF('<:>')
            case _:
                break
