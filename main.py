# importar as bibliotecas
import sqlite3
from sqlite3 import Error
import os  # Módulo os importado uma única vez no início

# o sqlite tenta e, se não acha um banco, ele mesmo cria
# criar uma função para criar a conexão com o banco
def conexao_banco():
    caminho = './agenda.db'
    # variável de conexão
    con = None
    # criar uma validação para o erro
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon = conexao_banco()

# criar uma função abstrata para fazer todas as transações
# com o banco de dados
def query(conexao, sql):
    try:
        c = conexao.cursor()  # chama o cursor
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print('Operação finalizada')

# criar a função que consulta os dados
def consultar(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    res = c.fetchall()
    return res

# criar o menu do programa
def menu_principal():
    os.system("cls")
    print("\n")
    print("1 - Inserir novo registro")
    print("2 - Deletar registro")
    print("3 - Atualizar Registro")
    print("4 - Consultar Registro")
    print("5 - Consultar Registro por Nome")
    print("6 - Sair")

def menu_inserir():
    os.system("cls")
    print("\n")
    vnome = input("Digite o nome do registro: ")
    vtelefone = input("Digite o telefone do registro: ")
    vemail = input("Digite o email do registro: ")
    vsql = "INSERT INTO tb_contatos (nome_contato, telefone_contato, email_contato) VALUES ('"+vnome+"','"+vtelefone+"','"+vemail+"')"
    query(vcon, vsql)

def menu_consultar():
    os.system("cls")
    print("\n")
    vsql = "SELECT * FROM tb_contatos"
    res = consultar(vcon, vsql)
    vlim = 10
    vcont = 0
    for r in res:
        print(
            "ID: {0:<3}  "
            "Nome: {1:<30}  "
            "Telefone: {2:<14}  "
            "Email: {3:<1}".format(r[0], r[1], r[2], r[3])
        )
        vcont += 1

opc = 0
while opc != 6:
    menu_principal()
    # ler a opção que o usuário vai digitar
    opc = int(input('Digite uma opção: '))
    # verifica qual a opção o usuário inseriu
    if opc == 1:
        menu_inserir()
    elif opc == 2:
        None
    elif opc == 3:
        None
    elif opc == 4:
        menu_consultar()
    elif opc == 5:
        None
    elif opc == 6:
        None



