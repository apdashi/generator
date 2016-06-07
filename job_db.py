# -*- coding: utf-8 -*-
import sqlite3

def sqlDB(sqlText):
    try:
        conn = sqlite3.connect('example.db')
        cur = conn.cursor()
        cur.execute(sqlText)
        conn.commit()
        conn.close()
        return True
    except:
        return False

def selectDB(sqlText):
    try:
        conn = sqlite3.connect('example.db')
        cur = conn.cursor()
        cur.execute(sqlText)
        table = cur.fetchall()
        conn.close()
        return table
    except:
        return (())


"""" Проверка подключения к БД"""
def connDB():
    try:
        conn = sqlite3.connect('example.db')
        cur = conn.cursor()
        cur.execute("select * FROM people, company")
        cur.fetchone()
        conn.close()
        return True
    except:
        if createDB():
            return True
        else:
            return False

""" создание БД"""
def createDB(self):
    sqlDB("CREATE TABLE company(id integer PRIMARY KEY AUTOINCREMENT, firma text);")
    sqlDB("CREATE TABLE people(id integer PRIMARY KEY AUTOINCREMENT, fio text, company integer,"
                 " email text, FOREIGN KEY(company) REFERENCES company(id));")


""" получение таблицы сотрудников"""
def tableDB():
    return selectDB("SELECT people.id, people.fio, company.firma, people.email, company.id FROM company,"
                    " people WHERE company.id = people.company ORDER BY company.firma, people.fio;")

""" удаление сотрудников"""
def delDB(id):
    return sqlDB("DELETE FROM people where people.id = %s;" % (id))

def selectCompany():
    return selectDB("SELECT * FROM company;")

def addPeople(spisok):
    return sqlDB("INSERT INTO people (fio, company, email ) VALUES ('%s', %s, '%s');" %
                    (spisok[0], spisok[1], spisok[2]))

def editPeople(spisok):
    return sqlDB("UPDATE people SET fio = '%s', company = %s, email = '%s' WHERE id = %s" %
                    (spisok[0], spisok[1], spisok[2], spisok[3]))

def addCompany(spisok):
    print("INSERT INTO company (firma) VALUES ('%s');" % (spisok[0]))
    return sqlDB("INSERT INTO company (firma) VALUES ('%s');" % (spisok[0]))


def editCompany(spisok):
    return sqlDB("UPDATE company SET firma = '%s' WHERE id = %s" % (spisok[0], spisok[1]))