import streamlit as st
import sqlite3 as lite
from datetime import datetime
import pandas as pd

# Funções para interagir com o banco de dados
def criar_banco():
    con = lite.connect('form.db')
    with con:
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Formulario (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nome TEXT,
                       email TEXT,
                       telefone TEXT,
                       dia_em DATE,
                       estado TEXT,
                       assunto TEXT)''')
        con.commit()

def inserir_dados(nome, email, telefone, dia, estado, assunto):
    con = lite.connect('form.db')
    with con:
        cur = con.cursor()
        cur.execute('''INSERT INTO Formulario (nome, email, telefone, dia_em, estado, assunto) 
                       VALUES (?, ?, ?, ?, ?, ?)''', 
                    (nome, email, telefone, dia, estado, assunto))
        con.commit()

def atualizar_dados(nome, email, telefone, dia, estado, assunto, id):
    con = lite.connect('form.db')
    with con:
        cur = con.cursor()
        cur.execute('''UPDATE Formulario SET nome=?, email=?, telefone=?, dia_em=?, estado=?, assunto=? 
                       WHERE id=?''',
                    (nome, email, telefone, dia, estado, assunto, id))
        con.commit()

def deletar_dados(id):
    con = lite.connect('form.db')
    with con:
        cur = con.cursor()
        cur.execute('DELETE FROM Formulario WHERE id=?', (id,))
        con.commit()

def selecionar_dados():
    con = lite.connect('form.db')
    with con:
        df = pd.read_sql_query('SELECT * FROM Formulario', con)
    return df

# Criar banco de dados
criar_banco()

# Configuração do Streamlit
st.title('Formulário de Consultoria')

# Inputs do usuário
nome = st.text_input('Nome:')
email = st.text_input('Email:')
telefone = st.text_input('Telefone:')
data_consulta = st.date_input('Data da Consulta', datetime.now())
estado = st.text_input('Estado da Consulta:')
assunto = st.text_input('Consulta Sobre:')

col1, col2, col3 = st.columns(3)

with col1:
    botao_inserir = st.button('Inserir')

with col2:
    botao_atualizar = st.button('Atualizar')

with col3:
    botao_deletar = st.button('Deletar')

# Exibir dados
st.subheader('Dados Registrados')
df = selecionar_dados()
st.dataframe(df)

if botao_inserir:
    if nome and email and telefone and estado and assunto:
        inserir_dados(nome, email, telefone, data_consulta, estado, assunto)
        st.success('Os dados foram inseridos com sucesso!')
    else:
        st.error('Preencha todos os campos')

if botao_atualizar:
    if nome and email and telefone and estado and assunto:
        id_atualizar = st.number_input('ID do Registro a Atualizar', min_value=1)
        if id_atualizar:
            atualizar_dados(nome, email, telefone, data_consulta, estado, assunto, id_atualizar)
            st.success('Os dados foram atualizados com sucesso!')
    else:
        st.error('Preencha todos os campos')

if botao_deletar:
    id_deletar = st.number_input('ID do Registro a Deletar', min_value=1)
    if id_deletar:
        deletar_dados(id_deletar)
        st.success('Os dados foram deletados com sucesso!')
