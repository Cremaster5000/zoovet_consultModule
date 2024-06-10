import os
import json
import platform
from jinja2 import Environment, FileSystemLoader 
from pyhtml2pdf import converter
import subprocess


class Recipe():
    def __init__(self, filename):
        print("created recipe")
        self.file = filename
        self.setSlash
        
    def setSlash(self):
        systemOs = os.system()
        if systemOs == "Windows":
            self.slash = '\\'
        elif systemOs == "Linux":
            self.slash = '/'

    def getData(self):
        print("entered to getData")
        try:
            with open(f"printer{self.slash}consults{self.slash}{self.file}.json", "r") as consult:
                data = json.loads(consult.read())
            self.date = self.transformDate(data["date"][0:-6])
            self.type = data["type"]
            self.anamnesis = data["anamnesis"]
            self.patient = data["patient"]
            self.owner = data["owner"]                        
            self.weight = data["weight"]
            self.dx = data["dx"]
            self.tx = data["tx"]
            self.next = self.transformDate(data["nextVisit"])
            self.motive = data["motive"]
            self.cost = data["cost"]
            print("data loaded")
        except Exception as e:
            print("Error: ", e)
            
    def transformDate(self, date):
        day, month, year = date.split("-")
        month = self.translate(month)
        date = f"{day} de {month} de {year}"
        print("date transformed")
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
        print("date translated")
        return spanish[month]
    
    def createHtml(self):
        
        environment = Environment(loader=FileSystemLoader(f"printer{self.slash}templates{self.slash}"))
        template = environment.get_template("template_recipe.html")        
        content = template.render(date = self.date, patient = self.patient,
                                  propietary = self.owner, weight = self.weight,
                                  dx = self.dx, tx = self.tx, next_visit = self.next,
                                  motive = self.motive, cost = self.cost)
        with open(f"printer{self.slash}html{self.slash}{self.file}.html", "w", encoding="utf-8") as test:
            test.write(content)
        print("created recipe on html")

    def htmlToPDF(self):
        path = os.path.abspath(f'printer{self.slash}html{self.slash}{self.file}.html')
        converter.convert(f"file:{self.slash}{self.slash}{self.slash}{path}", f"printer{self.slash}pdf{self.slash}{self.file}.pdf", print_options={"marginTop": 0,
                                                                                    "marginLeft":0,
                                                                                    "marginRight":0,
                                                                                    "marginBottom":0})
        print("created pdf from html")
        
    def openToPrint(self):
        path = os.path.abspath(f"printer{self.slash}pdf{self.slash}{self.file}.pdf")
        systemOs = platform.system()
        if systemOs == "Linux":
            subprocess.Popen(["evince", path])
        elif systemOs == "Windows":
            os.startfile(path)

    def printRecipe(self):
        self.getData()
        self.createHtml()
        self.htmlToPDF()
        self.openToPrint()
        

if __name__ == '__main__':
    recipe = Recipe()
    recipe.getData("niki-test")
    recipe.createHtml()
    recipe.htmlToPDF()