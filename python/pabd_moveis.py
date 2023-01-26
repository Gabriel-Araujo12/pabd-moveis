import mysql.connector

meubanco = mysql.connector.connect(
    host="localhost",
    database="moveis",
    user="root",
    password="labinfo"
)

cursor = meubanco.cursor()

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
        print('3 - Relatórios')
        r = int(input('Digite a opção: '))

        if r == 1:
            print('Digite o código: ')
            print('Digite o nome: ')
            print('Digite o tipo: ')
            print('Digite a descrição: ')
            print('Digite o valor: ')
            print('Digite a quantidade em estoque: ')
            print('Digite o CNPJ do fornecedor: ')

            cursor.execute(f"INSERT INTO filme VALUES ('{codigo}', '{titulo}', '{genero}')")
            meubanco.commit()

        elif r == 2:

        elif r == 3:

        else:
            print('Comando inválido...')
    
    elif r == 2:
        print('1 - Cadastrar')
        print('2 - Alterar')
        print('3 - Voltar')
        r = int(input('Digite a opção: '))

        if r == 1:
            print('Digite o cpf: ')
            print('Digite o nome: ')
            print('Digite a função: ')
            print('Digite o valor do salário: ')
            print('Digite o telefone: ')
            print('Digite o email: ')

            cursor.execute(f"INSERT INTO filme VALUES ('{codigo}', '{titulo}', '{genero}')")
            meubanco.commit()

        elif r == 2:

        elif r == 3:

    elif r == 3:
        print('1 - Lista de vendas por funcionário')
        print('2 - Lista de vendas por data')
        print('3 - Lista de vendas por produto')
        r = int(input('Digite a opção: '))

        if r == 1:
            cursor.execute("SELECT qntd_venda, funcionario.nome FROM venda, funcionario")

            for linha in cursor:
                print(linha)