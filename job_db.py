# -*- coding: utf-8 -*-
import psycopg2
import configparser

"""" Проверка подключения к БД"""
def connDB(self, dsn):
    numberDSN = dsn.find("user=")
    try:
        conn = psycopg2.connect(dsn[numberDSN:])
        cur = conn.cursor()
        cur.execute("select 1")
        cur.fetchone()
        cur.close()
        conn.close()
    except:
        return "Не правильные настройки подключения"

    try:
        conn = psycopg2.connect(dsn)
        cur = conn.cursor()
        cur.execute("select 1")
        cur.fetchone()
        cur.close()
        conn.close()
        return "Связь есть"
    except:
        return "Подключение к postgresql есть, но БД не создана"

""" создание БД"""
def createDB(self):
    conf = configparser.RawConfigParser()
    conf.read("config.conf")
    dsn = 'user=%s password=%s host=%s' % (conf.get("postgres", "user"),
                                                    conf.get("postgres", "password"),
                                                    conf.get("postgres", "host"))
    try:
        conn = psycopg2.connect(dsn)
        conn.set_isolation_level(0)
        cur = conn.cursor()
        cur.execute("CREATE DATABASE %s  " % (conf.get("postgres", "dbname")))
        conn.commit()
        cur.close()
        conn.close()
    except:
        return "Ошибка создания БД"

    try:
        conn = psycopg2.connect("%s dbname=%s " % (dsn, conf.get("postgres", "dbname")))
        cur = conn.cursor()
        cur.execute("CREATE TABLE company(id serial NOT NULL, firma text,"
                    "CONSTRAINT company_pkey PRIMARY KEY (id));")
        conn.commit()
        cur.execute("CREATE TABLE people(id serial NOT NULL, fio text, company integer REFERENCES company"
                    ", email text, CONSTRAINT people_pkey PRIMARY KEY (id));")
        conn.commit()
        cur.close()
        conn.close()
        return "БД создана"
    except:
        return "Ошибка создания таблиц"

""" получение таблицы сотрудников"""
def tableDB():
    conf = configparser.RawConfigParser()
    conf.read("config.conf")
    dsn = 'user=%s password=%s host=%s dbname=%s' % (conf.get("postgres", "user"), conf.get("postgres", "password"),
                                           conf.get("postgres", "host"), conf.get("postgres", "dbname"))
    try:
        conn = psycopg2.connect(dsn)
        cur = conn.cursor()
        cur.execute("SELECT people.id, people.fio, company.firma, people.email, company.id FROM public.company,"
                    " public.people WHERE company.id = people.company ORDER BY company.firma ASC, people.fio ASC;")
        table = cur.fetchall()
        cur.close()
        conn.close()
        return table
    except:
        return ()

""" удаление сотрудников"""
def delDB(id):
    conf = configparser.RawConfigParser()
    conf.read("config.conf")
    dsn = 'user=%s password=%s host=%s dbname=%s' % (conf.get("postgres", "user"), conf.get("postgres", "password"),
                                           conf.get("postgres", "host"), conf.get("postgres", "dbname"))
    try:
        conn = psycopg2.connect(dsn)
        conn.set_isolation_level(0)
        cur = conn.cursor()
        cur.execute("DELETE FROM people where people.id = %s;" % (id))
        cur.close()
        conn.close()
        return "Удаление успешно"
    except:
        return "Ошибка удаления"

def selectCompany():
    conf = configparser.RawConfigParser()
    conf.read("config.conf")
    dsn = 'user=%s password=%s host=%s dbname=%s' % (conf.get("postgres", "user"), conf.get("postgres", "password"),
                                                       conf.get("postgres", "host"), conf.get("postgres", "dbname"))
    try:
        conn = psycopg2.connect(dsn)
        cur = conn.cursor()
        cur.execute("SELECT * FROM public.company;")
        table = cur.fetchall()
        cur.close()
        conn.close()
        return table
    except:
        return ()

def addPeople(spisok):
    conf = configparser.RawConfigParser()
    conf.read("config.conf")
    dsn = 'user=%s password=%s host=%s dbname=%s' % (conf.get("postgres", "user"), conf.get("postgres", "password"),
                                                       conf.get("postgres", "host"), conf.get("postgres", "dbname"))
    try:
        conn = psycopg2.connect(dsn)
        cur = conn.cursor()
        conn.set_isolation_level(0)
        cur.execute("INSERT INTO people (fio, company, email ) VALUES ('%s', %s, '%s');" %
                    (spisok[0], spisok[1], spisok[2]))
        cur.close()
        conn.close()
        return "Успешно"
    except:
        return "Ошибка"

def editPeople(spisok):
    conf = configparser.RawConfigParser()
    conf.read("config.conf")
    dsn = 'user=%s password=%s host=%s dbname=%s' % (conf.get("postgres", "user"), conf.get("postgres", "password"),
                                                       conf.get("postgres", "host"), conf.get("postgres", "dbname"))
    try:
        conn = psycopg2.connect(dsn)
        conn.set_isolation_level(0)
        cur = conn.cursor()
        cur.execute("UPDATE people SET fio = '%s', company = %s, email = '%s' WHERE id = %s" %
                    (spisok[0], spisok[1], spisok[2], spisok[3]))
        cur.close()
        conn.close()
        return "Успешно"
    except:
        return "Ошибка"

def addCompany(spisok):
    conf = configparser.RawConfigParser()
    conf.read("config.conf")
    dsn = 'user=%s password=%s host=%s dbname=%s' % (conf.get("postgres", "user"), conf.get("postgres", "password"),
                                                       conf.get("postgres", "host"), conf.get("postgres", "dbname"))
    try:
        conn = psycopg2.connect(dsn)
        cur = conn.cursor()
        conn.set_isolation_level(0)
        cur.execute("INSERT INTO company (firma) VALUES ('%s');" % (spisok[0]))
        cur.close()
        conn.close()
        return "Успешно"
    except:
        return "Ошибка"

def editCompany(spisok):
    conf = configparser.RawConfigParser()
    conf.read("config.conf")
    dsn = 'user=%s password=%s host=%s dbname=%s' % (conf.get("postgres", "user"), conf.get("postgres", "password"),
                                                       conf.get("postgres", "host"), conf.get("postgres", "dbname"))
    try:
        conn = psycopg2.connect(dsn)
        conn.set_isolation_level(0)
        cur = conn.cursor()
        cur.execute("UPDATE company SET firma = '%s' WHERE id = %s" %
                    (spisok[0], spisok[1]))
        cur.close()
        conn.close()
        return "Успешно"
    except:
        return "Ошибка"