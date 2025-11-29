import os
from datetime import datetime


class fileLogger:
    def __init__(self, file_path):
        self.file_path = file_path
        path = os.path.dirname(self.file_path)
        print(path)
        if path != "" and not os.path.exists(path):
            os.makedirs(path)

    def log(self, message):
        tm= datetime.now().isoformat()
        message = tm +":  "+ message
        with open(self.file_path, "a") as f:
            f.write(message+ "\n")

    def read(self):
        with open(self.file_path, "r") as f:
            return f.read()

fl =fileLogger(file_path="log//a.log")
fl.log("hello world L")
print(fl.read())