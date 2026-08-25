import json

caminho_arquivo = 'dados.json'

with open(caminho_arquivo, 'r') as arquivo_json:
    dados = json.load(arquivo_json)

for pessoa in dados['pessoas']:
    nome = pessoa['nomes']
    idade = pessoa['Idade']
    profissao = pessoa['profissao']
    cidade = pessoa['cidade']
    pais = pessoa['pais']

    print(f"Nome: {nome}, Idade: {idade}, Profissão: {profissao}, Cidade: {cidade}, Pais: {pais}")