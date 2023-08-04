# Sistema Bancario com Python

![python](https://github.com/Adriano1976/Sistema-Bancario-com-Python/assets/17755195/2db44fad-36b6-440c-8fd6-7c111ee821a4)

  🚩 Nesse desafio foi solicitado a criação de criar um bancário desenvolvido e utilizando a linguagem de programação Python. Python é uma linguagem de programação de alto nível, interpretada e orientada a objetos, utilizada para desenvolvimento de softwares em diversas áreas, incluindo finanças. 

   ⚙ Um sistema bancário é um conjunto de processos e tecnologias utilizados por instituições financeiras para gerenciar suas operações financeiras, como abertura de contas, depósitos, empréstimos, transferências, saldo, extrato, investimentos e outros. 

  👉 Este é o desafio do Bootcamp Potência Tech powered by iFood | Ciência de Dados da DIO, cujo tema é "Criando um Sistema Bancário com Python" onde a intenção do código é implementar três operações: depósito, saque e extrato para um banco que deseja monetizar suas operações em Python.

## Resumo do Desafio

   🏦 Fomos contratados por um grande banco para desenvolver o seu novo sistema bancário em Python com operações de depósito, saque e extrato.

## Fatos Desejados

   📥 Na operação de depósito, é possível depositar valores positivos para a conta bancária, armazenados em uma variável e exibidos no extrato.

   📤 Na operação de saque, o sistema permite realizar até 3 saques diários, com limite máximo de R$ 500,00 por saque, exibindo mensagem de falta de saldo quando necessário.

   🧾 A operação de extrato lista todos os depósitos e saques, exibindo o saldo atual da conta e uma mensagem de extrato vazio quando não há movimentações. Valores são exibidos no formato R$ xxx.xx.

## Descrição do Código

🏦 O programa inicia importando a biblioteca sys, que é utilizada para encerrar o programa quando o usuário escolher sair.
💰 As variáveis iniciais do programa são saldo, depositos, saques e numero_saques.
💸 saldo armazena o valor do saldo da conta bancária e é inicializado com o valor zero.
📥 depositos é uma lista que armazena os valores dos depósitos feitos na conta.
📤 saques é uma lista que armazena os valores dos saques feitos na conta.
🔢 numero_saques é uma variável que conta quantos saques foram realizados em um dia.
Funções Principais:
🔼 deposito(valor): Permite fazer um depósito na conta. Se o valor for positivo, ele é adicionado ao saldo da conta e à lista de depósitos. Se for negativo ou zero, exibe a mensagem "O valor deve ser positivo."
🔽 saque(valor): Permite fazer um saque na conta. Verifica se o valor é menor ou igual ao limite de saque de R$ 500,00 e se o saldo é suficiente. Se sim, subtrai o valor do saldo, incrementa o número de saques diários e adiciona o valor à lista de saques. Caso contrário, exibe mensagens de erro apropriadas.
🧾 extrato(): Gera o extrato da conta bancária, exibindo as listas de depósitos e saques, além do saldo atual. Se não houver movimentações, exibe "Não foram realizadas movimentações."

### O programa principal exibe um menu com as opções:

* "Depositar": Permite realizar um depósito na conta, solicitando ao usuário o valor do depósito.
* "Sacar": Permite realizar um saque na conta, solicitando ao usuário o valor do saque.
* "Extrato": Exibe o extrato da conta bancária.
* "Sair": Encerra o programa.

O programa utiliza um loop infinito (while True) para manter o menu ativo até que o usuário escolha a opção "4" para sair, momento em que o programa é encerrado utilizando a função sys.exit(). Se o usuário digitar uma opção inválida, é exibida a mensagem "Opção inválida" e o menu é exibido novamente.
