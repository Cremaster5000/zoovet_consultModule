import os
import subprocess
from jinja2 import Environment, FileSystemLoader 
from pyhtml2pdf import converter
import json

class Consult_report():
    def __init__(self, filename):
        self.file = filename
        
    def printReport(self):
        if os.path.exists(f"{self.file}.html"):
            self.htmlToPDF()
            self.openToPrint()
        self.getData()
        self.createHtml()
        self.htmlToPDF()
        self.openToPrint()
        
    def getData(self):
        try:
            with open(f"printer/consults/{self.file}.json", "r") as consult:
                data = json.loads(consult.read())
            self.date = self.transformDate(data["date"][0:-6])
            self.type = self.setTypeConsult(data["type"]),
            self.anamnesis = data["anamnesis"]
            self.name = data["name"]
            self.edo_mental = data["mental"]
            self.linfo = data["linfonode"]
            self.fc = data["fc"]
            self.fr = data["fr"]
            self.cc = data["cc"]
            self.tc = data["tc"]
            self.rt = data["rt"]
            self.weight = data["weight"]
            self.rd = data["rd"]
            self.apulmo = data["auscPulm"]
            self.pabd = data["abdPalpat"]
            self.history = data["clinicHistory"]
            self.notes = data["notes"]
            self.next = self.transformDate(data["nextVisit"])
            self.motive = data["motive"]
            self.cost = self.findWords()
        except Exception as e:
            print("Error: ", e)
            
    def translate(self, month):
        spanish = {
                    "01": "enero",
                    "02": "febrero",
                    "03": "marzo",  
                    "04": "abril",
                    "05": "mayo",
                    "06": "junio",
                    "07": "julio",
                    "08": "agosto",
                    "09": "septiembre",
                    "10": "octubre",
                    "11": "noviembre",
                    "12": "diciembre"
                 }
        return spanish[month]

    def transformDate(self, date):
        day, month, year = date.split("-")
        month = self.translate(month)
        date = f"{day} de {month} de {year}"
        return date
    
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
            for word in self.motive.split("+"):
                word = word.rstrip().lstrip()        
                print(self.motive)
                if price != "": price+=(" + ")
                if word in control_cite: price+=("$300")
                if word in general_cite: price+=("$380")
                if word in desparasitation_cite: price += self.desparasitation_price()
                if word in laboratories: price+=("$400")
            price += "."
        except Exception as e:
            print("Error:", e)
        return price 
    
    def desparasitation_price(self):
        if self.species == "Felino":
            return "($154)"
        weight = float(self.weight.replace("kg", "").replace(" ",""))
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
                    
    def createHtml(self):
        print("entered to create report html")
        environment = Environment(loader=FileSystemLoader("printer/templates/"))
        template = environment.get_template("template_consult_report.html")        
        content = template.render(date = self.date, patient = self.name, anamnesis = self.anamnesis, tc = self.tc, cc = self.cc,
                                  emental = self.edo_mental, notes = self.notes, next = self.next, linfo = self.linfo, 
                                  type = self.type[0], motive = self.motive, rt = self.rt, fc = self.fc, weight = self.weight,
                                  fr = self.fr, rd = self.rd, apulmo = self.apulmo, pabd = self.pabd, cost = self.cost,
                                  history = self.history)
        with open(f"printer/reports/{self.file}.html", "w", encoding="utf-8") as test:
            test.write(content)
            print("created report html")
        
    def htmlToPDF(self):
        try:
            print("Entered to html to pdf")
            path = os.path.abspath(f'printer/reports/{self.file}.html')
            converter.convert(f"file:///{path}", f"printer/reports/{self.file}.pdf", print_options={"marginTop": 0,
                                                                                        "marginLeft":0,
                                                                                        "marginRight":0,
                                                                                        "marginBottom":0})
        except Exception as e:
            print("Error: ", e)
                    
    def openToPrint(self):
        path = os.path.abspath(f"printer/reports/{self.file}.pdf")
        subprocess.run(["evince", path])