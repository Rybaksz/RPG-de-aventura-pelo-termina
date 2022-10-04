from time import sleep
import sys
import random

class Crs:
    global vetor
  
#Cores
    branco = '\033[0m'	
    vermelho = '\033[1;31m'
    verde =	'\033[1;32m	'
    amarelo	= '\033[1;33m'	
    azul = '\033[1;34m'	                
    magenta = '\033[1;35m'	
    ciano = '\033[1;36m'	
    cinzaclaro = '\033[1;37m'	
    cinzaescuro = '\033[1;90m'	
    vermelhoclaro = '\033[1;91m'	
    verdeclaro	= '\033[1;92m'	
    amareloclaro = '\033[1;93m'	
    azulclaro = '\033[1;94m'
    magentaclaro = '\033[1;95m'	
    cianoclaro = '\033[1;96m'


  
#Introdução do jogo#

print(f'{Crs.ciano}---------------------------------------------------{Crs.ciano}')
texto = (f""" SEJA MUITO BEM VINDO AO: {Crs.vermelho}

___________.__            
\__    ___/|  |__   ____             
  |    |   |  |  \_/ __ \                           
  |    |   |   Y  \  ___/                 
  |____|   |___|  /\___  >                               
                \/     \/ 
_________.__                             
\______   \  | _____     ____   ____                  
 |     ___/  | \__  \   / ___\_/ __ \      
 |    |   |  |__/ __ \_/ /_/  >  ___/                          
 |____|   |____(____  /\___  / \___  >     
                    \//_____/    \/                 
.___                                       
|   | ____                                                   
|   |/    \                                       
|   |   |  \                           
|___|___|  /                               
         \/                                              
___________      __                    
\_   _____/_ ___/  |_ __ _________   ____  
 |    __)|  |  \   __\  |  \_  __ \_/ __ \         
 |     \ |  |  /|  | |  |  /|  | \/\  ___/                 
 \___  / |____/ |__| |____/ |__|    \___  > 
     \/                                \/  """) 

for linha in texto.splitlines():
  for caractere in linha:
      print(caractere,end="")
      sleep(0.002)
  print(" ")
  sleep(0.1)
print('------------------------------------------------------')

sleep(2)
print(f'{Crs.ciano}')
print()
input('Pressione enter para começar!')

sleep(2)
print('........')
print('..............')
print('Loading… ██[][][][][][][][] 20%')
sleep(2)
print('........')

sleep(2)
print('........')
print('.............')
print('..............')
print('Loading… ████[][][][][][][] 40%')
sleep(2)
print('........')
sleep(2)
print('........')
print('..............')
print('Loading… ██████████████████[] 80%')
sleep(2)
print('........')
print('..............')
print('Loading… ████████████████████ 100%')
sleep(2)
print('........')
print('..............')

sleep(2)
print('........')
print('..............')

#menu de escolha de nome
print(f''' {Crs.branco}

__________________§§§§§§§§§
_______________§§§§§§§§§§§§§§
_____________§§§§§§§§§§§§§§§§§§
____________§§§§§§§§§§§§§§§§§§§§
___________§§§§§§§§§§§§§§§§§§§§§§
__________§§§§§§§§§§§§§§§§§§§§§§§§
_________§§§§§§§§§§§§§§§§§§§§§§§§§§
_________§§§§§§§§§§§§§§§§§§§§§§§§§§
________§§§§§§§§§§§§§§§§§§§§§§§§§§§§
________§§§§§§§§§§§§§§§§§§§§§§§§§§§§
_______§§§§§§§§§§§§§§§§§§§§§§§§§§§§§
_______§§§§§§_§§§§_§§§§§ §§§§§§§§§§§§
_______§§§§§__§§§__§§§§§__§§§§§_§§§§§
_______§§§§§__§§§__§§§§§___§§§§__§§§§
_______§§§§___§§_____§§§____§§§__§§§§§
______§§§§§___§_______§§_____§§___§§__§
_____§__§§§____________§__________§§___§
_____§___§§___§§§___________§§§___§§___§
_____§___§§__§§§_§_________§§§_§__§§___§
_____§____§__§§§§§_________§§§§§__§____§
______§___§__§§§§§___§_§___§§§§§______§
_______§__§___§§§___________§§§___§§§§
________§§§§_______§_____§_______§
____________§_______§§§§§_______§
___________§§§§§_____________§§§
___________§____§§§§_____§§§§§
__________§___§§____§§§§§____§§
__________§_§§_______§§________§
_________§_§__§______§_§______§_§
_______§§§§____§§§§§§§__§§§§§§___§
______§____§_________§____________§
_____§_____§_________§____________§
_____§§§___§_________§_§§__§__§___§§
_§§§§§__§__§_________§_§§__§__§___§
§__§§§__§_§§§________§______§§__§__§
§__§§___§§§§§________§__________§__§
§______§_§__§________§_§§_______§__§
_§____§__§§§§________§_§§_______§__§
__§__§_____§§§§§§____§______§§§§§§_§
___§§______§____§____§______§____§_§
___________§____§____§_§§___§____§__§
___________§____§____§_§§___§____§__§
___________§____§____§______§____§§§§
___________§§§§§_____§_______§§§§_§
___________§_________§___________§§
___________§§§§§§§§§§§§§§§§§§§§§§§
_____________§§§§§§§§§§§§§§§§§§§
_____________§§§§§§§§§§§§§§§§§§§
_____________§§§§§§§§§§§§§§§§§§§
________________§____§_§____§
________________§____§_§____§
________________§§§§§§_§§§§§§
________________§____§_§____§
________________§____§_§____§
______________§§§____§_§____§§§
_____________§_______§_§_______§
_____________§_______§_§_______§
_____________§_______§_§_______§''')

personagem = input(f' {Crs.amareloclaro}Qual meu nome? ')

print(f'{personagem}! Otimo nome')

sleep(2)
print(f'{Crs.ciano}........')
print('..............')
print('..............')
print('..............')
sleep(5)
print('..............')
sleep(5)

#menu de escolha

