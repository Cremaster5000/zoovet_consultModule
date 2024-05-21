import os
import json
from jinja2 import Environment, FileSystemLoader 
from pyhtml2pdf import converter
import subprocess


class Recipe():
    def __init__(self, filename):
        self.file = filename

    def getData(self):
        try:
            with open(f"printer/consults/{self.file}.json", "r") as consult:
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
    
    def createHtml(self):
        environment = Environment(loader=FileSystemLoader("printer/templates/"))
        template = environment.get_template("template_recipe.html")        
        content = template.render(date = self.date, patient = self.patient,
                                  propietary = self.owner, weight = self.weight,
                                  dx = self.dx, tx = self.tx, next_visit = self.next,
                                  motive = self.motive, cost = self.cost)
        with open(f"printer/html/{self.file}.html", "w", encoding="utf-8") as test:
            test.write(content)

    def htmlToPDF(self):
        path = os.path.abspath(f'printer/html/{self.file}.html')
        converter.convert(f"file:///{path}", f"printer/pdf/{self.file}.pdf", print_options={"marginTop": 0,
                                                                                    "marginLeft":0,
                                                                                    "marginRight":0,
                                                                                    "marginBottom":0})
        
    def openToPrint(self):
        path = os.path.abspath(f"printer/pdf/{self.file}.pdf")
        subprocess.run(["evince", path])

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