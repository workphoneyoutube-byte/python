from assault import assault
# Define a simple battle sequence for the game
def battle_sequence():
    print("Welcome to the collosseum!")
    hero = assault.Hero("Arin","Warrior",50,30,15,20)
    enemy = assault.EnemyProto("Goblin","Infantry",30,0,10,5)
    hero.display_info()
    enemy.display_info()
    assault.start_battle(hero, enemy)
    print("The battle is over!")

