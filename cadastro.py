#!/usr/bin/env python
# coding: utf-8

# In[ ]:


usuarios = {}

def cadastrar_usuario(nome, senha):
    if nome in usuarios:
        print("Nome de usuário já existe. Por favor, escolha outro nome.")
    else:
        usuarios[nome] = senha
        print("Usuário registrado com sucesso!")

def fazer_login(nome, senha):
    if nome in usuarios and usuarios[nome] == senha:
        print("Login bem-sucedido!")
    else:
        print("Nome de usuário ou senha incorretos.")

def main():
    while True:
        print("1 - Cadastrar usuário")
        print("2 - Fazer login")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome de usuário: ")
            senha = input("Digite a senha: ")
            cadastrar_usuario(nome, senha)
        elif opcao == '2':
            nome = input("Digite o nome de usuário: ")
            senha = input("Digite a senha: ")
            fazer_login(nome, senha)
        elif opcao == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()


# In[ ]:




