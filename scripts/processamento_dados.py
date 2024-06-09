import json
import csv

class Data:
    def __init__(self, path, data_type):
        self.path = path
        self.data_type = data_type
        self.data = self.data_reader()

    def reader_json(self):
        data_json = []
        with open(self.path, 'r') as file:
            data_json = json.load(file)
        return data_json

    def reader_csv(self):
        data_csv = []
        with open(self.path, 'r') as file:
            # spamreader = csv.reader(file, delimiter=',')   # csv.reader criaria uma lista de listas
            spamreader = csv.DictReader(file, delimiter=',') # csv.DictReader para retorno o conteúdo do arquivo como uma lista de dicionários
            for row in spamreader:
                data_csv.append(row)

        return data_csv

    def data_reader(self):
        data = []

        if self.data_type == 'csv':
            data = self.reader_csv()
        
        elif self.data_type == 'json':
            data = self.reader_json()

        return data




