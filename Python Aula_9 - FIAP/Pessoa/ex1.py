class Pessoa:
    def __init__(self, nome, idade, peso, altura, sexo):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.sexo = sexo

    def descrever(self):
        print(f"ATRIBUTOS:\nNome: {self.nome}\nIdade: {self.idade}\nPeso: {self.peso}\nAltura: {self.altura}\nSexo: {self.sexo}\n")

    def envelhecer(self):
        self.idade += 1

    def comparar_idade(self, pessoa2):
        if self.idade < pessoa2.idade:
            print(f"{self.nome} é mais novo que {pessoa2.nome}")
        elif self.idade > pessoa2.idade:
            print(f"{self.nome} é mais velho que {pessoa2.nome}")
        else:
            print(f"{self.nome} tem a mesma idade que {pessoa2.nome}")
