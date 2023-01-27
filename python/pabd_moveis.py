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
    print('2 - Entrar como vendedor')
    r = int(input('Digite a opção: '))

    if r == 1:
        print('1 - Produtos')
        print('2 - Funcionários')
        print('3 - Relatórios')
        r = int(input('Digite a opção: '))

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

            else:
                print('Comando inválido...')
    
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

        elif r == 3:
            print('1 - Lista de vendas por funcionário')
            print('2 - Lista de vendas por data')
            print('3 - Lista de vendas por produto')
            r = int(input('Digite a opção: '))

            if r == 1:
                cursor.execute("SELECT qntd_venda, funcionario.nome FROM venda, funcionario")

                for linha in cursor:
                    print(linha)