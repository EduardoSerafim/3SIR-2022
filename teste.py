import random



class personagem():
    def __init__(self, nome):
        self.nome = nome
        self.x = 0
        self.y = 0
        self.experiencia = 2
        self.pokemons = []
            

    def questao2(self, sentido):
        if sentido == "cima":
            self.y = self.y + 1

        elif sentido == "baixo":
            self.y = self.y - 1

        elif sentido == "direita":
            self.x = self.x + 1

        elif sentido == "esquerda":
            self.x = self.x - 1
        else:
            self.x = 0
            self.y = 0
        return self.x, self.y

    def questao3(self):
        x = random.randint(0,5)
        if x + self.experiencia > 100:
            self.experiencia = 100
        else:
            self.experiencia = self.experiencia + x
        return self.experiencia


    def questao4(self, nomePokemon, defesa):
        forca = random.randint(-1, 3)
        forcaTotal = forca + self.experiencia
        if forcaTotal > defesa:
            self.pokemons = self.pokemons + [nomePokemon]
            return 1
        else:
            return 0
            
    def questao5(self, nomePokemon, defesa, x, y):
        xDistancia = self.x - x
        yDistancia = self.y - y
        if (xDistancia >= -1) and (xDistancia <= 1) and\
           (yDistancia >= -1) and (yDistancia <= 1):
            personagem.questao4(self, nomePokemon, defesa)
        return xDistancia, yDistancia

    


random.seed(0)  # o modulo random foi importado no inicio do codigo
print('--- Questao 1 ---')
meuPersonagem = personagem('Fernanda')
print('Atributos definidos no construtor: ')
print('Nome: ', meuPersonagem.nome)
print('Posicao x: ', meuPersonagem.x)
print('Posicao y:', meuPersonagem.y)
print('Experiencia: ', meuPersonagem.experiencia)
print('Lista de Pokemons: ', meuPersonagem.pokemons)

print('--- Questao 2 ---')
print('Andando para cima: ')
print(meuPersonagem.questao2('cima'))
print('Posicao: ', meuPersonagem.x, meuPersonagem.y)
print('Andando para a direita: ')
print(meuPersonagem.questao2('direita'))
print('Posicao: ', meuPersonagem.x, meuPersonagem.y)



print('--- Questao 3 ---')
print('Adquirindo experiencia: ')
print(meuPersonagem.questao3())
print('Experiencia: ',meuPersonagem.experiencia)
print('Adquirindo experiencia: ')
print(meuPersonagem.questao3())
print('Experiencia: ',meuPersonagem.experiencia)

print('--- Questao 4 ---')
print('Tentando capturar um Charmander: ')
print(meuPersonagem.questao4('Charmander',4))
print('Lista de Pokemons: ',meuPersonagem.pokemons)
print('Tentando capturar um Venusaur: ')
print(meuPersonagem.questao4('Venusaur',20))
print('Lista de Pokemons: ',meuPersonagem.pokemons)

print('--- Questao 5 ---')
print('Tentando capturar um Bulbasar: ')
print(meuPersonagem.questao5('Bulbasar',4,2,4))
print('Lista de Pokemons: ',meuPersonagem.pokemons)
print('Tentando capturar um Squirtle: ')
print(meuPersonagem.questao5('Squirtle',4,1,0))
print('Lista de Pokemons: ',meuPersonagem.pokemons)

# print('--- Questao 6 ---')
# meuNovoPersonagem = personagem2('Felipe')
# print('Atributos definidos no construtor: ')
# print('Nome: ',meuNovoPersonagem.nome)
# print('Posicao x:',meuNovoPersonagem.x)
# print('Posicao y:',meuNovoPersonagem.y)
# print('Experiencia: ',meuNovoPersonagem.experiencia)
# print('Lista de Pokemons: ',meuNovoPersonagem.pokemons)
# print('--- Questoes 7 e 8 ---')
# print('Quantidade de Charmanders na lista: ')
# print(meuNovoPersonagem.questao7('Charmander'))
# print('Tentando capturar uma Caterpillar: ')
# print(meuNovoPersonagem.questao4('Caterpillar',1))
# print('Lista de Pokemons: ',meuNovoPersonagem.pokemons)
# print('Tentando capturar uma outra Caterpillar: ')
# print(meuNovoPersonagem.questao5('Caterpillar',1,0,0))
# print('Lista de Pokemons: ',meuNovoPersonagem.pokemons)
# print('Tentando capturar um Pigeon: ')
# print(meuNovoPersonagem.questao4('Pigeon',2))
# print('Lista de Pokemons: ',meuNovoPersonagem.pokemons)
# print('Quantidade de Caterpillars na lista: ')
# print(meuNovoPersonagem.questao7('Caterpillar'))
# print('Quantidade de Pigeons na lista: ')
# print(meuNovoPersonagem.questao7('Pigeon'))
