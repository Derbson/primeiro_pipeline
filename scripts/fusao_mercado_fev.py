import json
import csv
from processamento_dados import Data

# buscando arquivos
path_json = '../data_raw/dados_empresaA.json'
path_csv = '../data_raw/dados_empresaB.csv'

dados_empresaA = Data(path_json, 'json')
dados_empresaB = Data(path_csv, 'csv')

# # ----------- mepear as chaves -----------
key_mapping = {
    'Nome do Item': 'Nome do Produto',
    'Classificação do Produto' :'Categoria do Produto',
    'Valor em Reais (R$)':'Preço do Produto (R$)',
    'Quantidade em Estoque':'Quantidade em Estoque',
    'Nome da Loja':'Filial',
    'Data da Venda':'Data da Venda'
}

dados_empresaB.rename_columns(key_mapping)
print(dados_empresaB.column_names)

# # -------------------- unido os dados -----------------------

joined_data = Data.join_data(dados_empresaA, dados_empresaB)

# print(f"quantidade de linhas dos arquivos juntos: {size_joined_data}")
print(joined_data.data[0])

# -------------  salvando os dados organizados em um arquivo .csv
path_joined_data = '../data_processed/dados_combinandos.csv'
joined_data.save_data(path_joined_data)