print(f''' {Crs.branco} {personagem} Vivia em uma sociedade
passada no ano de 2042 onde o mesmo trabalhava como jornalista.
Após descobrir que uma grande empresa desenvolveu uma nova doença para
acabar com a super população ele precisa fazer diversas escolhas para salvar a todos.
Quando ele estava para ir a público, recebeu uma pancada na cabeça e
acabou acordando em um beco escuro de sua cidade sem nenhum tipo de
lembrança.a {Crs.branco}''')
print('''
                                  _._
                               .-~ | ~-.
                               |   |   |
                               |  _:_  |                    .-:~--.._
                             .-"~~ | ~~"-.                .~  |      |
            _.-~:.           |     |     |                |   |      |
           |    | `.         |     |     |                |   |      |
  _..--~:-.|    |  |         |     |     |                |   |      |
 |      |  ~.   |  |         |  __.:.__  |                |   |      |
 |      |   |   |  |       .-"~~   |   ~~"-.              |   |      |
 |      |   |  _|.--~:-.   |       |       |         .:~-.|   |      |
 |      V   | |      |  ~. |       |   _.-:~--._   .' |   |   |      |
 |      I   | |      |   | |       |  |   |     |  |  |   |   |      |
 |      T   | |      |   | |       |  |   |     |  |  |   |   |      |
 |      |   | |      |   | |       |  |   |     |  |  |   |   |      |
 |      O   | |      |   | |       |  |   |     |  |  |   |   |      |
 |      R   | |      |   | |       |  |   |     |  |  |   |   |      |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')

#Beco escuro#


print(f' {Crs.amarelo}"Olá tem alguem ai? " - Você escuta uma voz fraca falar com você no fundo do beco escuro {Crs.amarelo}')
print('''

''')
print()
print('...')
sleep(2)
print('.......')
sleep(2)
sleep(2)
print('........')
print('..............')
sleep(2)
print('........')
print('..............')
sleep(2)
print('........')
print('..............')
sleep(2)
print('........')
print('..............')
sleep(2)
print('........')
print('..............')

print(f' {Crs.branco}Um Sem teto se levanta e você nota diversas manchas em seu rosto.... {Crs.branco}')
print ('''

════█████████████████████████═════
═══███████████████████████████════
═══███████████████████████████════
═══███████████████████████████════
═══███████████████████████████════
═══███████████████████████████════
═══██═══════════════════════██════
═══██═══════════════════════██════
═══██═══════════════════════██════
═══██═══════════════════════██════
═══██═█████████═══█████████═██════
═══██═█████████═══█████████═██════
═████════███═════════███════████══
█████════█═█═════════█═█════█████═
█████════███═════════███════█████═
█████═══════════════════════█████═
█████═══════════════════════█████═
█████═══════════════════════█████═
█████══════════███══════════█████═
█████═══════════█═══════════█████═
═████═══════════════════════████══
═══███████████████████████████════
═══█═██═██═██═██═██═██═██═██═█════
═══███████████████████████████════
═══██████═══════════════██████════
═══█═██═█═══════════════█═██═█════
═══███████═════════════███████════
═══███████████████████████████════
═══█═██═██═██═██═██═██═██═██═█════
═══███████████████████████████════
═══███████████████████████████════
═══████═██═██═██═██═██═██═████════
════█████████████████████████═════''')

print()
print('......')
sleep (2)
print('.........')
sleep (2)
print()
print('......')
sleep (2)
print('.........')
sleep (2)


print()
print(f' {Crs.branco}O que deseja fazer?{Crs.branco}')
print(f'''{Crs.cinzaescuro}

 [1] Ficar Quieto
 [2] Responder 


{Crs.cinzaescuro}''')


escolha = input (f' {Crs.ciano}Sua Escolha:  ')
if escolha.lower().strip() == '1':
  print (f' {Crs.branco}Você ficou quieto mas o sem teto já tinha te visto. ')

if escolha == '2':
  print (f'{Crs.branco}Você Respondeu ao seu teto e perguntou o que ele tinha.' )


print(f' {Crs.amarelo} O Sem teto cai e fala que está muito doente desde que eles vieram ')
print()
print('......')
sleep (2)
print('.........')
sleep (2)

print()
print(f'{Crs.branco}O que deseja fazer?')
print(f''' {Crs.cinzaescuro}

 [1] Ajudar ele
 [2] Ficar Afastado com medo da doença 


''')

escolha = input (f'{Crs.ciano}Sua escolha: ')
escolhadogusman = 0
if escolha == '1':
  escolhadogusman += 1
  print(f' {Crs.branco} Você ajudou o sem teto, mas após isso notou pequenas manchas em suas mãos, logo após se afastou rapidamente e perguntou quem são eles?')
elif escolha == '2':
  escolhadogusman += 2
  print(f' {Crs.branco}Você ficou afastado mas perguntou ao sem teto quem são eles? ')
  
  print()
print('......')
sleep (2)
print('.........')
sleep (2)


print (f' {Crs.amarelo}Eles estão em toda parte as empresas SilverLight eles controlam todo o racionamento, todos na cidade estão com fome!! ')

print()
print('...')
sleep(2)
print('.......')
sleep(2)

print(f' {Crs.ciano}Ambos ficam em Silencio')
print(f' {Crs.ciano}Grilo: Cri cri cri')

print()
print('...')
sleep(2)
print('.......')
sleep(2)



print(f' {Crs.amarelo}O Sem teto lhe conta que seu nome é Gusman')

print()
print('......')
sleep (2)
print('.........')
sleep (2)

print (f' {Crs.branco}"Olá Gusman Meu nome é {personagem}"')

print(f' {Crs.amarelo}Gusman lhe conta que uma terrivel doença está se espalhando pelos becos da cidade e te orienta a sair dali o mais rapido possivel')

print()
print('......')
sleep (2)
print('.........')
sleep (2)

print(f' {Crs.amarelo}"Olhe {personagem} eu não tenho muito tempo de vida então pegue este bastão neon irá de ajudar a encontrar a saida"')

print()
print('......')
sleep (2)
print('.........')
sleep (2)

print(f'{Crs.ciano}Item Adquirido bastão neon desgastado !')
sleep(5)
print('.......')
sleep(2)
print('.....')

print(f' {Crs.ciano} Gusman cai e você percebe que ele está tentando falar algo ')
print('Com suas ultimas forças gusman lhe fala..... ')
sleep(3)
print('.....')
print('Eu fiz muitas coisas nessas vida mas eu quero ir para o inferno, não para o céu......')
sleep(5)
print('.......')
sleep(2)
print('.....')
print(f"No inferno, gozarei da companhia de papas, reis e principes meu caro {personagem} ....")
sleep(5)
print('.......')
sleep(2)
print('.....')
print('No céu, só terei por companhia outros mendingos, monges, eremitas e apóstolos.')
sleep(5)
print('.......')
sleep(2)
print('.....')
print('Você nota cair uma lagrima do rosto desfalecido de gusman')
sleep(5)
print('.......')
sleep(2)
print('.....')
print(' e enfim o seu novo amigo dá o ultimo suspiro')



print()
print('......')
sleep(2)
print('.........')
sleep(2)

print(f' {Crs.branco}Você percebe que o Gusman  está morto ')

print()
print('......')
sleep (2)
print('.........')
sleep (2)

print(f'{Crs.branco}Você se despede dele: ')
sleep(5)
print('...........')
print('Meu caro Gusman não gosto de despedidas e nem acho que seja o caso. O mundo é pequeno e estamos todos em movimento, muito em breve vamos voltar a nos encontrar pelo caminho, em novos projetos e jornadas.')

print()
print('......')
sleep (2)
print('.........')
sleep (2) 
#Saida Do Beco
print (f' {Crs.branco}Você se vira triste pela sua perda e se depara com 3 caminhos pelo beco qual você irá seguir?')



print()
print(f' {Crs.branco}Qual caminho irá seguir?')


print(f''' {Crs.cinzaescuro}

    [1]Seguir reto  
    [2]Virar a esquerda
    [3]Virar a direita
    
  

''')
escolha = input(f'{Crs.ciano} Sua escolha: ')

if escolha.lower().strip() == "1":
  print (f' {Crs.branco}Você seguiu reto e se deparou com um paredão. ')
  print('.......')
  sleep(2)
  sleep(2)
  print('você voltou para trás e escolheu a esquerda mas somente encontrou uma mochila velha')
  print('''
            ██▓▓▓▓▓▓▓▓▓▓                    
                ██▓▓        ██▓▓                  
                ▒▒░░        ▒▒░░                  
            ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒            
          ▒▒▒▒▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░          
        ░░▒▒▒▒▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░        
        ▒▒▒▒▒▒▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░        
        ▒▒▒▒▒▒▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░        
  ░░  ░░▓▓▒▒▒▒▓▓▓▓▒▒▒▒░░▒▒░░▒▒▒▒▒▒░░▒▒▒▒░░  ░░    
        ▒▒▒▒▒▒▓▓▒▒░░░░▒▒▒▒░░░░▒▒░░░░░░▒▒░░      ░░
    ░░  ▒▒▒▒▒▒▓▓▒▒░░▒▒▓▓░░▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒        
        ▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒      
        ▒▒▒▒▒▒▓▓▒▒░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░      
        ▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒░░▒▒░░░░░░░░░░░░░░░░      
        ▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░      
        ▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░      
        ▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒      
          ▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒        
                                                  
                                                  
                                                  
                                                  
  ''')
  print('........')
  print('...........')
  sleep(2)

  print (f' {Crs.branco}Você encontrou uma mochila velha para poder guardar seus itens!')
  print('......')
  sleep(10)
  print('.......')
  print(f" {Crs.cinzaclaro}Mochila velha adquirida!")
  print(f' {Crs.branco}Logo após irritado você segue a direita')



elif escolha.lower().strip() == "2":
  print (f'{Crs.branco}Você encontrou uma mochila velha para poder guardar seus itens!')
  print(f" {Crs.cinzaclaro}Mochila velha adquirida!")

elif escolha.lower().strip() == "3":
 print (f' {Crs.branco}Você virou a direita e se deparou com mais 2 caminhos qual irá seguir?')

 print()
print(f'{Crs.branco}Qual caminho irá seguir?')

print(F''' {Crs.cinzaescuro}

  
    [1]Virar a esquerda
    [2]Virar a direita
    
  

''')
escolha = input(f' {Crs.branco} Sua escolha: ')

if escolha.lower().strip() == "1":
  print (f' {Crs.branco}Você entrou pela esquerda e conseguiu sair dos becos assim você se depara com uma rua suja e toda molhada')

  if escolha.lower().strip() == "2":
    print (f' {Crs.branco}Você se deparou com um muro! ')
   
    print(f' {Crs.branco} você volta e segue a esquerda')
    

  print()
print('......')
sleep (2)
print('.........')
sleep (2)

  #Logo após a saida do beco#


#Entrada no comercio
print (f' {Crs.branco}Você se depara com um pequeno comercio do outro lado da rua e fica tentado a entrar ')
print()
print('......')
sleep (2)
print('.........')
sleep (2)
print()
print('......')
sleep (2)
print('.........')
sleep (2)

print('''
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼.(▓)
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼███
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼███████
┼┼┼┼┼┼┼┼┼┼┼┼┼┼█████████
┼┼┼┼┼┼┼┼┼┼┼┼┼┼█████████
┼┼┼┼┼┼┼┼┼┼┼┼┼███████████
┼┼┼┼┼┼┼┼┼┼┼┼┼▒░░▒▒░░▒░░▒
┼┼┼┼┼┼┼┼┼┼┼┼┼▒░░▒░░▒▒░░▒
┼┼┼┼┼┼┼┼┼┼┼┼┼▒░░▒▒░░▒░░▒
┼┼┼┼┼┼┼┼┼┼┼┼┼███████████
┼┼┼┼┼┼┼┼┼┼┼┼┼┼█▒█████▒█
┼┼┼┼┼┼┼┼┼┼┼┼┼┼█▒█████▒█
┼┼┼┼┼┼┼┼┼┼┼┼┼┼█▒█████▒█
┼┼┼┼┼┼┼┼┼┼┼┼┼┼█▒█████▒█
┼┼┼┼┼┼┼┼┼┼┼┼┼███▒▒▒▒▒███
┼┼┼┼┼┼┼┼┼┼┼┼┼███▒▒▒▒▒███
┼┼┼┼┼┼┼┼┼┼┼┼┼███▒▒▒▒▒███
┼┼┼┼┼┼┼┼┼┼┼┼┼███▒▒▒▒▒███
┼┼┼┼┼┼┼┼┼┼┼┼┼███▒▒▒▒▒███
┼┼┼┼┼┼┼┼┼┼┼┼┼█▒▒█████▒▒█
┼┼┼┼┼┼┼┼┼┼┼┼┼█▒▒█████▒▒█
┼┼┼┼┼┼┼┼┼┼┼┼┼█▒▒█████▒▒█
┼┼┼┼┼┼┼┼┼┼┼┼┼█▒▒█████▒▒█
┼┼┼┼┼┼┼┼┼┼┼┼┼█▒▒█████▒▒█
┼┼┼┼┼┼┼┼┼┼┼┼████▒▒▒▒▒████
┼┼┼┼┼┼┼┼┼┼┼┼████▒▒▒▒▒████
┼┼┼┼┼┼┼┼┼┼┼┼████▒▒▒▒▒████
┼┼┼┼┼┼┼┼┼┼┼┼████▒▒▒▒▒████
┼┼┼┼┼┼┼┼┼┼┼┼████▒▒▒▒▒████
┼┼┼┼┼┼┼┼┼┼┼┼█▒▒▒█████▒▒▒█
┼┼┼┼┼┼┼┼┼┼┼┼█▒▒▒█████▒▒▒█
┼┼┼┼┼┼┼┼┼█┼┼█▒▒▒█████▒▒▒█
┼┼┼██████▒█████████████████
┼┼┼█████▒▒▒████████████████
┼┼┼████▒▒▒▒▒███████████████
┼┼┼███▒▒▒▒▒▒▒██████████████
┼┼┼██▒▒▒▒▒▒▒▒▒█████████████
┼┼┼█▒▒▒▒███▒▒▒▒█▒▒▒▒▒▒▒▒▒▒█
┼┼┼██▒▒█████▒▒██▒▒▒████▒▒██
┼┼┼█▒▒▒█████▒▒▒█▒▒▒█▒▒█▒▒▒█
┼┼┼██▒▒█████▒▒██▒▒▒████▒▒██
┼┼┼█▒▒▒█████▒▒▒█▒▒▒▒▒▒▒▒▒▒█
┼┼┼████████████████████████

''')
sleep (2)
print('.............')
sleep(2)
print(f' {Crs.branco}você decide entrar no comercio para pedir informaçoes ')

sleep (2)
print('.............')
sleep(2)

print(f''' {Crs.cinzaescuro}

[1] Você pergunta sobre a nova doença

[2] Voce pergunta como ir para o nível superior da cidade''')



escolha = input (f" {Crs.branco}Sua escolha:  ")

if escolha == "1":
  print (f' {Crs.branco}Voce perguntou sobre a nova doença e o atendente disse que nao poderá lhe contar sobre mas falou para voce evitar tocar nas pessoas')

elif escolha == "2":

 print (f' {Crs.branco}o atendente te disse que é somente você seguir rua acima e lhe perguntou se você é retardado para não pensar em uma coisa tão óbvia'
       )

sleep (2)
print('..........')
print('..............')
sleep(2)
#Saida da loja
print(f' {Crs.branco}Voce sai da loja e segue rua acima')

sleep(2)
print('..........')
sleep(2)
print('...........')


print('Voce chega ao final da rua e se depara com um muro gigante com somente uma porta que leva para um elevador ')

sleep(2)
print('........')
sleep (2)
print('...............')


print('''Você avista um guarda protegendo a entrada do elevador
                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                
              ████▓▓▓▓██████▓▓▓▓▓▓▓▓▓▓▓▓████            
            ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒██          
          ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓██        
        ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓██      
        ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓████      
      ██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓██    
      ████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓██    
    ████▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓██  
    ██▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒▒▒▒▒▒▒██  
  ██▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓▒▒▓▓▓▓▓▓██
  ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓██
    ████████▓▓████████████████████████████████████████  
    ██▓▓██▓▓▓▓██░░░░░░░░░░░░░░░░░░▒▒    ░░██▓▓▓▓██▒▒██  
  ██▓▓▒▒██▓▓██░░░░░░░░░░░░░░░░░░░░░░░░    ░░██▓▓██▒▒▒▒██
    ██████▓▓██░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ██▓▓██████  
  ██░░░░██▓▓██░░░░██░░░░░░░░░░░░░░░░░░██░░  ██▓▓██░░░░██
  ██░░░░██▓▓██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▓▓██░░░░██
  ██░░░░██▓▓██░░░░░░░░░░░░░░▓▓░░░░░░░░░░░░░░██▓▓██░░░░██
    ██░░██▓▓██░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░██▓▓██░░██  
      ████▓▓██░░░░░░░░▓▓▓▓▓▓░░▓▓▓▓▓▓░░░░░░░░██▓▓████    
        ██▓▓██░░░░░░░░▓▓▒▒▒▒▒▒▒▒▒▒▓▓░░░░░░░░██▓▓██      
        ░░██▓▓▓▓░░░░░░░░░░▒▒░░░░░░  ░░░░░░▓▓▒▒██        
            ▓▓▒▒▓▓░░░░░░░░░░░░░░░░░░░░░░██▒▒▓▓          
              ██▒▒▓▓░░░░░░░░░░░░░░░░░░██▒▒██            
                ▓▓████████████████████▓▓██              
              ████▓▓▓▓██░░░░░░░░░░██▓▓▒▒████            
          ██████▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓        
        ████████▓▓▓▓▓▓▓▓██░░░░░░██▓▓▓▓▓▓▒▒▒▒▓▓▓▓██      
        ████▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░██▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓██      
      ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██    
      ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██    
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██  
    ██████████████████████████████████████████████████  

''' )
          
          
   
      
print('O que você faz?')



print(f''' {Crs.cinzaescuro}

[1] Você vasculha seus bolsos a procura do seu crachá de passe livre

[2] Voce joga uma pedra para distrair o guarda e entrar correndo


''')


escolha = input (f' {Crs.branco}Sua escolha: ')

if escolha == "1":

  print(f'{Crs.ciano}Todos seus pertences sumiram enquanto estava desacordado  ')

elif escolha == "2":

  print(f' {Crs.branco}Voce joga uma pedra em um canto escuro e o guarda vai verificar que barulho foi aquele')

sleep(2)
print('.............')
sleep(2)
print('............')

print(f' {Crs.branco}Você corre para o elevador mas o guarda te avista assim tornando tarde demais ')
sleep(2)
print('.............')
sleep(2)
print('............')
sleep(2)
print('.............')
sleep(2)
print('............')

#PrimeiroPVP

  
GUARDA_HP = 200

print("Você decide atacar o guarda".upper())

sleep(3)

print('......')

print(
    f"""

[1] Bastão neon
dano de 1 a 100

[2] Soco
dano de 1 a 50

  """
)

while True:
    escolha = input("Escolha seu ataque: ")

    dano_ataque = random.randint(1, 50)
    if escolha == "1":
        dano_ataque = random.randint(1, 100)

    GUARDA_HP -= dano_ataque
    print(f"Você deu {dano_ataque} de dano, o guarda agora está com {GUARDA_HP} de HP.")

    if GUARDA_HP <= 0:
        print("O guarda está morto!!")
        break

    repetir = input("\nGostaria de atacar novamente? [S/n] ")
    if repetir == "n":
        print("O guarda continua vivo, Mas está ferido demais para lhe impedir!")
        break

    print("vamos atacar novamente, e matar esse desgraçado!".upper())

 
 
sleep(3)
sleep(5)
print('.......')
print('Antes de você entrar no elevador você vai até o guarda e rouba a arma dele!')
sleep(4)
print('''
      ████████                                                                  
      ██▓▓    ██          ████████████████████████████                          
    ████████████████████████                          ██                        
    ██                    ██░░██████████████████████░░  ██      ██████          
    ██░░░░░░░░░░░░░░░░░░░░██░░██                  ████░░  ██  ██      ██        
    ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░██░░████████████░░░░██░░██░░████░░░░████          
    ████████████████████████░░██░░▓▓▒▒▒▒▒▒▒▒▒▒██░░██░░  ████░░░░██              
        ██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░██░░████████████░░░░██░░░░████░░░░░░██            
          ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░██░░░░░░░░░░░░░░░░░░██░░▒▒██░░██░░░░██            
            ████████████████░░██▒▒████████████▒▒▒▒██▒▒▒▒██▒▒░░██████            
                          ██░░██████████████████████████▒▒▒▒▒▒▓▓▓▓▓▓██          
                            ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░██▓▓▓▓██▓▓▓▓██        
                              ██████████████████████████░░██▓▓██░░██▓▓██        
                                  ██▒▒██  ██▒▒▒▒██  ██▒▒████▓▓▓▓██▓▓▓▓██        
                                  ██▒▒██  ██▒▒██    ██▒▒▒▒██▓▓▓▓▓▓▓▓▓▓▓▓██      
                                  ██░░░░████████████░░░░██  ██▓▓▓▓▓▓▓▓▓▓██      
                                    ██░░░░░░░░░░░░░░░░██    ██▓▓▓▓▓▓▓▓▓▓██      
                                      ████████████████      ██  ▓▓▓▓▓▓▓▓▓▓██    
                                                            ██  ▓▓▓▓██▓▓▓▓██    
                                                            ██  ▓▓██░░██▓▓██    
                                                            ██▓▓  ▓▓██▓▓▓▓██    
                                                            ██▓▓▓▓▓▓▓▓▓▓▓▓██    
                                                              ██▓▓▓▓▓▓▓▓██      
                                                                ████████        
                                                                                
''')
sleep(10)
print(f'{Crs.branco}Arma adquirida!!!')
sleep(5)
print('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠠⣤⠀⠀⢀⡀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⣀⣀⣀⣁⣀⣀⣉⣁⣀⣀⣀⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠉⢹⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠺⠿⢸⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣤⣤⣼⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣶⣾⣷⣶⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿''')
print(f'{Crs.branco}Você entra no elevador mas esse só tinha acesso a classe média da cidade você pressiona o botão e começa a subir')
sleep(2)
print('................')
input(f'{Crs.ciano} Pressione enter para continuar.')


