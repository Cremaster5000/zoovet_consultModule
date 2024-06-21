from datetime import datetime
import json
from database_object import DatabaseObject
from warning import Warning
import os


class Consult():
	def __init__(self, data):
		self.created = data["date"].replace(":","")
		self.data = data 
		self.setData()
		patient = data["patient"]
		owner = data["owner"]
		self.filename = f"{patient}_{owner}_{self.created}"
		print(f"consult object created at: {self.created}")



	def createFolderConsults(self):
		folder = f"printer\\consults\\"
		if not os.path.exists(os.path.abspath(folder)):
			os.mkdir(os.path.abspath(folder))

	def createFolderHtml(self):
		folder = f"printer\\html\\"
		if not os.path.exists(os.path.abspath(folder)):
			os.mkdir(os.path.abspath(folder))
		

	def setData(self):
		self.data["type"] = self.setTypeConsult(self.data["type"]),
		self.data["cost"] = self.findWords()
    
	def setTypeConsult(self, type):
		types = {
                "Consulta general":0,
                "Cita control":1,
                "Entrega de resultados":2,
                "Otro":3
        }
		return types[type]
    
	def findWords(self):
		price = ""
		control_cite = ["cita control", "control", "seguimiento"]
		general_cite = ["consulta general", "primera consulta", "primera visita", "consulta"]
		desparasitation_cite = ["desparasitación interna", "desparasitante", "desparasitación", "desparasitacion"]
		laboratories = ["hemograma", "biometria hematica"]
		print("entered in findwords")
		try:
			for word in self.data["motive"].split("+"):
				word = word.rstrip().lstrip()        
				#print(self.motive)
				if price != "": price+=(" + ")
				if word in control_cite: price+=("$300")
				if word in general_cite: price+=("$380")
				if word in desparasitation_cite: price += self.desparasitation_price()
				if word in laboratories: price+=("$400")
		except Exception as e:
			print("Error:", e)
		return price 
    
	def desparasitation_price(self):
		if self.data["species"] == "Felino":
			return "($154)"
		weight = float(self.data["weight"].replace("kg", "").replace(" ",""))
		if weight < 5:
			return "($155)"
		if weight >= 5 and weight <10:
			return "($188)"
		if weight >= 10 and weight <15:
			return "($220)"
		if weight >= 15 and weight <20:
			return "($252.5)"
		if weight >= 20 and weight <30:
			return "($253)"
		if weight >= 30 and weight <40:
			return "($318)" 
                    
	def saveLocally(self):
		try:
			print(f"name of file: {self.filename}.json")
			with open(f"printer/consults/{self.filename}.json", 'w') as file:
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
		finally:
			print("consult object saved all info")
			return self.filename

	def saveDB(self, data):
		print("saved at database")



if __name__ == '__main__':
	pass
"""     app = QApplication(sys.argv)
    now = datetime.datetime.now()
    test = Consult_View(["niki", now, "macho", "4 meses", "mex. domestico", "castrado"])
    sys.exit(app.exec()) """