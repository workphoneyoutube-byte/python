# Enemy Assault
# Norse Music - Nordic Versecraft - Bloodr ok Eldr  --  Blood and Fire 

#BEGDEF
"Purpose: Stage 1 Enemy Prototype"

class EnemyProto:
    def __init__(self,name,type,hp,mp,defence,attack):
        self.enemy_Name = name
        self.enemyType = type
        self.enemyHP = hp
        self.enemyMP = mp
        self.enemyDEF = defence
        self.enemyATT = attack
    
    def take_damage(self,heroATT):
        damage = heroATT * ((100 - self.enemyDEF) / 100)
        self.enemyHP -= damage
        if self.enemyHP < 0:
            self.enemyHP = 0
        return damage
    
    def isBoss(self):
        return self.enemyType == "Chief"                
        
    def display_info(self):
        print("The enemies name is: " + self.enemy_Name)
        print("The enemies type is: " + self.enemyType)
        print("The enemies current HP: " + str(self.enemyHP))
        print("The enemies current MP: " + str(self.enemyMP))
        print("The enemies Defence: " + str(self.enemyDEF))
        print("The enemies Attack: " + str(self.enemyATT))
    
# Enemy Chief Prototype
class ChiefEnemy(EnemyProto):
    def __init__(self,name_in,spec_ab1,spec_ab2):
        self.name = name_in
        self.shoe_throw = spec_ab1
        self.fake_leg = spec_ab2

    def display_info(self):
        print("The enemy Chief's name is: " + self.name)
        print("The enemy Chief's type is: " + self.enemyType)
        print("The enemy Chief uses " + self.shoe_throw)
        print("The enemy Chief uses " + self.fake_leg)



# Hero Prototype

class Hero:
    def __init__(self,name,type,hp,mp,defence,attack):
         self.name = name
         self.type = type
         self.hp = hp
         self.mp = mp
         self.heroDEF = defence
         self.heroATT = attack
    
    def display_info(self):
         print(self.name)
         print(self.type)
         print(int(self.hp))
         print(int(self.mp))
         print(int(self.heroDEF))
         print(int(self.heroATT))

    def damageTaken(self,enemyATT):
        damage = enemyATT * ((100 - self.heroDEF) / 100)
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        return damage

class Thief(Hero):
    def __init__(self,name,type,hp,mp,defence,attack,spec_ab1,spec_ab2):
        super().__init__(name,type,hp,mp,defence,attack)
        self.steal = spec_ab1
        self.stab = spec_ab2

class Warrior(Hero):
    def __init__(self,name,type,hp,mp,defence,attack,spec_ab1,spec_ab2):
        super().__init__(name,type,hp,mp,defence,attack)
        self.roar = spec_ab1 
        self.rage = spec_ab2

#ENDDEF


#BEGDEF Battle Function
def start_battle(hero,enemy):
    "Runs a simple turn-based battled between hero and enemy prototypes"
    print("A wild " + enemy.enemy_Name + " appears!")
    while hero.hp > 0 and enemy.enemyHP > 0:
        damage_to_enemy = enemy.take_damage(hero.heroATT)
        print(hero.name + " attacks " + enemy.enemy_Name + " for " + str(int(damage_to_enemy)) + " damage!")
        if enemy.enemyHP <= 0:
            print(enemy.enemy_Name + " has been defeated!")
            break
        damage_to_hero = hero.damageTaken(enemy.enemyATT)
        print(enemy.enemy_Name + " attacks " + hero.name + " for " + str(int(damage_to_hero)) + " damage!")
        if hero.hp <= 0:
            print(hero.name + " has been defeated!")
            break
        print(hero.name + " HP: " + str(int(hero.hp)) + " | " + enemy.enemy_Name + " HP: " + str(int(enemy.enemyHP)))
#ENDDEF