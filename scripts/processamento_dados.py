import json
import csv

class Data:
    def __init__(self, path, data_type):
        self.path = path
        self.data_type = data_type
        self.data = self.data_reader()
        self.column_names = self.get_header()
        self.qtd_linhas = self.size_data()

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
        
        elif self.data_type == 'list':
            data = self.path
            self.path = 'lista em memoria'
        return data

    def get_header(self):
        return  list(self.data[0].keys())
    
    def rename_columns(self,key_mapping):
        new_data_csv = []

        for old_dict in self.data:
            dict_temp = {}
            for old_key, value in old_dict.items():
                dict_temp[key_mapping[old_key]] = value
            new_data_csv.append(dict_temp)

        self.data = new_data_csv
        self.column_names = self.get_header()
    
    def size_data(self):
        return len(self.data)
    
    def join_data(dataA, dataB):
        combined_list = []
        combined_list.extend(dataA.data)
        combined_list.extend(dataB.data)
        return Data(combined_list, 'list')

    def transformando_dados_tabela(self):
        dados_combinados_tabela = [self.column_names]

        for row in self.data:
            linha = []
            for coluna in self.column_names:
                linha.append(row.get(coluna, 'Indisponível'))
            dados_combinados_tabela.append(linha)
        return dados_combinados_tabela
    
    def save_data(self, path):

        combined_data_table = self.transformando_dados_tabela()

        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(combined_data_table)


