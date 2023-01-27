import mysql.connector

meubanco = mysql.connector.connect(
    host="localhost",
    database="crediario_sa",
    user="root",
    password="labinfo"
)

cursor = meubanco.cursor()

while(True):

    print('1 - Entrar como administrador')
    print('2 - Sair')
    r = int(input('Digite a opção: '))

    if r == 1:
        print('1 - Produtos')
        print('2 - Funcionários')
        print('3 - Relatórios')
        r = int(input('Digite a opção: '))

################ADMINISTRAÇÃO DE PRODUTOS#################

        if r == 1:
            print('1 - Cadastrar')
            print('2 - Alterar')
            print('3 - Voltar')
            r = int(input('Digite a opção: '))

            if r == 1:
                codigo = str(input('Digite o código: '))
                nome = str(input('Digite o nome: '))
                tipo = str(input('Digite o tipo: '))
                descricao = str(input('Digite a descrição: '))
                valor = float(input('Digite o valor: '))
                qntd = int(input('Digite a quantidade em estoque: '))
                cnpj = str(input('Digite o CNPJ do fornecedor: '))

                cursor.execute(f"INSERT INTO produto VALUES ('{codigo}', '{nome}', '{tipo}', '{descricao}', '{valor}', '{qntd}', '{cnpj}')")
                meubanco.commit()

            elif r == 2:
                print('Qual elemento você quer modificar?')
                print('1 - Código')
                print('2 - Nome')
                print('3 - Tipo')
                print('4 - Descrição')
                print('5 - Valor')
                print('6 - Quantidade')
                print('7 - CNPJ do fornecedor')
                r = int(input('Digite a opção: '))

                if r == 1:
                    codigo = str(input('Digite o código do produto que será alterado: '))
                    novo = str(input('Digite o novo código: '))

                    cursor.execute(f"UPDATE produto SET codigo ='{novo}' WHERE codigo = '{codigo}'")
                    meubanco.commit()

                elif r == 2:
                    codigo = str(input('Digite o código do produto que será alterado: '))
                    novo = str(input('Digite o novo nome do produto: '))

                    cursor.execute(f"UPDATE produto SET nome ='{novo}' WHERE codigo = '{codigo}'")
                    meubanco.commit()

                elif r == 3:
                    codigo = str(input('Digite o código do produto que será alterado: '))
                    novo = str(input('Digite o novo tipo do produto: '))

                    cursor.execute(f"UPDATE produto SET tipo ='{novo}' WHERE codigo = '{codigo}'")
                    meubanco.commit()

                elif r == 4:
                    codigo = str(input('Digite o código do produto que será alterado: '))
                    novo = str(input('Digite a nova descrição do produto: '))

                    cursor.execute(f"UPDATE produto SET descricao ='{novo}' WHERE codigo = '{codigo}'")
                    meubanco.commit()

                elif r == 5:
                    codigo = str(input('Digite o código do produto que será alterado: '))
                    novo = str(input('Digite o novo valor do produto: '))

                    cursor.execute(f"UPDATE produto SET valor ='{novo}' WHERE codigo = '{codigo}'")
                    meubanco.commit()

                elif r == 6:
                    codigo = str(input('Digite o código do produto que será alterado: '))
                    novo = str(input('Digite a nova quantidade do produto: '))

                    cursor.execute(f"UPDATE produto SET quantidade ='{novo}' WHERE codigo = '{codigo}'")
                    meubanco.commit()

                elif r == 7:
                    codigo = str(input('Digite o código do produto que será alterado: '))
                    novo = str(input('Digite o novo CNPJ do fornecedor do produto: '))

                    cursor.execute(f"UPDATE produto SET cnpj_fornecedor ='{novo}' WHERE codigo = '{codigo}'")
                    meubanco.commit()

            elif r == 3:
                print('Voltando...')

            else:
                print('Comando inválido...')

##########################FUNCIONÁRIO#################################
    
        elif r == 2:
            print('1 - Cadastrar')
            print('2 - Alterar')
            print('3 - Voltar')
            r = int(input('Digite a opção: '))

            if r == 1:
                cpf = str(input('Digite o cpf: '))
                nome = str(('Digite o nome: '))
                funcao = str(('Digite a função: '))
                salario = str(('Digite o valor do salário: '))
                telefone = str(('Digite o telefone: '))
                email = str(('Digite o email: '))

                cursor.execute(f"INSERT INTO funcionario VALUES ('{cpf}', '{nome}', '{funcao}', '{salario}', '{telefone}', '{email}')")
                meubanco.commit()

            elif r == 2:
                print('Qual elemento você quer modificar?')
                print('1 - CPF')
                print('2 - Nome')
                print('3 - Função')
                print('4 - Salário')
                print('5 - Telefone')
                print('6 - Email')
                r = int(input('Digite a opção: '))

                if r == 1:
                    codigo = str(input('Digite o cpf do funcionário que será alterado: '))
                    novo = str(input('Digite o novo cpf: '))

                    cursor.execute(f"UPDATE funcionario SET cpf ='{novo}' WHERE cpf = '{codigo}'")
                    meubanco.commit()

                elif r == 2:
                    codigo = str(input('Digite o cpf do funcionário que será alterado: '))
                    novo = str(input('Digite o novo nome: '))

                    cursor.execute(f"UPDATE funcionario SET nome ='{novo}' WHERE cpf = '{codigo}'")
                    meubanco.commit()
                    
                elif r == 3:
                    codigo = str(input('Digite o cpf do funcionário que será alterado: '))
                    novo = str(input('Digite a nova função: '))

                    cursor.execute(f"UPDATE funcionario SET funcao ='{novo}' WHERE cpf = '{codigo}'")
                    meubanco.commit()

                elif r == 4:
                    codigo = str(input('Digite o cpf do funcionário que será alterado: '))
                    novo = str(input('Digite o novo salário: '))

                    cursor.execute(f"UPDATE funcionario SET salario ='{novo}' WHERE cpf = '{codigo}'")
                    meubanco.commit()

                elif r == 5:
                    codigo = str(input('Digite o cpf do funcionário que será alterado: '))
                    novo = str(input('Digite o novo telefone: '))

                    cursor.execute(f"UPDATE funcionario SET telefone ='{novo}' WHERE cpf = '{codigo}'")
                    meubanco.commit()

                elif r == 6:
                    codigo = str(input('Digite o cpf do funcionário que será alterado: '))
                    novo = str(input('Digite o novo email: '))

                    cursor.execute(f"UPDATE funcionario SET email ='{novo}' WHERE cpf = '{codigo}'")
                    meubanco.commit()

                else:
                    print('Comando inválido')
            
            elif r == 3:
                print('Voltando...')

            else:
                print('Comando inválido')

##########################RELATÓRIO#################################

        elif r == 3:
            print('1 - Lista de vendas por funcionário')
            print('2 - Lista de vendas por data')
            print('3 - Lista de vendas por produto')
            r = int(input('Digite a opção: '))

            if r == 1:
                cursor.execute("SELECT qntd_venda, funcionario.nome FROM venda, funcionario WHERE funcionario.cpf = venda.cpf_funcionario")

                for linha in cursor:
                    print(linha)

            elif r == 2:
                cursor.execute("SELECT qntd_venda, data FROM venda")

                for linha in cursor:
                    print(linha)

            elif r == 3:
                cursor.execute("SELECT qntd_venda, produto.nome FROM venda, produto WHERE venda.cod_produto = produto.codigo")

                for linha in cursor:
                    print(linha)

            else:
                print('Comando inválido')

    elif r == 2:
        break