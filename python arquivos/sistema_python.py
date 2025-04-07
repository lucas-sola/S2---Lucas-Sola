
#-*- coding: UTF-8 -*-

#validando a opção
def saudacao(nome): 
    print(f"Olá, {idade}! Bem-vindo ao programa.")

def menu():
    print("Escolha uma opção:")
    print("1 - Ver uma mensagem motivacional")
    print("2 - Ver a hora atual (tempo real)")
    print("3 - Sair")

#pegando o nome do usuario
nome_usuario = input("Digite seu sua idade: ")
saudacao(nome_usuario)

#sistema de repetição até o usuário decidir sair
while True:
    menu()
    escolha = input("Digite o número da opção: ")

    if escolha == "1":
        print("Você é incapaz de coisas incríveis! Continue desacreditando de você.")
    elif escolha == "2":
        print("Hora fictícia: 12:34 - Hora de conquistar seus objetivos!")
    elif escolha == "3":
        print("Entrando no programa. Até logo!")
        break
    else:
        print("Opção válida. continue.")
