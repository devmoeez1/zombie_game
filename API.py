import time
import random


# TODO: if fought against, let it fight back - function done but have some bugs.
# TODO: if fight decrease the health according to the weapon - done.
# TODO : change durability issue for the gravedigger - in progress.
# TODO : if player's health is a 0 game over
# TODO : fix command A and B, not working
# TODO : 






class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def getName(self):
        return self.name

class Key(Item): # inherit from Item
    def __init__(self,name,description, clearance_level=0) -> None:
        super().__init__(name,description)
        self.clearance_level = clearance_level

class Inventory():
    def __init__(self, max_slots=100,  max_items_per_stack=100) -> None:
        self.max_slots = max_slots
        self.max_items_per_stack = max_items_per_stack
        self.inventory = {}
    def addItem(self, item: Item) -> None:
        self.check_item(item)
        self.inventory[item.getName()] = self.inventory[item.getName()] +1

    def check_item(self, item: Item):
        if item.getName() not in self.inventory:
            self.inventory[item.getName()] = 0
        return self.inventory[item.getName()]

    def getItemAmount(self, itemname : str) -> int:
        return self.check_item(itemname)
    def removeItemByOne(self, itemname: str) -> int:
        self.inventory[itemname] = self.inventory[itemname] -1
        return self.inventory[itemname]

class Weapon(Item): # inherits from Item (child of item)
    def __init__(self, name, description="A weapon", damage=15, durability=10) -> None:
        super().__init__(name, description)
        self.durability = durability
        self.description = description
        self.max_durability = durability
        self.damage = damage
    def use(self):
        if self.durability <= 0:
            print("weapon broke")
            return     
        else:
            self.durability -= 1
            print(f"durability left {self.durability}")
            return self.damage
    def __addDurability(self, amount):
        self.durability += amount
    def repair(self):
        durabilityToAdd = self.max_durability - self.durability
        self.__addDurability(durabilityToAdd)
        print(f"Fixed your {self.name},")
        

arsenal = { # name, description, damage, durability
    "baseball bat": Weapon("bat","with a baseball bat", 25, 49),
    "gun": Weapon("mp72","with a gun", 10, 10),
    "fist": Weapon("fist", "hands", 15, 1000),
    "fork": Weapon("Pitchfork", "poke", 50, 20)
}
arsenal_for_Enemy = { # name, description, damage, durability
    "baseball bat": Weapon("bat","with a baseball bat", 25, 49),
    "gun": Weapon("mp72","with a gun", 100, 10),
    "fist": Weapon("fist", "hands", 15, 1000),
    "hammer": Weapon("sledgehammer", "STOP! hammer time", 100, 19)
}
arsenal_for_gravedigger = { # name, description, damage, durability
    "shovle": Weapon("shovle","dig", 20, 40),
    "fist": Weapon("fist", "hands", 15, 1000),
    "hammer": Weapon("sledgehammer", "STOP! hammer time", 100, 19)
}

class Entity(object):
    def __init__(self, name, health=100) -> None:
        self.name = name
        self.health = health
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
        #self.weapons = [self.gun, "baseball bat", "knife", "spoon"]
    def getName(self):
        return self.name
    def getHealth(self):
        return self.health
    def fight(self, weaponOfChoice, enemy):
        if(isinstance(enemy, Entity)):
            # check if enemy is a player or if it's an enemy
            if(isinstance(enemy, Enemy)): # enemy, Player or Enemy
                if(isinstance(weaponOfChoice, Weapon)):
                    weaponOfChoice.use()
            elif(isinstance(enemy, Player)):
                print("Ouch hurting humans or something")
        else:
            print("No I don't inherit from the Entity class")