print()
#Entrada no nivel médio
sleep(3)
sleep(2)
print('........')
print('..............')
print('Loading… ██[][][][][][][][] 20%')
sleep(2)
print('........')
print('..............')
print('Loading… ███[][][][][][][] 30%')
sleep(2)
print('........')
print('..............')
print('Loading… ████[][][][][][] 40%')
sleep(2)
print('........')
print('..............')
print('Loading… █████[][][][][] 50%')
sleep(2)
print('........')
print('..............')
print('Loading… ████████[] 80%')
sleep(2)
print('........')
print('..............')
print('Loading… ████████████████████ 100')
sleep(2)
print('........')
print('..............')

print(f'{Crs.ciano} Você sai do elevador e pensa onde ir ')
sleep(3)
print('')
sleep(2)
input(' Pressione enter para continuar.')
print()
L1 = 'Praça central'
L2 = 'Casa da sua irmã'

print()

print(f''' {Crs.cinzaescuro} Qual lugar você quer ir?

--------------------

[1]Casa da sua irmã




''')

escolha_do_usuário = int(input(f'{Crs.ciano}Sua escolha: '))
if escolha_do_usuário  == 1:

   print('Escolheu bem,a Casa da sua irmã é um otimo lugar para tirar duvidas')
   sleep(5)
   print('...........')
   sleep(2)
   print('.................')
   print('...............')


 
  #Casa da irmã

   print('''
  
  ┼┼┼┼┼┼┼┼┼┼┼┼████████████████
┼┼┼┼┼┼┼┼┼┼┼┼██▒██▒███▒██▒███
┼┼┼┼┼┼┼┼┼┼┼███████▒█▒████████
┼┼┼┼┼┼┼┼┼┼┼████████▒█████▒█▒█
┼┼┼┼┼┼┼┼┼┼████████▒█▒█████▒███
┼┼┼┼┼┼┼┼┼┼████▒██▒███▒███▒█▒██
┼┼┼┼┼┼┼┼┼████▒▒▒███████████████
┼┼┼┼┼┼┼┼┼████▒▒▒████████████▒██
┼┼┼┼┼┼┼┼████▒▒▒▒▒███▒█▒█████████
┼┼┼┼┼┼┼┼████▒▒▒▒▒████▒███▒██▒███
┼┼┼┼┼┼┼████▒▒▒▒▒▒▒██▒█▒███▒█▒████
┼┼┼┼┼┼┼████▒▒▒▒▒▒▒█████████▒█████
┼┼┼┼┼┼████▒▒▒▒▒▒▒▒▒███████▒█▒█████
┼┼┼┼┼┼████▒▒▒▒▒▒▒▒▒███▒██▒███▒████
┼┼┼┼┼████▒▒▒▒▒▒▒▒▒▒▒███████████████
┼┼┼┼┼████▒▒▒▒▒▒▒▒▒▒▒███████▒███▒███
┼┼┼┼████▒▒▒███████▒▒▒███████████████
┼┼┼┼████▒▒▒█░░█░░█▒▒▒████▒███▒██████
┼┼┼████▒▒▒▒█░░█░░█▒▒▒▒████▒█▒███▒█▒██
┼┼┼████▒▒▒▒███████▒▒▒▒█████▒█████▒███
┼┼████▒▒▒▒▒█░░█░░█▒▒▒▒▒███▒█▒███▒█▒███
┼┼████▒▒▒▒▒█░░█░░█▒▒▒▒▒██▒███▒████████
┼████▒▒▒▒▒▒███████▒▒▒▒▒▒████████████▒██
┼████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███▒███████████
█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███████████████
█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███████████████
┼┼┼┼█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒█▒█▒█▒█▒█▒█
┼┼┼┼█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████████████
┼┼┼┼█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████████████
┼┼┼┼█▒▒▒█░█░█░█░█░█░█▒▒▒████▒▒▒▒▒▒▒███
┼┼┼┼█▒▒▒█████████████▒▒▒████▒░░▒░░▒███
┼┼┼┼█▒▒▒█░█░░░█░░░█░█▒▒▒████▒░░▒░░▒███
┼┼┼┼█▒▒▒███░░░█░░░███▒▒▒████▒░░▒░░▒███
┼┼┼┼█▒▒▒█░█░░░█░░░█░█▒▒▒████▒░░▒░░▒███
┼┼┼┼█▒▒▒█████████████▒▒▒████▒▒▒▒▒▒▒███
┼┼┼┼█▒▒▒█░█░░░█░░░█░█▒▒▒████▒░░▒░░▒███
┼┼┼┼█▒▒▒███░░░█░░░███▒▒▒████▒░░▒░░▒███
┼┼┼┼█▒▒▒█░█░░░█░░░█░█▒▒▒████▒░░▒░░▒███
┼┼┼┼█▒▒▒█████████████▒▒▒████▒░░▒░░▒███
┼┼┼┼█▒▒▒█░█░░░█░░░█░█▒▒▒████▒▒▒▒▒▒▒███
┼┼┼┼█▒▒▒███░░░█░░░███▒▒▒██████████████
┼┼┼┼█▒▒▒█░█░░░█░░░█░█▒▒▒██████████████
┼┼┼┼█▒▒▒█████████████▒▒▒██████████████
┼┼┼┼█▒▒▒█░█████████░█▒▒▒██████████████
┼┼┼┼█▒▒▒█████████████▒▒▒██████████████
┼┼┼┼█▒▒▒█░█████████░█▒▒▒██████████████
┼┼┼┼█▒▒▒█████████████▒▒▒██████████████
┼┼┼┼█▒▒▒█░█████████░█▒▒▒██████████████    ''')

   print ('Você vai até a casa da sua irmã e lá pergunta sobre a nova doença e por quanto tempo esteve fora ')
   print(f' {Crs.amarelo}Ela te responde que você sumiu por 1 mês e que todos estavam preucupados com você!')
   print (f' {Crs.branco}Você fala o que lhe aconteceu e pergunta novamente sobre a nova doença')

sleep(1)
print('.')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(1)
print('Está na hora de ir... ')
sleep(1)
print()


print(f' {Crs.branco}  {personagem} : POR QUE?!!"')
print (f'{Crs.amarelo } Irma: VOCÊ SUMIU POR 1 MES NOSSA MÃE PRESUMIU QUE VOCÊ ESTAVA MORTO')
print (f'{Crs.amarelo } Irma: ELA FOI PROCURAR VOCÊ NO ULTIMO NIVEL DA CIDADE E ACABOU CONTRAINDO A Black Allergy ESSA DOENÇA ESTÁ MATANDO A TODOS AQUI MAS ELA FOI A PRIMEIRA POR SUA SUA CULPA!')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(1)
print(f'{Crs.branco} {personagem} CO COMO?....')
print(f'{Crs.branco} Você senta e começa a chorar')
print (f'{Crs.branco} Você sai da casa da sua irmã com ódio e planeja de uma vez por todas que tornará publico quem fez a doença')

print (f'{Crs.branco}Você olha para trás pela ultima vez e deseja que sua irmã fique bem')



sleep(1)
print('.')
sleep(1)       
sleep(2)
input(' Pressione enter para continuar.')

#Fim da introdução começo do jogo 



#Começo do jogo na praça central
print (f'{Crs.branco} Você vai até a praça central')

print (f'{Crs.branco} Você se senta em um banco e pensa em como vai juntar novamente as provas para poder ir a público')

sleep(1)
print('.')
sleep(1)       
sleep(2)

print (f'{Crs.branco} Você se lembra que as empresas SilverLight tem uma pequena filial no nivel médio')


sleep(1)
print('.')
sleep(1)       
sleep(2)

print (f'{Crs.branco} Você decide ir até a filial')


sleep(1)
print('................')
sleep(1)   
print('................')
print('...................')
sleep(2)
print (f'{Crs.branco} Você começa a andar pela cidade e se depara com diversos corpos caidos pelas ruas todas as casas fechadas entre diversas outras coisas')
#Decisão Crucial para historia primeiro game over
print (f'{Crs.branco} Você atravessa uma rua e uma idosa pede um pouco de comida')
print('''
                                                                 
                                        ████████                                        
                                    ████▓▓▓▓▓▓▓▓████                                    
                                  ██▓▓▓▓▓▓░░░░▓▓▓▓▓▓██                                  
                                ██▓▓▓▓▓▓░░▒▒▒▒░░▓▓▓▓▓▓██                                
                              ██▓▓▓▓▓▓░░░░░░░░░░░░▓▓▓▓▓▓██                              
                              ██▓▓▓▓████████████████▓▓▓▓██                              
                              ██▓▓██░░░░░░░░░░░░░░░░██▓▓██                              
                              ██▓▓██░░░░░░░░░░░░░░░░██▓▓██                              
                              ██▓▓██░░░░██░░░░██░░░░██▓▓██                              
                              ██▓▓██░░░░██░░░░██░░░░██▓▓██                              
                            ██▓▓▓▓▓▓████░░░░░░░░████▓▓▓▓▓▓██                            
                            ██▓▓▓▓██░░░░████████░░░░██▓▓▓▓██                            
                              ████░░░░▒▒▒▒░░░░▒▒▒▒░░░░████                              
                                ██░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░██                                
                                ██░░██▒▒▒▒░░░░▒▒▒▒██░░██                                
                                ██░░██░░░░░░░░░░░░██░░██                                
                                  ████░░░░░░░░░░░░████                                  
                                    ██░░░░░░░░░░░░██                                    
                                    ██░░░░████░░░░██                                    
                                    ██▒▒▒▒████▒▒▒▒██                                    
                                      ████    ████           
''')
sleep(5)
print('......')
print ('''


[1] Ignorar e seguir reto
[2] Ajudar ela







''')

escolha_do_usuário = int(input(f'{Crs.ciano}Sua escolha: '))

escolhadaidosa = 0

if escolha_do_usuário  == 1:
  escolhadaidosa += 1
  print (f' {Crs.ciano}Você ignora a idosa e ela fala que o mundo dá voltas')

elif  escolha_do_usuário  == 2:
  escolhadaidosa += 2
  print (f''' {Crs.magentaclaro}
  VOCÊ DECIDE DAR UM CUPCAKE PARA A IDOSA


 ___________________¶¶¶¶¶¶
_________________¶¶¶¶¶___¶¶
________________¶¶¶¶¶¶¶___¶
_______________¶¶¶¶¶¶¶¶¶¶¶¶¶
___________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
________¶¶¶¶¶___¶¶¶¶¶¶¶¶¶¶¶____¶¶¶¶¶
_____¶¶¶¶_________¶¶¶¶¶¶¶__________¶¶¶
____¶¶¶______¶____________________¶__¶¶¶
___¶¶________¶¶__¶¶_____¶¶__¶¶¶________¶¶
__¶¶_______________¶¶__¶¶_____¶¶¶_______¶¶
_¶¶______________________________________¶
¶¶________________________________________¶
¶¶________________________________________¶
_¶¶¶____________________________________¶¶
___¶¶¶¶¶____________________________¶¶¶¶¶
____¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶
_____¶____¶_____¶____¶¶____¶_____¶¶___¶¶
_____¶____¶¶____¶____¶¶____¶_____¶____¶
_____¶¶____¶____¶¶___¶¶___¶¶____¶¶___¶¶
______¶____¶¶___¶¶___¶¶___¶¶____¶____¶
______¶¶____¶___¶¶___¶¶___¶¶___¶¶___¶¶
_______¶____¶¶___¶___¶¶___¶____¶¶___¶
_______¶¶___¶¶___¶___¶¶___¶____¶___¶¶
________¶____¶¶__¶¶__¶¶__¶¶___¶¶___¶
________¶¶____¶___¶__¶¶__¶___¶¶__¶¶  ''')

  print()
print('......')
sleep (2)
print('.........')
sleep (2)
print()
print('......')
sleep (2)
print('.........')
sleep (2)

print (f' {Crs.branco}Você sai de perto dela e segue em seu caminho')

sleep (2)
print()
print('......')
sleep (2)
print('.........')
sleep (2)

print ('Você de longe avista a filial')
sleep (2)
print()
print('......')
sleep (2)
print('.........')
sleep (2)


print ('''
                 VOCÊ CHEGOU NA FILIAL


                 ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼███
┼┼┼┼┼┼┼┼┼┼┼┼┼███████
┼┼┼┼┼┼┼┼┼┼██████████████
┼┼┼┼┼┼┼████████████████████
┼┼┼┼██████████████████████████
┼████████████████████████████████
██████████████████████████████████
┼████████████████████████████████
┼█░░░░██░░░░██████████░░░░██░░░░█
┼█░░░░██░░░░██████████░░░░██░░░░█
┼█░░░░██░░░░██████████░░░░██░░░░█
┼████████████████████████████████
┼█░░░░██░░░░██████████░░░░██░░░░█
┼█░░░░██░░░░██████████░░░░██░░░░█
┼█░░░░██░░░░██████████░░░░██░░░░█
┼████████████████████████████████
┼████████████████████████████████
┼████████████████████████████████
┼█░░░░██░░░░██████████░░░░██░░░░█
┼█░░░░██░░░░█▒▒▒▒▒▒▒▒█░░░░██░░░░█
┼█░░░░██░░░░█▒▒▒▒▒▒▒▒█░░░░██░░░░█
┼████████████▒▒▒░░▒▒▒████████████
┼█░░░░██░░░░█▒▒▒▒▒▒▒▒█░░░░██░░░░█
┼█░░░░██░░░░█▒▒▒▒▒▒▒▒█░░░░██░░░░█
┼█░░░░██░░░░█▒▒▒▒▒▒▒▒█░░░░██░░░░█
┼████████████▒▒▒▒▒▒▒▒████████████
┼████████████▒▒▒▒▒▒▒▒████████████
┼████████████▓▓▓▓▓▓▓▓████████████
████████████▓▓▓▓▓▓▓▓▓▓████████████
███████████▓▓▓▓▓▓▓▓▓▓▓▓██████████''')

