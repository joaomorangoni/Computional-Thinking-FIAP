import csv

caminho_arquivo = 'exemplo.csv'

with open(caminho_arquivo, mode='r', newline='', encoding='utf-8') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)

    matriz = list(leitor_csv)
    linhas = len(matriz)
    colunas = len(matriz[0])

    print(f"linhas: {linhas}, Colunas: {colunas}")

    for i in range(0,linhas):
        for j in range(0, colunas):
            print(f"| {matriz[i][j]} |", end="")
        print()