# -*- coding: utf-8 -*-
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from consult_view import Consult_View
from warning import Warning
import sys


class first_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.show()
        
    def setupUi(self):
        self.resize(250, 400)
        self.setMaximumSize(250, 400)
        self.setWindowTitle("Información básica")
        self.centralwidget = QWidget(self)
        
        self.create_button = QPushButton("Crear", self.centralwidget)
        self.create_button.setGeometry(QRect(140, 350, 89, 25))
        self.create_button.clicked.connect(self.create)
        
        self.cancel_button = QPushButton("Cancelar", self.centralwidget)
        self.cancel_button.setGeometry(QRect(30, 350, 89, 25))
        self.cancel_button.clicked.connect(self.cancel)
        
        self.widget = QWidget(self.centralwidget)
        self.widget.setGeometry(QRect(20, 10, 210, 250))
        
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout_7 = QFormLayout()
        self.label_name = QLabel("Nombre:",self.widget)
        self.formLayout_7.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_name)
        self.edit_name = QLineEdit(self.widget)
        self.formLayout_7.setWidget(0, QFormLayout.ItemRole.FieldRole, self.edit_name)
        self.verticalLayout.addLayout(self.formLayout_7)
        
        self.combobox_type_consult = QComboBox(self.widget)
        self.combobox_type_consult.addItem("Consulta general")
        self.combobox_type_consult.addItem("Cita control")
        self.combobox_type_consult.addItem("Entrega de resultados")
        self.combobox_type_consult.addItem("Otro")
        self.widget2 = QWidget(self)
        self.formLayout_8 = QFormLayout(self.widget2)
        self.widget2.setGeometry(QRect(20, 285, 200, 40))
        self.formLayout_8.setContentsMargins(0, 0, 0, 0)
        self.formLayout_8.setWidget(0, QFormLayout.ItemRole.FieldRole, self.combobox_type_consult)
        
        self.formLayout_6 = QFormLayout()
        self.label_owner = QLabel("Familia:",self.widget)
        

        self.formLayout_6.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_owner)

        self.edit_owner = QLineEdit(self.widget)

        self.formLayout_6.setWidget(0, QFormLayout.ItemRole.FieldRole, self.edit_owner)


        self.verticalLayout.addLayout(self.formLayout_6)

        self.formLayout_5 = QFormLayout()
        self.label_sex = QLabel("Sexo:", self.widget)

        self.formLayout_5.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_sex)

        self.edit_sex = QComboBox(self.widget)
        self.edit_sex.addItem("Hembra")
        self.edit_sex.addItem("Macho")

        self.formLayout_5.setWidget(0, QFormLayout.ItemRole.FieldRole, self.edit_sex)


        self.verticalLayout.addLayout(self.formLayout_5)

        self.formLayout_4 = QFormLayout()
        self.label_weight = QLabel("Peso:", self.widget)

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_weight)

        self.edit_weight = QLineEdit(self.widget)

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.FieldRole, self.edit_weight)


        self.verticalLayout.addLayout(self.formLayout_4)

        self.formLayout_3 = QFormLayout()
        self.label_castrated = QLabel("Esterilizado:", self.widget)

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_castrated)

        self.edit_castrated = QComboBox(self.widget)
        self.edit_castrated.addItem("Entero/a")
        self.edit_castrated.addItem("Esterilizado/a")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.edit_castrated)


        self.verticalLayout.addLayout(self.formLayout_3)

        self.formLayout_2 = QFormLayout()
        self.label_breed = QLabel("Raza:", self.widget)
        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_breed)
        self.edit_breed = QLineEdit(self.widget)
        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.edit_breed)
        
        self.label_species = QLabel("Especie:", self.widget)
        self.edit_species = QComboBox(self.widget)
        self.edit_species.addItem("Canino")
        self.edit_species.addItem("Felino")
        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_species)
        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.edit_species)

        self.verticalLayout.addLayout(self.formLayout_2)

        self.formLayout = QFormLayout()
        self.label_age = QLabel("Edad:", self.widget)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_age)

        self.edit_age = QLineEdit(self.widget)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.edit_age)


        self.verticalLayout.addLayout(self.formLayout)

        self.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(self)
        self.menubar.setGeometry(QRect(0, 0, 240, 22))
        self.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(self)
        self.setStatusBar(self.statusbar)




    def cancel(self):
        self.close()

    def create(self):
        if self.edit_name.text() == "" or self.edit_owner.text() == "":
            self.warning = Warning(self, "Inserte nombre y propietario")
        else:
            self.new_consult = Consult_View(self.package_info())
            self.close()
        
    def package_info(self):
        info = [
            self.edit_name.text(),
            self.edit_owner.text(),
            self.edit_sex.currentText(),
            self.edit_age.text(),
            self.edit_species.currentText(),
            self.edit_breed.text(),
            self.edit_castrated.currentText(),
            self.edit_weight.text(),
            self.combobox_type_consult.currentText()
        ]
        return info

if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = first_window()
    sys.exit(app.exec())
