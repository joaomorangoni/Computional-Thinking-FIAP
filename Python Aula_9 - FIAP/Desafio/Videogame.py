class VideoGame:
    def __init__(self, modelo, lote, marca, memoria):
        self.modelo = modelo
        self.lote = lote
        self.marca = marca
        self.memoria = memoria

    def descrever(self):
        print(f"ATRIBUTOS:\nModelo: {self.modelo}\nMarca: {self.marca}\nMemória: {self.memoria}\nLote: {self.lote}\n")

play = VideoGame("Playstation 5", 1200, "Sony", "1 Terabyte")
play.descrever()