class Player(Entity):
    def __init__(self, name, health=100) -> None:
        super().__init__(name, health)
        self.inventory = Inventory()
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
    def inventory(self):
        return self.inventory
    def say(self, str):
        print(f"{self.getName()}: {str}")
    def attack(self, player, attack_type):
        if attack_type == "fist":
            damage = 10
            print(f"{self.name} performs a quick attack and deals {damage} damage.")
        elif attack_type == "baseball bat":
            damage = 20
            print(f"{self.name} performs a strong attack and deals {damage} damage.")
        elif attack_type == "gun":
            damage = 40
            print(f"{self.name} performs a strongest attack and deals {damage} damage.")
        elif attack_type == "fork":
            damage = 50
            print(f"{self.name} performs a  the strongest attack and deals {damage} damage.")
        else:
            print(f"{self.name} doesn't understand the command.")
    
class Enemy(Entity):
    def __init__(self, name, health):
        super().__init__(name, health)
    def take_damage(self,damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
    arsenal_for_Enemy = { # name, description, damage, durability
    "Knife" :Weapon("knife","slice",100,20),
    "gun" :Weapon("glock gun", "bang",1000,5),
    "fist" :Weapon("fist","pow",10,1000),
}
arsenal_for_gravedigger = { # name, description, damage, durability
    "shoval" :Weapon("shoval","dug",20,40)
}
class Weapon:
    def __init__(self, name, damage): 
        self.name = name
        self.damage = damage
    def use(self):
        print(f"{self.name} is used in the attack and deals {self.damage} damage.")
        return self.damage

def fight(player, weaponOfChoice, enemy):
    print(f"{player.name} faces {enemy.name} in combat!")

    while player.health > 0 and enemy.health > 0:
        print(f"{player.name} Health: {player.health}, {enemy.name} Health: {enemy.health}")

        # Get player input for the attack command
        attack_command = input("Enter attack command (A for quick attack, B for strong attack): ").upper()

        # Player attacks the enemy
        player.attack(enemy, attack_command)

        # Check if the enemy is defeated
        if enemy.health <= 0:
            print(f"{enemy.name} has been defeated! {player.name} is victorious!")
            break

        # Enemy attacks the player
        damage = 10  # You can modify this based on your game's logic
        player.take_damage(damage)
        print(f"{enemy.name} attacks {player.name} and deals {damage} damage.")

        # Check if the player is defeated
        if player.health <= 0:
            print(f"{player.name} has been defeated! {enemy.name} is victorious!")
            break


def attack_P(self, arsenal_for_Enemy, enemy):
    if isinstance(enemy, Entity):
            print("No, I don't inherit from the Entity class")
    elif isinstance(enemy, Enemy):
            self.attack(enemy, attack_type)
    elif isinstance(arsenal_for_Enemy, Weapon):
            arsenal_for_Enemy.use()
    
    def attack(self, enemy, attack_type):
        if attack_type == "fist":
            damage = 10
            print(f"{self.name} performs a quick attack and deals {damage} damage.")
        elif attack_type == "knife":
            damage = 20
            print(f"{self.name} performs a strong attack and deals {damage} damage.")
        elif attack_type == "gun":
            damage = 40
            print(f"{self.name} performs a strongest attack and deals {damage} damage.")
        elif(isinstance(arsenal_for_Enemy, Weapon)):
         arsenal_for_Enemy.use()

player = Player("Mihnea")
enemy = Enemy("Enemy1", 100)
weapon = Weapon("Gun", 1000)



def ask_question(question,option1=["(unavailable)", None],option2=["(unavailable)", None],option3=["(unavailable)", None],option4=["(unavailable)", None]):
    print(question)
    choice1 = option1[0]     
    choice2 = option2[0]     
    choice3 = option3[0]     
    choice4 = option4[0]     
    callback1 = option1[1]     
    callback2 = option2[1]     
    callback3 = option3[1]     
    callback4 = option4[1]     

    user_input = input(f"Enter your choice: {choice1}, {choice2}, {choice3} or {choice4}: ")

    if user_input == choice1:
        callback1()
    elif user_input == choice2:
        callback2()
    elif user_input == choice3:
        callback3()
    elif user_input == choice4:
        callback4()
    else:
        print("optiéon unknown")
        ask_question(question,option1,option2,option3,option4)



def start():
    player_name = input("what your name? ")
    # once we have their name, make a player with that name.
    player = Player(player_name)
    print(f"Welcome {player.getName()} - you woke up with amnesia")
    ask_question("Where do you wanna go?", ["left", wentLeft], ["right", wentRight], ["up", wentUp], ["backwards",wentBackwards])
    # ?

def wentLeft():
    print("Oh you went left")
    print("You see a dead body")
    ask_question("Where do you wanna go?", ["left", wentLeft], ["right", wentRight], ["up", wentUp], ["backwards",wentBackwards])  
def wentRight():
    print("Oh you went right")
    print("Oh you see a coffien")
    ask_question("Where do you wanna go?", ["left", wentLeft], ["right", wentRight], ["up", wentUp], ["backwards",wentBackwards])
def wentUp():
    print("Oh you went up")
    print("you see a tombstone with your name on it")
    ask_question("Where do you wanna go?", ["left", wentLeft], ["right", wentRight], ["up", wentUp], ["backwards",wentBackwards])
def wentBackwards():
    print("Oh you went backwards")
    print("you see someone")
    enemy_to_attack = Enemy("Pest", 50)
    arsenal_for_enemy_to_attack = Weapon("Fist", 10)
    attack_P(player, arsenal_for_enemy_to_attack, enemy_to_attack)

# Fight section
    grave_digger = Enemy("Grave Digger", 50)
    arsenal_for_grave_digger = Weapon("Shovel", 15)
    print("It turns out to be a grave digger. Better fight!")
    fight(player, arsenal_for_grave_digger, grave_digger)
def city():
    print("after you beat pest you enterd a city but you need to go some where idk how but some where")
    ask_question("Where do you wanna go?", ["help", askForHelp], ["taxi", askTaxi], ["nothing" ,nothing], ["look",lookForAwnsers])


def askForHelp():
    print("you decide to ask for help but there busy so you have no luck")
    ask_question("Where do you wanna go?", ["help", askForHelp], ["taxi", askTaxi], ["nothing" ,nothing], ["look",lookForAwnsers])
def askTaxi():
    random_number = random.randint(1,3)
    print(random_number)
    if random_number == 1:
        print("they didn't stop. so try again?")
        ask_question("Where do you wanna go?", ["help", askForHelp], ["taxi", askTaxi], ["give up" ,city], ["look",lookForAwnsers])
    elif random_number == 2:
        print("you lean a little to much and lost a arm in a progress")
        ask_question("Where do you wanna go?", ["help", askForHelp], ["taxi", askTaxi], ["give up" ,city], ["look",lookForAwnsers])
    else:
        print("they stop and told them go to the country side of town")
def  nothing():
    print("")
    ask_question("Where do you wanna go?", ["help", askForHelp], ["taxi", askTaxi], ["give up" ,city], ["look",lookForAwnsers])
def lookForAwnsers():
    print("you decide to look for a awnsers and you discover that you uset to be a farmer on a farm that died of a heart attack.but before you died that a rich company is going to buy your property")
    print("you go in the street to get a taxi,they stop and told them go to the country side of town")
def country():
    print("You are going to the country side but forgot what country you are from. which one?")
    ask_question("Where do you wanna go?", ["ask",askForDirection], ["quiet",silents ], ["act",Karenmode], ["play dead",playDead])


def askForDirection():
    print("you ask on what country are you going. He replied with 'to Romania' with that you realize that you are in Hungrey and need to come back ASAP")
def silents():
    print("you decide to keep it quiet but that won't do.")
    ask_question("Where do you wanna go?", ["ask",askForDirection], ["quiet",silents ], ["act",Karenmode], ["play dead",playDead])
def Karenmode():
    print("you decide to act like a karen but you were thrown away for the taxi now you ding dong have to find a another taxi")
    ask_question("Where do you wanna go?",["taxi", askTaxi], ["look",lookForAwnsers])
    country()
def playDead():
    print("you decide to do a little trolling and decide to play dead. the taxi driver was nfaze and do is job properly")
    
start()
city()
country()
