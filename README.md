Objetivo:

A aplicação possui 2 telas
- Tela de cadastro de cidade e listagem das cidades cadastradas: Permitir o usuário
cadastrar somente cidades validas na API (que retornem dados).
- Na listagem de cidades deve ter um link para visualizar os detalhes da previsão (Tela
de detalhe das previsões)
- Tela de detalhe das previsões: Exibe um “forecast” de 5 dias para a cidade selecionada.

Estrutura:

No projeto não foi utilizado banco de dados(SGBD), os dados são gravados em um arquivo dentro do projeto.

Lista de tecnologias usadas:

- Docker
- Docker-compose
- Framework Flask
- API externa openweathermap
- Tests no momendo de build

Passos para Rodar o Projeto e Pre requisitos:

Passo 1:
	- ter o Docker instalado em seu computador
	caso nao tenha, acessa o link https://docs.docker.com/install/

Passo 2:
	- Ter o docker-compose instalado em seu computador
	caso nao tenha, acessa o link https://docs.docker.com/compose/install/

Passo 3:
    - O projeto está ouvindo a porta 80, portanto, certificar se que seu computador, está com a porta 80 livre, caso não esteje, mudar no projeto o arquivo docker-compose para a porta que desejar

Passo 4:
	- Na Raiz do projeto executar o comando: $ docker-compose up

Passo 5:
    - Acessa o endereco http://localhost/ em seu browser, caso nao tenha mudado a porta do projeto.