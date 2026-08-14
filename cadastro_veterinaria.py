class Animal:
    def __init__(self, nome):
        self.nome = nome

    def descrever(self):
        pass

class Cachorro(Animal):
    def descrever(self):
        return f"Cachorro: {self.nome}"

class Gato(Animal):
    def descrever(self):
        return f"Gato: {self.nome}"

# Uso com polimorfismo
animais = [Cachorro("Rex"), Gato("Mimi")]

for a in animais:
    print(a.descrever())
