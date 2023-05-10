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
    time.sleep(5)
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
    print(" [_____N_____]")
    print(" |[*]     [ ]|")
    print(" |W         E|")
    print(" |[ ]     [f]|")
    print(" [__  _S_____]")
    try:
        action1 = input("Press enter turn your spoon into a lockpick, or press 'w' to wait...")
        if action1 == 'w':
            print("You waited so long that eventually the guards sobered, came back to the prison and you missed your best opportunity to escape! Game Over!")
            sys.exit()
    except SyntaxError:
            print("You inputted an incorrect command!")
    inventory.append('lockpick')
    print("You obtained a lockpick! Your inventory now includes :" , inventory[0])
    try:
        action2 = input("Would you like to explore the prison or leave? (Press enter to leave, press 'e' to explore! )")
        if action2 == 'e':
             inventory.append('bread')
             print("You picked up a loaf of bread when exploring from the south-eastern cell! Your inventory now includes: ", inventory)
             time.sleep(3)
             
        else:
             print("You exit the prison and head for the dungeon!")
    except SyntaxError:
            print("You inputted an incorrent command!")
## Act 2, Dungeon
    
def act_2():
    print("After making it to the dungeon, you take your time and hide in corner where the dim light of the torches doesn't reach. You scout out the area and make a crude mental image of it in your brain: ")
    print(" [_  *N_____]")
    print(" |[]      []|")
    print("W|[]      []|E")
    print(" |[]    G[T]|")
    print(" [_   S_____]")
    time.sleep(5)
    try:
        action3 = input("There are more prison cells in the dungeon, plus a guard keeping watch. That guard is guarding a small treasure chest. The guard appears to be cold out; there is a heavy smell of alcohol in the air. What will you do? (Press Enter to sneak past the guard, or press S to steal the treasure!)")
        if action3 == 's':
            current_gold = 0
            inventory.append('Bronze Volgar Figurine')
            current_gold = gold + 20
            print("After you silently unlock the cell, you open the chest and discover 20 gold pieces and a bronze figurine resembling Prince Volgar. You pocket everything!")
            print(f"You currently possess {current_gold} pieces, and these items: {inventory} !")
            print("With a glee formed on your face, you sneak past the guard and head towards the barracks!")
            return current_gold, gold
        else:
            print("You decided not to risk it and sneak past the guard towards the next area towards the south, the barracks!")
    except SyntaxError:
            print("You inputted an incorrect command!")  
    
    
## Act 3, Barracks
def act_3():
    print("You brace yourself when you walk into the barracks; the smell of alcohol is even stronger here. You scout once more from the safety of the shadow the door creates and form a mental image of the area: ")
    print("Legend: ]=Weapon Rack, \ = Crumbling Wall, G = Guard")
    print(" [_  *N_____]")
    print(" |]        [|")
    print("W|\G       [] E")
    print(" |]        [| ")
    print(" [_G  S_____]")
    '''
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
act_2()
act_3()
#act_3()
#bonus_act()
#act_4()
#act5()