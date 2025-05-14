# Menu para o usuário selecionar o tipo de operação
menu = """

[D] Depositar
[S] Sacar
[E] Extrato
[Sr] Sair

=> """

# Saldo inicial, o limite de saque, o extrato vazio, número de saques feitos até o momento e o limite de saques por dia
saldo = 0
limite = 500
extrato = ""
numeros_saque = 0
LIMITE_SAQUE = 3

# Laço principal que executa até o usuário decidir sair
while True:
    # Mostra o menu e recebe a opção escolhida pelo usuário
    opcao = input(menu)

    # Verifica se a opção é depósito
    if opcao == "D":
        valor = float(input("Por favor, informar o valor do depósito: "))  # Solicita valor a ser depositado
        
        if valor > 0:  # Verifica se o valor é positivo
            saldo += valor  # Soma o valor ao saldo
            extrato += f"Depósito: R$ {valor:.2f}\n"  # Registra o depósito no extrato
        else:
            print("O valor informado é inválido best, por favor tente novamente!")  # Alerta de valor inválido

    # Verifica se a opção é saque
    elif opcao == "S":
        valor = float(input("Por favor, informe o valor do saque: "))  # Solicita valor a ser sacado

        # Verifica se o saque ultrapassa o saldo disponível
        excedeu_saldo = valor > saldo

        # Verifica se o saque ultrapassa o limite de R$500
        excedeu_limite = valor > limite

        # Verifica se já foi atingido o limite diário de saques
        excedeu_saques = numeros_saque >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Saldo insuficiente, Diva(o)!")  # Mensagem para saldo insuficiente

        elif excedeu_limite:
            print("Miga(o), infelizmente o saque excede o limite")  # Mensagem para saque maior que o limite

        elif excedeu_saques: 
            print("Ihhh, número de saque excedido!")  # Mensagem para saque excedido no dia

        elif valor > 0:
            saldo -= valor  # Subtrai o valor do saldo
            extrato += f"Saque: R$ {valor:.2f}\n"  # Registra o saque no extrato
            numeros_saque += 1  # Aumenta a contagem de saques realizados
        else:
            print("Gata, o valor informado é inválido!")  # Mensagem para valor inválido

    # Verifica se a opção é extrato
    elif opcao == "E":
        print("\n============= EXTRATO ============")
        if extrato == "":  # Verifica se ainda não houve movimentações
            print("Não tivemos movimentações por aqui... Parabéns ou falida?")
        else:
            print(extrato)  # Exibe o extrato das operações
        print(f"\nSaldo: R$ {saldo:.2f}")  # Exibe o saldo atual
        print("=====================================")

    # Verifica se a opção é sair
    elif opcao == "Sr":
        break  # Encerra o laço e finaliza o programa

    # Caso o usuário digite algo que não está no menu
    else:
        print("Opção inválida, tente novamente!")  # Mensagem de erro para opção inválida
