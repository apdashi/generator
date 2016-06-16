# -*- coding: utf-8 -*-
import sqlite3


def sqlDB(sqlText, par=None):
    try:
        conn = sqlite3.connect('example.db')
        cur = conn.cursor()
        if par is None:
            cur.execute(sqlText)
        else:
            cur.execute(sqlText, par)
        conn.commit()
        conn.close()
        return True
    except:
        return False


def selectDB(sqlText, par=None):
    try:
        conn = sqlite3.connect('example.db')
        cur = conn.cursor()
        if par is None:
            cur.execute(sqlText)
        else:
            cur.execute(sqlText, par)
        table = cur.fetchall()
        conn.close()
        return table
    except:
        return None


def connDB():
    """" Проверка подключения к БД"""
    if selectDB("select * FROM company") is None:
        if not(sqlDB("CREATE TABLE company(id integer PRIMARY KEY AUTOINCREMENT, firma text,"
                     " priority integer DEFAULT (9));")):
            return False
    textQuest = "CREATE TABLE people(id integer PRIMARY KEY AUTOINCREMENT, fio text, company integer," \
                 " email text, FOREIGN KEY(company) REFERENCES company(id));"
    if selectDB("select * FROM people") is None:
        if not (sqlDB(textQuest)):
            return False
    textQuest = "CREATE TABLE project(id integer PRIMARY KEY AUTOINCREMENT, namePr text, app1 text, app2 text," \
                "app3 text, app4 text, IPapp1 text, IPapp2 text, IPapp3 text, IPapp4 text, Capp1 text, Capp2 text," \
                "Capp3 text, Capp4 text, pApp text, svn text, test1 text, test2 text, test3 text, test4 text, " \
                "cache integer DEFAULT (0), comCache text, tableSave text);"
    if selectDB("select * FROM project") is None:
        if not (sqlDB(textQuest)):
            return False
    return True


def nProject(id):
    return sqlDB("INSERT INTO project (namePr) VALUES (?);", id)


def selectProject():
    return selectDB("SELECT id, namePr FROM project")

def sProject(table):
    return sqlDB("UPDATE project SET app1 = ?, app2 = ?, app3 = ?, app4 = ? , IPapp1 = ?, IPapp2 = ?, "
                 "IPapp3 = ?, IPapp4 = ?, Capp1 = ?, Capp2 = ?, Capp3 = ?, Capp4 = ?, pApp = ?, svn = ?,"
                 " test1 = ?, test2 = ?, test3 = ?, test4 = ?, cache = ?, comCache = ?, tableSave = ? "
                 "where id = ?", table)

def editProject(spisok):
    return sqlDB("UPDATE project SET namePr = ? WHERE id = ?", spisok)

def lProject(id):
    return selectDB("SELECT * FROM project where id = ?", (id,))

def dProject(id):
    return sqlDB("DELETE FROM project where id = ?;", (id,))

def tableDB():
    """ получение таблицы сотрудников"""
    return selectDB("SELECT people.id, people.fio, company.firma, people.email, company.id, company.priority "
                    "FROM company, people WHERE company.id = people.company "
                    "ORDER BY company.priority, company.firma, people.fio;")

def delDB(id):
    """ удаление сотрудников"""
    return sqlDB("DELETE FROM people where people.id = ?;", (id,))

def selectCompany():
    return selectDB("SELECT * FROM company;")

def addPeople(spisok):
    return sqlDB("INSERT INTO people (fio, company, email ) VALUES (?, ?, ?);", spisok)

def editPeople(spisok):
    return sqlDB("UPDATE people SET fio = ?, company = ?, email = ? WHERE id = ?", spisok)

def addCompany(spisok):
    return sqlDB("INSERT INTO company (firma, priority) VALUES (?, ?);", spisok)

def editCompany(spisok):
    return sqlDB("UPDATE company SET firma = ?, priority = ? WHERE id = ?", spisok)
