import random

dmg = 100


class ENEMY:
    def __init__(self, hp, attack, defence):
        self.hp = int(hp)
        self.attack = int(attack)
        self.defence = int(defence)

wild_dog = ENEMY(50, 75, 10)


class PLAYER:
    def __init__(self, min_attack, max_attack, defence, hp = 100):
        self.hp = int(hp)
        self.min_attack = int(min_attack)
        self.max_attack = int(max_attack)
        self.defence = int(defence)

    def strike(self):
        damage = self.attack
        return damage


class SWORD_MASTER(PLAYER):
    def __init__(self, hp = 100, min_attack = 55, max_attack = 100, defence = 75):
        self.hp = int(hp)
        self.min_attack = int(min_attack)
        self.max_attack = int(max_attack)
        self.defence = int(defence)

    def strike(self):
        damage = self.attack
        return damage

    def stats(self):
        return "HP: {}, Min_Attack: {}, Max_Attack: {}, Defence: {}".format(self.hp, self.min_attack, self.max_attack, self.defence)


class ARCHER(PLAYER):
    def __init__(self, hp = 100, min_attack = 25, max_attack = 150, defence = 25):
        self.hp = int(hp)
        self.defence = int(defence)
        self.min_attack = int(min_attack)
        self.max_attack = int(max_attack)
    def strike(self):
        damage = dmg * (self.attack*0.01)
        return damage

    def stats(self):
        return "HP: {}, Min_Attack: {}, Max_Attack: {}, Defence: {}".format(self.hp, self.min_attack, self.max_attack, self.defence)



def start():
    print("Welcome to my game! \n What is your name?")
    name = input()
    return classes()


def classes():
    global player_class
    print("The following classes are available. \n Swordmaster: {} \n Archer: {}".format(SWORD_MASTER().stats(),ARCHER().stats()))
    chosen_class = input("Which class do you want to be")
    if chosen_class == "archer":
        player_class = ARCHER()

    elif chosen_class == "swordmaster":
        player_class=SWORD_MASTER()

    else:
        print("You chose an class which isn't available. Please choose again")
        return classes()
    return first_part()


def first_part():
    print("You come across a wild dog. He attacks you")
    player_class.hp -= (wild_dog.attack - player_class.defence)
    print("You lose {} hp and leaves you with {} hp."
          .format(wild_dog.attack - player_class.defence, player_class.hp))
    action = input("Do you want to run away or attack.")
    if action == "run away":
        return run_away()
    elif action == "attack":
        return fight(wild_dog)


def fight(enemy):
    count = 0
    damage = random.randint(player_class.min_attack, player_class.max_attack)
    enemy.hp -= damage
    if enemy.hp<0:
        print("With your strike you dealt {} damage and caused your enemy to die".format(damage, enemy.hp))
    else:
        print("With your strike you dealt {} damage and caused your enemy lifepoints to drop to {}"
              .format(damage, enemy.hp))


if __name__=="__main__":
    start()

