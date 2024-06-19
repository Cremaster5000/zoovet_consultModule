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
            print("checkVersion entered")
            with open("version.txt", 'r') as version_file:
                local_version = version_file.readline()
            print("local version: ",local_version)
            online_version_url = "https://raw.githubusercontent.com/Cremaster5000/zoovet_consultModule/miispeek/version.txt"
            with request.urlopen(online_version_url) as response:
                online_version = response.read().decode('utf-8')
            print("online version: ", online_version)
            if online_version != local_version:
                self.updated = False
                self.downloadVersion()
        except Exception as error:
            print("error: ", error)

    def downloadVersion(self):
        print("entered to download version")
        try:
            github = "https://www.github.com/Cremaster5000/zoovet_consultModule"
            self.warning = Warning_Update(self.main, "Actualizando...")
            git_path = "C:\\Program Files\\Git\\cmd\\git.exe"
            command = [git_path, "pull", github, "miispeek"]
            print("ejecutando comando...", command)
            process = subprocess.run(command, capture_output=True, shell=True)
            print(process.stderr, process.stdout, process.returncode)
        except Exception as error:
            self.updated = False 
            print("Error en updater: ", error)

    def isUpdate(self):
        return self.updated

class Warning_Update(Warning):
    def __init__(self, main, info:str):
       super().__init__(main, info)
       print("created warning update")
       self.data = info
       self.main = main 

    def createWindow(self):
        super().createWindow()
        print("created window warning update", self.data)
        super().butonOk.setDisabled(True)

    def updated(self):
        self.data.setText("Reinicia la aplicación")
        self.butonOk.setEnable(True)
        self.butonOk.setText("Cerrar")

    def ok(self):
        self.main.close()

if __name__ == '__main__':
    pass