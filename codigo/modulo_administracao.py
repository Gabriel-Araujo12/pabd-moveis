import mysql.connector

meubanco = mysql.connector.connect(
    host="localhost",
    database="pabd_moveis",
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

                print('1 - Sala')
                print('2 - Cozinha')
                print('3 - Quarto')
                tip = int(input('Selecione o tipo do produto: '))

                if tip == 1:
                    tipo = 'Sala'

                elif tip == 2:
                    tipo = 'Cozinha'

                elif tip == 3:
                    tipo = 'Quarto'


                descricao = str(input('Digite a descrição: '))
                valor = float(input('Digite o valor: '))
                qntd = int(input('Digite a quantidade em estoque: '))
                cnpj = str(input('Digite o CNPJ do fornecedor: '))

                cursor.execute(f"INSERT INTO produto VALUES ('{codigo}', '{nome}', '{tipo}', '{descricao}', '{valor}', '{qntd}', '{cnpj}')")
                meubanco.commit()

                print('Produto cadastrado!')

            elif r == 2:
                print('Qual elemento você quer modificar?')
                print('1 - Nome')
                print('2 - Tipo')
                print('3 - Descrição')
                print('4 - Valor')
                print('5 - Quantidade')
                print('6 - CNPJ do fornecedor')
                r = int(input('Digite a opção: '))
                
                if r == 1:
                    codigo = str(input('Digite o código do produto que será alterado: '))
                    novo = str(input('Digite o novo nome do produto: '))

                    cursor.execute(f"UPDATE produto SET nome ='{novo}' WHERE codigo = '{codigo}'")
                    meubanco.commit()

                    print('Dados do produto alterados!')

                elif r == 2:
                    codigo = str(input('Digite o código do produto que será alterado: '))
                    novo = str(input('Digite o novo tipo do produto: '))

                    cursor.execute(f"UPDATE produto SET tipo ='{novo}' WHERE codigo = '{codigo}'")
                    meubanco.commit()

                    print('Dados do produto alterados!')

                elif r == 3:
                    codigo = str(input('Digite o código do produto que será alterado: '))
                    novo = str(input('Digite a nova descrição do produto: '))

                    cursor.execute(f"UPDATE produto SET descricao ='{novo}' WHERE codigo = '{codigo}'")
                    meubanco.commit()

                    print('Dados do produto alterados!')

                elif r == 4:
                    codigo = str(input('Digite o código do produto que será alterado: '))
                    novo = str(input('Digite o novo valor do produto: '))

                    cursor.execute(f"UPDATE produto SET valor ='{novo}' WHERE codigo = '{codigo}'")
                    meubanco.commit()

                    print('Dados do produto alterados!')

                elif r == 5:
                    codigo = str(input('Digite o código do produto que será alterado: '))
                    novo = str(input('Digite a nova quantidade do produto: '))

                    cursor.execute(f"UPDATE produto SET qntd_estoque ='{novo}' WHERE codigo = '{codigo}'")
                    meubanco.commit()

                    print('Dados do produto alterados!')

                elif r == 6:
                    codigo = str(input('Digite o código do produto que será alterado: '))
                    novo = str(input('Digite o novo CNPJ do fornecedor do produto: '))

                    cursor.execute(f"UPDATE produto SET cnpj_fornecedor ='{novo}' WHERE codigo = '{codigo}'")
                    meubanco.commit()

                    print('Dados do produto alterados!')

                else:
                    print('Comando inválido')

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
                nome = str(input('Digite o nome: '))
                funcao = str(input('Digite a função: '))
                salario = float(input('Digite o valor do salário: '))
                telefone = str(input('Digite o telefone: '))
                email = str(input('Digite o email: '))

                cursor.execute(f"INSERT INTO funcionario VALUES ('{cpf}', '{nome}', '{funcao}', '{salario}', '{telefone}', '{email}')")
                meubanco.commit()

                print('Funcionário cadastrado!')

            elif r == 2:
                print('Qual elemento você quer modificar?')
                print('1 - Nome')
                print('2 - Função')
                print('3 - Salário')
                print('4 - Telefone')
                print('5 - Email')
                r = int(input('Digite a opção: '))

                if r == 1:
                    cpf = str(input('Digite o cpf do funcionário que será alterado: '))
                    novo = str(input('Digite o novo nome: '))

                    cursor.execute(f"UPDATE funcionario SET nome ='{novo}' WHERE cpf = '{cpf}'")
                    meubanco.commit()

                    print('Dados do funcionário alterados!')
                    
                elif r == 2:
                    cpf = str(input('Digite o cpf do funcionário que será alterado: '))
                    novo = str(input('Digite a nova função: '))

                    cursor.execute(f"UPDATE funcionario SET funcao ='{novo}' WHERE cpf = '{cpf}'")
                    meubanco.commit()

                    print('Dados do funcionário alterados!')

                elif r == 3:
                    cpf = str(input('Digite o cpf do funcionário que será alterado: '))
                    novo = str(input('Digite o novo salário: '))

                    cursor.execute(f"UPDATE funcionario SET salario ='{novo}' WHERE cpf = '{cpf}'")
                    meubanco.commit()

                    print('Dados do funcionário alterados!')

                elif r == 4:
                    cpf = str(input('Digite o cpf do funcionário que será alterado: '))
                    novo = str(input('Digite o novo telefone: '))

                    cursor.execute(f"UPDATE funcionario SET telefone ='{novo}' WHERE cpf = '{cpf}'")
                    meubanco.commit()

                    print('Dados do funcionário alterados!')

                elif r == 5:
                    cpf = str(input('Digite o cpf do funcionário que será alterado: '))
                    novo = str(input('Digite o novo email: '))

                    cursor.execute(f"UPDATE funcionario SET email ='{novo}' WHERE cpf = '{cpf}'")
                    meubanco.commit()

                    print('Dados do funcionário alterados!')

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
                cursor.execute("SELECT funcionario.cpf, funcionario.nome, compra.qntd_compra, compra.data FROM compra, funcionario WHERE funcionario.cpf = compra.cpf_funcionario")

                for linha in cursor:
                    cpf = linha[0]
                    nom = linha[1]
                    qntd = linha[2]
                    data = linha[3]

                    print(f' ------------------------- \n CPF do funcionário: {cpf}\n Nome do funcionário: {nom}\n Quantidade de vendas: {qntd}\n Data da venda: {data}\n ------------------------- \n')

            elif r == 2:
                cursor.execute("SELECT compra.id, compra.qntd_compra, compra.data FROM compra")

                for linha in cursor:
                    id = linha[0]
                    qntd = linha[1]
                    data = linha[2]

                    print(f' ------------------------- \n ID da venda: {id}\n Quantidade vendida: {qntd}\n Data da venda: {data}\n ------------------------- \n')

            elif r == 3:
                cursor.execute("SELECT produto.codigo, produto.nome, compra.qntd_compra, compra.data FROM compra, produto WHERE compra.codigo_produto = produto.codigo")

                for linha in cursor:
                    cod = linha[0]
                    nom = linha[1]
                    qntd = linha[2]
                    data = linha[3]

                    print(f' ------------------------- \n Código do produto: {cod}\n Nome do produto: {nom}\n Quantidade vendida: {qntd}\n Data da venda: {data}\n ------------------------- \n')

            else:
                print('Comando inválido')

    elif r == 2:
        break