import time
import os
import platform

def limpar_tela():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


saldo = 3000
senha_user = 120304


limpar_tela() 
print('Bem Vindo ao Sistema de Saque')
print('Por Favor Aguarde', end='', flush=True)
for i in range(3):
    print('.', end='', flush=True)
    time.sleep(1) 
print()


limpar_tela()
senha_insert = int(input('Insira Sua Senha: '))
if senha_insert != senha_user:
    limpar_tela()
    print('Senha Incorreta\nFinalizando', end='', flush=True)
    for i in range(3):
        print('.', end='', flush=True)
        time.sleep(0.5)
    print()

else:

    limpar_tela()
    print('Senha Inserida Corretamente!')
    opc = input('Selecione (saque) ou (sair): ')


    if opc == 'sair':
        limpar_tela()
        print('Saindo do Sistema', end='', flush=True)
        for i in range(3):
            print('.', end='', flush=True)
            time.sleep(0.5)
        print()

    elif opc == 'saque':
        limpar_tela()
        valor = int(input(f'Seu saldo é: R${saldo:.2f}\nDigite a quantia que deseja sacar: '))
        
        if valor <= saldo:
            limpar_tela()
            print('Retire o Dinheiro e o cartão')
            time.sleep(2.0)

            limpar_tela()
            recibo = input('Deseja imprimir o recibo (sim / nao): ').lower()

            if recibo == 'sim':
                limpar_tela()
                print('Retire o seu recibo')
                time.sleep(1.5)

            elif recibo == 'nao':
                pass 

            else:
                limpar_tela()
                print('Opção de recibo inválida.')
                time.sleep(1.5)
            
            saldo -= valor 
            limpar_tela()
            print('Sistema Finalizado', end='', flush=True)
            for i in range(3):
                print('.', end='', flush=True)
                time.sleep(0.5)
            print()

        else: 
            limpar_tela()
            print('Saldo insuficiente!\nValor negado.\n\nFinalizando', end='', flush=True)
            for i in range(3):
                print('.', end='', flush=True)
                time.sleep(0.5)
            print()

    else:
        limpar_tela()
        print('Opção Inválida')
        print('Sistema Finalizado', end='', flush=True)
        for i in range(3):
            print('.', end='', flush=True)
            time.sleep(0.5)
        print()

limpar_tela()
print('Obrigado por usar nosso sistema!')
print(f'Seu saldo final é: R${saldo:.2f}') 