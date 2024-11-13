import os
import subprocess
from platform import system
from jinja2 import Environment, FileSystemLoader 
from pyhtml2pdf import converter
import json

class Consult_report():
    def __init__(self, filename):
        self.file = filename
        self.createDirectory()
        
        
    def createDirectory(self):
        if not os.path.exists(f"/home/lalo/Consultas/{self.file}"):
            os.mkdir(f"/home/lalo/Consultas/{self.file}")
        
    def getData(self):
        try:
            with open(f"printer/consults/{self.file}.json", "r") as consult:
                data = json.loads(consult.read())
            self.date = self.transformDate(data["date"][0:-6])
            self.type = data["type"]
            self.anamnesis = data["anamnesis"]
            self.patient = data["patient"]
            self.owner = data["owner"]
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
        self.getData()
        self.createHtml()
        self.htmlToPDF_popen()
        self.openToPrint()
 
    def createHtml(self):
        print("entered to create report html")
        environment = Environment(loader=FileSystemLoader(f"printer/templates/"))
        template = environment.get_template("template_consult_report.html")        
        content = template.render(date = self.date, patient = self.patient, owner = self.owner, anamnesis = self.anamnesis, tc = self.tc, cc = self.cc,
                                  emental = self.edo_mental, notes = self.notes, next = self.next, linfo = self.linfo, acard = self.acard,
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
            print(path)
            target = f"/home/lalo/Consultas/{self.file}/{self.file}.pdf"
            converter.convert(f"file:///{path}", target, print_options={"marginTop": 0,
                                                                                        "marginLeft":0,
                                                                                        "marginRight":0,
                                                                                        "marginBottom":0})
            print("created report in pdf")
        except Exception as e:
            print("Error: ", e)
            
    def htmlToPDF_popen(self):
        pdf = f"/home/lalo/Consultas/{self.file}/{self.file}.pdf"
        html = os.path.abspath(f"printer/reports/{self.file}.html")
        command = ["google-chrome", "--headless", "--disable-gpu", "--print-to-pdf", f"--print-to-pdf={pdf}", html]
        try:    
            subprocess.check_call(command)
            print("saved pdf")
            os.wait()
        except Exception as e:
            subprocess.Popen(command)
                    
    def openToPrint(self):
        path = os.path.abspath(f"/home/lalo/Consultas/{self.file}/{self.file}.pdf")
        subprocess.Popen(["evince", path])
        

        """_summary_
        papi: no ha estado comiendo desd el sabado en la tarde, sin apetito
        heces color gris oscuro verdoso, toma suero forzado, solo comio un poco de a/d
        2.7 kg
        """