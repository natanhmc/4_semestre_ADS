from Data import Data
from Contato import Contato

class Menu:
    
    def menu(self):
        data = Data()
        perfil = Contato()
        data.criar_banco()
        try:
            while True:
                print("\n1. Adicionar Contato")
                print("2. Listar Contatos")
                print("3. Excluir Contato")
                print("0. Sair")
                escolha = input("Escolha uma opção: ")
                
                
                
                if escolha == "1":
                    nome = input("Nome do Contato: ")
                    perfil_linkedin = input("Perfil do contato: ")
                    perfil.adicionar_contato(nome, perfil_linkedin, data)
                elif escolha == "2":
                    contatos = perfil.listar_contatos(data)
                    for contato in contatos:
                        print(f"ID : {contato[0]},Nome: {contato[1]}, Perfil Linkedin: {contato[2]}")
                elif escolha == "3":
                    id = input("Informe o Id do Contato: ")
                    perfil.excluir_contato(id, data)
                    print("Contato excluido!!")
                elif escolha == "0":
                    break
                else:
                    print("Opção inválida. Tente novamente")
        finally:
            data.fechar_banco()
            
             
