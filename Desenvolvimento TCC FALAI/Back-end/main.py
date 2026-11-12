from fastapi import FastAPI, HTTPException
import mysql.connector
from pydantic import BaseModel, EmailStr
from pwdlib import PasswordHash 

app = FastAPI()

class UsuarioCadastro(BaseModel):
    nome: str
    email: EmailStr
    senha: str

senha_hash = PasswordHash.recommended()
def conectar_banco():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="falai",
        port=3306
    )

@app.get("/")
def inicio():
    return {"mensagem": "API do FALAI funcionando!"}

@app.get("/teste-banco")
def teste_banco():
    conexao = conectar_banco()
    conexao.close()
    return {"mensagem": "Conexão com MySQL funcionando!"}

    
    cadastrar_usuario
@app.post("/usuarios")
def cadastrar_usuario(usuario: UsuarioCadastro):

    conexao = conectar_banco()
    cursor = conexao.cursor()

    senha_protegida = senha_hash.hash(usuario.senha)

    sql = """
        INSERT INTO usuarios (nome, email, senha_hash)
        VALUES (%s, %s, %s)
    """

    cursor.execute(sql, (
        usuario.nome,
        usuario.email,
        senha_protegida
    ))

    conexao.commit()

    cursor.close()
    conexao.close()

    return {"mensagem": "Usuário cadastrado com sucesso!"}