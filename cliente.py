import socket
import struct
import sys

def send_request(client_socket, action, data=None):
    if data is not None:
        request = f"{action} {data}"
    else:
        request = action
    send_message(client_socket, request)
    response = receive_message(client_socket)
    return response


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

def main():
    host = "127.0.0.1"
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    while True:
        print("\nMenu:")
        print("1. Adicionar Pokémon")
        print("2. Consultar Pokémon")
        print("3. Atualizar Pokémon")
        print("4. Excluir Pokémon")
        print("5. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            nome = input("Nome do Pokémon: ")
            tipo = input("Tipo do Pokémon: ")
            raridade = input("Raridade do Pokémon: ")
            peso = float(input("Peso do Pokémon: "))
            altura = float(input("Altura do Pokémon: "))
            numero = int(input("Número na Pokédex: "))

            data = {
                'numero': numero,
                'nome': nome,
                'tipo': tipo,
                'raridade': raridade,
                'peso': peso,
                'altura': altura
            }
            response = send_request(client_socket, 'create', data)
            print(response)

        elif choice == "2":
            response = send_request(client_socket, 'read-all')
            if "não encontrado" not in response:
                print("Lista de Pokémon:")
                print(response)

        elif choice == "3":
            numero = int(input("Número na Pokédex do Pokémon a ser atualizado: "))
            nome = input("Novo nome do Pokémon: ")
            tipo = input("Novo tipo do Pokémon: ")
            raridade = input("Nova raridade do Pokémon: ")
            peso = float(input("Novo peso do Pokémon: "))
            altura = float(input("Nova altura do Pokémon: "))

            data = {
                'numero': numero,
                'nome': nome,
                'tipo': tipo,
                'raridade': raridade,
                'peso': peso,
                'altura': altura
            }
            response = send_request(client_socket, 'update', data)
            print(response)

        elif choice == "4":
            numero = int(input("Número na Pokédex do Pokémon a ser excluído: "))
            response = send_request(client_socket, 'delete', str(numero))
            print(response)

        elif choice == "5":
            send_request(client_socket, 'exit')
            print("Encerrando o programa.")
            client_socket.close()
            break

        else:
            print("Opção inválida. Tente novamente.")

    client_socket.close()

if __name__ == "__main__":
    main()
