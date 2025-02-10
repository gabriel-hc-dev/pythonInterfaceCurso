class Retangulo:
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2

    def muda_valor(self, l1_novo, l2_novo):
        self.l1 = l1_novo
        self.l2 = l2_novo

    def retorna_lado(self):
        print(f'O retângulo possui dimensões {self.l1}m * {self.l2}m')
    
    def area(self):
        return self.l1 * self.l2