print ('Como você irá entrar?')
print ('''

[1] Entrar pelo esgoto

''')
escolha = input (f' {Crs.ciano}Sua Escolha: ')
if escolha.lower().strip() == '1':
  print(' Você avista uma passagem pelo esgoto da filial e se apressa para entrar ')

  print('No meio das aguas sujas do esgoto você avista uma coisa')
  sleep(5)
  print('........')
  sleep(2)
  print('''
         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░█▓░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░█▒░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░▒██░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░▓█▒▓▒░░░░░░░░░░░░░░░░▓██▒░░░░░░
░░░░░░░░░░░░▒██░░░░░░░░░░░░░▒██▓░░░░░░░░░
░░░░░░░░░░░░░▒▓▓▒░░░░░░░░░▒▓▓▒░░░▒▒▓░░░░░
░░░░░░░░░░░░░▓▒░▒▓░░▒▒░░░▓▓░░░░██▓▓▒░░░░░
░░░░░░░░░░░░░▓█░░░▓▓███░▓▒░░░░░█░░░░░░░░░
░░░░░░░░░░░░░▒█▓░░░█████░░░░░░▓▓░░░░░░░░░
░░░░░░░░░░░░░░▓█░░░█████░░░░░░█▒░░░░░░░░░
░░░░░░░░░▒▒▒░░▓██▒██████▒░░░░██░░░░░░░░░░
░░░░░░░░░░░▒▒░░▓████████▓░░▓█▓▒░░░░░░░░░░
░░░░░░░░░░░░░░░▒█████████▓█▓░▓▓░░░░░░░░░░
░░░░░░░░░░▒▓▓▓█████████████░▓▒░░░░░░░░░░░
░░░░░░░░░░███████████████████▓▒▒▒▒▒▓█▓█▒░
░░░░░░░░░▒██████████████████████░▒██▒▒▒░░
░░░░░░░░▓▓▒█████▓▒▒▒▓▓▒▓███████▒░▒░░░░░░░
░░░░░░▒▓░░░███████▓▓▓▓▓████████▒░░░░░░░░░
░░░▒███▓▒▒▓███████████████████▒░░░░░░░░░░
░░██▒░░░░░▒███████████████████▒░░░░░░░░░░
░░░░░░░░░░░███████████████████▓▒░░░░░░░░░
░░░░░░░░░░░███████████████████▒░░░░░░░░░░
░░░░░░░███████████████████████▒░░░░░░░░░░
░░░░░░▓█▒░░███████████████████░░░░░░░░░░░
░░░░░░▓▒░░▓███████████████████░░░░░░░░░░░
░░░░░░░█▓▓████████████████████▒░░░░░░░░░░
░░░░░░▒█▒░▓███████████████████▓█▓░░░░░░░░
░░░░░░░█░░▓███████████████████░▒█▒░░░░░░░
░░░░░░░▓▒░▒███████████████████▓▒▓▒░░░░░░░
░░░░░░░▒█░▒██████████████████▒░▓█░░░░░░░░
░░░░░░░░█▒░█████████▓████████▒░▒█░░░░░░░░
░░░░░░░░▒█░██████████████████▒░▓▒░░░░░░░░
░░░░░░░░░██▓████████████████▓░▒▓░░░░░░░░░
░░░░░░░░▒█▒▓████████████████▓░▓▒░░░░░░░░░
░░░░░░░▒█░░▓███████████████▓▒▓▓░░░░░░░░░░
░░░░░░▒█░░░▒▓█████████████▓▓▓█░░░░░░░░░░░
░░░░░░░░░░░░▓▓████████████▓██░░░░░░░░░░░░
░░░░░░░░░░░░▓▓███████████▓▓█▓░░░░░░░░░░░░
░░░░░░░░░░░░░▓██████████▓▓▒░█░░░░░░░░░░░░
░░░░░░░░░░░░░▒▓█████████▓▒░░▒▓░░░░░░░░░░░
░░░░░░░░░░░░░░▓▓██████▓▓▒░░░░█▒░░░░░░░░░░
░░░░░░░░░░░░░░░▓▓▓███▓▓▒░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░
  
  ''')
  print('........')
  print('Você avista uma barata!')
  print('Você sente vontade de gritar')
  print('........')
  sleep(5)
  print('Você continua a se arrastar pelo esgoto e entra na filial')
  print('......')
  sleep(5)
  print('Dentro da filial você se depara com diversos caminhos qual irá escolher?')
  saida = True
while saida: 

  print(f''' 
  
  
  [1] Andar de cima
  [2] Seguir reto
  [3] Sair da filial 
  
  
  
  
  ''')
  escolha = int(input(' Selecione o que deseja fazer: ' ))
  print('.......')
  sleep(5)
  print(f'{escolha}');

  if escolha == 1: 
    print('Você entrou no andar superior e encontrou um escritório.')
    print('''

  [1] Vasculhar gaveta
  [2] Entrar no computador
  [3] Vasculhar lixo
  [4] Sair do escritório
  
  
   ''')
    #escritorio
    escritorio = int(input('Selecione o que quer fazer:  '))
    sleep(5)
    print('....')
    print(escritorio)

    if escritorio == 1:
      print('Você vasculhou as gavetas e encontrou diversos papeis bagunçados .')
    elif escritorio == 2:
      print('Você tenta entrar no computador mas ele está protegido com senha.')
    elif escritorio == 3:
      print('Você vasculha o lixo e encontra uma pagina rasgada e a guarda')
      sleep(5)
    elif escritorio == 4:
      print('Você saiu do escritorio.')
      

  #Seguir reto

  if escolha == 2:
    print('Você Seguiu reto e encontrou uma sala de vigia.')

    vigia = 0

    while vigia < 4:
      print(vigia)
      print('''
      
      [1] Verificar as cameras
      [2] Verificar as gavetas
      [3] Verificar o computador
      [4] Sair da sala de vigia
      
      ''')
      vigia = int(input('Selecione o que quer fazer:  '))
      if vigia == 1:
        print('Você verificou as cameras de segurança e notou guardas entrando pelos fundos seja rapido!!')
      elif vigia == 2:
        print('Você verificou as gavetas e encontrou diversas fotos e um crachá de acesso ao nivel alto .')
      elif vigia == 3:
        print('Você verificou a gaveta de baixo  e conseguiu diversos documentos antigos.')
        print('Você guarda todos os achados')
      elif vigia == 4:
        print('Você saiu da sala de vigia.')
        

  if escolha == 3:
      print('Você saiu da filial com todos os documentos guardados ')
      saida = False
    

print('Logo após a saida da filial você se depara com diversos guardas te seguindo')
sleep(5)
print('..........')
sleep(1)
print('Você começa a correr')
print('......')
sleep(3)
print(f'''{Crs.branco}
                                  ░░░░░░░░                  
                                ▓▓▒▒▓▓    ▒▒░░              
                              ▓▓▒▒▒▒                        
                            ▒▒▒▒▒▒▒▒                        
                          ░░▒▒▒▒▒▒                          
                          ▓▓▒▒▒▒▒▒              ░░          
                          ▓▓▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    
                          ▓▓▒▒▒▒██████████░░▓▓░░▓▓          
                          ▒▒▓▓▓▓▓▓██▒▒░░░░░░░░░░▒▒          
                            ▓▓▓▓░░  ░░      ░░░░▒▒          
                              ██░░                ░░        
                            ▒▒██▓▓▒▒          ▓▓  ░░        
                      ████▓▓░░██▓▓▒▒░░          ▒▒          
                  ▒▒██▒▒      ██▓▓██░░▒▒░░░░░░░░            
              ░░▓▓░░░░░░    ▓▓▓▓▓▓██▓▓████▓▓  ▒▒░░          
          ▓▓░░░░░░░░▓▓▓▓██▓▓▓▓▓▓▓▓▓▓░░████▓▓▒▒▒▒  ░░        
          ░░    ░░░░▓▓██▓▓▓▓▓▓▓▓▒▒██░░▓▓▒▒▒▒████░░░░        
      ░░        ▒▒  ▒▒▓▓▓▓████▒▒▒▒░░░░▒▒██░░░░░░▒▒          
        ▒▒    ████    ██▓▓▓▓▓▓▓▓▒▒░░▓▓██  ▓▓▓▓              
          ░░░░        ████▒▒▒▒▒▒░░████                      
      ██▒▒          ▓▓▒▒██▒▒░░░░▒▒    ██                    
    ░░░░▓▓▓▓      ░░██▒▒▒▒██▓▓▓▓░░  ▓▓░░                    
    ▒▒▓▓▓▓▓▓██████▒▒░░██▒▒▒▒  ▒▒░░▒▒  ░░                    
  ▒▒▓▓▓▓▓▓▓▓██▒▒██░░▒▒          ▒▒    ▓▓░░░░▓▓░░▓▓          
  ▒▒▒▒▒▒▓▓████░░░░░░                    ▒▒▒▒  ██▒▒▓▓▒▒▒▒▒▒▒▒
  ▒▒▓▓██▒▒▓▓██                            ██  ▒▒██░░  ▓▓▒▒░░
  ▒▒▓▓░░░░██▒▒                              ▓▓▒▒▒▒▓▓▓▓▒▒░░▒▒
  ▒▒▓▓                                      ▒▒▒▒▒▒▒▒▒▒░░▒▒  
                                              ▒▒▒▒▒▒  ▒▒    
                                                ▒▒░░░░      
                                                ░░░░        
        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓            


''')
sleep(2)
print(f' {Crs.ciano}Correndo você avista a idosa novamente')
print('..........')
sleep(2)
print('..........')
sleep(1)
print('Ela se lembra da sua escolha anterior ')

if escolhadaidosa == 1:
  print('Você negou ajuda a idosa')
  print('.....')
  sleep(2)
  print('Ela grita e alerta os guardas')
  sleep(5)
  print('.......')
  print('Você foi preso!')
  sleep(5)
  print('......')
  print('........')
  print('''
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼███┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██████┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼████████┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██████████┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼████████████┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██████████████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼████████████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█████████┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼█┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼███┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼████┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼██████┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼''')
  sys.exit() 

elif escolhadaidosa == 2:
  print('Você ajudou a idosa e ela te escondeu dentro da casa dela')
  sleep(5) 
  print('.........')
  sleep(2)
  print('...........')

print(f'{Crs.branco}Dentro da casa da idosa você explica para ela todo ocorrido')
print('......')
sleep(3)
print(f'{Crs.ciano}Ela diz que é impossivel pois as empresas SilverLight esta ajudando a todos')
print('e pergunta se você tem provas?')
print('.....')
sleep(5)
print('....')
print(f'{Crs.branco}Você lembra que pegou diversos documentos dentro da filial')
print('Você mostra para ela todos os documentos')
sleep(5)
print('........')
print(f' {Crs.ciano}Ela diz que isso é impossivel')
print('Ela cai em si e diz que acredita em você')
sleep(2)
print('....')
print('A idosa conta que seu nome é selena')
print(f"Prazer selena meu nome é {personagem}")
sleep(2)
print('...')
print(f' {Crs.ciano}Selena lhe conta que antes do caos se espalhar pela cidade ela era uma subordinada proxima do prefeito do nivel médio')
print('.........')
sleep(2)
print('Ela lhe pergunta se pode fazer copias dos seus documentos para mostrar para o prefeito')
print('.........')
sleep(5)
print(f'{Crs.branco}Você entrega os documentos para ela e ela vai até a copiadora')
sleep(5)
print(f'{Crs.azulclaro}........')
sleep(2)
print('''
      ████████████████      
      ██            ██      
      ██            ██      
████████████████████████████
██                        ██
██                    ██  ██
██                        ██
██                        ██
██    ████████████████    ██
████████            ████████
      ████████████████      
''')
sleep(5)
print('.....')
sleep(5)
print('''
        ████████████████████████████        
        ██                        ██        
        ██                        ██        
        ██                        ██        
        ██                        ██        
        ██                        ██        
████████████████████████████████████████████
██                                        ██
██    ████████████████████████████████    ██
██    ██                            ██    ██
██    ████████████████████████████████    ██
██        ██                    ██        ██
██        ██                    ██        ██
██        ██    ████████████    ██        ██
██        ██                    ██        ██
████████████    ████████████    ████████████
          ██                    ██          
          ██    ████████████    ██          
          ██                    ██          
          ██                    ██          
          ██████████            ██          
            ██    ██            ██          
              ██████            ██          
                ██████████████████          
''')
sleep(5)
print('....')
print(f'{Crs.ciano}Ela diz que vai ter uma reunião com o prefeito ')
sleep(2)
print('E que irá explicar para ele o que está acontecendo para saber se vão a publico')
print(f'{Crs.branco}Você agradece a idosa e vai verificar se os guardas já foram')
print(f'{Crs.ciano} Ela te recomenda para ficar lá por algumas horas e esperar ficar de noite para você sair')
print(f'{Crs.branco} Você agradece a ela e espera até de noite')
sleep(2)
print('........')
print('..............')
print('Loading… ██[][][][][][][][] 20%')
sleep(2)
print('........')

sleep(2)
print('........')
print('.............')
print('..............')
print('Loading… ████[][][][][][][] 40%')
sleep(2)
print('........')
sleep(2)
print('........')
print('..............')
print('Loading… ██████████████████[] 80%')
sleep(2)
print('........')
print('..............')
print('Loading… ████████████████████ 100%')
sleep(2)
print('........')
print('..............')
sleep(2)
print('........')
print('..............')
print(f'{Crs.branco}Depois de esperar algumas horas você nota que começou a chover')
print('''
_______________▄▄▄▄▄▄__▄▄▄▄▄ 
__________▄▄▀▀_______▀▀▀____▀▀█▄
_____▄▄▄█▀________________▄▄▄▄▄██▄
__█▀▀▄▄▄▄▄▄▄██████████████████▄
_███████████████████████████████▄
█████████████████████████████████
▀████████████████████████████████
_▀██████████████████████████████▀
___▀██████████████████████████▀▀
__________▀███████████████████▀
________▄▄____▀▀▀▀▀▀_____▄_▀▀
_____▄███_________▄____▄██
___█████_______▄██___████____▄
____▀██▀_____▄████___▀▀▀__▄██
__________▄█__████________████
_______▄███___▀▀_________████
________▀▀_________________▀▀
________▄________________▄
____▄███_________▄____▄██
__█████_______▄██___████____▄
___▀██▀_____▄████___▀▀▀__▄██
_________▄█__████________████
______▄███___▀▀_________████
_______▀▀_________________▀▀



''')
print(f'{Crs.ciano}Selena te dá um guarda chuva ')
sleep(5)
print('....')
print(f'{Crs.branco} Você se despede de selena e agradece pela ajuda')

