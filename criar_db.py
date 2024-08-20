import sqlite3 as lite
import os

def criar_banco():
    # Verifica se o banco de dados já existe
    if not os.path.exists('form.db'):
        # Cria conexão com o banco de dados
        con = lite.connect('form.db')

        # Cria a tabela
        with con:
            cur = con.cursor()
            cur.execute("""
                CREATE TABLE Formulario (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    email TEXT,
                    telefone TEXT,
                    dia_em DATE,
                    estado TEXT,
                    assunto TEXT
                )
            """)

if __name__ == '__main__':
    criar_banco()