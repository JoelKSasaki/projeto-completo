class Voo():
    def __init__(self, limite):
        self.limite = limite
        self.passageiros = []
        
    def addpassageiro(self, nome):
        if not self.assentovazio():
            return False
        else:
            self.passageiros.append(nome)
            return True
        
    def assentovazio(self):
        return self.limite - len(self.passageiros)
    
Gol = Voo(4)

ifsp = ["Rafael", "Milhomem", "Júlio", "Memphis", "Thomas", "Rony Rústico"]

for aluno in ifsp:
    sucesso = Gol.addpassageiro(aluno)
    if sucesso:
        print(f"{aluno} adicionado ao voo")
    else:
        print(f"Não há assento vazio para {aluno}")