print(f'{Crs.cianoclaro}Para onde deseja ir?')

print('''


[1] Elevador para o andar do nivel alto
[2] Andar pela cidade


''')


escolha = input (f'{Crs.ciano}Sua escolha: ')
if escolha == '1':
  print('Você seguiu até o elevador para o outro andar e se deparou com outro guarda fortemente armado')

elif escolha == '2':
  print('Você decide andar pela cidade ')
  print('Andando pela cidade você se depara com muitos corpos caidos ')
  print('Você não aguenta aquela visão e decide voltar para ir para o elevador')
  sleep(5)
  print('......')
  print('.......')
  sleep(2)
  print('......')


  print('Você verifica se a arma está carregada e caminha em direção aos guardas')

  print("Com odio no coração você chega atirando e atinge um dando um tiro fatal em sua cabeça")
  sleep(5)
  #SegundoPVP
  
GUARDA_HP = 600
PERSONAGEM = 200



print("Você decide atacar o guarda restante".upper())

print('......')

print(
    f"""

[1] Bastão neon
dano de 1 a 100

[2] Arma
dano de 1 a 250

  """
)

while True:
    escolha = input("Escolha seu ataque: ")

    dano_ataque = random.randint(1, 250)
    if escolha == "1":
        dano_ataque = random.randint(1, 100)
    sleep(5)

    GUARDA_HP -= dano_ataque
    print(f"Você deu {dano_ataque} de dano, o guarda agora está com {GUARDA_HP} de HP.")

    print('O Guarda te ataca: ')
    atq_guarda = random.randint(25, 50)

      
    if escolha == "1":
        atq_guarda = random.randint(25,50)
    sleep(5)

    PERSONAGEM -= atq_guarda
    print(f"o guarda te deu {atq_guarda} de dano, e você agora está com {PERSONAGEM} de HP.")

    if GUARDA_HP <= 0:
        print("O guarda está morto!!")
        break

      

      

    elif PERSONAGEM <= 0:
        print(".......")
        sleep(5)
        print('''
                                      ██████████████                                                  
                      ████████░░░░░░░░██▒▒██                                                  
                  ▓▓██░░▒▒░░░░░░░░░░░░██▒▒██                                                  
              ████▒▒▒▒░░░░░░░░░░░░░░░░██▒▒██                                                  
            ▓▓▒▒▒▒░░░░░░░░░░░░▓▓▒▒▒▒▒▒██▒▒██                                                  
          ██░░░░░░░░░░▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓██▒▒██                                                  
        ██░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒██                                                  
      ██░░░░▓▓▓▓▒▒▓▓▓▓▓▓▓▓██████████████▒▒██                                                  
    ██░░▒▒▓▓▓▓██████████░░            ██▒▒██                                                  
░░██░░▓▓▓▓████                        ██▒▒██                                                  
  ██▒▒████  ▒▒                        ██▒▒██                                                  
░░████                                ██▒▒██                                                  
                                      ██▒▒██                      ██████████████████████      
                                      ██▒▒██                  ████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██      
                                      ██▒▒██                ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██        
                                      ██▒▒██              ██▓▓▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▓██          
                                      ██▒▒██            ██▓▓▒▒▒▒▓▓██░░░░██▓▓▓▓▓▓▓▓██          
                                      ██▒▒██            ██▒▒▓▓▒▒██░░░░░░░░██▓▓▓▓▓▓██          
                                      ██▒▒██          ██▓▓▓▓▓▓██░░░░░░░░░░░░██▓▓▓▓▓▓██        
                                      ██▒▒██          ██▓▓▓▓██░░██▓▓░░░░▓▓██░░██▓▓▓▓██        
                                      ██▒▒██          ██▓▓▓▓██░░▓▓▓▓░░░░██▓▓░░██▓▓▓▓██        
                                      ██▒▒██        ██▓▓▓▓██░░░░░░░░░░░░░░░░░░░░██▓▓▓▓██      
                                      ██▒▒██        ██▓▓▓▓██░░░░░░░░░░░░░░░░██░░██▓▓▓▓██      
                                      ██▒▒██        ██▓▓▓▓▓▓██░░██░░██░░██░░████▓▓▓▓▓▓██      
                                      ██▒▒██          ████▓▓▓▓████░░██░░██░░██▓▓▓▓████        
                                      ██▒▒██              ██▓▓▓▓████████████▓▓▓▓██            
                                      ██████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██            
                                      ██░░░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██          
                                      ██░░░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██        
                                      ████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██      
                                      ██▒▒████▓▓▓▓▓▓▓▓▓▓████▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓    
                                      ██▒▒██  ██▓▓▓▓▓▓██  ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓██    
                                      ██▒▒██  ██▓▓████    ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓██      
                                      ██▒▒██  ████        ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓██░░      
                                      ██▒▒██              ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████          
                                      ██▒▒██              ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓          
                                      ██▒▒██              ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██            
                                      ██▒▒██              ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██            
                                      ██▒▒██              ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██          
                                      ██▒▒██            ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓        
                                      ██▒▒██            ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██      
                                      ██▒▒██            ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██    
                                      ██▒▒▒▒██        ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  
                                        ██▒▒██▓▓      ██▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
                                        ██▒▒██████    ████▓▓▓▓▓▓▓▓████████▓▓████████▓▓▓▓██████
                                        ░░████████            ██████    ██████                
        ''')
        sleep(5)
        print('Você morreu meu camarada muhahahahaha')
        sleep(2)
        print('''
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼███┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██████┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼████████┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██████████┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼████████████┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██████████████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼████████████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█████████┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
        ''')
        sleep(2)
        sys.exit() 
        
       

    print("vamos atacar novamente!".upper())


sleep(5)
print('..........')
sleep(2)
print('Você revista o corpo do guarda e consegue um crachá de acesso para todos os andares ')
sleep(4)
print('''
                                         ░░▒▒▓▓████████████████████████████▒▒            
                            ░░▒▒▓▓▓▓██████████████████████████████████████████▓▓            
              ░░▒▒▓▓██████████████████████████▓▓████░░▒▒  ██████████████████████            
        ▓▓██████████████████████▓▓▒▒░░░░░░████░░████  ██▒▒▓▓████████████████████            
      ▒▒████████████████████░░▓▓  ▒▒░░░░▓▓▓▓██▒▒▒▒▒▒▒▒░░▒▒██████████████████████░░          
      ▓▓████████████████████░░██  ▓▓░░░░▓▓▒▒▓▓██████████████████████████████████░░          
      ▒▒████████████████████▓▓████████████████████▓▓▒▒▒▒██▓▓▒▒▒▒▒▒██████████████░░          
      ░░████████████████████████████▓▓▓▓██  ██  ▓▓░░░░▒▒██▓▓▒▒░░░░██████████████▒▒          
      ░░██████████████▓▓██░░▒▒▓▓████░░░░▓▓░░░░░░░░▒▒▓▓▓▓██████████████████▓▓▓▓▒▒▓▓          
        ██████████████░░░░▒▒██░░████▒▒██▓▓██████████████████▓▓▓▓░░              ██          
        ██████████████▓▓████████████████████▓▓▓▓▒▒░░                            ██          
        ████████████████████▓▓▓▓▒▒░░░░                                          ▓▓          
        ▓▓████▓▓▓▓░░░░                                                          ▓▓░░        
        ▓▓                                                                        ░░        
        ▒▒                                                                      ░░░░        
        ░░                                                                        ▒▒        
          ░░                                                                      ▓▓        
          ▒▒                                                                      ██        
          ▓▓                                                                      ▓▓        
          ▓▓                                                                      ▓▓░░      
          ▓▓                                                                      ▓▓░░      
          ▓▓                                                                      ▒▒░░      
          ░░                                                                  ░░░░▓▓▒▒      
            ░░                                                    ▒▒▓▓██████████████▒▒      
            ▒▒                                  ░░▒▒▓▓▓▓████████████████████████████░░      
            ▓▓                    ░░▒▒▓▓▓▓██████████████████████████████████████▓▓▒▒░░      
            ▓▓    ░░▒▒▓▓▓▓████████████████████████████████████████▓▓▓▓▒▒▒▒▒▒░░░░░░          
            ██████████████████████████████████████▓▓▓▓▒▒▒▒▒▒░░░░░░░░                        
            ▒▒████████████████████▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░                                        
              ▒▒████▓▓▓▓▒▒▒▒▒▒░░░░░░                                                        
''')
sleep(5)
print('Antes de entrar no elevador você olha para trás uma ultima vez')
sleep(5)
print('E deseja que todos fiquem seguros até você tentar resolver tudo')
sleep(3)
print('..........')
print("................")
print('Você entra no elevador')
sleep(5)
sleep(5)
print('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠠⣤⠀⠀⢀⡀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⣀⣀⣀⣁⣀⣀⣉⣁⣀⣀⣀⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠉⢹⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠺⠿⢸⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣤⣤⣼⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣶⣾⣷⣶⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿''')
sleep(2)
print('................')
#Entrada no nivel alto
sleep(3)
sleep(2)
print('........')
print('..............')
print('Loading… ██[][][][][][][][] 20%')
sleep(2)
print('........')
print('..............')
print('Loading… ███[][][][][][][] 30%')
sleep(2)
print('........')
print('..............')
print('Loading… ████[][][][][][] 40%')
sleep(2)
print('........')
print('..............')
print('Loading… █████[][][][][] 50%')
sleep(2)
print('........')
print('..............')
print('Loading… ████████████████ 80%')
sleep(2)
print('........')
print('..............')
print('Loading… ████████████████████ 100')
sleep(2)
print('........')
print('..............')
input(f'{Crs.cianoclaro} Pressione enter para continuar.')


print()

