from models.LinkedList import LinkedList

lista = LinkedList()

def inserir_inicio(scan, lista):
    lista.insert_at_start(scan[1])
    lista.traverse_list()
    return lista

def inserir_fim(scan):
    lista.insert_at_end(scan[1])
    lista.traverse_list()
    return lista

def inserir_antes(scan):
    lista.insert_before_item(scan[2], scan[1])
    lista.traverse_list()
    return lista

def inserir_depois(scan):
    lista.insert_after_item(scan[2], scan[1])
    lista.traverse_list()
    return lista

def inserir_indice(scan):
    lista.insert_at_index(int(scan[2]), scan[1])
    lista.traverse_list()
    return lista

def verificar_numero():
    return lista.get_count()

def verificar_pais(scan):
    return lista.search_item(scan[1])

def eliminar_inicio():
    x = lista.start_node
    lista.delete_at_start()
    return x

def eliminar_fim():
    x = lista.get_last_node()
    lista.delete_at_end()
    return x

def eliminar_pais(scan):
    lista.delete_element_by_value(scan[1])
    return lista