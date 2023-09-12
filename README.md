**Documentação do Sistema de Pokedex**

Este documento fornece uma visão geral detalhada do sistema de Pokedex, incluindo seus componentes, funcionalidades, requisitos e instruções para uso. O sistema de Pokedex é um aplicativo de servidor-cliente que permite aos usuários gerenciar uma lista de Pokémon, incluindo a capacidade de criar, ler, atualizar e excluir informações sobre eles.

**1. Visão Geral**

O sistema de Pokedex é composto por um servidor e um ou mais clientes que se comunicam por meio de sockets TCP/IP. O servidor mantém uma lista de Pokémon, enquanto os clientes podem enviar solicitações para executar operações específicas na Pokedex, como adicionar, ler, atualizar ou excluir Pokémon.

**2. Componentes do Sistema**

O sistema de Pokedex possui os seguintes componentes:

- **Servidor**: Responsável por gerenciar a Pokedex e aceitar conexões de clientes. Ele aguarda solicitações de clientes e executa as operações solicitadas na Pokedex.

- **Cliente**: Os clientes se conectam ao servidor para interagir com a Pokedex. Eles podem enviar solicitações para criar, ler, atualizar ou excluir Pokémon na Pokedex.

**3. Funcionalidades**

O sistema de Pokedex oferece as seguintes funcionalidades:

- **Criar Pokémon**: Os clientes podem adicionar informações sobre um novo Pokémon à Pokedex. Isso inclui dados como número, nome, tipo, raridade, peso e altura.

- **Ler Pokémon**: Os clientes podem solicitar a leitura de informações sobre Pokémon específicos ou de toda a Pokedex. A resposta incluirá os dados do Pokémon ou a lista completa, respectivamente.

- **Atualizar Pokémon**: Os clientes podem atualizar os dados de um Pokémon existente na Pokedex, fornecendo novas informações.

- **Excluir Pokémon**: Os clientes podem solicitar a exclusão de um Pokémon da Pokedex com base no número do Pokémon.

**4. Requisitos de Sistema**

Para usar o sistema de Pokedex, é necessário:

- Python 3.x instalado tanto no servidor quanto nos clientes.
- Conexão de rede funcional entre o servidor e os clientes.

**5. Uso do Sistema**

A seguir, estão as instruções para executar o sistema de Pokedex:

**5.1. Configuração do Servidor**

- Execute o arquivo `server.py` no servidor. Isso iniciará o servidor e o colocará em modo de escuta.

**5.2. Configuração do Cliente**

- Execute o arquivo `client.py` em um ou mais clientes. Isso abrirá uma interface de linha de comando interativa.

**5.3. Uso da Interface do Cliente**

- Quando a interface do cliente estiver ativa, siga as instruções exibidas no menu.

- Use as opções do menu para criar, ler, atualizar ou excluir Pokémon.

- Para criar um Pokémon, forneça os detalhes solicitados, como número, nome, tipo, raridade, peso e altura.

- Para ler informações sobre Pokémon, escolha entre ler a Pokedex completa ou ler informações sobre um Pokémon específico.

- Para atualizar um Pokémon, forneça o número do Pokémon e os novos detalhes.

- Para excluir um Pokémon, forneça o número do Pokémon a ser excluído.

- Para sair do cliente, escolha a opção "Sair".

**6. Exemplos de Uso**

Aqui estão alguns exemplos de como usar as funcionalidades do sistema de Pokedex:

- Para criar um novo Pokémon:

```
1. Adicionar Pokémon
Nome do Pokémon: Pikachu
Tipo do Pokémon: Elétrico
Raridade do Pokémon: Comum
Peso do Pokémon: 6.0
Altura do Pokémon: 0.4
Número na Pokédex: 25
```

- Para ler a Pokedex completa:

```
2. Ler Pokémon
Opções:
1. Ler a Pokedex completa
2. Ler dados de um Pokémon
Escolha uma opção: 1
```

- Para ler dados de um Pokémon específico:

```
2. Ler Pokémon
Opções:
1. Ler a Pokedex completa
2. Ler dados de um Pokémon
Escolha uma opção: 2
Número na Pokédex do Pokémon a ser lido: 25
```

- Para atualizar um Pokémon:

```
3. Atualizar Pokémon
Número na Pokédex do Pokémon a ser atualizado: 25
Novo nome do Pokémon: Pikachu Raichu
Novo tipo do Pokémon: Elétrico
Nova raridade do Pokémon: Raro
Novo peso do Pokémon: 30.0
Nova altura do Pokémon: 0.8
```

- Para excluir um Pokémon:

```
4. Excluir Pokémon
Número na Pokédex do Pokémon a ser excluído: 25
```

**7. Considerações de Segurança**

- Este sistema não implementa autenticação ou autorização, portanto, qualquer cliente pode acessar e modificar a Pokedex. Para uso em um ambiente de produção, considere adicionar autenticação e autorização robustas.

- Certifique-se de proteger o acesso ao servidor, permitindo apenas conexões de clientes confiáveis e evitando exposição à Internet pública.

**8. Conclusão**

Este documento forneceu uma visão geral detalhada do sistema de Pokedex, incluindo seus componentes, funcionalidades, requisitos e instruções para uso. O sistema de Pokedex é uma ferramenta versátil para gerenciar informações sobre Pokémon e pode ser estendido e aprimorado para atender às necessidades específicas de um ambiente de aplicação real.
