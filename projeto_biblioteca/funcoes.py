def adicionar_cliente(base_clientes):
    nome = input("Escreva seu nome: ")
    cpf = input("Escreva seu CPF: ")
    idade = int(input("Escreva sua idade: "))
    saldo = float(input("Quanto você quer colocar na sua carteira da biblioteca? "))

    cliente = {"nome": nome, "cpf" : cpf, "idade": idade, "saldo": saldo}
    base_clientes[cpf] = cliente  
    print(f"O leitor {nome} com {idade} anos foi adicionado.")

def editar_cliente(base_clientes):
    cpf = input("Escreva o CPF do indivíduo: ")
    if cpf in base_clientes:
        opcao = int(input("O que você quer editar? \n"
                          "1. Nome \n"
                          "2. CPF \n"
                          "3. Idade \n"
                          "4. Saldo \n"
                          "5. Sair \n"))

        if opcao == 1: 
            novo_nome = input("Escreva o novo nome: ")
            base_clientes[cpf]["nome"] = novo_nome
            print(f"O nome atual é {novo_nome}")

        elif opcao == 2: 
            novo_cpf = input("Escreva o novo CPF: ")
            registro = base_clientes[cpf]
            base_clientes[novo_cpf] = registro
            base_clientes[novo_cpf]["cpf"] = novo_cpf
            del base_clientes[cpf]
            print(f"O CPF atual é {novo_cpf}")

        elif opcao == 3: 
            nova_idade = input("Escreva a nova idade: ")
            if nova_idade.isdigit(): 
                base_clientes[cpf]["idade"] = int(nova_idade)
                print(f"A idade atual é {nova_idade}")
            else:
                print("Idade inválida! Deve ser um número.")

        elif opcao == 4: 
            saldo_adicional = float(input("Escreva o valor a adicionar: "))
            saldo_adicional = float(saldo_adicional)
            base_clientes[cpf]["saldo"] += saldo_adicional
            print(f"O saldo atual é R${base_clientes[cpf]['saldo']:.2f}")

            
            if base_clientes[cpf]["divida"] > 0:
                if base_clientes[cpf]["saldo"] >= base_clientes[cpf]["divida"]:
                    base_clientes[cpf]["saldo"] -= base_clientes[cpf]["divida"]
                    print(f"A dívida foi paga! Saldo atual: R${base_clientes[cpf]['saldo']:.2f}")
                    base_clientes[cpf]["divida"] = 0 
                else:
                    base_clientes[cpf]["divida"] -= base_clientes[cpf]["saldo"]
                    print(f"Parte da dívida foi paga. Dívida restante: R${base_clientes[cpf]['divida']:.2f}")
                    base_clientes[cpf]["saldo"] = 0  
            else:
                print("Valor inválido! Deve ser um número.")
                

        elif opcao == 5: 
            print("Voltando...")

        else: 
            print("Número inválido")
    else: 
        print("Cliente não existe\nVoltando...")

def remover_cliente(base_clientes):
    cpf = input("Escreva o CPF do indivíduo: ")
    if cpf in base_clientes: 
        del base_clientes[cpf]
        print("O cliente foi deletado com sucesso!")
    else:
        print("Cliente não encontrado.")       

def multar_cliente(base_clientes):
    cpf = input("Digite o cpf do cliente: ")

    
    if cpf not in base_clientes:
        print("Cliente não encontrado.")
        return
    multas = float(input("escreva o valor da multa: "))
    
    valor_multa = multas
        
        
    saldo = base_clientes[cpf]['saldo']
        
    if saldo >= valor_multa:
        base_clientes[cpf]['saldo'] -= valor_multa  
        print(f"{cpf}Valor da multa: R${valor_multa:.2f}.")
        print(f"Saldo restante: R${base_clientes[cpf]['saldo']:.2f}.")
    else:   
        base_clientes[cpf]['divida'] += valor_multa
        base_clientes[cpf]['saldo'] -= valor_multa
        print(f"{base_clientes[cpf]['nome']} não possui saldo suficiente. A multa de R${valor_multa:.2f} foi adicionada à dívida.")
        print(f"Dívida atual: R${base_clientes[cpf]['saldo']:.2f}.")

