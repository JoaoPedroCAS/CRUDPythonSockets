import socket  # Importa a biblioteca socket para comunicação por rede.
import struct  # Importa a biblioteca struct para empacotar e desempacotar dados binários.

# Função para enviar uma solicitação ao servidor.
def send_request(client_socket, action, data=None):
    if data is not None:
        request = f"{action} {data}"  # Cria uma mensagem que inclui a ação e os dados, se fornecidos.
    else:
        request = action  # Cria uma mensagem apenas com a ação.
    send_message(client_socket, request)  # Envia a mensagem para o servidor.
    response = receive_message(client_socket)  # Recebe a resposta do servidor.
    return response  # Retorna a resposta.

# Função para enviar uma mensagem ao servidor.
def send_message(client_socket, message):
    message = message.encode()  # Codifica a mensagem em bytes.
    message_size = len(message)  # Calcula o tamanho da mensagem em bytes.
    size_packed = struct.pack("!I", message_size)  # Empacota o tamanho da mensagem como um valor de 4 bytes (formato de rede big-endian).
    client_socket.send(size_packed)  # Envia o tamanho da mensagem para o servidor.
    client_socket.send(message)  # Envia a mensagem para o servidor.

# Função para receber uma mensagem do servidor.
def receive_message(client_socket):
    size_packed = client_socket.recv(4)  # Recebe os 4 bytes iniciais que representam o tamanho da mensagem.
    if not size_packed:
        return None  # Se não houver dados recebidos, retorna None.
    message_size = struct.unpack("!I", size_packed)[0]  # Desempacota o tamanho da mensagem.
    message = client_socket.recv(message_size).decode()  # Recebe a mensagem com base no tamanho desempacotado e a decodifica.
    return message  # Retorna a mensagem recebida.

# Função principal do cliente.
def main():
    host = "127.0.0.1"  # Define o endereço IP do servidor.
    port = 12345  # Define a porta a ser usada para a conexão com o servidor.

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria um socket TCP.
    client_socket.connect((host, port))  # Conecta-se ao servidor especificado.

    while True:
        print("\nMenu:")
        print("1. Adicionar Pokémon")
        print("2. Ler Pokémon")
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
            print("Opções:")
            print("1. Ler a Pokedex completa")
            print("2. Ler dados de um Pokémon")
            choice_sub = input("Escolha uma opção: ")

            if choice_sub == "1":
                response = send_request(client_socket, 'read-all')
                if "A Pokedex está vazia." not in response:
                    print("Lista de Pokémon:")
                    print(response)
            elif choice_sub == "2":
                pokedex_number = int(input("Número na Pokédex do Pokémon a ser lido: "))
                response = send_request(client_socket, 'read', str(pokedex_number))
                if "Pokémon não encontrado." not in response:
                    print("Dados do Pokémon:")
                    print(response)
            else:
                print("Opção inválida. Tente novamente.")

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
