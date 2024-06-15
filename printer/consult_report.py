# -*- coding: utf-8 -*-
import os
import subprocess
from jinja2 import Environment, FileSystemLoader 
import json
import win32print

class Consult_report():
    def __init__(self, filename):
        self.file = filename
        self.setActiveUser()
        self.setDirectory()
        self.createFolder()

    def createFolder(self):
        self.folder_path = f"C:\\Users\\{self.user}\\Documents\\Consultas\\{self.file}"
        if not os.path.exists(self.folder_path):
            os.mkdir(self.folder_path)

    def setActiveUser(self):
        self.user = os.getlogin()

    def setDirectory(self):
        if os.path.exists("C:\\Users"):
            self.users = "Users"
        else:
            self.users = "Usuarios"
        documents = f"C:\\{self.users}\\{self.user}\\Documents"
        if os.path.exists(documents):
            self.documents = "Documents"
        else: 
            self.documents = "Documentos"
        
        
    def getData(self):
        try:
            with open(f"printer\\consults\\{self.file}.json", "r") as consult:
                data = json.loads(consult.read())
            self.date = self.transformDate(data["date"][0:-6])
            self.type = data["type"]
            self.anamnesis = data["anamnesis"].replace("\n", "<br>")
            self.patient = data["patient"]
            self.edo_mental = data["mental"]
            self.linfo = data["linfonode"]
            self.fc = data["fc"]
            self.fr = data["fr"]
            self.cc = data["cc"]
            self.tc = data["tc"]
            self.rt = data["rt"]
            self.weight = data["weight"]
            self.copro = data["copro"]
            self.hydra = data["hydra"]
            self.wound = data["wound"]
            self.lab = data["laboratory"]
            self.rd = data["rd"]
            self.apulmo = data["auscPulm"]
            self.acard = data["auscCardiac"]
            self.pabd = data["abdPalpat"]
            self.history = data["clinicHistory"].replace("\n", "<br>")
            self.notes = data["notes"].replace("\n", "<br>")
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
        self.htmlToPDF()
        self.openToPrint()
 
    def createHtml(self):
        print("entered to create report html")
        css_path = os.path.abspath("printer\\templates\\style_consult_report.css")
        environment = Environment(loader=FileSystemLoader(f"printer\\templates\\"))
        template = environment.get_template("template_consult_report.html")        
        content = template.render(css_path=css_path, date = self.date, patient = self.patient, anamnesis = self.anamnesis, tc = self.tc, cc = self.cc,
                                  emental = self.edo_mental, notes = self.notes, next = self.next, linfo = self.linfo, acard = self.acard,
                                  type = self.type[0], motive = self.motive, rt = self.rt, fc = self.fc, weight = self.weight,
                                  fr = self.fr, rd = self.rd, apulmo = self.apulmo, pabd = self.pabd, cost = self.cost,
                                  history = self.history, copro = self.copro, wound = self.wound, lab = self.lab, hydra = self.hydra)
        with open(f"printer\\reports\\{self.file}.html", "w", encoding="utf-8") as test:
            test.write(content)
            print("created report html")

    def htmlToPDF(self):
        html = os.path.abspath(f"printer\\reports\\{self.file}.html")
        pdf = f"C:\\{self.users}\\{self.user}\\{self.documents}\\Consultas\\{self.file}\\{self.file}.pdf"
        print(pdf)
        edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
        command = [edge_path, "--headless", "--disable-gpu", "--print-to-pdf", f"--print-to-pdf={pdf}", html]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
                    
    def openToPrint(self):
        path = f"C:\\{self.users}\\{self.user}\\{self.documents}\\Consultas\\{self.file}\\{self.file}.pdf"
        os.startfile(path)

