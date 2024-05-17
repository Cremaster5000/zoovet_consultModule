#import mysql.connector
import os
from dotenv import load_dotenv

class DatabaseObject():
    def __init__(self):
        load_dotenv()
    
    def conectDB(self):
        self.conector = mysql.connector.connect(user =os.getenv("DB_USER"), 
                                                password = os.getenv("DB_PASSWORD"), 
                                                host = os.getenv("DB_HOST"),
                                                database = os.getenv("DATABASE"))
        return self.conector.cursor()
        
    def closeConection(self):
        self.conector.close()
        
    def addProduct(self, product):
        try:
            cursor = self.conectDB()
            cursor.execute()
            return True 
        except Exception as e:
            print(e)
            return False
        finally:
            self.closeConection()
    
    def delProduct(self, product):
        try:
            cursor = self.conectDB()
            cursor.execute()
        except Exception as e:
            print(e)
            return False
        finally:
            self.closeConection()
    
    def searchProduct(self, product):
        try:
            cursor = self.conectDB()
            cursor.execute("SELECT * FROM")
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
            return False
        finally: self.closeConection()
    
    def getInventory(self, inventory):
        try:
            cursor = self.conectDB()
            cursor.execute()
            result = cursor.fetchall()
            return result  
        except Exception as e:
            print(e)
            return False
        finally: self.closeConection()
    
    def saveInventory(self, inventory):
        try:
            cursor = self.conectDB()
            cursor.execute()
            return True 
        except Exception as e:
            print(e)
            return False
        finally: self.closeConection()
    
    def saveConsult(self, consult):
        pass