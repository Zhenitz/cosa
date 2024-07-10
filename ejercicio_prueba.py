import os, json
os.system

def agregar_paciente(pacientes):
    nombre = input("Ingrese el nombre del paciente: ")
    if pacientes:
        id = max(pacientes.keys())
    else:
        id = int(input("ingrese el ID del paciente: "))
    pacientes[id] = nombre
    return f"\nPaciente {nombre} agregado con ID {id}\n"

def borrar_paciente(pacientes):
    id = int(input("Ingrese el ID del paciente que desea eliminar: "))
    if id in pacientes:
        nombre = pacientes[id]
        del pacientes[id]
        return f"\nEl paciente {nombre} con ID {id} ha sido eliminado\n"
    else:
        return f"\nNo se encontró ningún paciente con el ID {id}\n"

def buscar_paciente(pacientes):
    id = int(input("Ingrese el ID del paciente que desea buscar: "))
    if id in pacientes:
        nombre = pacientes[id]
        return f"\nEl paciente con ID {id} se llama {nombre}\n"
    else:
        return f"\nNo se encontró ningún paciente con el ID {id}\n"

pacientes = {}

while True:
    print("Bienvenido al sistema de pacientes")
    print("1. Agregar paciente")
    print("2. Borrar paciente")
    print("3. Buscar paciente")
    print("4. Salir")
    
    opcion = int(input("Ingrese una opción: "))
    
    if opcion == 1:
        print(agregar_paciente(pacientes))
    elif opcion == 2:
        print(borrar_paciente(pacientes))
    elif opcion == 3:
        print(buscar_paciente(pacientes))
    elif opcion == 4:
        print("Saliendo del sistema")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

with open ("d:\ing informatica\prueba2.json", "w", encoding="utf-8") as salida:
    json.dump(pacientes, salida, ensure_ascii=False, indent=4)