import random, sys, time
# Declaring health and gold as global variables so python doesn't get confused with in-function declaration.

global health, gold, inventory
health = 100
gold = 0
inventory = []

def main_game():
    
## Definining interactible game objects (traps, food)
    ''' Unfortunately, there was not enough time to implement more complex features to the game, like consumables that recover the player's health or traps, but they might be considered for a future update

    foodstuff = {"bread":10,"cheese":15, "pizza":25}
    def trap(trap_damage):
         trap_damage = (10,20,30)
         return random.sample(trap_damage, 1)

    ''' 
## The game progression is pretty linear, as you might read in the README file. The game is presented via a series of prints, and the player has to react to what appears before them.     
    
## Act 0, Prologue
def act_0():
    print("ACT 0, Prologue")    
    print("Welcome, Adventurer! You have been imprisoned by Prince Volgar in his dungeons for stealing his rubber duck! You need to escape, hopefully with as much gold as possible! But beware of traps! ")
    input("Press Enter to continue every time you see '...'!")
    print("While twindling your thumbs imprisoned in Prince Volgar's foul dungeons, you devise a plan to escape, deciding the best time to carry it out is during Volgar's corronation date! ")
    input("...")
## Act 1, Prison
def act_1():
    print("ACT 1, Prison")
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
        action1 = input("Press 'l' to turn your spoon into a lockpick, or press 'w' to wait...")
        if action1 == 'w':
            print("You waited so long that eventually the guards sobered, came back to the prison and you missed your best opportunity to escape! Game Over!")
            main_game()
        elif action1 == 'l':
             inventory.append('lockpick')
             print("You obtained a lockpick! Your inventory now includes :" , inventory[0])
    except SyntaxError:
            print("You inputted an incorrect command!")
    
    try:
        action2 = input("You use your masterfully-crafted lockpick to unlock your cell and get out. Would you like to explore the prison or leave? (Press 'l' to leave, press 'e' to explore! )")
        if action2 == 'e':
             inventory.append('bread')
             print("You picked up a loaf of bread when exploring from the south-eastern cell! Your inventory now includes: ", inventory)
             input("...")
        elif action2 == 'l':
             print("You exit the prison and head for the dungeon!")
             input("...")
    except SyntaxError:
            print("You inputted an incorrent command!")
## Act 2, Dungeon
    
def act_2():
    print("ACT 2, Dungeon")
    print("After making it to the dungeon, you take your time and hide in corner where the dim light of the torches doesn't reach. You scout out the area and make a crude mental image of it in your brain: ")
    print("Legend: g = Guard, f = Food, t = Treasure(!), * = You! ")
    print(" [_  *N_____]")
    print(" |[]      []|")
    print("W|[]      []|E")
    print(" |[]    G[T]|")
    print(" [_   S_____]")
    input("...")
    try:
        action3 = input("There are more prison cells in the dungeon, plus a guard keeping watch. That guard is guarding a small treasure chest. The guard appears to be cold out; there is a heavy smell of alcohol in the air. What will you do? (Press 'N' to sneak past the guard, or press 'S' to steal the treasure!)")
        if action3 == 's':
            inventory.append('Bronze Volgar Figurine')
            gold =+ 20
            print("After you silently unlock the cell, you open the chest and discover 20 gold pieces and a bronze figurine resembling Prince Volgar. You pocket everything!")
            print("With a slight glee formed on your face, you sneak past the guard and head towards the barracks!")
            input('...')
            return gold
        elif action3 == 'n':
            print("You decided not to risk it and sneak past the guard towards the next area towards the south, the barracks!")
            gold =+ 0
            return gold
    except SyntaxError:
            print("You inputted an incorrect command!")
    return gold

## Act 3, Barracks
def act_3():
    print("Act 3, Barracks")
    print("You brace yourself when you walk into the barracks; the smell of alcohol is even stronger here. You scout once more from the safety of the shadow the door creates and form a mental image of the area: ")
    print("Legend: ]=Weapon Rack, \ = Crumbling Wall, G = Guard, * = You!")
    print(" [_  *N_____]")
    print(" |]        [|")
    print("W|\G       [] E")
    print(" |]        [| ")
    print(" [_G  S_____]")
    print("You notice there are at least two guards in the area, and there might be more...")
    input("...")
    try:
        action4 = input("What would you like to do? (Press 's' to search the weapon racks, press 'a' to ambush the nearest guard, press 'n' try and sneak past the guards")
        if action4 == 's':
            print("You make too much noise while searching the racks, the nearest guard is alerted to your presence and alarms the rest! Game Over!")
            action5 = input("Press enter to quit or press 'r' to restart the game")
            if action5 == 'r':
                act_1()    
            else:
                sys.exit()
        if action4 == 'a':
            print("You make some noise by knocking the door you're hiding behind. The guard is lured to your position to check the noise out... You try to knock him out as soon as he turns, but he smacks you in the face! (-10 Health). You swiftly recover and sweep his feet with a kick then choke him and knock him out!")
            input('...')
            health =- 10
            action6 = input("The noise thankfully did not alert the guard at the other side of the room. Is he asleep or under the effects of intoxication? Regardless, you have more choices now... Press 'e' to examine the crumbling wall, press 's' to sneak past the guard to the next area, or press 'w' to wait. ")
            if action6 == 'e':
                bonus_act()
        if action4 == 's':
            print("You find it very difficult to sneak past the watchful gaze of this particular guard; you realise the gold you're carrying is making too much noise! You have no other choise but to drop all your gold to sneak through to the next area...")
            gold = 0
            return gold
    except SyntaxError:
         print("You inputted an incorrect command!")

