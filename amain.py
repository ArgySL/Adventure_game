import random, sys, time
health = 100
gold = 0
foodstuff = {"bread":10,"cheese":15, "pizza":25}
inventory = []

def main_game():
    
## Definining interactible game objects (traps, food)
    def trap(trap_damage):
         trap_damage = (10,20,30)
         return random.sample(trap_damage, 1)
    
        
    
## Act 0, Prologue
def act_0():    
    print("Welcome, Adventurer! You have been imprisoned by Prince Volgar in his dungeons for stealing his rubber duck! You need to escape, hopefully with as much gold as possible! But beware of traps! ")
    time.sleep(10)
    print("While twindling your thumbs imprisoned in Prince Volgar's foul dungeons, you devise a plan to escape, deciding the best time to carry it out is during Volgar's corronation date! ")
    input("...")
## Act 1, Prison
def act_1():
    print("Two weeks have passed, and it is finally Volgar's corronation date! The time to act would be while the guards are... distracted by the festivities!")
    input("...")
    print("You had gathered information before about Cpt. Bingo, the chief prison warden. He's known to party real hard when there are celebrations of any kind, and you'll be taking advantage of that!")
    input("...")
    print("You find yourself in a 4x4 prison cell. There are 3 more similar cells in the prison. Now that the guards have stopped ")
    print("Below is a top-down map of the Prison: ")
    print("Legend: g = Guard, f = Food, t = Treasure(!), * = You! ")
    print(" [_____N____]")
    print(" [*]      [ ]")
    print("W[          ]E")
    print(" [ ]      [f]")
    print(" [__  _S____]")
    try:
        action1 = input("Press enter turn your spoon into a lockpick, or press 'w' to wait...")
        if action1 == 'w':
            print("You waited so long that eventually the guards sobered, came back to the prison and you missed your best opportunity to escape! Game Over!")
            sys.exit()
    except SyntaxError:
            print("You inputted an incorrect command!")
    inventory.append('lockpick')
    print("You obtained the cells' keys! Your inventory now includes :" , inventory[0])
    try:
        action2 = input("Would you like to explore the prison or leave? (Press enter to leave, press 'e' to explore! )")
        if action2 == 'e':
             print("")

## Act 2, Dungeon
    
    def act_2():
        print("After ")
    '''
    print(" [____N____]")
    print(" [*]      []")
    print("W[         ]E")
    print(" []       []")
    print(" [_   S____]")
## Act 3, Barracks
    #def act_3():
    print(" [____N____]")
    print(" [*]      []")
    print("W[         ]E")
    print(" []       []")
    print(" [_   S____]")
## Bonus, Treasury
    #def bonus_act():
    print(" [____N____]")
    print(" [*]      []")
    print("W[         ]E")
    print(" []       []")
    print(" [_   S____]")
## Act 4, Garden
    #def act_4():
    print(" [____N____]")
    print(" [*]      []")
    print("W[         ]E")
    print(" []       []")
    print(" [_   S____]")
## Act 5, Streets
    #def act_5():
    print(" [____N____]")
    print(" [*]      []")
    print("W[         ]E")
    print(" []       []")
    print(" [_   S____]")
    '''
main_game()
act_0()
act_1()
#act_2()
#act_3()
#bonus_act()
#act_4()
#act5()