class Pessoa:
    menbros_superiores = 2
    menbro_inferiores=2
    def __init__(self,*familia,name=None,idade=17):
         self.name= name
         self.familia= list(familia)
         self.idade= idade

    def comprimentar(self):
          return 'hello my code'
    def despedisir(self):
          return 'diz tchau ;3'
    def contar_1(self):
     return list(range(10,1,-1))

    @staticmethod
    def estatico ():
     return 50

    @classmethod
    def atributodeclasse(cls):
        return f'{cls} - membros superiores {cls.menbros_superiores},membros inferiores {cls.menbro_inferiores}'


if __name__ == '__main__':
    djony = Pessoa(name='djony', idade=17)
    mother = Pessoa(djony,name='mother',idade=46)
    type (djony)
    print(djony.comprimentar())
    print(djony.contar_1())
    print(djony.name)
    print(mother.name)
    for familia in mother.familia:
     print(familia.name,familia.idade)
     print(djony.__dict__)
     print(Pessoa.estatico())
     print(Pessoa.atributodeclasse())