print('O Elevador começa a subir ')
sleep(2)
print('Você chegou no nivel alto da cidade')
sleep(2)
sleep(3)
print('Quando você sai do elevador e vê uma cidade linda funcionando perfeitamente')
sleep(5)
print('''
_______  |      ·                                           ·                                                                                                      .-'· ·   · · · ·   · · · · · ·   · ·|  _______
|`:|::|  |                                                                  _..._            *                       ·                                          _.'··· · · · · · ··· · · · · · · · · · |  |`:|::|
|  |`:|  |                                                                .:#:'~ `                    .'`.                                      ·             .'··· · · · · ··· · · · · ··  · · · · ···|  |  |`:|
|--|--|  |                                                      *        ¡##¡                        /    \                                              _.--'·· · · · · ··· · · · · ··· · · · ··· · · |  |--|--|
|  |  |  |                        *                                      !##!      :            ___.' ·   ·\                                          _.' ··· · · ··· · · ·=··· · · · ··· · · · ··· · ·|  |  |  |
!==!==!  |                                           __                  `:##.                .' · · ·   · ·`.__                 ·         _ _      .' ··· · · ··· · · ···|¨|· ··· · · ··· · · ··· · ··|  !==!==!
         |                                       __.'  `.                  `-:::·'           /· · · ·   · · · · `.                        | | |=|`-----------------·------| |---------. ··· · ··· · ···|         
_______  |   ..                           _____.'        `-----.___                       _.'  · · · · ·   · · · ·`.                      |   | |_|_|_|_|_|_|_|_|_/.\|_|_||¨||_|_|_|_||·:···:· ·::··:· |  _______
|`:|::|  |  /  \           /\    /\     .'  ·   ·   ·   ·   ·   ·  `._____         /\   .'· · · · · ·   · · · · · · `.___        /\       !_!_!=||_|_|_|_|_|_|_|_// \\|_|_! !_|_|_|_|_| · ··· · : : · ·|  |`:|::|
|  |`:|  |-'    `'`'`..'`.'  `..'  `'`./ · ·   ·   ·   · ·   ·   · ·   · ·`.-'`-'`'  `.'·· · · · · · ··· · · · · · ···   `.__.'`'  `·'`·.' ___  |_|_|_|_|_|_|_|_//   \\|_|_|_|_|_|_|_||_ · ··: ·:· ·:· |  |  |`:|
|--|--|  |  ·   .------.    ·  .------'   · · ·   ·   · ·   · ·   ·   · · · \  ·   · /· · · · .------.· ··· · · · ··· · · ···`._ ·  .-~' ·|   |=||_|_|_|_|_|_|_//   ¨ \\|_|_|_|_|_|_|_|:`.·:: : ·:: ::·|  |--|--|
|  |  |  |      !------!      /· · · ·   ·   · · ·   · ·   · ·   · · ·   _ · `.__   /··· · ···!------! · · · · ··· · · · ··· · ·`..'· · · | | | |_|_|_|_|_|_|_//       \\|_|_|_|_|_|_||·:··._: ::· · _.|  |  |  |
!==!==!  |·   · |[][][]| ·   ;· · · · · · · · _ · · · · · · · · · · · ·_|-| ·    `./·:· · ···:|[][][]|· ··· · ·:···    ______....' · · · ·!___!=||_|_|_|_|_|_//   ___   \\|_|_|_|_|_|_|:·:·:·`. ::_.':·|  !==!==!
         |      |[][][]|   .'··_ ··· ··· ··· |-|_··· ··· ··· ··· ··· ·|-|:|· · ·   \_···:·:···|[][][]|····:·:·..---~~~~:·:·:_:·:·:·:·:_ ·  ___  |_|_|_|_|_|_//  .:___:.  \\|_|_|_|_|_||·:_:·:·:\.' _:·:|         
_______  |------|[][][]| _::·_|-|_:.------.:_|:|-|_:··_:_·_·: _:_ ··: |:|:| ····=· |-|:.------|[][][]|:_:_::.'_ _.------.:_|-|_·:·:·_|-|_:|_ _|=||_|_|_|_|_//  ||_|_|_||  \\|_|_|_|_|_|:|-|_·:·:·_|-|_·|  _______
|`:|::|  |------|[][][]||-|_|-|:|-|!------!|-|:|:|-|_|-|-|-|_|-|-|.------------|¨|---.|!------|[][][]||-|-|/ |-|-|------!|-|:|-|:_:|-|:|-| | |  |_|_|_|_|_// ¨ ||_|_|_||   \\|_|_|_|_||-|:|-|·_·|-|:|-||  |`:|::|
|  |`:|  |[][][]|[][][]||:_ .------|[][][]||:_:___:_-_:_:_:_-_:_: ||_|_|_|_/\|_!_!_|_|:|[][][]|[][][]|::_:.------|[][][]|::_::::|-i------::|_|==||_|_|_|_//    ||_|_|_||    \\|_|_|_|_|:_::::|-i------:|  |  |`:|
|--|--|  |[][][]|[][][]|:|-|!------|[][][]|:|-¡++/\++++/\++++/\++¡|_|_|_|_//\\|_|_|_||:|[][][]|[][][]|:|-|!------|[][][]|:|-|:_:|:!------!:___::|_|_|_|_//     `·=====·'     \\|_|_|_|||-|:::|:!------!|  |--|--|
|  |  |  |[][][]|[][][]|:|:||[][][]|[][][]|:|:|+/__\++/__\++/__\+|||_|_|_//¨ \\|_|_|_|:|[][][]|[][][]|:|:||[][][]|[][][]|:|:||-|::|[][][]|| __!=||_|_|_//   ¨     ___         \\|_|_|_||:|·=·::|[][][]||  |  |  |
!==!==!  |[][][]|[][][]|·=·:|[][][]|[][][]|·=·|/ HH \/ HH \/ H·=·||_|_|_//    \\|_|_||:|[][][]|[] _______ |[·=·[]|[][][]|::::::·=·|[][][]|| __! |_|_|_// __     .:___:.  ¨  __ \\|_|_||:::|¨|::|[][][]||  !==!==!
         |--------------|¨|----------------|¨|. .-------------| |-||_|_//.----.\\|_|_|_!__TT__!__¡+++++++¡--|¨|-------------.:.| |--------!___!=||_|_//.'__`.  ||_|_|_||  .'__`.\\|_|_`---| |----------|         
_______  |_|_|_|_|/\|_|_!_!_|_|_|_|_/\|_|_|| || |_|_|_|_|/\|_||¨|||_|_//||_||_||\\|_||===========|+++++++||_!_!_|_/\|_|_|_|_|_||¨||_|_|/\| _ |_||_|_//||_||_|| ||_|_|_|| ||_||_||\\|_|_|_|| ||/\|_|adel|  _______
|`:|::|  ||_|_|_|//\\|_|_|_|_|_|_|_//\\|_|_!_!|_||_|_|_|//\\|_!_!_||_// ||_||_|| \\|_|+++++/\++++|¯¯¯¯¯¯¯|_|_|_|_//\\|_|_|_||#|!_!_|_|//\\| |===||_// ||_||_|| ||_|_|_|| ||_||_|| \\|_|_|_!_!//\\|faure|  |`:|::|
|  |`:|  |_|_|_|//  \\|_|_|_|_|_|_//  \\|_|_|_|-|_|_|_|//  \\|_|_||_//¨ ||_||_||¨ \\||+++·=·_\+++|·[==][=||_|_|_//  \\|_|_|_|#|_|_|_|// ¨\| |_ ||_//  ||_||_|| `·=====·' ||_||_||  \\|_|_|_|// ¨\\|2022|  |  |`:|
|--|--|  ||_|_|//  ¨ \\|_|_|_|_|_//  ¨ \\|_|_||-||_|_|// ¨  \\|_|_|//              \\|+++|¨|H \++|·.·.·.·|_|_|_//    \\|_|_||#||_|_|//    !___!=|//  ¨        ___________           \\|_|_|// __ \\|_|_|  |--|--|
|  |  |  |_|_|//.----.\\|_|_|_|_//.----.\_____|:|_|_|//.----.\\|_||' .---.  ¨ .---. `|+.-| |-------------'|_|_//.----. _____|¯|_|_|//.----.\\|_||' .---.    .:___________:.  ¨ .---.  _____ .'__`.\\|_||  |  |  |
!==!==!  ||_|//||_||_||\\|_|_|_//||_||__(.   _)__|_|//||_||_||\\|_| ||_|_||  ||_|_|| |+|_!_!_|_|/\_|_|_|_|_|_//||_|| _(.   _)__|_|//||_||_||\\|_| ||_|_||  ||_|_|_|_|_|_|_||  ||_|_||(.   _)__||_||\\|_|  !==!==!
         |_|// ||_||_|| \\|_|_// ||_||(:.:._(.  .)|// ||_||_|| \\|| ||_|_||  ||_|_|| |-||_|_|_|//\\_|_|_|_|_// ||_||(:.:._(.  .)|// ||_||_|| \\|| ||_|_||  ||_|_|_|_|_|_|_||  ||_|_(:.:._(.  .)|_|| \\||         
_______  ||// ¨||_||_||  \\|_//  ||_|(__  (.     .)/  ||_||_||  `~' ||_|_||¨ ||_|_|| |:|_|_|_|//  \\_|_|_|_//  ||_|(__  (.     .)/¨ ||_||_|| ¨\\| ||_|_||¨ `·=============·'  ||_|(__  (.     .)_||  \\|  _______
|`:|::|  |//              \\//  ¨    ( .).:::.   _)___ ___     ¨___ ___ ___ ___ ___  |:||_|_|// __ \\_|_|_//  ¨    ( .).:::.   _)___ _ _ ___ __`'___       ___ ___ ___ ___ __     ( .).:::.   _)_||   `|  |`:|::|
|  |`:|  |' .---.  ¨ .---. `' .---. (_.::::(_   _)¡ _ ¡  _|    | __!_ _¡   ¡ _ ¡ __! |:|_|_|//|====|\\_|_// .---. (_.::::(_   _)¡ _ ¡ ! ¡   ¡   ¡ __!     ¡ __!_ _¡   ¡ _ ¡ _!   (_.::::(_   _)      ¨ |  |  |`:|
|--|--|  | ||_|_||  ||_|_||¨ ||_|_|| (__):::::__) | __! |_   ¨ !__ || || | |   ! __! |_||_|//|======|\\ // ||_|_|| (__):::::__) | __!   | | | | | __!  ¨  !__ || || | |   ! _!    (__):::::__) ¨       |  |--|--|
|  |  |  | ||_|_||  ||_|_||  ||_|_||  ||(_____)_|¨!_! !___|____!___!!_!!___!_!_\.__! |_|_|//  |====|  \V/  ||_|_||  ||(_____)-| !_! !_!_!___!_!_!___!_____!___!!_!!___!_!_\._!  ¨  .:(_____)---------. |  |  |  |
!==!==!  | ||_|_||¨ ||_|_||  ||_|_||  ||_||:| |_| :--------------------------------:¨|_||//  |======|  ¨   ||_|_||  ||_||:| | |¨:--------------------------------------------:    ./\:\|:| H O T E L | |  !==!==!
         |                 ¨              |:| | | | Por favor compre computadores | | |//    ¨          ¨              |:| |-| | Compre celulares não computadores  |   .:\/\:|:|-----------' |         
_______  |¨ .---.    .---.    .---.  ¨ .--|:| | |_|--------------------------------| | |' .---.    .===.    .---.  ¨ .--|:|¨| |_|--------------------------------------------|  ./::\: |:|  .-----. _  |  _______
|`:|::|  |  | 1 | ¨ ||_|_||   | 2 |   ||_||:| |·|3||¯¯¯|  .---. .---. .---. .---.  | | |¨|=====| ¨||\ <||   | 5 |   ||_||:| |·|6||¯¯¯|    __   __   __   __   __   __   __   | .:\::·· |:|  |  |  ||7| |  |`:|::|
|  |`:|  |  |  o|   ||_|_||   |  o|   ||_||:|¨| |¯|| __| .|[=]|-|[=]|-|[=]|-|[=]|. | | |  |===|   ||/ /||   |  o|   ||_||:| | |¯|| __| .-([])-([])-([])-([])-([])-([])-([])-.|:/\:\/.  |:|  | o|o | ¯  |  |  |`:|
|--|--|  | ¨|   |   ·=====· ¨ |   |¨  ·===|:| |·| || ~~| |·===· ·===· ·===· ·===·| |¨| | |=====|  ·=====· ¨ |   | ¨     |:|¨|·| || ~~| |  ¯¯   ¯¯   ¯¯   ¯¯   ¯¯   ¯¯   ¯¯  ||:\/\:·   |:|  |  |  | ¨  |  |--|--|
|  |  |  |__|---|{0}{0}{0}{0}_|---|_______|:|_| |_||___| ! 666§  799§  899§  999§! |_| |__|---|_____________|---|_______|:|_| |_||___| ! 299§ 399§ 499§ 599§ 699§ 799§ 999§ !|·:\      |:|__|-----|____|  |  |  |
!==!==!  | ` ' `(\|/\|/\|/\|/):` ' ` ' ` '|:|' ` ' ` ' `¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯` ' ` ' ` ':·············:  ` ' ` ' ` :|` ' ` ' `  ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|:| ` ' ` ' ` ' |  !==!==!
         | ' ` '`~~~~~~~~~~~~~'' ` ' ` '.-|:|-.' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ``~~~~~~~~~~~~~'` ' ` ' `.-|:|-.` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' .-|:|-. ` ' ` ' ` |         
_______  | ` ' ` ' ` ' ` ' ` ' ` ' ` ' `|(`-')|` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` '|(`-')|' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` |(`-')| ' ` ' ` ' |  _______
|`:|::|  | ' ` ' ` ' ` ' ` ' ` ' ` ' ` ':=====:' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' `:=====:` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' ` ' :=====: ` ' ` ' ` |  |`:|::|
|  |`:|  |_____________________________________________________________________________________________________________________________________________________________________________________________|  |  |`:|
|--|--|  |                                                                                                                                                                                             |  |--|--|
|  |  |  |---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---|  |  |  |
!==!==!  |_____________________________________________________________________________________________________________________________________________________________________________________________|  !==!==!


''')
sleep(5)
print(f"{Crs.cianoclaro} Você chora com a vista da sua cidade e fica aliviado que pelo menos ela continua da mesma forma")
sleep(3)
print('Você nota algo de diferente')
sleep(2)
print('''
                          ░░  ░░                                  
                      ░░    ░░▓▓▓▓▒▒▓▓▓▓▓▓                        
      ▓▓            ░░▒▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░    ▓▓▓▓            
      ▒▒▓▓▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░  ▓▓▒▒▒▒          
        ▓▓▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████░░▓▓▒▒▓▓          
        ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████▓▓▒▒▓▓          
      ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓██▓▓▒▒▒▒▒▒▒▒      
    ▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓██▒▒▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒  
  ▓▓▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▒▒▓▓▓▓██▒▒▓▓██▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▒▒▓▓▒▒▒▒  
  ▒▒▓▓████████▒▒▒▒▓▓▒▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓██▓▓▒▒▒▒▒▒▓▓████▓▓▒▒▓▓██▒▒░░  
▒▒▓▓▒▒████████▒▒▓▓▓▓▒▒██▓▓▒▒▓▓▒▒▓▓██▒▒▒▒▒▒▒▒▓▓██▓▓██▓▓▒▒▒▒░░▒▒▒▒  
░░  ████████▓▓▓▓▓▓▓▓▓▓▓▓██▓▓░░▒▒▒▒▓▓▒▒▒▒▒▒▓▓▓▓▓▓▒▒▓▓▒▒▒▒░░▒▒▓▓▓▓░░
  ▒▒██▓▓██████▓▓▓▓░░██▓▓██░░░░▒▒▒▒░░▒▒▓▓▒▒░░▓▓▒▒▒▒▓▓▓▓░░▒▒▓▓▓▓▓▓▓▓
  ▓▓▓▓▓▓▓▓████▓▓▓▓▒▒▓▓░░░░░░░░░░████░░░░░░░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓██▓▓▓▓▓▓
  ▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░    ░░░░░░██░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓
  ░░▓▓▓▓▓▓▒▒░░░░              ░░░░░░░░░░░░░░▓▓░░▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓
    ▓▓▓▓██░░░░                  ░░░░░░░░░░░░▒▒░░▓▓▓▓▓▓▓▓▓▓░░░░░░▒▒
    ▓▓▓▓▓▓░░  ░░▒▒                  ░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓▒▒░░░░▒▒
        ▒▒    ▓▓▓▓                    ░░░░░░░░░░░░░░▓▓▓▓▓▓▒▒  ░░▓▓
        ▒▒    ██▓▓                  ░░▓▓██░░░░░░░░░░▓▓▓▓▒▒░░  ░░░░
  ▒▒▒▒▓▓▓▓    ▒▒▒▒                  ░░▓▓▓▓  ░░░░░░▒▒▓▓░░    ░░██  
    ░░▓▓▓▓                            ▓▓░░      ░░▓▓▓▓░░  ░░██░░  
      ▓▓██                                        ▓▓▒▒░░▓▓▓▓▓▓    
      ▓▓  ▒▒    ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒░░          ▒▒░░████████░░    
        ▒▒▓▓░░                                  ░░▓▓██▓▓██▓▓       NO WAY
        ▓▓▓▓▓▓                                ▒▒░░▓▓████▓▓▓▓      
        ▒▒▓▓░░▒▒                            ▒▒░░██▓▓████▓▓▓▓      
          ▓▓  ▓▓▒▒                        ▒▒░░████▓▓▓▓██▓▓▓▓      
              ▒▒▓▓▓▓░░                ▒▒  ▒▒██▓▓██▓▓▒▒  ░░▓▓██    
                ░░▓▓    ▓▓▒▒▒▒░░▒▒▒▒░░▒▒▒▒  ██▒▒▒▒▓▓              
                        ░░▓▓▓▓██▓▓▓▓▒▒▒▒░░  ▓▓  ▒▒▓▓              
                              ▓▓  ░░    ░░                        
                                ░░▒▒░░  ▒▒░░                      
                                ░░▓▓▒▒▒▒▓▓▒▒▒▒                    
                              ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒                    
                            ░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░                
                          ░░░░░░▒▒░░▒▒▒▒▒▒░░▒▒▒▒▒▒░░░░            
                          ░░░░░░▒▒░░░░░░▒▒░░░░▒▒▒▒░░              
                          ░░▒▒▒▒▓▓  ░░    ░░░░░░▒▒░░              
                            ░░▓▓▒▒░░░░░░░░▓▓▒▒░░░░░░              
                            ░░░░░░░░░░░░░░▒▒▒▒░░░░░░              
                              ░░░░░░░░░░░░▒▒▒▒░░  ░░              
                          ░░  ▒▒░░░░░░░░░░░░▒▒░░                  
                          ░░  ░░░░░░░░░░░░░░▒▒▒▒                  
                        ░░    ░░░░░░░░░░░░░░▒▒▒▒                  
                        ░░  ░░░░░░░░░░░░░░▒▒▒▒▒▒    ░░            
                ░░▒▒░░▒▒    ▒▒░░░░░░░░░░░░▒▒▒▒▒▒░░  ▒▒            
                ░░  ▒▒      ░░▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒  ░░            
                ░░          ░░▒▒▒▒░░░░▒▒▓▓▓▓▓▓▓▓▓▓                
                      ░░░░░░▓▓▓▓▓▓▓▓▓▓██████████▒▒    ░░          
                          ░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓░░                
                            ▒▒▒▒▓▓▓▓▒▒  ▓▓▓▓▓▓▓▓▓▓▒▒    ░░        
                            ▒▒▒▒▒▒▓▓▒▒  ▓▓▓▓▓▓▓▓▓▓▒▒  ▒▒          
                            ▒▒▒▒▒▒▓▓▒▒  ▒▒▓▓▓▓▓▓▒▒▓▓░░░░          
                            ▓▓▒▒▒▒▓▓▒▒    ▓▓▓▓▓▓▓▓▓▓              
                            ▒▒▒▒▒▒▒▒░░    ▓▓▒▒▓▓▓▓▒▒              
                            ▒▒▒▒▒▒▒▒      ▓▓▒▒▒▒▒▒▒▒              
                            ░░▒▒▒▒▒▒      ▒▒▒▒▒▒▒▒▒▒              
                              ▒▒▒▒▓▓        ▒▒▒▒▒▒▒▒              
                              ▒▒▒▒▓▓        ▒▒▒▒▒▒▒▒              
                              ▓▓▓▓▓▓        ▓▓▒▒▒▒▒▒              
                              ▒▒▓▓▓▓        ░░▒▒▒▒▒▒              
                              ▒▒▓▓▒▒          ▓▓▓▓▓▓░░            
                              ▓▓▓▓▓▓          ▓▓▓▓▓▓░░            
                            ████▒▒▓▓        ▓▓▒▒▒▒▓▓▒▒            
                          ▓▓██████▓▓        ▒▒▓▓████▒▒            
                          ██▓▓████▓▓        ▓▓████████            
                          ████████▓▓      ░░██▒▒██████            
                            ░░            ░░████████              





''')
sleep(2)
print('Você nota que está cercado de diversos guardas')
sleep(2)
print('''
        ████████████                                ████████████                      
      ██▒▒▒▒▒▒▒▒▒▒▒▒████                          ██▓▓▓▓▓▓▓▓▓▓▓▓████                  
      ██▓▓████▓▓▓▓▓▓▓▓▓▓██                        ██▓▓████▓▓▓▓▓▓▓▓▓▓██                
        ██░░░░██▓▓▓▓▓▓▓▓▓▓██                        ██░░░░██▓▓▓▓▓▓▓▓▓▓██              
      ████████████████▓▓▓▓▓▓████                  ████████████████▓▓▓▓▓▓████          
    ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓██              ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓██        
    ██████████████████████▓▓▓▓▓▓██              ██████████████████████▓▓▓▓▓▓██        
      ██▒▒██░░░░░░░░██▒▒▒▒████▓▓██                  ██░░░░░░░░░░░░░░░░████▓▓██        
      ████░░▓▓░░░░▓▓░░██▒▒▒▒▒▒██                    ██░░██░░░░██░░░░░░░░░░██          
        ██  ██    ██  ░░████▒▒██                    ██  ██    ██    ████░░██          
        ██  ██    ██    ░░██░░██                    ██        ░░    ░░██░░██          
        ██  ░░    ░░    ██▒▒░░██                    ██              ██▒▒██            
        ██            ░░██░░██                      ██  ▒▒▒▒▒▒▒▒    ░░░░██            
        ██    ▓▓▓▓    ░░██░░██                      ██    ▓▓▓▓    ░░░░██              
          ██  ▓▓▓▓  ░░██▒▒██                          ██  ▓▓▓▓  ░░░░██                
            ████████░░██▒▒██                            ████████░░░░██                
          ██░░██░░░░██████████                        ██▓▓██░░░░██████████            
        ██░░██░░████░░░░██░░░░██                    ██▓▓██▓▓████▓▓▓▓██▓▓▓▓██          
      ██░░░░░░██░░░░████░░░░░░░░██                ██▓▓▓▓▓▓██▓▓▓▓████▓▓▓▓▓▓▓▓██        
    ██░░░░░░░░░░████░░░░░░░░░░░░██              ██▓▓▓▓▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▓▓▓██        
    ██████████░░░░████████░░░░░░██              ██████████▓▓▓▓████████▓▓▓▓▓▓██        
  ██  ██      ██████░░    ██░░▓▓              ██▓▓██    ░░██████░░    ██▓▓██          
░░██  ██            ████░░████▒▒              ██▒▒██░░░░██▓▓▓▓▓▓████░░██▓▓██          
░░██  ░░████░░░░        ██░░░░██              ██░░▒▒████▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓██          
░░██░░░░░░░░████░░░░  ░░░░░░████              ██░░▒▒▓▓▓▓████▓▓▓▓▓▓▓▓▓▓▓▓████          
    ████████████████░░░░░░██░░██                ████████████████▓▓▓▓▓▓██▓▓██          
        ██░░░░░░░░░░██████░░░░██                  ██▓▓▓▓▓▓▓▓▓▓▓▓██████▓▓▓▓██          
        ██░░░░░░░░░░░░░░░░░░████                  ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████          
        ████████████████████▒▒██                    ████████████████████▒▒██          
        ██░░██    ██▒▒░░░░▒▒▒▒██                    ██▒▒██░░░░██▒▒▒▒▒▒▒▒▒▒██          
          ████████████▓▓▓▓██████                      ██████████████████████          
          ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                      ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██          
          ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                      ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██          
          ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                      ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██          
          ██▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓██                      ██▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓██          
          ██▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓██                      ██▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓██          
          ██▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓██                      ██▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓██          
          ██▓▓▓▓▓▓██▓▓▓▓▓▓▓▓██░░                      ██▓▓▓▓▓▓██▓▓▓▓▓▓▓▓██░░          
          ██▓▓▓▓▓▓██▓▓▓▓▓▓▓▓██                        ██▓▓▓▓▓▓██▓▓▓▓▓▓▓▓██            
          ██▓▓▓▓▓▓██▓▓▓▓▓▓▓▓██                        ██▓▓▓▓▓▓██▓▓▓▓▓▓▓▓██            
          ██▓▓▓▓▓▓██▓▓▓▓▓▓▓▓██                        ██▓▓▓▓▓▓██▓▓▓▓▓▓▓▓██            
          ██▓▓▓▓▓▓██▓▓▓▓▓▓▓▓██                        ██▓▓▓▓▓▓██▓▓▓▓▓▓▓▓██            
          ██▓▓▓▓▓▓██▓▓▓▓▓▓▓▓██                        ██▓▓▓▓▓▓██▓▓▓▓▓▓▓▓██            
          ██▓▓▓▓▓▓██▓▓▓▓▓▓▓▓██                        ██▓▓▓▓▓▓██▓▓▓▓▓▓▓▓██            
          ██▓▓▓▓▓▓██▓▓▓▓▓▓▓▓██                        ██▓▓▓▓▓▓██▓▓▓▓▓▓▓▓██            
          ████████████████████                        ████████████████████            
        ██░░░░▒▒██░░░░░░▒▒▒▒██                      ██▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██  
''')

