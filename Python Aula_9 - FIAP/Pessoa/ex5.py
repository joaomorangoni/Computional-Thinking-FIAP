from ex4 import Pessoa

Pessoa1 = Pessoa("João", 18, 57, 1.75, "Masculino")
Pessoa2 = Pessoa("Maria", 17, 55, 1.70, "Feminino")
Pessoa3 = Pessoa("Douglas", 21, 78, 1.82, "Masculino")
Pessoa4 = Pessoa("Flávia", 19, 58, 1.72, "Feminino")
Pessoa5 = Pessoa("Mario", 15, 50, 1.68, "Masculino")

Pessoas = [Pessoa1, Pessoa2, Pessoa3, Pessoa4, Pessoa5]

for i in Pessoas:
    i.descrever()