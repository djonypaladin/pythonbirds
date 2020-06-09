class Pessoa:
      def __init__(self,*familia,name=None,idade=17):
         self.name= name
         self.familia= list(familia)
         self.idade= idade

      def comprimentar(self):
          return 'hello my code'
      def despedisir(self):
          return 'diz tchau ;3'
      def contar_1(self):
          return list(range(10,0,-1))

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