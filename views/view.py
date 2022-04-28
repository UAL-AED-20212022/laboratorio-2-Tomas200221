from controllers.controller import *


def executar():
    try:
        while True:
            scan = input().split()
            match scan[0].upper():
                case "RPI":
                    inserir_inicio(scan, lista)
                case "RPF":
                    inserir_fim(scan)
                case "RPDE":
                    inserir_depois(scan)
                case "RPAE":
                    inserir_antes(scan)
                case "RPII":
                    inserir_indice(scan)
                case "VNE":
                    print(f"O número de elementos são {verificar_numero()}")
                case "VP":
                    if not verificar_pais(scan) or verificar_pais(scan) is None:
                        print(f"O país {scan[1]} não faz parte da lista.")
                    else:
                        print(f"O país {scan[1]} faz parte da lista.")
                case "EPE":
                    x = eliminar_inicio()
                    print(f"O país {x} foi eliminado com sucesso da lista")
                case "EUE":
                    x = eliminar_fim()
                    print(f"O país {x} foi eliminado com sucesso da lista")
                case "EP":
                    eliminar_pais(scan)
                    if not verificar_pais(scan) or verificar_pais(scan) is None:
                        print(f"O país {scan[1]} não faz parte da lista.")
                    else:
                        print(f"O país {scan[1]} foi eliminado com sucesso da lista")
                case _:
                    pass

    except:
        pass