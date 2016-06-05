# -*- coding: utf-8 -*-
import psycopg2
import configparser

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
        cur.execute("CREATE DATABASE %s  WITH OWNER = %s" % (conf.get("postgres", "dbname"), conf.get("postgres", "user")))
        conn.commit()
        cur.close()
        conn.close()
    except:
        return "Ошибка создания БД"

    try:
        conn = psycopg2.connect("%s dbname=%s " % (dsn, conf.get("postgres", "dbname")))
        cur = conn.cursor()
        cur.execute("CREATE TABLE people(id serial NOT NULL, fio text, company text, email text, "
                    "CONSTRAINT people_pkey PRIMARY KEY (id));")
        conn.commit()
        cur.close()
        conn.close()
        return "БД создана"
    except:
        return "Ошибка создания таблиц"

def tableDB():
    conf = configparser.RawConfigParser()
    conf.read("config.conf")
    dsn = 'user=%s password=%s host=%s dbname=%s' % (conf.get("postgres", "user"), conf.get("postgres", "password"),
                                           conf.get("postgres", "host"), conf.get("postgres", "dbname"))
    try:
        conn = psycopg2.connect(dsn)
        cur = conn.cursor()
        cur.execute("select * from people;")
        table = cur.fetchall()
        cur.close()
        conn.close()
        return table
    except:
        return ()

