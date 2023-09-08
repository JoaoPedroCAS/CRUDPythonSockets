import socket
import struct

# Dados iniciais da Pokedex
pokedex = []

def create_pokemon(data):
    pokedex.append(data)

def read_pokemon(pokedex_number):
    return pokedex

def update_pokemon(pokedex_number, data):
    for i, pokemon in enumerate(pokedex):
        if pokemon['numero'] == pokedex_number:  # Convertendo para int
            pokedex[i] = data
            return True
    return False

def delete_pokemon(pokedex_number):
    for i, pokemon in enumerate(pokedex):
        if pokemon['numero'] == pokedex_number:
            del pokedex[i]
            return True
    return False

def send_message(client_socket, message):
    message = message.encode()
    message_size = len(message)
    size_packed = struct.pack("!I", message_size)
    client_socket.send(size_packed)
    client_socket.send(message)

def receive_message(client_socket):
    size_packed = client_socket.recv(4)
    if not size_packed:
        return None
    message_size = struct.unpack("!I", size_packed)[0]
    message = client_socket.recv(message_size).decode()
    return message

def handle_client(client_socket):
    while True:
        request = receive_message(client_socket)
        if not request:
            break

        request_data = request.split(" ", 1)
        action = request_data[0]

        if action == 'create':
            data = request_data[1]
            create_pokemon(eval(data))
            response = "Pokémon criado com sucesso!"

        elif action == 'read-all':
            if pokedex:
                response = str(pokedex)
            else:
                response = "A Pokedex está vazia."

        elif action == 'update':
            data = request_data[1]
            data = data.split()
            #print(f"\n{data[1][0:-1]}\n{data[3][1:-2]}\n{data[5][1:-2]}\n{data[7][1:-2]}\n{data[9][0:-1]}\n{data[11][0:-1]}\n")
            pokedex_number = int(data[1][0:-1])
            data_dict = {
                'numero': int(data[1][0:-1]),
                'nome': data[3][1:-2],
                'tipo': data[5][1:-2],
                'raridade': data[7][1:-2],
                'peso': float(data[9][0:-1]),
                'altura': float(data[11][0:-1])
            }
            if update_pokemon(pokedex_number, data_dict):
                response = "Pokémon atualizado com sucesso!"
            else:
                response = "Pokémon não encontrado."

        elif action == 'delete':
            pokedex_number = int(request_data[1])
            delete_pokemon(pokedex_number)
            response = "Pokémon excluído com sucesso!"

        else:
            response = "Ação inválida."

        send_message(client_socket, response)

    client_socket.close()

def main():
    host = "127.0.0.1"
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Servidor escutando em {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Conexão de {addr[0]}:{addr[1]} estabelecida.")
        handle_client(client_socket)

if __name__ == "__main__":
    main()
