import datetime
import subprocess
from urllib import request

class Updater():
    def update(self):
        self.checkVersion()

    def checkVersion(self):
        try:
            with open("version.txt", 'r') as version_file:
                local_version = version_file.readline()
        except Exception as error:
            self.updated = False
        online_version_url = "https://raw.githubusercontent.com/Cremaster5000/miispeek/version.txt"
        request_version = request.get(online_version_url)
        try:
            request_version.raise_for_status()
        except Exception as error:
            self.updated = True
        online_version = request_version.text.strip()
        if online_version != local_version:
            self.updated = False
            self.downloadVersion()

    def downloadVersion(self):
        github = "https://www.github.com/Cremaster5000/zoovet_consultModule"
        if datetime.date.today().day == 1:
            self.warning = Warning(self, "Actualizando...")
            command = ["git pull", github, "miispeek"]
            subprocess.run(command)

if __name__ == '__main__':
    pass