print(f'{Crs.amareloclaro}Parado ai {personagem} você esta preso por furto,invasão de propriedade e assasinato!')
sleep(5)
print('..............')
print('................')
print('O que deseja fazer?')


print('''

[1]Entrar em combate
[2]Se entregar
[3]Tentar fugir





''')
escolha = input (f'{Crs.ciano}Sua escolha: ')

if escolha == "1":
  print('Você tentou entrar em combate mas assim que foi pegar sua arma acabou levando diversos tiros ')
  sleep(5)
  print('............')
  print(".......")
  sleep(5)
  print('''
                                      ██████████████                                                  
                      ████████░░░░░░░░██▒▒██                                                  
                  ▓▓██░░▒▒░░░░░░░░░░░░██▒▒██                                                  
              ████▒▒▒▒░░░░░░░░░░░░░░░░██▒▒██                                                  
            ▓▓▒▒▒▒░░░░░░░░░░░░▓▓▒▒▒▒▒▒██▒▒██                                                  
          ██░░░░░░░░░░▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓██▒▒██                                                  
        ██░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒██                                                  
      ██░░░░▓▓▓▓▒▒▓▓▓▓▓▓▓▓██████████████▒▒██                                                  
    ██░░▒▒▓▓▓▓██████████░░            ██▒▒██                                                  
░░██░░▓▓▓▓████                        ██▒▒██                                                  
  ██▒▒████  ▒▒                        ██▒▒██                                                  
░░████                                ██▒▒██                                                  
                                      ██▒▒██                      ██████████████████████      
                                      ██▒▒██                  ████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██      
                                      ██▒▒██                ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██        
                                      ██▒▒██              ██▓▓▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▓██          
                                      ██▒▒██            ██▓▓▒▒▒▒▓▓██░░░░██▓▓▓▓▓▓▓▓██          
                                      ██▒▒██            ██▒▒▓▓▒▒██░░░░░░░░██▓▓▓▓▓▓██          
                                      ██▒▒██          ██▓▓▓▓▓▓██░░░░░░░░░░░░██▓▓▓▓▓▓██        
                                      ██▒▒██          ██▓▓▓▓██░░██▓▓░░░░▓▓██░░██▓▓▓▓██        
                                      ██▒▒██          ██▓▓▓▓██░░▓▓▓▓░░░░██▓▓░░██▓▓▓▓██        
                                      ██▒▒██        ██▓▓▓▓██░░░░░░░░░░░░░░░░░░░░██▓▓▓▓██      
                                      ██▒▒██        ██▓▓▓▓██░░░░░░░░░░░░░░░░██░░██▓▓▓▓██      
                                      ██▒▒██        ██▓▓▓▓▓▓██░░██░░██░░██░░████▓▓▓▓▓▓██      
                                      ██▒▒██          ████▓▓▓▓████░░██░░██░░██▓▓▓▓████        
                                      ██▒▒██              ██▓▓▓▓████████████▓▓▓▓██            
                                      ██████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██            
                                      ██░░░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██          
                                      ██░░░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██        
                                      ████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██      
                                      ██▒▒████▓▓▓▓▓▓▓▓▓▓████▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓    
                                      ██▒▒██  ██▓▓▓▓▓▓██  ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓██    
                                      ██▒▒██  ██▓▓████    ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓██      
                                      ██▒▒██  ████        ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓██░░      
                                      ██▒▒██              ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████          
                                      ██▒▒██              ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓          
                                      ██▒▒██              ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██            
                                      ██▒▒██              ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██            
                                      ██▒▒██              ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██          
                                      ██▒▒██            ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓        
                                      ██▒▒██            ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██      
                                      ██▒▒██            ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██    
                                      ██▒▒▒▒██        ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  
                                        ██▒▒██▓▓      ██▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
                                        ██▒▒██████    ████▓▓▓▓▓▓▓▓████████▓▓████████▓▓▓▓██████
                                        ░░████████            ██████    ██████                
        ''')
  sleep(5)
  print('Você morreu meu camarada muhahahahaha')
  sleep(2)
  print('''
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼███┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██████┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼████████┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██████████┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼████████████┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██████████████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼████████████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█████████┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
        ''')
  sleep(2)
  sys.exit() 

if escolha == "2":
  print('Você se entregou para os policiais ')
  sleep(5)
  print('''
                  ▓▓██▓▓██                                    
                ██████▒▒▓▓                  ████        ██  
    ▓▓██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████      ██░░░░██  ██░░░░██
  ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒██    ██░░██      ██░░██
██▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒██  ██░░██      ██░░██
  ██▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒██    ██░░  ████▓▓░░░░██
    ▓▓██████████████████████████████        ██░░░░░░░░░░██  
  ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██        ██████████    
    ██████████▓▓████████████████████              ██        
    ████        ██    ██        ████            ██████      
  ██░░██    ████        ████    ██  ██          ██  ██      
    ████    ████        ████    ████            ▓▓████      
      ██                        ██                ██        
        ██    ▓▓        ▓▓    ██                  ██        
          ██    ▓▓▓▓▓▓▓▓    ██                  ▓▓▓▓▓▓      
        ██▒▒██████████▓▓████▒▒██                ██  ▓▓      
      ██▒▒░░      ▒▒▒▒    ░░  ▒▒██              ▓▓▓▓▓▓      
    ▓▓░░░░░░▓▓▒▒░░▒▒▒▒  ▒▒██░░░░░░▓▓              ▓▓        
  ██░░██░░████░░  ▒▒▒▒░░░░████░░██  ██            ▓▓        
██      ██  ██░░░░▒▒▒▒░░░░██  ██      ██        ▓▓▓▓▓▓      
██    ██    ██░░░░    ░░░░██    ██    ██        ▓▓  ▓▓      
██████      ▓▓████████████▓▓      ██▓▓██        ▓▓▓▓██      
            ██▒▒▒▒▒▒▒▒▒▒▒▒██                      ▓▓        
            ██▒▒▒▒████▒▒▒▒██                  ██████████    
            ██▒▒▒▒████▒▒▒▒██                ██░░░░░░░░░░██  
            ██▒▒▒▒████▒▒▒▒██              ██░░░░████▓▓░░░░██
            ██▒▒▒▒████▒▒▒▒██              ██░░██      ██░░██
            ████▓▓██████████              ▓▓░░██      ██░░██
          ██▒▒▒▒▒▒████▒▒▒▒▒▒▓▓    ░░░░░░  ▒▒░░░░██  ▒▒░░░░▓▓
          ▓▓██████████████████              ████      ████  
  ''')
  sleep(5)
  print('você tem o direito de permanecer calado tudo o que disser poderá ser usado contra você num tribunal ')
  sleep(5)
  print('Você foi preso!')
  print('''
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼███┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██████┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼████████┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██████████┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼████████████┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██████████████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼████████████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█████████┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
        ''')
sys.exit()  

