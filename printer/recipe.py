import os
import json
import platform
from jinja2 import Environment, FileSystemLoader 
from pyhtml2pdf import converter
import subprocess
from getpass import getuser


class Recipe():
    def __init__(self, filename):
        print("created recipe")
        self.file = filename
        self.user = getuser()
        self.createDirectory()
        
        
    def createDirectory(self):
        if not os.path.exists(f"/home/lalo/Consultas/{self.file}"):
            os.mkdir(f"/home/lalo/Consultas/{self.file}")
        
    def setSlash(self):
        systemOs = os.system()
        if systemOs == "Windows":
            self.slash = '\\'
        elif systemOs == "Linux":
            self.slash = '/'

    def getData(self):
        print("entered to getData")
        try:
            with open(f"printer/consults/{self.file}.json", "r") as consult:
                data = json.loads(consult.read())
            self.date = self.transformDate(data["date"][0:-6])
            print("date:" , self.date)
            self.type = data["type"]
            self.anamnesis = data["anamnesis"]
            self.patient = data["patient"]
            self.owner = data["owner"]                        
            self.weight = data["weight"]
            self.dx = data["dx"]
            self.tx = data["tx"].replace('\n', '<br>')
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
        environment = Environment(loader=FileSystemLoader(f"printer/templates/"))
        template = environment.get_template("template_recipe.html")        
        content = template.render(date = self.date, patient = self.patient,
                                  propietary = self.owner, weight = self.weight,
                                  dx = self.dx, tx = self.tx, next_visit = self.next,
                                  motive = self.motive, cost = self.cost)
        with open(f"printer/html/{self.file}.html", "w", encoding="utf-8") as test:
            test.write(content)
        print("created recipe on html")

    def htmlToPDF_popen(self):
        pdf = f"/home/lalo/Consultas/{self.file}/Receta_{self.file}.pdf"
        html = os.path.abspath(f"printer/html/{self.file}.html")
        command = ["google-chrome", "--disable-gpu", f"--print-to-pdf={pdf}", "--no-margins", html,  "--headless"]
        try:
           subprocess.check_call(command)
        except subprocess.CalledProcessError as e:
            print("Error: ", e, "retrying...")
        
    def openToPrint(self):
        path = os.path.abspath(f"/home/{self.user}/Consultas/{self.file}/Receta_{self.file}.pdf")
        systemOs = platform.system()
        if systemOs == "Linux":
            subprocess.Popen(["evince", path])
        elif systemOs == "Windows":
            os.startfile(path)


    def printRecipe(self):
        self.getData()
        self.createHtml()
        self.htmlToPDF_popen()
        self.openToPrint()
        
        

if __name__ == '__main__':
    recipe = Recipe()
    recipe.getData("niki-test")
    recipe.createHtml()
    recipe.htmlToPDF()