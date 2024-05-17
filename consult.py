from datetime import datetime
import json
from database_object import DatabaseObject
from warning import Warning


class Consult():
	def __init__(self, data):
		self.created = data["date"].replace(":","")
		owner = data["owner"]
		name = data["name"]
		self.data = data
		self.name = f"{name}_{owner}_{self.created}"
		print(f"consult object created at: {self.created}")

	def setData(self, data):
		pass  

	def saveLocally(self):
		try:
			print(f"name of file: {self.name}.json")
			with open(f"printer/consults/{self.name}.json", 'w') as file:
				file.write(json.dumps(self.data))
				print("saved locally")
		except Exception as e:
			print("Error", e)

	def saveConsult(self):
		try:
			self.saveLocally()
			self.saveDB(self.data)
		except Exception as e:
			self.warning = Warning(self, f"Error: {e}")
			print(f"warning: {self.data} cant be saved")
			return False
		try: 
			with open("consults_cache.txt", "a") as cache:
				print("entered to modified1")
				print("writable: ", cache.writable())
				print("readable: ", cache.readable())
				cache.write(self.name+'\n')
				print("file writed")
				print("cache list modified")
		except Exception as e:
			with open("consults_cache.txt", "w") as cache:
				cache.write(self.name+'\n')
				print("cache list modified2")
		finally:
			print("consult object saved all info")
			return self.name



	def saveDB(self, data):
		print("saved at database")

	def getData(self):
		pass  



if __name__ == '__main__':
	pass
"""     app = QApplication(sys.argv)
    now = datetime.datetime.now()
    test = Consult_View(["niki", now, "macho", "4 meses", "mex. domestico", "castrado"])
    sys.exit(app.exec()) """