def adicionar_livro(base_Livros):
    titulo = input("Escreva o título do livro: ")
    genero = input("Escreva o gênero do livro: ")
    faixa_etaria = input("Escreva a faixa etária recomendada: ")
    isbn = input("Escreva o ISBN do livro: ")
    editora = input("Escreva o nome da editora: ")
    status = "Disponível"
    valor = float(input("Escreva o valor do livro: "))

    livro = {"titulo": titulo,"genero": genero,"faixa_etaria": faixa_etaria,"isbn": isbn,"editora": editora,"status": status,"valor": valor}
    base_Livros[isbn] = livro
    print(f"\nO livro '{titulo}' foi adicionado à prateleira.\n")

def editar_livro(base_Livros):
    isbn = input("Escreva o ISBN do livro: ")
    if isbn in base_Livros:
        opcao = int(input("O que você quer editar? \n"
                          "1. Título \n"
                          "2. Gênero \n"
                          "3. Faixa Etária \n"
                          "4. Editora \n"
                          "5. Valor \n"
                          "6. Sair \n"))

        if opcao == 1: 
            novo_titulo = input("Escreva o novo título: ")
            base_Livros[isbn]["titulo"] = novo_titulo
            print(f"O título atual é {novo_titulo}")

        elif opcao == 2: 
            novo_genero = input("Escreva o novo gênero: ")
            base_Livros[isbn]["genero"] = novo_genero
            print(f"O gênero atual é {novo_genero}")

        elif opcao == 3: 
            nova_faixa_etaria = input("Escreva a nova faixa etária: ")
            base_Livros[isbn]["faixa_etaria"] = nova_faixa_etaria
            print(f"A faixa etária atual é {nova_faixa_etaria}")

        elif opcao == 4: 
            nova_editora = input("Escreva o nome da nova editora: ")
            base_Livros[isbn]["editora"] = nova_editora
            print(f"A editora atual é {nova_editora}")

        elif opcao == 5: 
            novo_valor = float(input("Escreva o novo valor: "))
            base_Livros[isbn]["valor"] = novo_valor
            print(f"O valor atual é {novo_valor}")

        elif opcao == 6: 
            print("Voltando...")

        else: 
            print("Número inválido")
    else: 
        print("Livro não existe\nVoltando...")

def remover_livro(base_Livros):
    
    isbn = input("Escreva o CPF do indivíduo: ")
    if isbn in base_Livros: 
        del base_Livros[isbn]
        print("O livro foi deletado com sucesso!")
    else:
        print("livro não encontrado.")

def comprar_livro(base_Livros, base_clientes):
    
    cpf = input("Digite o CPF do cliente: ")
    if cpf not in base_clientes:
        print("Cliente não encontrado.")
        return

    isbn = input("Digite o ISBN do livro: ")
    
    if isbn not in base_Livros:
        print("Livro não encontrado.")
        return

    cliente = base_clientes[cpf]
    livro = base_Livros[isbn]
    
    if cliente['divida'] > 0:
        print(f"{cliente['nome']} não pode comprar '{livro['titulo']}' devido à dívida de R${cliente['divida']:.2f}.")
        return
    
    if cliente['idade'] < livro['faixa_etaria']:
        print(f"{cliente['nome']} não pode comprar '{livro['titulo']}' devido à restrição de faixa etária.")
        return

    
    if cliente['saldo'] < livro['valor']:
        print(f"{cliente['nome']} não tem saldo suficiente para comprar '{livro['titulo']}'.")
        return

    
    if livro['status'] != 'Disponível':
        print(f"O livro '{livro['titulo']}' não está disponível para compra.")
        return

    
    cliente['saldo'] -= livro['valor']
    livro['status'] = 'Indisponível'
    print(f"{cliente['nome']} comprou '{livro['titulo']}' por R${livro['valor']:.2f}. Saldo restante: R${cliente['saldo']:.2f}.")

