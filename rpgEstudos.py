import time
import random

class Personagens:
    def __init__(self,level,classe,forca,Agilidade,inteligencia,vida):
        self.level = level
        self.classe = classe
        self.forca = forca
        self.agilidade = Agilidade
        self.inteligencia = inteligencia
        self.vida = vida


guerreiro = Personagens(0,'Guerreiro',1500,1000,800, 900)
mago = Personagens(0,'Mago',800,900,1500, 800)
ranger = Personagens(0,'Ranger',800,1500,900, 900)

inimigo1 = Personagens(3,'Madara',1500,1000,800, 1500)
inimigo2 = Personagens(3,'Kabuto',1500,1000,800, 1500)
inimigo3 = Personagens(3,'Obito',1500,1000,800, 1500)

#Escolha de personagens.
#funcões de inicialização. 
while True:
    user = str(input('Qual é o seu nome ? '))
    print(f'Seja Bem vindo: {user} , Tenha um bom jogo!')
    print('_______RPG______')
    print('1 - Guerreiro:')
    print('2 - Mago:')
    print('3 - Ranger:')
    opcao = int(input('Escolha um personagem:'))
    time.sleep(1)
    
    
    
    if opcao == 1:
        print('_________________________________________________________________________________________________________________________')
        print(f'Ótima escolha {user} , Esses são os atributos do seu personagem. ')
        print('Força e determinação: Capacidade de persistir diante de obstáculos e adversidades, com foco no objetivo a ser alcançado. ')
        print('__________________________________________________________________________________________________________________________')
        print(f'Level: {guerreiro.level}')
        print(f'Classe: {guerreiro.classe}')
        print(f'Força : {guerreiro.forca}')
        print(f'Agilidade: {guerreiro.agilidade}')
        print(f'Inteligencia: {guerreiro.inteligencia}')
        print(f'Vida: {guerreiro.vida}')
        print('_________________________________________________________________________________________________________________________')
    
    
    
    elif opcao ==2:
        print('_________________________________________________________________________________________________________________________')
        print('Ser mago é ter a alma marcada por uma aura poderosa. É descobrir, praticar, desvendar o oculto e por à prova seus conhecimentos.')
        print('_________________________________________________________________________________________________________________________')
        print(f'Level: {ranger.level}')
        print(f'Classe: {ranger.classe}')
        print(f'Força : {ranger.forca}')
        print(f'Agilidade: {ranger.agilidade}')
        print(f'Inteligencia: {ranger.inteligencia}')
        print(f'Vida: {ranger.vida}')
        print('_________________________________________________________________________________________________________________________')
    
    
    
    
    elif opcao == 3:
        print('_________________________________________________________________________________________________________________________')
        print('Rangers podem usar tanto Força quanto Destreza como atributo principal para ataques, dependendo do estilo de combate preferido (corpo a corpo')
        print('_________________________________________________________________________________________________________________________')
        print(f'Level: {mago.level}')
        print(f'Classe: {mago.classe}')
        print(f'Força : {mago.forca}')
        print(f'Agilidade: {mago.agilidade}')
        print(f'Inteligencia: {mago.inteligencia}')
        print(f'Vida: {mago.vida}')
        print('_________________________________________________________________________________________________________________________')
    else:
        print("Opção inválida! Tente novamente.")
        continue


















#while i < 4:
   # atack = random.randint(50,100)
  #  i+=1
  #  print(f'Você foi atingido com {atack} de Dano!')
 #   life[0] -= atack
    
#print(f'Vida Total ao final do ataque: {life}')
    

#
