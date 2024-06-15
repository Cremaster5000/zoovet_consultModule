""" # -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader 
import os
import subprocess
 

path_wkhtmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
slash = '\\'

# css_path = os.path.abspath("printer\\templates\\style_consult_report.css")
# print(css_path)
# html_path = os.path.abspath("printer\\templates\\template_consult_report.html")
# pdf_path = os.path.abspath("printer\\reports\\test.pdf")
# command = [path_wkhtmltopdf, "--enable-local-file-access", html_path, pdf_path]

# """
# environment = Environment(loader=FileSystemLoader(f"printer\\templates\\"))
# template = environment.get_template("template_consult_report.html")        
# content = template.render(date = "hoy", css_path=css_path)
# with open(f"printer\\reports\\test.html", "w", encoding="utf-8") as test:
#     test.write(content)
# print("created report html")
# """
# result = subprocess.run(command, capture_output=True, text=True)

# print("Salida: ",result.stdout)
# print("Error: ", result.stdout)
# print("Code: ", result.returncode)
# os.startfile(pdf_path)"""

"""import os
import subprocess
html_file = os.path.abspath("printer\\templates\\test.html")
edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
command = [edge_path, "--headless", "--disable-gpu", "--print-to-pdf", f"--print-to-pdf={html_file.replace('html', 'pdf')}", html_file]
result = subprocess.run(command, capture_output=True, text=True, check=True)
print("resultado: ",result.stdout)
print("error: ", result.stderr)
print("returncode: ", result.returncode)"""
import win32print 
import subprocess

printer = win32print.
command = ["print", printer, "C:\\Users\\mirmo\\Documents\\Consultas\\akane.pdf"]
subprocess.run(command)