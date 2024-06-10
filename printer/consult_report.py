import os
import subprocess
from platform import system
from jinja2 import Environment, FileSystemLoader 
from pyhtml2pdf import converter
import json

class Consult_report():
    def __init__(self, filename):
        self.file = filename
        self.setSlash()
        
    def setSlash(self):
        if system() == "Windows":
            self.slash = '\\'
        elif system() == "Linux":
            self.slash = '/'
        
    def getData(self):
        try:
            with open(f"printer{self.slash}consults{self.slash}{self.file}.json", "r") as consult:
                data = json.loads(consult.read())
            self.date = self.transformDate(data["date"][0:-6])
            self.type = data["type"]
            self.anamnesis = data["anamnesis"]
            self.patient = data["patient"]
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
            self.acard = data["auscCardiac"]
            self.pabd = data["abdPalpat"]
            self.history = data["clinicHistory"]
            self.notes = data["notes"]
            self.next = self.transformDate(data["nextVisit"])
            self.motive = data["motive"]
            self.cost = data["cost"]
        except Exception as e:
            print("Error: ", e)
            
    def transformDate(self, date):
        day, month, year = date.split("-")
        month = self.translate(month)
        date = f"{day} de {month} de {year}"
        return date
    
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
        
    def printReport(self):
        if not os.path.exists(f"..{self.slash}{self.file}/"):
            #agregar creacion de carpeta contenedora por consulta
            os.mkdir(self.file)
        if os.path.exists(f"{self.file}.html"):
            self.htmlToPDF()
            self.openToPrint()
        self.getData()
        self.createHtml()
        self.htmlToPDF()
        self.openToPrint()
 
    def createHtml(self):
        print("entered to create report html")
        environment = Environment(loader=FileSystemLoader(f"printer{self.slash}templates{self.slash}"))
        template = environment.get_template("template_consult_report.html")        
        content = template.render(date = self.date, patient = self.patient, anamnesis = self.anamnesis, tc = self.tc, cc = self.cc,
                                  emental = self.edo_mental, notes = self.notes, next = self.next, linfo = self.linfo, acard = self.acard,
                                  type = self.type[0], motive = self.motive, rt = self.rt, fc = self.fc, weight = self.weight,
                                  fr = self.fr, rd = self.rd, apulmo = self.apulmo, pabd = self.pabd, cost = self.cost,
                                  history = self.history)
        with open(f"printer{self.slash}reports{self.slash}{self.file}.html", "w", encoding="utf-8") as test:
            test.write(content)
            print("created report html")
        
    def htmlToPDF(self):
        try:
            print("Entered to html to pdf")
            path = os.path.abspath(f'printer{self.slash}reports{self.slash}{self.file}.html')
            print(path)
            converter.convert(f"file:{self.slash}{self.slash}{self.slash}{path}", f"printer{self.slash}reports{self.slash}{self.file}.pdf", print_options={"marginTop": 0,
                                                                                        "marginLeft":0,
                                                                                        "marginRight":0,
                                                                                        "marginBottom":0})
        except Exception as e:
            print("Error: ", e)
                    
    def openToPrint(self):
        path = os.path.abspath(f"printer{self.slash}reports{self.slash}{self.file}.pdf")
        if system() == "Windows":
            os.startfile(path)
        elif system() == "Linux":
            subprocess.Popen(["evince", path])
