class Pessoa:
    "Isto é uma classe Pessoa"
    idade = 17

    def saudacao(self):
        print("Olá Pessoas")

gabriel = Pessoa()

print(gabriel.idade)

print(gabriel.saudacao)

gabriel.saudacao()