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