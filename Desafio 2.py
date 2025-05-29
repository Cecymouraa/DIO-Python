# Dicionários simples para armazenar os dados
usuarios = {}  # chave = cpf, valor = nome
contas = {}    # chave = numero da conta, valor = cpf
saldos = {}    # chave = numero da conta, valor = saldo
extratos = {}  # chave = numero da conta, valor = lista de transações

# Função para criar usuário
def criar_usuario():
    print("\n=== Criar Usuário ===")
    cpf = input("CPF (somente números): ")

    if cpf in usuarios:
        print("Usuário já existe.")
    else:
        nome = input("Nome completo: ")
        usuarios[cpf] = nome
        print("Usuário criado com sucesso!")

# Função para criar conta vinculada a um CPF
def criar_conta():
    print("\n=== Criar Conta ===")
    cpf = input("Informe o CPF do usuário: ")

    if cpf not in usuarios:
        print("Usuário não encontrado. Crie o usuário primeiro.")
    else:
        numero = len(contas) + 1  # número da conta gerado automaticamente
        contas[numero] = cpf
        saldos[numero] = 0
        extratos[numero] = []
        print(f"Conta criada com sucesso! Número da conta: {numero}")

# Função para depositar
def depositar():
    print("\n=== Depósito ===")
    numero = int(input("Número da conta: "))
    
    if numero not in contas:
        print("Conta não encontrada.")
        return
    
    valor = float(input("Valor do depósito: "))

    if valor <= 0:
        print("Valor inválido.")
    else:
        saldos[numero] += valor
        extratos[numero].append(f"Depósito: +R$ {valor:.2f}")
        print("Depósito realizado com sucesso.")

# Função para sacar
def sacar():
    print("\n=== Saque ===")
    numero = int(input("Número da conta: "))

    if numero not in contas:
        print("Conta não encontrada.")
        return

    valor = float(input("Valor do saque: "))

    if valor <= 0:
        print("Valor inválido.")
    elif valor > saldos[numero]:
        print("Saldo insuficiente.")
    else:
        saldos[numero] -= valor
        extratos[numero].append(f"Saque: -R$ {valor:.2f}")
        print("Saque realizado com sucesso.")

# Função para mostrar o extrato
def ver_extrato():
    print("\n=== Extrato ===")
    numero = int(input("Número da conta: "))

    if numero not in contas:
        print("Conta não encontrada.")
        return

    print("\nMovimentações:")
    for item in extratos[numero]:
        print(item)
    
    print(f"\nSaldo atual: R$ {saldos[numero]:.2f}")

# Menu principal
def menu():
    while True:
        print("""
====== MENU ======
[1] Criar usuário
[2] Criar conta
[3] Depositar
[4] Sacar
[5] Ver extrato
[0] Sair
""")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_usuario()
        elif opcao == "2":
            criar_conta()
        elif opcao == "3":
            depositar()
        elif opcao == "4":
            sacar()
        elif opcao == "5":
            ver_extrato()
        elif opcao == "0":
            print("Saindo... Obrigado por usar!")
            break
        else:
            print("Opção inválida.")

# Iniciar o programa
menu()
