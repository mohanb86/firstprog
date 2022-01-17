# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 06:36:51 2021

@author: mobhaska
"""

import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "create table if not exists users (id int, username text, password text)"
cursor.execute(create_table)

insert_query = "insert into users values (?,?,?)"

user=(1,'mohan','asdf')
cursor.execute(insert_query, user) #for one query


user_m=[(2,'niha','niha'),
        (3,'vani','vani')]
cursor.executemany(insert_query, user_m) #for many query

select_query = "select * from users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()