def sacar (valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado!")
        print("Retire o seu dinheiro na boca do caixa.")

    print("Saldo insuficiente!")

sacar(1000)

def depositar(valor):
    saldo = 500
    saldo += valor 
    
    print("Valor depositado com sucesso!")
    
depositar(500)