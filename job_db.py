# -*- coding: utf-8 -*-
import sqlite3

def sqlDB(sqlText, par=None):
    conn = sqlite3.connect('example.db')
    cur = conn.cursor()
    if par is None:
        cur.execute(sqlText)
    else:
        cur.execute(sqlText, par)
    conn.commit()
    conn.close()
    return True

def selectDB(sqlText):
    try:
        conn = sqlite3.connect('example.db')
        cur = conn.cursor()
        cur.execute(sqlText)
        table = cur.fetchall()
        conn.close()
        return table
    except:
        return None


"""" Проверка подключения к БД"""
def connDB():
    if selectDB("select * FROM people, company") is None:
        if createDB():
            return True
    return False

""" создание БД"""
def createDB():
    sqlDB("CREATE TABLE company(id integer PRIMARY KEY AUTOINCREMENT, firma text);")
    sqlDB("CREATE TABLE people(id integer PRIMARY KEY AUTOINCREMENT, fio text, company integer,"
                 " email text, FOREIGN KEY(company) REFERENCES company(id));")


""" получение таблицы сотрудников"""
def tableDB():
    return selectDB("SELECT people.id, people.fio, company.firma, people.email, company.id FROM company,"
                    " people WHERE company.id = people.company ORDER BY company.firma, people.fio;")

""" удаление сотрудников"""
def delDB(id):
    return sqlDB("DELETE FROM people where people.id = ?;", (id,))

def selectCompany():
    return selectDB("SELECT * FROM company;")

def addPeople(spisok):
    return sqlDB("INSERT INTO people (fio, company, email ) VALUES (?, ?, ?);", spisok)

def editPeople(spisok):
    return sqlDB("UPDATE people SET fio = ?, company = ?, email = ? WHERE id = ?", spisok)

def addCompany(spisok):
    return sqlDB("INSERT INTO company (firma) VALUES (?);", spisok)

def editCompany(spisok):
    return sqlDB("UPDATE company SET firma = ? WHERE id = ?", spisok)
