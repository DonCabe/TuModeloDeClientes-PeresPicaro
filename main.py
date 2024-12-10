from models import Client, ClientManager

def show_menu():
    print("\n=== Gestión de Clientes ===")
    print("1. Listar clientes")
    print("2. Agregar cliente")
    print("3. Modificar cliente")
    print("4. Eliminar cliente")
    print("5. Guardar cambios")
    print("6. Salir")
    return input("Selecciona una opción: ")

def add_client(manager):
    print("\n=== Agregar Cliente ===")
    id = manager.next_id  # Usa el próximo ID disponible
    manager.next_id += 1  # Incrementa para el siguiente cliente
    name = input("Nombre: ")
    while True:
        age = input("Edad: ")
        if not str(age).isdigit() or int(age) <= 0:
            print("La edad debe ser un número mayor a 0. Intenta de nuevo.")
            continue
        break
    address = input("Dirección: ")
    email = input("Email: ")
    new_client = Client(id, name, age, address, email)
    manager.clients_list.append(new_client)
    print(f"Cliente agregado con ID: {id}")

def update_client(manager):
    print("\n=== Modificar Cliente ===")
    id = input("Ingresa el ID del cliente a modificar: ")
    for client in manager.clients_list:
        if client.id == id:
            print("Cliente encontrado:")
            print(client)
            new_name = input("Nuevo nombre (dejar vacío para no modificar): ")
            while True:
                new_age = input("Nueva edad (dejar vacío para no modificar): ")
                if not str(new_age).isdigit() or int(new_age) <= 0:
                    print("La edad debe ser un número mayor a 0. Intenta de nuevo.")
                    continue
                break
            new_address = input("Nueva dirección (dejar vacío para no modificar): ")
            new_email = input("Nuevo email (dejar vacío para no modificar): ")

            if new_name:
                client.name = new_name
            if new_age:
                client.age = int(new_age)
            if new_address:
                client.address = new_address
            if new_email:
                client.email = new_email

            print("Cliente modificado con éxito.")
            return
    print("Cliente no encontrado.")

def delete_client(manager):
    print("\n=== Eliminar Cliente ===")
    id = input("Ingresa el ID del cliente a eliminar: ")
    for client in manager.clients_list:
        if client.id == id:
            manager.clients_list.remove(client)
            print("Cliente eliminado con éxito.")
            return
    print("Cliente no encontrado.")

def main():
    manager = ClientManager()
    manager.read_file_csv()

    while True:
        opcion = show_menu()
        if opcion == "1":
            print("\n=== Lista de Clientes ===")
            print(manager.list_clients())
        elif opcion == "2":
            add_client(manager)
        elif opcion == "3":
            update_client(manager)
        elif opcion == "4":
            delete_client(manager)
        elif opcion == "5":
            manager.save_file_csv()
            print("Cambios guardados en el archivo.")
        elif opcion == "6":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    main()