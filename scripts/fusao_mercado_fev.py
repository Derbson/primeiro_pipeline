import json
import csv


def leitura_json(path_json):
    dados_json = []
    with open(path_json, 'r') as file:
        dados_json = json.load(file)
    return dados_json

def leitura_csv(path_csv):
    dados_csv = []
    with open(path_csv, 'r') as file:
        # spamreader = csv.reader(file, delimiter=',')   # csv.reader criaria uma lista de listas
        spamreader = csv.DictReader(file, delimiter=',') # csv.DictReader para retorno o conteúdo do arquivo como uma lista de dicionários
        for row in spamreader:
            dados_csv.append(row)

    return dados_csv

path_json = '../data_raw/dados_empresaA.json'
path_csv = '../data_raw/dados_empresaB.csv'

dados_json = leitura_json(path_json)
dados_csv = leitura_csv(path_csv)
