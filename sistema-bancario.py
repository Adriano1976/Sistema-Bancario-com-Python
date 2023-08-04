# Importando as bibliotecas necessárias
import sys

# Definindo as variáveis iniciais
saldo = 0
depositos = []
saques = []
numero_saques = 0

# Função para fazer um depósito
def deposito(valor):
    global saldo
    global depositos

    # Verificando se o valor é positivo
    if valor > 0:
        # Adicionando o valor ao saldo
        saldo += valor        
        # Adicionando o valor à lista de depósitos
        depositos.append(valor)
    else:
        print("O valor deve ser positivo.")

# Função para fazer um saque
def saque(valor):
    global saldo
    global saques
    global numero_saques

    # Verificando se o valor é menor ou igual ao limite de saque
    if valor <= 500:
        # Verificando se o saldo é suficiente para o saque
        if saldo >= valor:
            # Reduzindo o saldo pelo valor do saque
            saldo -= valor
            # Contando o número de saques ao dia
            numero_saques += 1
            # Verificando se o número de saques excede ao limite de 3 ao dia.
            if numero_saques > 3:
                print("O número de saques deve ser menor ou igual a 3 vezes ao dia.")          
            # Adicionando o valor à lista de saques
            saques.append(valor)
        else:
            print("Saldo insuficiente para o saque.")
    else:
        print("O valor do saque deve ser menor ou igual a R$ 500,00.")

# Função para gerar o extrato
def extrato():
    global saldo
    global depositos
    global saques

    # Se a lista de depósitos ou saques estiver vazia, exibir a mensagem "Não foram realizadas movimentações."
    if not depositos or not saques:
        print("Não foram realizadas movimentações.")
    else:
        # Exibir a lista de depósitos
        print("Depósitos:")
        for deposito in depositos:
            print(f"R$ {deposito:.2f}")

        # Exibir a lista de saques
        print("Saques:")
        for saque in saques:
            print(f"R$ {saque:.2f}")

        # Exibir o saldo atual
        print()
        print(f"Saldo: R$ {saldo:.2f}")

# Exibindo o menu
print("Seja bem-vindo ao sistema bancário!")
while True:
    print()
    print("|============MENU=========-===|")
    print("Escolha uma opção:")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Extrato")
    print("4. Sair")
    print("|======= Banco Virtual =======|")

    # Lendo a opção do usuário
    escolha = input("Digite a operação desejada: ")

    # Verificando a opção do usuário
    if escolha == "1":
        # Solicitando o valor do depósito
        valor = float(input("Informe o valor do depósito: "))
        deposito(valor)
    elif escolha == "2":
        # Solicitando o valor do saque
        valor = float(input("Informe o valor do saque: "))
        saque(valor)
    elif escolha == "3":
        extrato()
    elif escolha == "4":
        # Encerrando o programa
        sys.exit()
    else:
        print("Opção inválida.")
