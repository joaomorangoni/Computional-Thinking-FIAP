from ex01 import Veiculo

carro = Veiculo("Ford", "Focus", 2020)
carro2 = Veiculo("Fiat", "Uno", 1990)
carro3 = Veiculo("Ford", "GT", 2024)
carro4 = Veiculo("BMW", "M4", 2025)
carro5 = Veiculo("Porsche", "911 Carrera", 2026)

veiculos = [carro, carro2, carro3, carro4, carro5]

for i in veiculos:
    i.info()