import socket  # Importa a biblioteca socket para comunicação por rede.
import struct  # Importa a biblioteca struct para empacotar e desempacotar dados binários.

# Dados iniciais da Pokedex
pokedex = []

## FUNÇÕES PARA MANIPULAR A POKEDEX
def create_pokemon(data):
    pokedex.append(data)  # Adiciona um Pokémon à Pokedex.

def read_pokemon(pokedex_number):
    return pokedex  # Retorna a Pokedex completa.

def update_pokemon(pokedex_number, data):
    for i, pokemon in enumerate(pokedex):
        if pokemon['numero'] == pokedex_number:
            pokedex[i] = data  # Atualiza os dados de um Pokémon na Pokedex.
            return True
    return False  # Retorna False se o Pokémon não for encontrado.

def delete_pokemon(pokedex_number):
    for i, pokemon in enumerate(pokedex):
        if pokemon['numero'] == pokedex_number:
            del pokedex[i]  # Remove um Pokémon da Pokedex.
            return True
    return False  # Retorna False se o Pokémon não for encontrado.

## --------------------------------------------------------------------------

## Função que envia a mensagem
def send_message(client_socket, message):
    message = message.encode()  # Codifica a mensagem em bytes.
    message_size = len(message)  # Calcula o tamanho da mensagem em bytes.
    size_packed = struct.pack("!I", message_size)  # Empacota o tamanho da mensagem como um valor de 4 bytes (formato de rede big-endian).
    client_socket.send(size_packed)  # Envia o tamanho da mensagem para o cliente.
    client_socket.send(message)  # Envia a mensagem para o cliente.

## --------------------------------------------------

## Função que recebe a mensagem
def receive_message(client_socket):
    size_packed = client_socket.recv(4)  # Recebe os 4 bytes iniciais que representam o tamanho da mensagem.
    if not size_packed:
        return None
    message_size = struct.unpack("!I", size_packed)[0]  # Desempacota o tamanho da mensagem.
    message = client_socket.recv(message_size).decode()  # Recebe a mensagem com base no tamanho desempacotado e a decodifica.
    return message  # Retorna a mensagem recebida.

## -----------------------------------------------------

## Recebe e processa as solicitações
def handle_client(client_socket):
    while True:
        request = receive_message(client_socket)  # Recebe uma mensagem do cliente.
        if not request:
            break

        request_data = request.split(" ", 1)
        action = request_data[0]  # Extrai a ação da mensagem.

        ## Cria um novo Pokémon
        if action == 'create':
            data = request_data[1]
            create_pokemon(eval(data))  # Avalia e adiciona um novo Pokémon à Pokedex com base nos dados recebidos.
            response = "Pokémon criado com sucesso!"
        ## -----------------------------------------

        ## Lê a Pokedex completa
        elif action == 'read-all':
            if pokedex:
                response = str(pokedex)  # Converte a Pokedex em uma string para envio.
            else:
                response = "A Pokedex está vazia."
        ## ----------------------------------------

        ## Lê dados de um único Pokémon por número
        elif action == 'read':
            pokedex_number = int(request_data[1])
            pokemon_data = None
            for pokemon in pokedex:
                if pokemon['numero'] == pokedex_number:
                    pokemon_data = pokemon
                    break
            if pokemon_data:
                response = str(pokemon_data)  # Converte os dados do Pokémon em uma string para envio.
            else:
                response = "Pokémon não encontrado."
        ## ----------------------------------------

        ## Atualiza todos os dados de um Pokémon de acordo com as novas entradas
        elif action == 'update':
            data = request_data[1]
            data = data.split()
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
        ## ----------------------------------------------

        ## Deleta um Pokémon
        elif action == 'delete':
            pokedex_number = int(request_data[1])
            delete_pokemon(pokedex_number)  # Remove um Pokémon da Pokedex com base no número.
            response = "Pokémon excluído com sucesso!"
        ## ----------------------------------------------
        else:
            response = "Ação inválida."

        ## Envia a mensagem de resposta para o cliente
        send_message(client_socket, response)

    client_socket.close()  # Fecha o socket do cliente após o processamento.

## ------------------------------------------------------------------------------------------------------------------------------------------

## Definições do servidor
def main():
    host = "127.0.0.1"  # Define o endereço IP do servidor.
    port = 12345  # Define a porta a ser usada para a conexão com o servidor.

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria um socket TCP.
    server_socket.bind((host, port))  # Associa o socket ao endereço IP e à porta especificados.
    server_socket.listen(5)  # Coloca o servidor no modo de escuta, permitindo até 5 conexões pendentes.
    print(f"Servidor escutando em {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()  # Aceita uma nova conexão do cliente.
        print(f"Conexão de {addr[0]}:{addr[1]} estabelecida.")
        handle_client(client_socket)  # Chama a função para lidar com as solicitações do cliente.

if __name__ == "__main__":
    main()  # Inicia a execução do servidor.
