class Pessoa:
      def __init__(self):
         self.name= None

      def comprimentar(self):
          return 'hello my code'
      def despedisir(self):
          return 'diz tchau ;3'
      def contar_1(self):
          return list(range(10,0,-1))

if __name__ == '__main__':
    p = Pessoa()
    type (p)
    print(p.comprimentar())
    print(p.contar_1())
    p.name = 'paladin djony'
    print(p.name, p.despedisir())