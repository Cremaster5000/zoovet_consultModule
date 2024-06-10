
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import datetime

import sys
from consult import Consult
from printer.consult_report import Consult_report
from printer.recipe import Recipe


class Consult_View(QMainWindow):
    
    def __init__(self, info):
        super().__init__()
        self.time_creation = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        self.setupUi(info)
        self.show()
        self.owner = info[1]

    def setupUi(self, info):
        self.type_consult = info[8]
        
        self.setGeometry(QRect(0,0,639,650))
        #self.setMaximumSize(639, 650)
        self.setWindowTitle("Consulta")
        self.centralwidget = QWidget(self)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QRect(0, 0, 637, 648))    
        self.EFG = QWidget()
        self.widget = QWidget(self.EFG)
        self.widget.setGeometry(QRect(40, 420, 571, 171))
        self.formLayout_17 = QFormLayout(self.widget)
        self.formLayout_17.setContentsMargins(0, 0, 0, 35)

        self.label_12 = QLabel("Anamnesis:", self.widget)

        self.formLayout_17.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_12)

        self.edit_anamnesis = QTextEdit(self.widget)

        self.formLayout_17.setWidget(1, QFormLayout.ItemRole.SpanningRole, self.edit_anamnesis)

        self.widget1 = QWidget(self.EFG)
        self.widget1.setGeometry(QRect(50, 20, 201, 19))
        self.formLayout = QFormLayout(self.widget1)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_pacient = QLabel(self.widget1)
        self.label = QLabel("Paciente:", self.widget1)
        self.label_patient = QLabel(info[0], self.widget1)
        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)
        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.label_patient)


        self.widget2 = QWidget(self.EFG)
        self.widget2.setGeometry(QRect(460, 20, 191, 19))
        self.formLayout_2 = QFormLayout(self.widget2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_date = QLabel("Fecha:", self.widget2)
        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_date)
        self.date = QLabel(datetime.datetime.today().strftime("%d/%m/%Y %H:%M"), self.widget2)
        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.date)


        self.widget26 = QWidget(self.EFG)
        self.widget26.setGeometry(QRect(180, 20, 90, 19))
        self.formlayout_27 = QFormLayout(self.widget26)
        self.formlayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_weight = QLabel("Peso:", self.widget26)
        self.weight = QLabel(info[7], self.widget26)
        self.formlayout_27.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_weight)
        self.formlayout_27.setWidget(0, QFormLayout.ItemRole.FieldRole, self.weight)


        self.widget3 = QWidget(self.EFG)
        self.widget3.setGeometry(QRect(50, 90, 91, 27))
        self.formLayout_3 = QFormLayout(self.widget3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel("FC:", self.widget3)

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.edit_fc = QLineEdit(self.widget3)

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.edit_fc)
        
        self.widget28 = QWidget(self.EFG)
        self.widget28.setGeometry(QRect(160, 90, 100, 27))
        self.formlayout_29 = QFormLayout(self.widget28)
        self.formlayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel("CC:", self.widget28)
        self.edit_cc = QComboBox(self.widget28)
        self.edit_cc.addItem("1/5")
        self.edit_cc.addItem("2/5")
        self.edit_cc.addItem("3/5")
        self.edit_cc.addItem("4/5")
        self.edit_cc.addItem("5/5")
        self.formlayout_29.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_28)
        self.formlayout_29.setWidget(0, QFormLayout.ItemRole.FieldRole, self.edit_cc)

        self.widget4 = QWidget(self.EFG)
        self.widget4.setGeometry(QRect(280, 90, 101, 27))
        self.formLayout_4 = QFormLayout(self.widget4)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel("FR:", self.widget4)

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.edit_fr = QLineEdit(self.widget4)

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.FieldRole, self.edit_fr)

        self.widget5 = QWidget(self.EFG)
        self.widget5.setGeometry(QRect(290, 130, 121, 27))
        self.formLayout_5 = QFormLayout(self.widget5)
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel("RT:", self.widget5)

        self.formLayout_5.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.combobox_rt = QComboBox(self.widget5)
        self.combobox_rt.addItem("Positivo")
        self.combobox_rt.addItem("Negativo")

        self.formLayout_5.setWidget(0, QFormLayout.ItemRole.FieldRole, self.combobox_rt)

        self.widget6 = QWidget(self.EFG)
        self.widget6.setGeometry(QRect(460, 90, 111, 27))
        self.formLayout_6 = QFormLayout(self.widget6)
        self.formLayout_6.setContentsMargins(0, 0, 0, 0)
        self.edit_tc = QLineEdit(self.widget6)

        self.formLayout_6.setWidget(0, QFormLayout.ItemRole.FieldRole, self.edit_tc)

        self.label_5 = QLabel("TC:", self.widget6)

        self.formLayout_6.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.widget7 = QWidget(self.EFG)
        self.widget7.setGeometry(QRect(470, 130, 124, 27))
        self.formLayout_7 = QFormLayout(self.widget7)
        self.formLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel("RD:", self.widget7)

        self.formLayout_7.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.combobox_rd = QComboBox(self.widget7)
        self.combobox_rd.addItem("Positivo")
        self.combobox_rd.addItem("Negativo")

        self.formLayout_7.setWidget(0, QFormLayout.ItemRole.FieldRole, self.combobox_rd)

        self.widget8 = QWidget(self.EFG)
        self.widget8.setGeometry(QRect(50, 130, 210, 27))
        self.formLayout_8 = QFormLayout(self.widget8)
        self.formLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel("Edo. Mental:", self.widget8)

        self.formLayout_8.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_14)

        self.combobox_emental = QComboBox(self.widget8)
        self.combobox_emental.adjustSize()
        self.combobox_emental.addItem("Alerta")
        self.combobox_emental.addItem("Comatoso")
        self.combobox_emental.addItem("Estupor")
        self.combobox_emental.addItem("Desorientado")
        self.combobox_emental.addItem("Deprimido")
        self.combobox_emental.addItem("Exitado")

        self.formLayout_8.setWidget(0, QFormLayout.ItemRole.FieldRole, self.combobox_emental)

        self.widget9 = QWidget(self.EFG)
        self.widget9.setGeometry(QRect(40, 190, 281, 27))
        self.formLayout_9 = QFormLayout(self.widget9)
        self.formLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel("Auscultación cardiaca:", self.widget9)

        self.formLayout_9.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.combobox_ac = QComboBox(self.widget9)
        self.combobox_ac.addItem("Normal")
        self.combobox_ac.addItem("Soplo")
        self.combobox_ac.addItem("Arritmia")
        self.combobox_ac.addItem("Bradicardia")
        self.combobox_ac.addItem("Taquicardia")

        self.formLayout_9.setWidget(0, QFormLayout.ItemRole.FieldRole, self.combobox_ac)

        self.widget10 = QWidget(self.EFG)
        self.widget10.setGeometry(QRect(360, 190, 251, 27))
        self.formLayout_10 = QFormLayout(self.widget10)
        self.formLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel("Linfonodos:", self.widget10)

        self.formLayout_10.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_10)

        self.edit_linfo = QLineEdit(self.widget10)

        self.formLayout_10.setWidget(0, QFormLayout.ItemRole.FieldRole, self.edit_linfo)

        self.widget11 = QWidget(self.EFG)
        self.widget11.setGeometry(QRect(40, 240, 270, 27))
        self.formLayout_11 = QFormLayout(self.widget11)
        self.formLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel("Auscultación pulmonar:", self.widget11)

        self.formLayout_11.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_9)

        self.combobox_ap = QComboBox(self.widget11)
        self.combobox_ap.addItem("Normal")
        self.combobox_ap.addItem("Reducido")
        self.combobox_ap.addItem("Liquido")
        self.combobox_ap.addItem("Sibilancias")
        self.combobox_ap.addItem("Estertor")
        self.combobox_ap.addItem("Estridor")
        self.combobox_ap.addItem("Roncus")


        self.formLayout_11.setWidget(0, QFormLayout.ItemRole.FieldRole, self.combobox_ap)

        self.widget12 = QWidget(self.EFG)
        self.widget12.setGeometry(QRect(340, 240, 276, 27))
        self.formLayout_12 = QFormLayout(self.widget12)
        self.formLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel("Palpación abdominal:", self.widget12)

        self.formLayout_12.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_11)

        self.combobox_palpation = QComboBox(self.widget12)
        self.combobox_palpation.addItem("Sin dolor")
        self.combobox_palpation.addItem("Dolor")
        self.combobox_palpation.addItem("Gas")
        self.combobox_palpation.addItem("Gas con dolor")
        self.combobox_palpation.addItem("Líquido")
        self.combobox_palpation.addItem("Ocupado")

        self.formLayout_12.setWidget(0, QFormLayout.ItemRole.FieldRole, self.combobox_palpation)

        self.widget13 = QWidget(self.EFG)
        self.widget13.setGeometry(QRect(340, 20, 111, 19))
        self.formLayout_13 = QFormLayout(self.widget13)
        self.formLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel("Sexo:", self.widget13)

        self.formLayout_13.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_16)

        self.label_sex = QLabel(info[2],self.widget13)

        self.formLayout_13.setWidget(0, QFormLayout.ItemRole.FieldRole, self.label_sex)

        self.widget14 = QWidget(self.EFG)
        self.widget14.setGeometry(QRect(50, 50, 111, 19))
        self.formLayout_14 = QFormLayout(self.widget14)
        self.formLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel("Edad:", self.widget14)

        self.formLayout_14.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_15)

        self.label_age = QLabel(info[3],self.widget14)
        self.formLayout_14.setWidget(0, QFormLayout.ItemRole.FieldRole, self.label_age)

        self.widget29 = QWidget(self.EFG)
        self.widget29.setGeometry(QRect(200, 50, 138, 19))
        self.formLayout_30 = QFormLayout(self.widget29)
        self.formLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_29 = QLabel("Especie:", self.widget29)
        self.species = QLabel(info[4], self.widget29)
        self.formLayout_30.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_29)
        self.formLayout_30.setWidget(0, QFormLayout.ItemRole.FieldRole, self.species)
        
        self.widget15 = QWidget(self.EFG)
        self.widget15.setGeometry(QRect(330, 50, 131, 19))
        self.formLayout_15 = QFormLayout(self.widget15)
        self.formLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel("Raza:", self.widget15)

        self.formLayout_15.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_17)

        self.label_breed = QLabel(info[4], self.widget15)

        self.formLayout_15.setWidget(0, QFormLayout.ItemRole.FieldRole, self.label_breed)

        self.widget16 = QWidget(self.EFG)
        self.widget16.setGeometry(QRect(40, 300, 571, 101))
        self.formLayout_16 = QFormLayout(self.widget16)
        self.formLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel("Historia clínica:", self.widget16)

        self.formLayout_16.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_13)

        self.edit_history = QTextEdit(self.widget16)

        self.formLayout_16.setWidget(1, QFormLayout.ItemRole.SpanningRole, self.edit_history)

        self.widget17 = QWidget(self.EFG)
        self.widget17.setGeometry(QRect(450, 50, 200, 19))
        self.formLayout_26 = QFormLayout(self.widget17)
        self.formLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel("Esterilizado:", self.widget17)

        self.formLayout_26.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_26)

        self.label_castrated = QLabel(info[6], self.widget17)

        self.formLayout_26.setWidget(0, QFormLayout.ItemRole.FieldRole, self.label_castrated)

        self.tabWidget.addTab(self.EFG, "EFG")
        self.DX = QWidget()
        
        self.buton_print = QPushButton("Imprimir receta", self.DX)
        self.buton_print.setGeometry(QRect(500, 540, 113, 25))
        self.buton_print.clicked.connect(self.printPrescription)
        self.buton_cancel = QPushButton("Cancelar", self.DX)
        self.buton_cancel.setGeometry(QRect(50, 540, 89, 25))
        self.buton_cancel.clicked.connect(self.cancel)
        self.buton_save = QPushButton("Guardar", self.DX)
        self.buton_save.setGeometry(QRect(195, 540, 89, 25))
        self.buton_save.clicked.connect(self.saveData)
        self.buton_report = QPushButton("Reporte", self.DX)
        self.buton_report.setGeometry(QRect(350, 540, 93, 25))
        self.buton_report.clicked.connect(self.report)
        self.widget18 = QWidget(self.DX)
        self.widget18.setGeometry(QRect(370, 100, 241, 27))
        self.formLayout_18 = QFormLayout(self.widget18)
        self.formLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel("Laboratorio:", self.widget18)

        self.formLayout_18.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_21)

        self.editlaboratory = QLineEdit(self.widget18)

        self.formLayout_18.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editlaboratory)

        self.widget19 = QWidget(self.DX)
        self.widget19.setGeometry(QRect(40, 150, 271, 121))
        self.formLayout_19 = QFormLayout(self.widget19)
        self.formLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel("Diagnostico:", self.widget19)

        self.formLayout_19.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_22)

        self.edit_diferencial = QTextEdit(self.widget19)

        self.formLayout_19.setWidget(1, QFormLayout.ItemRole.SpanningRole, self.edit_diferencial)

        self.widget20 = QWidget(self.DX)
        self.widget20.setGeometry(QRect(370, 40, 241, 27))
        self.formLayout_20 = QFormLayout(self.widget20)
        self.formLayout_20.setContentsMargins(0, 0, 0, 0)
        self.edit_samples = QLineEdit(self.widget20)

        self.formLayout_20.setWidget(0, QFormLayout.ItemRole.FieldRole, self.edit_samples)

        self.label_20 = QLabel("Muestras:", self.widget20)

        self.formLayout_20.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_20)

        self.widget21 = QWidget(self.DX)
        self.widget21.setGeometry(QRect(40, 100, 231, 27))
        self.formLayout_21 = QFormLayout(self.widget21)
        self.formLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel("Lesiones:", self.widget21)

        self.formLayout_21.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_19)

        self.edit_wound = QLineEdit(self.widget21)

        self.formLayout_21.setWidget(0, QFormLayout.ItemRole.FieldRole, self.edit_wound)

        self.widget22 = QWidget(self.DX)
        self.widget22.setGeometry(QRect(40, 40, 201, 27))
        self.formLayout_22 = QFormLayout(self.widget22)
        self.formLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel("Copro:", self.widget22)

        self.formLayout_22.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_18)

        self.edit_copro = QLineEdit(self.widget22)

        self.formLayout_22.setWidget(0, QFormLayout.ItemRole.FieldRole, self.edit_copro)

        self.widget23 = QWidget(self.DX)
        self.widget23.setGeometry(QRect(350, 150, 264, 121))
        self.formLayout_23 = QFormLayout(self.widget23)
        self.formLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel("Notas:", self.widget23)

        self.formLayout_23.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_23)

        self.edit_notes = QTextEdit(self.widget23)

        self.formLayout_23.setWidget(1, QFormLayout.ItemRole.LabelRole, self.edit_notes)

        self.widget24 = QWidget(self.DX)
        self.widget24.setGeometry(QRect(150, 310, 197, 28))
        self.formLayout_24 = QFormLayout(self.widget24)
        
        self.widget27 = QWidget(self.DX)
        self.widget27.setGeometry(QRect(400, 310, 197, 28))
        self.formLayout_28 = QFormLayout(self.widget27)
        self.formLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel("Motivo:", self.widget27)
        self.edit_next_visit = QLineEdit(self.widget27)
        self.formLayout_28.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_27)
        self.formLayout_28.setWidget(0, QFormLayout.ItemRole.FieldRole, self.edit_next_visit)
        
        self.formLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel("Próxima visita:")

        self.next_visit = QDateEdit(self.widget24)
        self.next_visit.setDate(QDate.currentDate())
        self.next_visit.setCalendarPopup(True)
        
        self.formLayout_24.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_25)
        self.formLayout_24.setWidget(0, QFormLayout.ItemRole.FieldRole, self.next_visit)
        


        self.widget25 = QWidget(self.DX)
        self.widget25.setGeometry(QRect(40, 318, 571, 198))
        self.formLayout_25 = QFormLayout(self.widget25)
        self.formLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_24 = QLabel("Tratamiento", self.widget25)

        self.formLayout_25.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_24)

        self.edit_Tx = QTextEdit(self.widget25)

        self.formLayout_25.setWidget(1, QFormLayout.ItemRole.SpanningRole, self.edit_Tx)

        self.tabWidget.addTab(self.DX, "DX")
        self.setCentralWidget(self.centralwidget)
        self.tabWidget.raise_()
        self.label_7.raise_()
        self.combobox_rd.raise_()
        self.statusbar = QStatusBar(self)
        self.setStatusBar(self.statusbar)

        self.tabWidget.setCurrentIndex(0)

    def saveData(self):
        print("save pressed")
        self.consult = Consult(self.packageData())
        self.file = self.consult.saveConsult()
        self.warning = Warning(self, "Consulta guardada")
        return self.file

    def cancel(self):
        self.close()
        

    def packageData(self):
        data = {
                "date":self.date.text().replace("/","-").replace(" ", "_"),
                "type":self.type_consult,
                "patient":self.label_patient.text(),
                "owner": self.owner,
                "age":self.label_age.text(),
                "weight": self.weight.text(),
                "cc": self.edit_cc.currentText(),
                "sex": self.label_sex.text(),
                "species": self.species.text(),
                "breed": self.label_breed.text(),
                "castrated": self.label_castrated.text(),
                "anamnesis": self.edit_anamnesis.toPlainText(),
                "fc":self.edit_fc.text(),
                "fr": self.edit_fr.text(),
                "tc": self.edit_tc.text(),
                "rt": self.combobox_rt.currentText(),
                "rd": self.combobox_rd.currentText(),
                "mental": self.combobox_emental.currentText(),
                "auscCardiac": self.combobox_ac.currentText(),
                "linfonode": self.edit_linfo.text(),
                "auscPulm": self.combobox_ap.currentText(),
                "abdPalpat": self.combobox_palpation.currentText(),
                "clinicHistory": self.edit_history.toPlainText(),
                "laboratory": self.editlaboratory.text(),
                "dx": self.edit_diferencial.toPlainText(),
                "samples": self.edit_samples.text(),
                "wound": self.edit_wound.text(),
                "copro": self.edit_copro.text(),
                "notes": self.edit_notes.toPlainText(),
                "nextVisit": self.next_visit.date().toPyDate().strftime("%d-%m-%Y"),
                "motive": self.edit_next_visit.text(),
                "tx": self.edit_Tx.toPlainText()
                }
        return data

    def printPrescription(self):
        filename = self.saveData()
        recipe = Recipe(filename)
        recipe.printRecipe()
        
        
    def report(self):
        filename = self.saveData()        
        report = Consult_report(filename)
        report.printReport()
    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    now = datetime.datetime.now()
    test = Consult_View(["Akane", "Tellez", "macho", "4 meses", "mex. domestico", "castrado", "2kg"])
    sys.exit(app.exec())

