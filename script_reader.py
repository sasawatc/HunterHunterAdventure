import csv


class ScriptReader:
    def __init__(self, csv_file):
        file = open(csv_file, newline='')
        self.reader = csv.reader(file, delimiter=',', quotechar='"')
        self.header = []
        self._init_header()

    def read_next(self):
        script = dict()
        for header, data in zip(self.header, next(self.reader)):
            script.update({header: data})
            # print("Script: ", script)
        return script

    def _init_header(self):
        self.header = next(self.reader)
