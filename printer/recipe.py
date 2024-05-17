import os
import json
from jinja2 import Environment, FileSystemLoader 
from pyhtml2pdf import converter
import subprocess


class Recipe():
    def __init__(self, filename):
        self.file = filename
        
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

    def getData(self):
        try:
            print(os.path.relpath(f"consults/{self.file}.json"))
            with open(f"printer/consults/{self.file}.json", "r") as consult:
                raw_data = json.loads(consult.read())
            self.date = self.transformDate(raw_data["date"][0:-6])
            self.name = raw_data["name"]
            self.owner = raw_data["owner"]
            self.weight = raw_data["weight"]
            self.dx = raw_data["dx"]
            self.tx = raw_data["tx"].replace("\n", "<br>")
            self.next = self.transformDate(raw_data["nextVisit"])
            self.motive = raw_data["motive"]
            self.cost = self.findWords(self.motive)
        except Exception as e:
            print("Error: ", e)

    def createHtml(self):
        environment = Environment(loader=FileSystemLoader("printer/templates/"))
        template = environment.get_template("template_recipe.html")        
        content = template.render(date = self.date, patient = self.name,
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
        
    def findWords(self, motive):
        price = ""
        control_cite = ["cita control", "control", "seguimiento"]
        general_cite = ["consulta general", "primera consulta", "primera visita", "consulta"]
        desparasitation_cite = ["desparasitación interna", "desparasitante", "desparasitación", "desparasitacion"]
        laboratories = ["hemograma", "biometria hematica"]
        for word in motive.split("+"):
            word = word.rstrip().lstrip()
            if price != "": price+=(" + ")
            if word in control_cite: price+=(f"{word} ($300)")
            if word in general_cite: price+=(f"{word} ($380)")
            if word in desparasitation_cite: price+=(f"{word} ($180)")
            if word in laboratories: price+=(f"{word} ($400)")
        return price  
            
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