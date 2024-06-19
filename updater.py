import subprocess
from urllib import request

class Updater():
    def __init__(self, main):
        self.updated = True 
        self.main = main 

    def update(self):
        self.checkVersion()

    def checkVersion(self):
        try:
            with open("version.txt", 'r') as version_file:
                local_version = version_file.readline()
            online_version_url = "https://raw.githubusercontent.com/Cremaster5000/zoovet_consultModule/miispeek/version.txt"
            with request.urlopen(online_version_url) as response:
                online_version = response.read().decode('utf-8')
            if online_version != local_version:
                self.updated = False
                self.downloadVersion()
        except Exception as error:
            print("error: ", error)

    def downloadVersion(self):
        try:
            github = "https://www.github.com/Cremaster5000/zoovet_consultModule"
            self.warning = Warning_Update(self.main, "Actualizando...")
            command = ["git pull", github, "miispeek"]
            subprocess.run(command)
        except Exception as error:
            self.updated = False 
            print("Error: ", error)

    def isUpdate(self):
        return self.updated

class Warning_Update(Warning):
    def __init__(self, main, info:str):
       super().__init__(main, info)
       self.data = info
       self.main = main 
       self.butonOk.setDisabled(True)

    def updated(self):
        self.data.setText("Reinicia la aplicación")
        self.butonOk.setEnable(True)
        self.butonOk.setText("Cerrar")

    def ok(self):
        self.main.close()

if __name__ == '__main__':
    pass