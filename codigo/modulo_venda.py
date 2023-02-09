import mysql.connector

meubanco = mysql.connector.connect(
    host="localhost",
    database="pabd_moveis",
    user="root",
    password="labinfo"
)

cursor = meubanco.cursor()

while(True):

    print('1 - Entrar como funcionário')
    print('2 - Sair')
    r = int(input('Digite a opção: '))

    if r == 1:

        CPF = input("Digite seu cpf: ")

        cursor.execute("SELECT cpf FROM funcionario")

        for linha in cursor:

            if CPF == linha[0]:

                while(True):

                    meubanco = mysql.connector.connect(
                        host="localhost",
                        database="pabd_moveis",
                        user="root",
                        password="labinfo"
                    )

                    cursor = meubanco.cursor()

                    print('1 - Clientes')
                    print('2 - Exibir produtos')
                    print('3 - Realizar vendas')
                    print('4 - Relatórios')
                    r = int(input('Digite a opção: '))

            ##########################CLIENTE#################################

                    if r == 1:
                        print('1 - Cadastrar')
                        print('2 - Alterar')
                        print('3 - Voltar')
                        r = int(input('Digite a opção: '))

                        if r == 1:
                            cpf = str(input('Digite o CPF: '))
                            nome = str(input('Digite o nome: '))
                            endereco = str(input('Digite o endereço: '))
                            telefone = str(input('Digite o telefone: '))
                            email = str(input('Digite o email: '))

                            cursor.execute(f"INSERT INTO cliente VALUES ('{cpf}', '{nome}', '{endereco}', '{telefone}', '{email}')")
                            meubanco.commit()

                            print('Cliente cadastrado!')

                        elif r == 2:
                            print('Qual elemento você quer modificar?')
                            print('1 - Nome')
                            print('2 - Endereço')
                            print('3 - Telefone')
                            print('4 - Email')
                            r = int(input('Digite a opção: '))

                            if r == 1:
                                cpf = str(input('Digite o cpf do cliente que será alterado: '))
                                novo = str(input('Digite o novo nome do cliente: '))

                                cursor.execute(f"UPDATE cliente SET nome ='{novo}' WHERE cpf = '{cpf}'")
                                meubanco.commit()

                                print('Dados do cliente alterados!')

                            elif r == 2:
                                cpf = str(input('Digite o cpf do cliente que será alterado: '))
                                novo = str(input('Digite o novo endereço do cliente: '))

                                cursor.execute(f"UPDATE cliente SET endereco ='{novo}' WHERE cpf = '{cpf}'")
                                meubanco.commit()

                                print('Dados do cliente alterados!')

                            elif r == 3:
                                cpf = str(input('Digite o cpf do cliente que será alterado: '))
                                novo = str(input('Digite o novo telefone do cliente: '))

                                cursor.execute(f"UPDATE cliente SET telefone ='{novo}' WHERE cpf = '{cpf}'")
                                meubanco.commit()

                                print('Dados do cliente alterados!')

                            elif r == 4:
                                cpf = str(input('Digite o cpf do cliente que será alterado: '))
                                novo = str(input('Digite o novo email do cliente: '))

                                cursor.execute(f"UPDATE cliente SET email ='{novo}' WHERE cpf = '{cpf}'")
                                meubanco.commit()

                                print('Dados do cliente alterados!')

                            else:
                                print('Comando inválido')

                        elif r == 3:
                            print('Voltando...')

                        else:
                            print('Comando inválido...')

            ##########################EXIBIR PRODUTOS#################################

                    elif r == 2:
                        print('1 - Exibir produtos da categoria para cozinha')
                        print('2 - Exibir produtos da categoria para sala')
                        print('3 - Exibir produtos da categoria para quarto')
                        r = int(input('Digite a opção: '))

                        if r == 1:
                            tipo = "cozinha"

                        elif r == 2:
                            tipo = "sala"

                        elif r == 3:
                            tipo = "quarto"

                        else:
                            print('Comando inválido')
                                
                        cursor.execute(f"SELECT codigo, nome, descricao, valor, qntd_estoque FROM produto WHERE tipo='{tipo}'")

                        for linha in cursor:
                                cod = linha[0]
                                nom = linha[1]
                                desc = linha[2]
                                val = linha[3]
                                qntd = linha[4]

                                print(f' ------------------------- \n Código: {cod}\n Nome: {nom}\n Descrição: {desc}\n Valor: {val}\n Estoque: {qntd} \n ------------------------- \n')

            ##########################REALIZAR VENDA#################################

                    elif r == 3:
                        c = input('Digite o código do produto a ser vendido: ')
                        q = int(input('Digite a quantidade do produto a ser vendida: '))
                        cc = int(input('Digite o CPF do cliente: '))
                        cf = int(input('Digite o seu CPF: '))
                        dt = input('Digite a data de hoje (AAAA-MM-DD): ')

                        cursor.execute(f"INSERT INTO compra(cpf_cliente, codigo_produto, cpf_funcionario, data, qntd_compra) VALUES ('{cc}', '{c}', '{cf}', '{dt}', '{q}')")
                        meubanco.commit()

                        cursor.execute(f"SELECT qntd_estoque from produto WHERE codigo={c}")
                        for linha in cursor:
                            qt = int(linha[0])

                        n = qt - q

                        cursor.execute(f"UPDATE produto SET qntd_estoque ='{n}' WHERE codigo = '{c}'")
                        meubanco.commit()

                        print('Venda Realizada!')

            ##########################RELATÓRIO#################################

                    elif r == 4:
                        print('1 - Pesquisar produto')
                        print('2 - Ver últimas compras do cliente')
                        print('3 - Voltar')
                        r = int(input('Digite a opção: '))

                        if r == 1:
                            p = input('Digite o nome do produto: ')

                            cursor.execute(f"SELECT * FROM produto WHERE nome LIKE '%{p}%'")

                            for linha in cursor:
                                cod = linha[0]
                                nom = linha[1]
                                tip = linha[2]
                                des = linha[3]
                                val = linha[4]
                                qtd = linha[5]
                                cnf = linha[6]

                                print(f' ------------------------- \n Código: {cod}\n Nome: {nom}\n Tipo: {tip}\n Descrição: {des}\n Valor: R$ {val}\n Estoque: {qtd}\n CNPJ do Fornecedor: {cnf} \n ------------------------- \n')

                        elif r == 2:
                            cpf = input('Digite o cpf do cliente: ')

                            cursor.execute(f"SELECT cliente.nome, produto.nome, compra.data FROM cliente, compra, produto WHERE cliente.cpf={cpf} and cliente.cpf = cpf_cliente and produto.codigo = compra.codigo_produto")

                            for linha in cursor:
                                cnome = linha[0]
                                pnome = linha[1]
                                data = linha[2]

                                print(f'O cliente {cnome} comprou {pnome} na data {data}.')

                        elif r == 3:
                            print('Voltando...')

                        else:
                            print('Comando inválido')

    elif r ==2:
        break