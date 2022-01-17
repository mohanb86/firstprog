# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 07:54:49 2021

@author: mobhaska
"""

import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "create table if not exists users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "create table if not exists items (id INTEGER PRIMARY KEY, name text, price real)"
cursor.execute(create_table)

cursor.execute("Insert into items values(1,'chair1',10.99)")
cursor.execute("Insert into items values(2,'chair2',10.99)")
cursor.execute("Insert into items values(3,'chair3',10.99)")



connection.commit()
connection.close()