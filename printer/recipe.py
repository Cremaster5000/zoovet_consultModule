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
        self.setUser()
        self.createFolder()

    def setUser(self):
        self.user = os.getlogin()

    def createFolder(self):
        self.folder_path = f"C:\\Users\\{self.user}\\Documents\\Consultas\\{self.file}"
        if not os.path.exists(self.folder_path):
            os.mkdir(self.folder_path)

    def getData(self):
        print("entered to getData")
        try:
            with open(f"printer\\consults\\{self.file}.json", "r") as consult:
                data = json.loads(consult.read())
            self.date = self.transformDate(data["date"][0:-6])
            self.type = data["type"]
            self.patient = data["patient"]
            self.owner = data["owner"]                        
            self.weight = data["weight"]
            self.dx = data["dx"]
            self.tx = data["tx"].replace("\n", "<br>")
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
        css_path = os.path.abspath("printer\\templates\\style_recipe.css")
        environment = Environment(loader=FileSystemLoader(f"printer\\templates\\"))
        template = environment.get_template("template_recipe.html")        
        content = template.render(css_path=css_path, date = self.date, patient = self.patient,
                                  propietary = self.owner, weight = self.weight,
                                  dx = self.dx, tx = self.tx, next_visit = self.next,
                                  motive = self.motive, cost = self.cost)
        with open(f"printer\\html\\receta_{self.file}.html", "w", encoding="utf-8") as test:
            test.write(content)
        print("created recipe on html")

    def htmlToPDF(self):
        html = os.path.abspath(f"printer\\html\\receta_{self.file}.html")
        pdf = f"C:\\Users\\{self.user}\\Documents\\Consultas\\{self.file}\\receta_{self.file}.pdf"
        print(pdf)
        edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
        command = [edge_path, "--headless", "--no-pdf-header-footer", "--disable-gpu", "--print-to-pdf", f"--print-to-pdf={pdf}", html]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        
    def openToPrint(self):
        path = f"C:\\Users\\{self.user}\\Documents\\Consultas\\{self.file}\\receta_{self.file}.pdf"
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