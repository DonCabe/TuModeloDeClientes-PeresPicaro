class Client:
    def __init__(self, id, name, age, address, email):
        if not str(age).isdigit() or int(age) <= 0:
            raise ValueError("La edad debe ser un número mayor a 0.")
        
        self.id = int(id)
        self.name = name
        self.age = int(age)
        self.address = address
        self.email = email

    # Getters
    def getAddress(self):
        return self.address

    def getEmail(self):
        return self.email

    # Setters
    def setAddress(self, new_address):
        self.address = new_address

    def setEmail(self, new_email):
        self.email = new_email

    # Others
    def convert_to_CSV(self):
        return f"{self.id},{self.name},{self.age},{self.address},{self.email}"

    def __str__(self):
        return f"ID: {self.id}\tName: {self.name}\tAge: {self.age}\tAddress: {self.address}\tE-mail: {self.email}"


class ClientManager:
    def __init__(self):
        self.PATH_FILE_CSV = './TuModeloDeClientes+PeresPicaro/clients.csv'
        self.clients_list = []
        self.next_id = 1  # Inicia en 1
        
    def list_clients(self):
        list_c = ''
        for client in self.clients_list:
            list_c += client.__str__() + '\n'
        return list_c

    # CSV reading and saving methods
    def read_file_csv(self):
        try:
            with open(self.PATH_FILE_CSV, 'r') as clients:
                lines = clients.readlines()
                for line in lines:
                    id, name, age, address, email = line.split(',')
                    new_client = Client(id, name, age, address, email.strip())
                    self.clients_list.append(new_client)
                # Actualizar el próximo ID autoincremental
                if self.clients_list:
                    self.next_id = max(int(client.id) for client in self.clients_list) + 1
        except FileNotFoundError:
            print(f"Error: El archivo '{self.PATH_FILE_CSV}' no fue encontrado.")
        except Exception as e:
            print(f"Se produjo un error al leer el archivo: {e}")

    def save_file_csv(self):
        try:
            with open(self.PATH_FILE_CSV, 'w') as clients:
                for client in self.clients_list:
                    clients.write(client.convert_to_CSV() + '\n')
        except Exception as e:
            print(f"Se produjo un error al guardar el archivo: {e}")