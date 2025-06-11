# Importar as bibliotecas
import sqlite3
from sqlite3 import Error
import os  # Módulo os importado uma única vez no início


# Criar a conexão com o banco de dados
def conexao_banco():
    caminho = './agenda.db'
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con


vcon = conexao_banco()


# Função para realizar transações no banco de dados
def query(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print('Operação finalizada')


# Função para consultar os dados
def consultar(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    return c.fetchall()


# Menu principal do programa
def menu_principal():
    os.system("cls")
    print("\n")
    print("1 - Inserir novo registro")
    print("2 - Deletar registro")
    print("3 - Atualizar registro")
    print("4 - Consultar registro")
    print("5 - Consultar registro por nome")
    print("6 - Sair")


# Função para inserir registros
def menu_inserir():
    os.system("cls")
    print("\n")
    vnome = input("Digite o nome do registro: ")
    vtelefone = input("Digite o telefone do registro: ")
    vemail = input("Digite o email do registro: ")

    vsql = f"INSERT INTO tb_contatos (nome_contato, telefone_contato, email_contato) VALUES ('{vnome}', '{vtelefone}', '{vemail}')"
    query(vcon, vsql)


# Função para consultar todos os registros
def menu_consultar():
    os.system("cls")
    print("\n")
    vsql = "SELECT * FROM tb_contatos"
    res = consultar(vcon, vsql)
    vlim = 10
    vcont = 0

    for r in res:
        print(f"ID: {r[0]:<3}  Nome: {r[1]:<30}  Telefone: {r[2]:<14}  Email: {r[3]:<1}")
        vcont += 1
        if vcont == vlim:
            vcont = 0
            os.system("pause")
            os.system("cls")

    print('Fim da listagem de contatos!')
    os.system("pause")


# Função para consultar registros por nome
def menu_consultar_nome():
    os.system("cls")
    print("\n")
    vnome = input("Digite o nome do registro: ")

    vsql = f"SELECT * FROM tb_contatos WHERE nome_contato LIKE '%{vnome}%'"
    res = consultar(vcon, vsql)
    vlim = 10
    vcont = 0

    for r in res:
        print(f"ID: {r[0]:<3}  Nome: {r[1]:<30}  Telefone: {r[2]:<14}  Email: {r[3]:<1}")
        vcont += 1
        if vcont == vlim:
            vcont = 0
            os.system("pause")
            os.system("cls")

    print('Fim da listagem de contatos!')
    os.system("pause")


# Função para deletar registros
def menu_deletar():
    os.system("cls")
    print("\n")
    vid = input("Digite o ID do registro a ser deletado: ")

    vsql = f"DELETE FROM tb_contatos WHERE id_contato = {vid}"
    query(vcon, vsql)


# Função para atualizar registros
def menu_atualizar():
    os.system("cls")
    print("\n")
    vid = input("Digite o ID do registro a ser atualizado: ")

    r = consultar(vcon, f"SELECT * FROM tb_contatos WHERE id_contato={vid}")
    if not r:
        print("Registro não encontrado.")
        return

    rnome, rtelefone, remail = r[0][1], r[0][2], r[0][3]

    vnome = input("Digite o nome do registro a ser atualizado: ") or rnome
    vtelefone = input("Digite o telefone do registro a ser atualizado: ") or rtelefone
    vemail = input("Digite o email do registro a ser atualizado: ") or remail

    vsql = f"UPDATE tb_contatos SET nome_contato = '{vnome}', telefone_contato = '{vtelefone}', email_contato = '{vemail}' WHERE id_contato = {vid}"
    query(vcon, vsql)


# Loop principal do menu
opc = 0
while opc != 6:
    menu_principal()
    opc = int(input("Digite uma opção: "))

    if opc == 1:
        menu_inserir()
    elif opc == 2:
        menu_deletar()
    elif opc == 3:
        menu_atualizar()
    elif opc == 4:
        menu_consultar()
    elif opc == 5:
        menu_consultar_nome()
    elif opc == 6:
        os.system("cls")
        print("Programa finalizado com sucesso!")
    else:
        os.system("cls")
        print("Opção inválida!")
        os.system("pause")

vcon.close()
os.system("pause")