import mysql.connector

meubanco = mysql.connector.connect(
    host="localhost",
    database="crediario_sa",
    user="root",
    password="labinfo"
)

cursor = meubanco.cursor()

while(True):

    print('Entrando como funcionário')

    CPF = input('Digite seu CPF: ')

    for CPF in cursor.execute("SELECT cpf FROM funcionario"):
        while(True):
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
                    email = float(input('Digite o email: '))

                    cursor.execute(f"INSERT INTO produto VALUES ('{cpf}', '{nome}', '{endereco}', '{telefone}', '{email}')")
                    meubanco.commit()

                elif r == 2:
                    print('Qual elemento você quer modificar?')
                    print('1 - CPF')
                    print('2 - Nome')
                    print('3 - Endereço')
                    print('4 - Telefone')
                    print('5 - Email')
                    r = int(input('Digite a opção: '))

                    if r == 1:
                        cpf = str(input('Digite o cpf do cliente que será alterado: '))
                        novo = str(input('Digite o novo cpf do cliente: '))

                        cursor.execute(f"UPDATE produto SET cpf ='{novo}' WHERE cpf = '{cpf}'")
                        meubanco.commit()

                    elif r == 2:
                        nome = str(input('Digite o nome do cliente que será alterado: '))
                        novo = str(input('Digite o novo nome do cliente: '))

                        cursor.execute(f"UPDATE produto SET nome ='{novo}' WHERE codigo = '{nome}'")
                        meubanco.commit()

                    elif r == 3:
                        endereco = str(input('Digite o endereço do cliente que será alterado: '))
                        novo = str(input('Digite o novo endereço do cliente: '))

                        cursor.execute(f"UPDATE produto SET tipo ='{novo}' WHERE codigo = '{endereco}'")
                        meubanco.commit()

                    elif r == 4:
                        telefone = str(input('Digite o telefone do cliente que será alterado: '))
                        novo = str(input('Digite o novo telefone do cliente: '))

                        cursor.execute(f"UPDATE produto SET descricao ='{novo}' WHERE codigo = '{telefone}'")
                        meubanco.commit()

                    elif r == 5:
                        email = str(input('Digite o email do produto que será alterado: '))
                        novo = str(input('Digite o novo email do cliente: '))

                        cursor.execute(f"UPDATE produto SET valor ='{novo}' WHERE codigo = '{email}'")
                        meubanco.commit()

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

##########################REALIZAR VENDA#################################

            elif r == 3:
                c = input('Digite o código do produto a ser vendido: ')
                q = input('Digite a quantidade do produto a ser vendida: ')

                qt = cursor.execute(f"SELECT qntd_estoque from produto")

                cursor.execute(f"UPDATE produto SET qntd_estoque ='{qt - q}' WHERE codigo = '{c}'")
                meubanco.commit()

##########################RELATÓRIO#################################

            elif r == 4:
                print('1 - Pesquisar produto')
                print('2 - Ver últimas compras do cliente')
                print('3 - Voltar')
                r = int(input('Digite a opção: '))

                if r == 1:
                    p = input('Digite o nome do produto: ')

                    cursor.execute(f"SELECT * FROM produto WHERE nome={p}")

                    for linha in cursor:
                        print(linha)

                elif r == 2:
                    cpf = input('Digite o cpf do cliente: ')

                    cursor.execute(f"SELECT cliente.nome, produto.nome, compra.data FROM cliente, compra, produto WHERE cliente.cpf={cpf}")

                    for linha in cursor:
                        print(linha)

                elif r == 3:
                    print('Voltando...')

                else:
                    print('Comando inválido')