if escolha == "3":
  print('Você fingiu que iria se entregar....')
  sleep(2)
  print('Você esperou um momento de distração dos guardas e conseguiu correr')
  print(f'''{Crs.branco}
                                  ░░░░░░░░                  
                                ▓▓▒▒▓▓    ▒▒░░              
                              ▓▓▒▒▒▒                        
                            ▒▒▒▒▒▒▒▒                        
                          ░░▒▒▒▒▒▒                          
                          ▓▓▒▒▒▒▒▒              ░░          
                          ▓▓▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    
                          ▓▓▒▒▒▒██████████░░▓▓░░▓▓          
                          ▒▒▓▓▓▓▓▓██▒▒░░░░░░░░░░▒▒          
                            ▓▓▓▓░░  ░░      ░░░░▒▒          
                              ██░░                ░░        
                            ▒▒██▓▓▒▒          ▓▓  ░░        
                      ████▓▓░░██▓▓▒▒░░          ▒▒          
                  ▒▒██▒▒      ██▓▓██░░▒▒░░░░░░░░            
              ░░▓▓░░░░░░    ▓▓▓▓▓▓██▓▓████▓▓  ▒▒░░          
          ▓▓░░░░░░░░▓▓▓▓██▓▓▓▓▓▓▓▓▓▓░░████▓▓▒▒▒▒  ░░        
          ░░    ░░░░▓▓██▓▓▓▓▓▓▓▓▒▒██░░▓▓▒▒▒▒████░░░░        
      ░░        ▒▒  ▒▒▓▓▓▓████▒▒▒▒░░░░▒▒██░░░░░░▒▒          
        ▒▒    ████    ██▓▓▓▓▓▓▓▓▒▒░░▓▓██  ▓▓▓▓              
          ░░░░        ████▒▒▒▒▒▒░░████                      
      ██▒▒          ▓▓▒▒██▒▒░░░░▒▒    ██                    
    ░░░░▓▓▓▓      ░░██▒▒▒▒██▓▓▓▓░░  ▓▓░░                    
    ▒▒▓▓▓▓▓▓██████▒▒░░██▒▒▒▒  ▒▒░░▒▒  ░░                    
  ▒▒▓▓▓▓▓▓▓▓██▒▒██░░▒▒          ▒▒    ▓▓░░░░▓▓░░▓▓          
  ▒▒▒▒▒▒▓▓████░░░░░░                    ▒▒▒▒  ██▒▒▓▓▒▒▒▒▒▒▒▒
  ▒▒▓▓██▒▒▓▓██                            ██  ▒▒██░░  ▓▓▒▒░░
  ▒▒▓▓░░░░██▒▒                              ▓▓▒▒▒▒▓▓▓▓▒▒░░▒▒
  ▒▒▓▓                                      ▒▒▒▒▒▒▒▒▒▒░░▒▒  
                                              ▒▒▒▒▒▒  ▒▒    
                                                ▒▒░░░░      
                                                ░░░░        
        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓            


''')
sleep(2)
print('Você fugiu dos guardas')
sleep(5)
print('Você olha para trás e percebe que conseguiu despistar eles')
sleep(2)
print('Você se senta e começa a pensar como vai fazer tudo que pensou sendo que você é somente um jornalista')
sleep(5)
print('Você decide que vai direto para a empresa SilverLight mas antes vai postar tudo no ortsbok e irá mandar todos os documentos para o jornal')
sleep(5)
print('Você se levanta')
if escolhadogusman == 1:
  
  print('Você começa a se sentir tonto')
  sleep(2)
  print('Você pensa na possibilidade de ter contraido a doença')
  sleep(2)
  print('Você se lembra.....')
  sleep(2)
  print('Que ajudou o Gusman quando ele estava doente')
  sleep(2)
  print('.....')
  sleep(3)
  print('Você cai')
  sleep(2)
  print('As manchas em suas mãos já estão em todo seu corpo')
  sleep(5)
  print('.......')
  print('Você tenta se  levantar mas sua vista escurece!')
  sleep(5)
  print('......')
  sleep(2)
  print('........')
  print('''
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼███┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██████┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼████████┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██████████┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼████████████┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██████████████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼████████████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█████████┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼█┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼███┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼████┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼██████┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼''')
  sys.exit() 

if escolhadogusman == 2:
  print('Você se levanta e vai até a sua casa para publicar tudo de uma vez')
  sleep(5)
  print('Chegando em sua casa você se depara com diversos guardas na entrada')
  sleep(2)
  print('.....')
  print('Como deseja entrar?')

  print('''

 [1] Entrar pela portinha do cachorro nos fundos
 [2] ir pelos fundos e entrar pela janela do seu quarto

  
  
  ''')

escolha = input (f' {Crs.ciano}Sua Escolha:  ')

if escolha == "1":
  print('Você tenta entrar pela portinha do cachorro e fica preso')
  sleep(5)
  print('Um guarda te avista e te prende ')
  print('Game Over')
  #sys.exit() 


elif escolha == "2":
  print('Você consegue escalar e entrar no seu quarto')
  sleep(5)
  print('Você avista seu computador e vai ate ele')



print('Você tenta logar no seu computador mas por algum motivo não lembra a senha')
print('''
            ████████████████████████████████████████████████████████                                  
            ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██                                  
            ██▒▒██████████████████▓▓▓▓██████████████████████████▒▒██                                  
            ██▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒██                                  
            ██▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒██                                  
            ██▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒██                                  
            ██▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒██                                  
            ██▒▒██▒▒  ▒▒▒▒▒▒        ▒▒        ▒▒  ▒▒  ▒▒▒▒  ▒▒██▒▒██                                  
            ██▒▒██▒▒  ▒▒▒▒▒▒  ▒▒▒▒  ▒▒  ░░▒▒▒▒▒▒  ▒▒    ▒▒  ▒▒██▒▒██                                  
            ██▒▒██▒▒  ▒▒▒▒▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒  ▒▒  ▒▒  ░░    ▒▒██▒▒██                                  
            ██▒▒██▒▒  ░░  ▒▒        ▒▒        ▒▒  ▒▒  ▒▒░░  ▒▒██▒▒██                                  
            ██▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒██                                  
            ██▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒██                                  
            ██▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒██                                  
            ██▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒██                                  
            ██▒▒████████████████████████████████████████████████▒▒██                                  
            ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██                                  
            ████████████████████████████████████████████████████▓▓▓▓                                  
          ████▒▒░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▒▒                                
        ████░░░░██░░██░░██░░██░░▓▓░░██░░██░░██░░██░░██░░██░░██░░▓▓░░████████████████████████          
      ████▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████                ████        
    ████▒▒░░░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░░░████                ████      
  ████▒▒░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░▒▒████                ██      
████░░░░░░██▓▓▓▓░░██░░██▒▒░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓██░░▓▓▓▓░░██░░██▓▓▓▓░░░░████              ██      
██▒▒░░░░░░▒▒▒▒▒▒░░░░░░░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░░░▒▒▒▒░░▒▒░░▒▒▒▒▒▒░░░░▒▒██              ██      
██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██          ██▓▓██▓▓██  
                                                                                        ██▒▒▒▒██▒▒▒▒██
                                                                                        ██▒▒██████▒▒██
                                                                                        ██████░░██████
                                                                                        ██░░░░░░░░░░██
                                                                                        ██░░░░░░░░░░██
                                                                                        ████░░░░░░████
                                                                                          ██████▓▓██  
''')
sleep(2)
print('Você nota que tentaram acessar seu computador muitas vezes e só possui mais uma tentativa de login')
sleep(5)
print('Você tenta lembrar sua senha e vem em sua mente 3 combinaçoes qual deseja tentar?')
sleep(2)

print('''

[1] 402145
[2] 564332
[3] 459321
''') 
escolha = input (f' {Crs.ciano}Sua Escolha:  ')

if escolha.lower().strip() == '1':
  print('A senha está incorreta você bloqueou seu computador e sua unica chance de conseguir postar tudo')

elif escolha.lower().strip() == '2':
  print('A senha está incorreta você bloqueou seu computador e sua unica chance de conseguir postar tudo ')

elif escolha.lower().strip() == '3':
  print('A senha está incorreta você bloqueou seu computador e sua unica chance de conseguir postar tudo ')


print('Você irritado sai pela janela novamente ')
sleep(5)

print('Você decide ir para a sede principal da empresa SilverLight')
sleep(5)
print('Quando você estava saindo da casa um guarda te avista!')
sleep(3)
print('Você decide entrar em combate!')

#TerceiroPVP

GUARDA_HP = 800
PERSONAGEM = 301



print("Você decide atacar o guarda restante".upper())

print('......')

print(
    f"""

[1] Bastão neon
dano de 1 a 100

[2] Arma
dano de 1 a 250

  """
)

while True:
    escolha = input("Escolha seu ataque: ")

    dano_ataque = random.randint(1, 250)
    if escolha == "1":
        dano_ataque = random.randint(1, 100)
    sleep(5)

    GUARDA_HP -= dano_ataque
    print(f"Você deu {dano_ataque} de dano, o guarda agora está com {GUARDA_HP} de HP.")

    print('O Guarda te ataca: ')
    atq_guarda = random.randint(25, 50)

      
    if escolha == "1":
        atq_guarda = random.randint(30,50)
    sleep(5)

    PERSONAGEM -= atq_guarda
    print(f"o guarda te deu {atq_guarda} de dano, e você agora está com {PERSONAGEM} de HP.")

    if GUARDA_HP <= 0:
        print("O guarda está morto!!")
        break

      

      

    elif PERSONAGEM <= 0:
        print(".......")
        sleep(5)
        print('''
                                      ██████████████                                                  
                      ████████░░░░░░░░██▒▒██                                                  
                  ▓▓██░░▒▒░░░░░░░░░░░░██▒▒██                                                  
              ████▒▒▒▒░░░░░░░░░░░░░░░░██▒▒██                                                  
            ▓▓▒▒▒▒░░░░░░░░░░░░▓▓▒▒▒▒▒▒██▒▒██                                                  
          ██░░░░░░░░░░▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓██▒▒██                                                  
        ██░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒██                                                  
      ██░░░░▓▓▓▓▒▒▓▓▓▓▓▓▓▓██████████████▒▒██                                                  
    ██░░▒▒▓▓▓▓██████████░░            ██▒▒██                                                  
░░██░░▓▓▓▓████                        ██▒▒██                                                  
  ██▒▒████  ▒▒                        ██▒▒██                                                  
░░████                                ██▒▒██                                                  
                                      ██▒▒██                      ██████████████████████      
                                      ██▒▒██                  ████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██      
                                      ██▒▒██                ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██        
                                      ██▒▒██              ██▓▓▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▓██          
                                      ██▒▒██            ██▓▓▒▒▒▒▓▓██░░░░██▓▓▓▓▓▓▓▓██          
                                      ██▒▒██            ██▒▒▓▓▒▒██░░░░░░░░██▓▓▓▓▓▓██          
                                      ██▒▒██          ██▓▓▓▓▓▓██░░░░░░░░░░░░██▓▓▓▓▓▓██        
                                      ██▒▒██          ██▓▓▓▓██░░██▓▓░░░░▓▓██░░██▓▓▓▓██        
                                      ██▒▒██          ██▓▓▓▓██░░▓▓▓▓░░░░██▓▓░░██▓▓▓▓██        
                                      ██▒▒██        ██▓▓▓▓██░░░░░░░░░░░░░░░░░░░░██▓▓▓▓██      
                                      ██▒▒██        ██▓▓▓▓██░░░░░░░░░░░░░░░░██░░██▓▓▓▓██      
                                      ██▒▒██        ██▓▓▓▓▓▓██░░██░░██░░██░░████▓▓▓▓▓▓██      
                                      ██▒▒██          ████▓▓▓▓████░░██░░██░░██▓▓▓▓████        
                                      ██▒▒██              ██▓▓▓▓████████████▓▓▓▓██            
                                      ██████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██            
                                      ██░░░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██          
                                      ██░░░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██        
                                      ████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██      
                                      ██▒▒████▓▓▓▓▓▓▓▓▓▓████▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓    
                                      ██▒▒██  ██▓▓▓▓▓▓██  ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓██    
                                      ██▒▒██  ██▓▓████    ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓██      
                                      ██▒▒██  ████        ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓██░░      
                                      ██▒▒██              ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████          
                                      ██▒▒██              ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓          
                                      ██▒▒██              ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██            
                                      ██▒▒██              ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██            
                                      ██▒▒██              ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██          
                                      ██▒▒██            ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓        
                                      ██▒▒██            ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██      
                                      ██▒▒██            ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██    
                                      ██▒▒▒▒██        ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  
                                        ██▒▒██▓▓      ██▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
                                        ██▒▒██████    ████▓▓▓▓▓▓▓▓████████▓▓████████▓▓▓▓██████
                                        ░░████████            ██████    ██████                
        ''')
        sleep(5)
        print('Você morreu meu camarada muhahahahaha')
        sleep(2)
        print('''
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼███┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██████┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼████████┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██████████┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼████████████┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██████████████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼████████████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█████████┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
        ''')
        sleep(2)
        sys.exit() 
        
       

    print("vamos atacar novamente!".upper())


print('Depois do confronto com o guarda você continua seguindo pela cidade ')
sleep(2)
print('Você fica pensativo como ninguem está doente nessa parte da cidade')
sleep(3)
print('.......')
sleep(2)
print('Antes que pudesse concluir seu pensamento vocE se depara com dois caminhos qual irá seguir?')
sleep(2)
print('''

[1]Esquerda
[2]Direita
''')

escolha = input (f' {Crs.ciano}Sua Escolha:  ')

if escolha == '1':
  print('Você seguiu pela esquerda e se deparou com uma rua super movimentada com diversas pessoas')
  sleep(2)
  print('Na rua você aborda uma pessoa e pergunta sobre a doença')
  sleep(5)
  print('A pessoa lhe pergunta de que doença você está falando?')
  sleep(2)
  print('Você percebe que a doença está somente nos andares abaixo ')
  sleep(2)
  print('Eles estão deixando somente a elite....')
  sleep(2)
  print('Você agradece a pessoa e se despede')
elif escolha == '2':
  print('Você seguiu pela direita ')
  sleep(5)
  print('Pela direita você se depara com varias ruas com diversas empresas')
  sleep(2)
  
  
  




   



  
  











        





    







    

    




  

   