# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 12:04:28 2021

@author: mobhaska
"""
from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):


    def get(self, name):
        store = StoreModel.find_item_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not found'}

    def post(self, name):
         
        if StoreModel.find_item_by_name(name):
            return {'message': "a store with name '{}' already exists.".format(name)}, 400
        
        store = StoreModel(name)
        
        try:
            store.save_to_db()
        except:
            return {"message": "Error occured during insert"}, 500
        
        return {"message": "Store Inserted"}, 201
    
    def delete(self, name):
        store = StoreModel.find_item_by_name(name)
        if store:
            store.delete_from_db()
            return {"message": "Store deleted successfully"}
        else:
            return {"message": "Store not found"}

    
class StoreList(Resource):
        def get(self):
            return {'stores': [store.json() for store in StoreModel.query.all()]}