def bonus_act():
    print("Bonus Act, Treasury!")
    print("You try to examine the crumbling wall, knock on it, feel it with your hands; eventually part of the wall crumbles and you take a sneak peak inside... ")
    input("...")
    print("The room behind the wall looks pretty luxurious, there are at least 4 coffers of valuables across the other side of the room! The room is dimly lit, there appears to be no other exit; seems like the entrance is supposed to be hidden but you were lucky enough to find a crumbling wall to sneak in!!!")
    print("Legend: T=Treasure, ] = Weapon Racks")
    print(" [____N____]")
    print(" |]        |")
    print(" |T]       |")
    print("W|T][T]   * E")
    print(" |T]       |")
    print(" []___S____]")
    action7 = input("You're trembling with excitement over the thoughts of riches... What would you like to do?! (Press 'L' to loot all the treasure chests, press 'r' to leave)")
    try:
         if action7 == 'l':
            print("You open all the chests one by one with impunity, greed oozing from your eyes! You are simply not able to carry everything on your own, but you pocket the most valuable articles: ")
            gold =+ 200
            inventory.extend(["Ruby","Sapphire","Diamond","Emerald","Pile of Zircons"])
            print("You obtained 200 gold, many valuable gems!")
            status = input("Would you like to view your status? (Inventory, gold, health points) (y/n)")
            if status == 'y':
                print(f"You inventory consists of: {inventory}, your health is: {health}, and your gold is: {gold}")
                input("...")
            
            print("By the time you're finished looting, you head back to the barracks, only to discover that the other guard is lying on the flour, with a small lake of puke next to him. He passed out from drinking too much, the fool... You head outside towards the next area...")
            input('...')
    except SyntaxError:
         print("You inputted an incorrect command!")
    return gold, health
         
## Act 4, Garden
def act_4():
    print("Act 4, Royal Garden")
    input('...')
    print("After exiting the barracks, you find yourself in a spacious scenery of green, dazzling lights, chatter, laughter and overal chaos. You realise you are in the Royal Garden and the festivities are going wild.")
    print("Legend: , t = Table, G = Guard, P = Patron, S = Servant, * = You!")
    print(" [___ *No_____]")
    print(" [P   S  P(t) |___")
    print("We[(t) PP  PP (t) |Ea")
    print(" [T]PP    SPP (t) |__")
    print(" [_____G   G_________]")
    print("          So        ")
    input('...')
    action8 = input("Everyone is in a festive mood; the atmosphere is exhilarating, but not for you... You have to get away! (Press 'w' to walk towards the exit, 'c' to chat with the nearest patron or servant, 'l' to look around the tables...) ")
    try:
         if action8 == 'w':
              print("You try to shuffle through the patrons, while trying your best to appear inconspicuous. You can feel the sneering gaze of some of them, as well as the servants', but you do not care. You reach the gate and walk out like no one's business! Apparently the guards were instructed to thoroughly check everyone who walks in, but not people who walk out... ")
              input('...')
    except SyntaxError:
         print("You inputted an incorrect command!")    

## Act 5, Streets
def act_5():
    print("Act 5, Streets")
    print("After you finally make it past the gate of the Royal Garden, you find yourself in the streets surrounding the castle. In order to feel safe, you want to get to your hideout...")
    input('...')
    print("You cannot clearly make out what's going on in the streets, what with all the lights and festivities going on so what you can figure out is listed below:")
    print("Legend: P = Passerby, S = Stall, H = Hideout, * = You!")
    print(" [___ *No____]")
    print(" [S  P   P   ]")
    print(" [SP    P PS ]")
    print("We[ P   P P S]Ea")
    print(" [ P  P  P S ]")
    print(" [P  P   P   ]")
    print(" [__  So____H]")
    input("...")
    action9 = input("How are you going to proceed? (Press 'c' to chat with the nearest passerby, 's' to check the stalls, or 'h' to head straight to your hideout...)")
    try:
         if action9 == 'h':
              print(f"Congrats! You reached your hideout and you're safe and sound, at least for the time being! Your total gold is: {gold} and you successfully looted: {inventory}")
    except SyntaxError:
        print("You inputted the wrong command!")
         
main_game()
act_0()
act_1()
act_2()
act_3()
act_4()
act_5()