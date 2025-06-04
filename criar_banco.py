# Importar as bibliotecas
import sqlite3
from sqlite3 import Error

# Criar uma função para criar a conexão com o banco
def conexao_banco():
    caminho = './agenda.db'
    conexao = None
    try:
        conexao = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return conexao  # Corrigi a indentação do retorno

conexao = conexao_banco()

# Criar uma tabela via comando
vsql = """
CREATE TABLE tb_contatos (
    idcontato INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_contato VARCHAR(100),
    telefone_contato VARCHAR(20),
    email_contato VARCHAR(255)
);
"""
print(vsql)

# Criar função para criar a tabela
def criar_tabela(conexao, sql):
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        print('Tabela criada com XUSEQSU!')
    except Error as ex:
        print(ex)

criar_tabela(conexao, vsql)