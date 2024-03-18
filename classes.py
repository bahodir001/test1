from connect_db import Database

class Base:
    @staticmethod
    def select(table, column_name):
        query = f"SELECT * FROM {table} ORDER BY {column_name}_id"
        return Database.connect(query, "select")

    @staticmethod
    def delete_id(table, id):
        query = f"DELETE FROM {table} WHERE student_id = {id}"
        return Database.connect(query, "delete")

    @staticmethod
    def delete(table, column_name, data):
        query = f"DELETE FROM {table} WHERE {column_name} = {data}"
        return Database.connect(query, "delete")



    @staticmethod
    def update_id(table, colum_name, old_data, new_data):
        query = f"UPDATE {table} SET {colum_name} = {new_data} WHERE {colum_name} = '{old_data}'"
        return Database.connect(query, "update")

    @staticmethod
    def update(table, colum_name, old_data, new_data):
        query = f"UPDATE {table} SET {colum_name} = '{new_data}' WHERE {colum_name} = '{old_data}'"
        return Database.connect(query, "update")


class Payment(Base):
    def __init__(self, card, cash):
        self.card = card
        self.cash = cash

    def insert_payment(self):
        query = (f"INSERT INTO payment(card, cash) VALUES ('{self.card}', '{self.cash}')")
        return Database.connect(query, "Insert")



    @staticmethod
    def update_payment(column_name, old_data, new_data):
        query = (f"UPDATE payment SET {column_name} = '{new_data}' WHERE {column_name} = ' {old_data}'")
        return Database.connect(query, "Update")

    @staticmethod
    def delete_payment(column_name, vaulue):
        query = (f"DELETE FROM payment WHERE {column_name} = '{vaulue}'")
        return Database.connect(query, "Delete")


    @staticmethod
    def select_payment():
        query = (f"SELECT * FROM payment")
        return Database.connect(query, "Select")


class Storehouse(Base):
    def __init__(self, storage_id, last_update, create_date):
        self.storage_id = storage_id
        self.last_update = last_update
        self.create_date = create_date
        self.table_name = "storehouse"

    @staticmethod
    def update_id(column_name, old_data, new_data):
        query = f"UPDATE storehouse SET {column_name} = {new_data} WHERE {column_name} = '{old_data}'"
        return Database.connect(query, "update")


    @staticmethod
    def select():
        query = f"SELECT * FROM storage"
        return Database.connect(query, "select")


class Product(Base):
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.table_name = "product"


    def insert(self, table):
        query = (f"INSERT INTO {table}(name, price) "
                 f"VALUES ('{self.name}', '{self.price}', '{self.price}')")
        return Database.connect(query, "INSERT")

    @staticmethod
    def select():
        query = (f"SELECT * FROM product.product_id, product.name, product.price, product.create_date ")
        return Database.connect(query, "select")

    @staticmethod
    def delete_product(column_name, value):
        if type(column_name) == int:
            query = (f" DELETE FROM product WHERE {column_name} = {value}")
        else:
            query = (f" DELETE FROM product WHERE {column_name} = {value}")
        return Database.connect(query, "Delete")


    @staticmethod
    def update(column_name, old_data, new_data):
        query = (f"UPDATE product SET {column_name} = {old_data} WHERE {column_name} = '{old_data}'")
        return Database.connect(query, "Update")


class Customer(Base):
    def __init__(self, first_name,):
        self.first_name = first_name
        self.table_name = "Customer"

    def insert(self, first_name):
        query = (
            f"INSERT INTO customer(first_name) VALUES ('{self.first_name}')")
        return Database.connect(query, "Insert")

    @staticmethod
    def delete_customer(column_name, value):
        if type(column_name) == int:
            query = (f"DELETE FROM customer WHERE {column_name} = '{value}'")
        else:
            query = (f"DELETE FROM customer WHERE {column_name} = {value}")
        return Database.connect(query, "Delete")

    @staticmethod
    def select_customer(table):
        query = (f"SELECT * FROM table")
        return Database.connect(query, "Select")

    @staticmethod
    def update_customer(table, column_name, old_data, new_data):
        query = (f"UPDATE table {table} SET {column_name} = {new_data} WHERE {old_data} = '{old_data}'")
        return Database.connect(query, "Update")


