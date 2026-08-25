import csv

caminho_arquivo = 'novo_exemplo.csv'

dados = [
    ['Nome', 'Idade', 'Profissão', 'Cidade', 'Paris'],
    ['João', '30', 'Engenheiro', 'São Paulo', 'Brasil'],
    ['Maria', '25', 'Médico', 'Lisboa', 'Portual'],
    ['Carlos', '40', 'Professor', 'Madrid', 'Espanha'],
    ['Ana', '35', 'Arquiteta', 'Paris', 'França'],
    ['Renato', '37', 'garoto de programa', 'Recife', 'Pernambuco']
]

with open(caminho_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)

    for linha in dados:
        escritor_csv.writerow(linha)
print(f"Arquivo: '{caminho_arquivo}' criado com sucesso.")