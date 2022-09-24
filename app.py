from database_user.db import DataBase
from database_user.validacpf import valida_cpf

user = DataBase('usuario.db')

print('BEM-VINDO. VAMOS AO CADASTRO.')
name = input('Digite seu nome: ')
cpf = input('Digite seu CPF: ')

user.sql_insert(name, cpf)
print('Cadastro feito com sucesso!')
user.close()





