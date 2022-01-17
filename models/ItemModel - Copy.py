# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 15:59:20 2021

@author: mobhaska
"""
import sqlite3
from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    
    def __init__(self,name,price):
        self.name = name
        self.price = price
    
    def json(self):
        return {'name': self.name, 'price': self.price}
    
    @classmethod
    def find_item_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "SELECT * FROM items where name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()
        
        if row:
            return cls(*row)
        
    def insert(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "insert into items values(?, ?)"
        cursor.execute(query, (self.name, self.price))
        
        connection.commit()
        connection.close()
        
    def update(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "update items set price=? where name=?"
        cursor.execute(query, (self.price, self.name))
        
        connection.commit()
        connection.close()