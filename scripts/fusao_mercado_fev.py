import json
import csv
from processamento_dados import Data


# def reader_json(path_json):
#     data_json = []
#     with open(path_json, 'r') as file:
#         data_json = json.load(file)
#     return data_json

# def reader_csv(path_csv):
#     data_csv = []
#     with open(path_csv, 'r') as file:
#         # spamreader = csv.reader(file, delimiter=',')   # csv.reader criaria uma lista de listas
#         spamreader = csv.DictReader(file, delimiter=',') # csv.DictReader para retorno o conteúdo do arquivo como uma lista de dicionários
#         for row in spamreader:
#             data_csv.append(row)

#     return data_csv

def get_header(data):
    header = list(data[0].keys())
    return header

def rename_columns(data,key_mapping):
    new_data_csv = []

    for old_dict in data:
        dict_temp = {}
        for old_key, value in old_dict.items():
            dict_temp[key_mapping[old_key]] = value
        new_data_csv.append(dict_temp)

    return new_data_csv

def join_data(dataA, dataB):
    combined_list = []
    combined_list.extend(dataA)
    combined_list.extend(dataB)
    return combined_list

def size_data(data):
    return len(data)

path_json = '../data_raw/dados_empresaA.json'
path_csv = '../data_raw/dados_empresaB.csv'

dados_empresaA = Data(path_json, 'json')
dados_empresaB = Data(path_csv, 'csv')
print(dados_empresaA.data[0])
print(dados_empresaB.data[0])

# lendo os 2 arquivos e retornando como lista de dicionários
# data_json = reader_json(path_json)
# data_csv = reader_csv(path_csv)

# # tamanho dos arquivos
# size_data_json = size_data(data_json)
# size_data_csv = size_data(data_csv)

# print(f"quantidade de linhas empresaA {size_data_json}")
# print(f"quantidade de linhas empresaB {size_data_csv}")


# # mepear as chaves
# header_json = get_header(data_json)
# header_csv = get_header(data_csv)

# key_mapping = {
#     'Nome do Item': 'Nome do Produto',
#     'Classificação do Produto' :'Categoria do Produto',
#     'Valor em Reais (R$)':'Preço do Produto (R$)',
#     'Quantidade em Estoque':'Quantidade em Estoque',
#     'Nome da Loja':'Filial',
#     'Data da Venda':'Data da Venda'
# }

# data_csv = rename_columns(data_csv, key_mapping)
# column_names_csv = get_header(data_csv)

# # unido os dados 
# joined_data = join_data(data_json,data_csv)
# size_joined_data = size_data(joined_data)

# print(f"quantidade de linhas dos arquivos juntos: {size_joined_data}")

# print(joined_data[-1])