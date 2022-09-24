import sqlite3
from hashlib import sha256
from uuid import uuid4
from database_user.validacpf import valida_cpf


class DataBase:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cursor = self.con.cursor()
        self.data_user = []

    def sql_insert(self, name, cpf):
        self.data_user.append(User(name, cpf))
        for value in self.data_user:
            self.cursor.execute(f'INSERT INTO User VALUES (?,?,?)', (value.id, value.name, value.cpf))
        self.con.commit()

    def close(self):
        self.con.close()


class User:
    def __init__(self, name, cpf):
        self.id = str(uuid4())
        self.name = name
        self.cpf = cpf

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, value):
        while not valida_cpf(value):
            value = input("CPF inválido. Digite novamente: ")
        self._cpf = str(sha256(value.encode()).hexdigest())
