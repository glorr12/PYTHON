import pymysql
from pymysql.cursors import DictCursor


class DB:

    def __init__(self, config):
        self.conn = pymysql.connect(**config)
        print("открыто")  # для себя

    def execute(self, sql, params=None):
        with self.conn.cursor() as cursor:
            cursor.execute(sql, params)
            if cursor.description:
                return cursor.fetchall()


    def commit(self):
        self.conn.commit()

    def create_and_use(self, name):
        self.execute(f"create database if not exists {name}")
        self.execute(f"use {name}")



    def create_table(self,table_name,param=None):
        if not param:
            raise ValueError("необходимо хотя бы одно поле для заполнения")
        with self.conn.cursor() as cursor:
            cursor.execute(f" create table if not exists {table_name} ({param})")


    def add_to_table(self, table_name, columns, values):
        columns = ', '.join([f"`{col.strip()}`" for col in columns])
        cont = ", ".join(["%s"] * len(values))
        with self.conn.cursor() as cursor:
            cursor.execute(f"insert into {table_name} ({columns}) values ({cont})", values)



    def display(self):
        with self.conn.cursor(DictCursor) as cursor:
            cursor.execute('select title from notes')
            rows = cursor.fetchall()
            for row in rows:
                print(f"Note added: {row['title']}")


    def rollback(self):
        self.conn.rollback()


    def close(self):
        self.conn.close()


query = """
      create table if not exist notes_app_121225_IgorF(
      id int auto_increment primary key,
      title varchar(255) not null,
      content text
        """

config = {
    'host': 'ich-edit.edu.itcareerhub.de',
    'user': 'ich1',
    'password': 'ich1_password_ilovedbs',
    'cursorclass': pymysql.cursors.DictCursor
}


db = DB(config)


try:
    db.create_and_use("notes_app_121225_IgorF")
except pymysql.MySQLError as e:
    print(f" Не удалось создать или выбрать базу данных: {e}")

try:
    db.create_table("notes", "id int auto_increment primary key, title varchar(255) not null, content text")
except pymysql.MySQLError as e:
    print(f" Ошибка при создании таблицы 'notes': {e}")

try:
    db.add_to_table("notes", ["title","content"], ["Shopping list", "Milk, bread, eggs"])
except pymysql.MySQLError as e:
    db.rollback()
    print(f" Не удалось добавить заметку в таблицу: {e}")
except Exception as e:
    db.rollback()  #
    print(f" Внутренняя ошибка приложения при вставке: {e}")

try:
    db.display()
except pymysql.MySQLError as e:
    print(f"[ERROR] Ошибка при чтении данных из базы (DictCursor): {e}")
finally:
    db.close()
    print("Соединение с БД успешно закрыто.")