import requests
import json
from time import sleep #IMPORT DE TEMPO PARA PAUSAS NO ALGORITMO
import os # IMPORT DE LIMPAR TERMINAL

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()
cotacao_dolar = cotacoes['USDBRL']['bid']
cotacao_eu = cotacoes['EURBRL']['bid']
cotacao_btc = cotacoes['BTCBRL']['bid']




def menu():
    print("\n---Bem vindo o menu de cotações---")
    print("1. Cotações")
    print("2. Encerrar")
    print("-----------------------------------\n")



def cota():
    print("1. Dolar")
    print("2. Euro")
    print("3. Bitcoin")
    print("4. Voltar")
    opcao2 = int(input("Digite a opção: "))
    if opcao2 == 1:
        print("\nDolar: ", cotacao_dolar)
        voltar_ao_menu()
    elif opcao2 == 2:
        print("\nEuro: ", cotacao_eu)
        voltar_ao_menu()
    elif opcao2 == 3:
        print("\nBitcoin: ", cotacao_btc)
        voltar_ao_menu()
    elif opcao2 == 4:
        os.system('cls')
    

def voltar_ao_menu():
    input("\nPressione Enter para voltar ao menu principal.")
    os.system('cls')



while True:
    menu()
    opcao = int(input("Digite a opção: "))
    if opcao == 1:
        os.system('cls')
        cota()
    elif opcao == 2:
        os.system('cls')
        print("Encerrado!")
        break
    else:
        print("Digite uma opção válida!")
        sleep(3)
        os.system('cls')