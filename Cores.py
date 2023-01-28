class Cor:
    def __init__(self, tipo):
        self.tipo = tipo

    def cor(self):
        if self.tipo == 'Vermelho':
            return '\033[31m'
        elif self.tipo == 'Verde':
            return '\033[32m'
        elif self.tipo == 'Amarelo':
            return '\033[33m'
        elif self.tipo == 'Azul':
            return '\033[34m'
        elif self.tipo == 'Roxo':
            return '\033[35m'
        elif self.tipo == 'Azul Claro':
            return '\033[36m'
        elif self.tipo == 'Cinza':
            return '\033[37m'
        else:
            return "Tipo de cor inválido"
