class Veiculo:

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def info(self):
        print(f"INFORMAÇÕES\nMarca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}\n")
    
    def atualizar_ano(self):
        novo_ano = input("Digite o novo ano do veiculo: ")
        self.ano = novo_ano
        print("Ano atualizado!\n")

    def comparar(self, veiculo2):
        if self.ano > veiculo2.ano:
            print(f"o {veiculo2.marca} do modelo {veiculo2.modelo} é mais velho que o {self.marca} do modelo {self.modelo}")
        elif self.ano < veiculo2.ano:
            print(f"o {self.marca} do modelo {self.modelo} é mais velho que o {veiculo2.marca} do modelo {veiculo2.modelo}")
        else:
            print(f"Ambos os veículos são do mesmo ano!")
        
