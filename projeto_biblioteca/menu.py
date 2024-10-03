from funcoes import *

base_clientes = {
    '123548': {'nome': 'Leticio', 'cpf': '123548', 'idade': 14, 'saldo': 50.5, 'divida': 0.0},
    '234659': {'nome': 'Maria', 'cpf': '234659', 'idade': 25, 'saldo': 100.0, 'divida': 0.0},
    '345760': {'nome': 'João', 'cpf': '345760', 'idade': 30, 'saldo': 75.3, 'divida': 0.0},
    '456871': {'nome': 'Ana', 'cpf': '456871', 'idade': 22, 'saldo': 200.0, 'divida': 0.0},
    '567982': {'nome': 'Carlos', 'cpf': '567982', 'idade': 45, 'saldo': 150.0, 'divida': 0.0},
    '678093': {'nome': 'Beatriz', 'cpf': '678093', 'idade': 18, 'saldo': 80.0, 'divida': 0.0},
    '789104': {'nome': 'Pedro', 'cpf': '789104', 'idade': 35, 'saldo': 120.5, 'divida': 0.0}
}

base_Livros = {
    '7854632': {'titulo': 'Lucia no País das Malas', 'genero': 'Ficção', 'faixa_etaria': 16, 'isbn': '7854632', 'editora': 'Clend', 'status': 'Disponível', 'valor': 80.5},
    '2346591': {'titulo': 'O Mistério da Casa Verde', 'genero': 'Mistério', 'faixa_etaria': 12, 'isbn': '2346591', 'editora': 'Editora Exemplo', 'status': 'Disponível', 'valor': 45.0},
    '3457602': {'titulo': 'Aventuras no Espaço', 'genero': 'Aventura', 'faixa_etaria': 10, 'isbn': '3457602', 'editora': 'Livros & Cia', 'status': 'Disponível', 'valor': 60.0},
    '4568713': {'titulo': 'O Segredo do Lago', 'genero': 'Fantasia', 'faixa_etaria': 18, 'isbn': '4568713', 'editora': 'Publicações ABC', 'status': 'Disponível', 'valor': 75.3},
    '5679824': {'titulo': 'Histórias de Fantasia', 'genero': 'Fantasia', 'faixa_etaria': 14, 'isbn': '5679824', 'editora': 'Editora XYZ', 'status': 'Disponível', 'valor': 50.0},
    '6780935': {'titulo': 'O Enigma do Relógio', 'genero': 'Mistério', 'faixa_etaria': 16, 'isbn': '6780935', 'editora': 'Clend', 'status': 'Disponível', 'valor': 90.0},
    '7891046': {'titulo': 'Contos de Fadas', 'genero': 'Infantil', 'faixa_etaria': 10, 'isbn': '7891046', 'editora': 'Editora Exemplo', 'status': 'Indisponivel', 'valor': 100.0}
}

while True:
    opcao1 = int(input("O que quer está relacionado com:\n"
                        "Clientes - 1 \n"
                        "Biblioteca - 2 \n"
                        "Sair - 0\n"))
    if opcao1 == 1:
        while True:
            opcao = int(input("Você quer:\n"
                            "Adicionar um cliente? - 1\n"
                            "Editar um cliente? - 2\n"
                            "Remover um cliente? - 3\n"
                            "Multar um cliente? - 4\n"
                            "ver a clinetes? - 5\n"
                            "voltar para o menu principal - 0\n"))
            if opcao == 1:
                adicionar_cliente(base_clientes)
            elif opcao == 2:
                editar_cliente(base_clientes)
            elif opcao == 3:
                remover_cliente(base_clientes)
            elif opcao == 4:
                multar_cliente(base_clientes)
            elif opcao == 5:
                print(base_clientes)
                print("esses sao os clientes que temos! ")
            elif opcao == 0:
                break
            else:
                print("Opção inválida. Tente novamente.")

    elif opcao1 == 2:

        while True:
            opcao = int(input("Você quer:\n"
                            "Adicionar um livro? - 1\n"
                            "Editar um livro? - 2\n"
                            "Remover um livro? - 3\n"
                            "comprar um livro - 4\n"
                            "pesquisar por um livro -5\n" 
                            "muder o livro para estar disponivel -6\n" 
                            "ver a biblioteca? - 7\n"
                            "voltar para o menu principal? - 0\n"))
            if opcao == 1:
                adicionar_livro(base_Livros)
            elif opcao == 2:
                editar_livro(base_Livros)
            elif opcao == 3:
                remover_livro(base_Livros)
            elif opcao == 4:
                comprar_livro(base_Livros,base_clientes)
            elif opcao == 5:
                pesquisar_livro(base_Livros)
            elif opcao == 6:
                mudar_status(base_Livros)
            elif opcao == 7:
                print(base_Livros)
                print("esses sao o livros que temos!")
            elif opcao == 0:
                break
            else:
                print("Opção inválida. Tente novamente.")

    elif opcao1 == 0:
        print("saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")