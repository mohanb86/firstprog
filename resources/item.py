# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 12:04:28 2021

@author: mobhaska
"""

from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.ItemModel import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=str,
                        required=True,
                        help="This field cannot be blank.")

    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help="This field cannot be blank.")

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_item_by_name(name)
        if item:
            return item.json()
        return {'message': 'item not found'}

    def post(self, name):
         
        if ItemModel.find_item_by_name(name):
            return {'message': "an item with name '{}' already exists.".format(name)}, 400
        
        data = Item.parser.parse_args()
        
        item = ItemModel(name, data['price'],data['store_id'])
        
        try:
            item.save_to_db()
        except:
            return {"message": "Error occured during insert"}, 500
        
        return {"message": "Item Inserted"}, 201
    
    def delete(self, name):
        item = ItemModel.find_item_by_name(name)
        if item:
            item.delete_from_db()
            return {"message": "Item deleted successfully"}
        else:
            return {"message": "Item not found"}

    def put(self, name):
        
        data = Item.parser.parse_args()
        
        item = ItemModel.find_item_by_name(name)
        
        if item is None:
            try :
                item.ItemModel(name,data['price'],data['store_id'])
            except:
                return {"message":"Error occured while insert"}, 500
        else:
            try:
                item.price=data['price']
                item.store_id=data['store_id']
                item.save_to_db()
            except:
                return {"message":"Error occured while update"}, 500
        
        return item.json()

    
class ItemList(Resource):
        def get(self):
            return {'items': [item.json() for item in ItemModel.query.all()]}