def mudar_status(base_Livros):
    isbn = input("Digite o ISBN do livro: ")
    if isbn in base_Livros:
        status = input("Digite o novo status do livro (1 - Disponível / 2 - Indisponível): ")
        
        if status == '1':  
            base_Livros[isbn]['status'] = 'Disponível'  
            print("Agora o status está Disponível.")
        elif status == '2':  
            base_Livros[isbn]['status'] = 'Indisponível'  
            print("Agora o status está Indisponível.")
        else:
            print("Status inválido. Escolha 1 ou 2.")
    else:
        print("ISBN não encontrado.")

def pesquisar_livro(base_Livros):
    while True:
        op1 = input("O que você quer pesquisar? \n"
                    "Título - 1 \n"
                    "Gênero - 2 \n"
                    "Faixa etária - 3\n"
                    "Editora - 4 \n"
                    "Status - 5 \n"
                    "Valor - 6 \n"
                    "Voltar - 7 \n")

        if op1 == '1':  
            titulo = input("Escreva o título que quer: ")
            livros_encontrados = False
            for livro in base_Livros.values():
                if titulo.lower() in livro['titulo'].lower(): 
                    print(f"Título: {livro['titulo']}, Gênero: {livro['genero']}, Faixa Etária: {livro['faixa_etaria']}, Editora: {livro['editora']}, Status: {livro['status']}, Valor: R${livro['valor']:.2f}")
                    livros_encontrados = True

            if not livros_encontrados:
                print("Nenhum livro encontrado para esse título.")

        elif op1 == '2':  
            genero = input("Escreva o gênero que quer: ")
            livros_encontrados = False
            for livro in base_Livros.values():
                if livro['genero'].lower() == genero.lower():
                    print(f"Título: {livro['titulo']}, Gênero: {livro['genero']}")
                    livros_encontrados = True

            if not livros_encontrados:
                print("Nenhum livro encontrado para esse gênero.")

        elif op1 == '3':  
            fe = input("Escreva a faixa etária que quer: ")
            if fe.isdigit():
                fe = int(fe)
                livros_encontrados = False
                for livro in base_Livros.values():
                    if livro['faixa_etaria'] <= fe:
                        print(f"Título: {livro['titulo']}, Faixa Etária: {livro['faixa_etaria']}")
                        livros_encontrados = True

                if not livros_encontrados:
                    print("Nenhum livro encontrado para essa faixa etária.")
            else:
                print("Por favor, insira um número válido para a faixa etária.")

        elif op1 == '4':  
            editora = input("Escreva a editora que quer: ")
            livros_encontrados = False
            for livro in base_Livros.values():
                if livro['editora'].lower() == editora.lower():
                    print(f"Título: {livro['titulo']}, Editora: {livro['editora']}")
                    livros_encontrados = True

            if not livros_encontrados:
                print("Nenhum livro encontrado para essa editora.")

        elif op1 == '5':  
            status = input("Escreva o status que quer (disponível ou não disponível): ")
            livros_encontrados = False
            for livro in base_Livros.values():
                if livro['status'].lower() == status.lower():
                    print(f"Título: {livro['titulo']}, Status: {livro['status']}")
                    livros_encontrados = True

            if not livros_encontrados:
                print("Nenhum livro encontrado para esse status.")

        elif op1 == '6': 
            valor = input("Escreva o valor máximo que quer: ")
            if valor.replace('.', '', 1).isdigit(): 
                valor = float(valor)
                livros_encontrados = False
                for livro in base_Livros.values():
                    if livro['valor'] <= valor:
                        print(f"Título: {livro['titulo']}, Valor: R${livro['valor']:.2f}")
                        livros_encontrados = True

                if not livros_encontrados:
                    print("Nenhum livro encontrado para esse valor.")
            else:
                print("Por favor, insira um valor válido.")

        elif op1 == '7':  
            print("Voltando ao menu anterior.")
            break  
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")