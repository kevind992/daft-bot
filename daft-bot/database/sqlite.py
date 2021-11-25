#!/usr/bin/python

import sqlite3

def connect():
    conn = sqlite3.connect('bot_db.db')
    define_table(conn)
    return conn.cursor()


def define_table(conn):
    conn.execute('''
            CREATE TABLE HOUSE
            (ID INT PRIMARY KEY     NOT NULL,
            TIMESTAMP   TEXT    NOT NULL,
            PRICE   TEXT    NOT NULL,
            ADDRESS     TEXT,
            URL     TEXT);''')
    print("Table created successfully")


def backup(conn, data):
    for d in data:
        conn.execute("INSERT INTO HOUSE (TIMESTAMP, PRICE, ADDRESS, URL) VALUES (" +
                     data.date + "," + data.price + "," + data.address + "," + data.url + ");")

    conn.commit()
    print("Records backed up")
