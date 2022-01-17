# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 15:59:20 2021

@author: mobhaska
"""
from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')
    
    def __init__(self,name,price,store_id):
        self.name = name
        self.price = price
        self.store_id = store_id
    
    def json(self):
        return {'id':self.id, 'name': self.name, 'price': self.price, 'store_id': self.store_id}
    
    @classmethod
    def find_item_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
        #select * from items where name=name and id=1
        
    def save_to_db(self):
        db.session.add(self)  #insert
        db.session.commit()   #commit
        
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        
#    def find_all_item(self):
#        return self.query.filter_by