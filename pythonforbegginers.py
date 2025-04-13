import sys

number = 4
if number > 8:
    print(number)
else:
    print('wrong')

#choice = int(input("enter:\n\n"))
choice = 2
print(type(choice))
if choice < 1 or choice > 3:
    sys.exit("enter 1-3")

print('\n\n')
players = ['birdo', 'koopa', 'wario', 'shyguy']
print(players[0:])
playerscopy = players[:]
print(playerscopy)
players.append('mario')
print(players)

mytuple = tuple(players)
print(mytuple)

print('\n\n')


class player:
    def __init__(self, character):
        self.character = character
        self.health = 100
        self.strength = 10
        self.inventory = {'coins': 10, 'stars': 0}

    def attack(self,player,type):
        if type == 'smack':
            player.health = player.health - self.strength
        elif type == 'poke':
            player.health -= self.strength*.1
        else:
            print('attack failed')
        
    def steal(self, player, number):
        player.inventory['coins'] -= number
        self.inventory['coins'] += number

    def openinventory(self):
        print(self.character, 'inventory\n', self.inventory,'\n')
        
# initialize players
tess = player('koopa')
print('new player', tess.character, 'joined')
tess.openinventory()
zach = player('yoshi')
print('\nnew player', zach.character, 'joined')
zach.openinventory()

# tess finds a star
tess.inventory['stars'] += 1
tess.openinventory()

# zach attacks tess
zach.attack(tess,'poke')
print(tess.health)

# tess steals coins from zach
tess.steal(zach, 10)
tess.openinventory()
zach.openinventory()



