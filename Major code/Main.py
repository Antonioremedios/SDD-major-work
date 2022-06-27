#Importing all the classes and tools I will be using to create the code 
import time
import random
import colorama
from Enemy import generate_enemies, instantiate_enemies
from Hero import generate_heros
from Scroll import generate_scrolls
from Merchant import generate_merchants

def new_game_page():#the code that will be able to print a game page when I type new_game_page() instead of writing it the whole time
    for i in range(1,20):
        print("")
        time.sleep(.1)

def add_enemies():#adds all the enemies into a list so they can be added to the correct place in the game
    generation = generate_enemies()

    enemies = [generation[0], 
                generation[2], 
                generation[4], 
                generation[6], 
                generation[8]]
    
    bosses = [generation[1], 
                generation[3], 
                generation[5], 
                generation[7], 
                generation[9]]

    return(bosses, enemies)


# the choose hero menu for the code makes it so that 

def choose_starter_hero(gob, archer, knight):
    new_game_page()

    check = 0
    while check == 0: 
        print(colorama.Fore.BLUE +"Chosse a Hero for this adventure:")#gives the player the options so they can choose 
        print(""+colorama.Fore.GREEN)
        print("Goblin:" +colorama.Fore.WHITE , "Is weak but is sneaky and grabs more loot per conflict.")
        print(""+colorama.Fore.MAGENTA)
        print("Archer:"+colorama.Fore.WHITE, "Is very fast, a mid tier hero will have 1 less conflict per level.")
        print(""+colorama.Fore.CYAN)
        print("Kight:"+colorama.Fore.WHITE, "Is a slow hero but very strong, will have 1 extra conflict per level")
        print("")
        print("")
        herochoice = input("Pick again: ")
        if herochoice.lower() == "goblin" or int(herochoice) == 1:#Checks herochoice to see what hero that the player chose 
            check = 1
            player = gob
            check_if_hero_used_give_name(player)

        elif herochoice.lower() == "archer" or int(herochoice) == 2:
            check = 1
            player = archer
            check_if_hero_used_give_name(player)
        
        elif herochoice.lower() == "knight" or int(herochoice) == 3:
            check = 1
            player = knight
            check_if_hero_used_give_name(player)
        
        else:
            new_game_page()
            print("Unable to decipher your hero")
    return(player)
    

def check_if_hero_used_give_name(player):#gives the hero that they chose a name if they havent given one already
    new_game_page()
    if player.used == 0:
        print(colorama.Fore.BLUE+"You havent used this hero yet")
        print(""+colorama.Fore.WHITE)
        name = input("Give this hero a name: ")
        new_game_page()
        player.name = name
        player.used = 1
    print(colorama.Fore.WHITE+ "Lets start an adventure with"+colorama.Fore.BLUE, player.name , player.charactertype)

def combat(player, enemy, scrolls):#the combat bewtween an enemy and this makes it so that it is a fight 
    print("You encounter a"+colorama.Fore.RED, enemy.name,colorama.Fore.WHITE + 
                "seems easy enough,"+colorama.Fore.RED, "TiMe fOR A FiGht!!!")
    while player.health > 0 and enemy.health > 0: 
        check = 0
        opp_action = random.randint(1,2)
        while check == 0:#Makes the enemy do thei next move when the player has completed their turn  
            print(colorama.Fore.WHITE)
            print("Its your turn what will you do")#give the player their options 
            print(colorama.Fore.RED)
            print("Attack", player.damage)
            print(colorama.Fore.CYAN)
            print("Block:" ,player.block)
            print(colorama.Fore.MAGENTA)
            print("Inventory: for scrolls")
            print(colorama.Fore.WHITE)
            if opp_action == 1:#tells the player if the enemy will be blocking or attacking
                print("The"+colorama.Fore.MAGENTA,enemy.name, colorama.Fore.WHITE+ 
                    "has"+colorama.Fore.RED, str(enemy.health),colorama.Fore.WHITE+ 
                    "health left and will be attacking for"+colorama.Fore.RED, str(enemy.damage))
            else:
                print("The"+colorama.Fore.MAGENTA,enemy.name, colorama.Fore.WHITE+ 
                    "has"+colorama.Fore.RED, str(enemy.health),colorama.Fore.WHITE+ 
                    "health left and will be blocking for"+colorama.Fore.CYAN, str(enemy.block))
            print("")
            print(colorama.Fore.BLUE+"You have"+colorama.Fore.RED,str(player.health)+colorama.Fore.BLUE,"health left")
            print("")
            print(colorama.Fore.BLUE)
            choice = input("what will you do: ")
            new_game_page()#does the choice that the player chose
            if choice.lower() == "attack":#does the attack move
                print(colorama.Fore.WHITE+"you go for the"+colorama.Fore.RED, "attack")
                if opp_action == 2:
                    print(colorama.Fore.WHITE)
                    print("The enemy tries to block your attack for"+ colorama.Fore.CYAN, str(enemy.block)
                                                                                    + colorama.Fore.WHITE)
                    print("")
                    damage = player.damage - enemy.block
                    if damage <= 0:
                        print("You end up doing zero damage your attack isn't strong enough")
                        print("")
                    else:
                        print("You end up doing"+colorama.Fore.RED, str(damage),colorama.Fore.WHITE )
                        print("")
                        enemy.health = enemy.health - damage
                else:
                    print(colorama.Fore.WHITE)
                    enemy.health = enemy.health - player.damage
                    print("You deal"+ colorama.Fore.RED,str(player.damage)+colorama.Fore.WHITE,
                            "damage to the"+colorama.Fore.RED,enemy.name)
                    if enemy.health > 0:
                        print(colorama.Fore.WHITE)
                        print("The enemy takes your attack and tries to do one better")
                        print("")
                        print("The enemy goes for the attack doing"+colorama.Fore.RED,str(enemy.damage)
                                                                        +colorama.Fore.WHITE,"damage")
                        player.health = player.health - enemy.damage
                    else:
                        print(colorama.Fore.WHITE)
                        print("You have killed the"+colorama.Fore.RED,enemy.name)
                        print(colorama.Fore.WHITE)
                        print("time for your next battle")
                check = 1
            
            elif choice.lower() == "block":#does the block move
                print(colorama.Fore.WHITE+"you go for the"+colorama.Fore.CYAN, "Block")
                if opp_action == 1:
                    print(colorama.Fore.WHITE)
                    print("The enemy tries to attack you for"+ colorama.Fore.RED, str(enemy.damage)+ colorama.Fore.WHITE)
                    print("")
                    damage = enemy.damage - player.block
                    if damage <= 0:
                        print("Their attack isnt strong enough and they dont deal any damage to you")
                        print("")
                    else:
                        print("You end up getting"+colorama.Fore.RED, str(damage),colorama.Fore.WHITE+ "damage done to you" )
                        print("")
                        player.health = player.health - damage
                else:
                    print(colorama.Fore.WHITE)
                    print("Blocking while the enemy is blocking haven't seen that one before")
                    print("")
                check = 1
            
            elif choice.lower() in "inventory":#opening inventory and using a scroll does not count as a move that is why check still equals 0 at the end of inventory
                if player.inventory[0] == 0 and player.inventory[1] == 0 and player.inventory[2] == 0 and player.inventory[3] == 0:
                    print("You dont have any Scrolls yet")
                else:
                    see = 0
                    while see == 0:
                        new_game_page()
                        print(colorama.Fore.WHITE)
                        print("Here are the Scrolls you have (Damage, Add health)")
                        print(colorama.Fore.GREEN)
                        print(scrolls[0].name, 
                                str(player.inventory[0]), 
                                "("+str(scrolls[0].damage)+",", str(scrolls[0].block)+")")
                        print(colorama.Fore.RED)
                        print(scrolls[1].name, 
                                str(player.inventory[1]), 
                                "("+str(scrolls[1].damage)+",", str(scrolls[1].block)+")")
                        print(colorama.Fore.CYAN)
                        print(scrolls[2].name, 
                                str(player.inventory[2]), 
                                "("+str(scrolls[2].damage)+",", str(scrolls[2].block)+")")
                        print(colorama.Fore.MAGENTA)
                        print(scrolls[3].name, 
                                str(player.inventory[3]), 
                                "("+str(scrolls[3].damage)+",", str(scrolls[3].block)+")")
                        print(colorama.Fore.WHITE)
                        scroll_choice = input("Choose a Scroll or go back: ")
                        new_game_page()

                        if scroll_choice.lower() == "grass scroll" or scroll_choice.lower() == "grass" and player.inventory[0] > 0:
                            print("You use a"+colorama.Fore.GREEN, scrolls[0].name)
                            player.inventory[0] = player.inventory[0] - 1
                            see = 1
                            enemy.health = enemy.health - scrolls[0].damage
                            player.health = player.health + scrolls[0].block
                            print(colorama.Fore.WHITE)
                            print("You deal"+colorama.Fore.RED,str(scrolls[0].damage)+colorama.Fore.WHITE,"damage to"+colorama.Fore.RED,enemy.name)
                            print(colorama.Fore.WHITE)
                            print("And give yourself"+colorama.Fore.BLUE,str(scrolls[0].block)+colorama.Fore.WHITE,"health")
                            time.sleep(2)
                            print("")

                        elif scroll_choice.lower() == "fire scroll" or scroll_choice.lower() == "fire" and player.inventory[1] > 0:
                            print("You use a"+colorama.Fore.RED, scrolls[1].name)
                            player.inventory[1] = player.inventory[1] - 1
                            see = 1
                            enemy.health = enemy.health - scrolls[1].damage
                            print(colorama.Fore.WHITE)
                            print("You deal"+colorama.Fore.RED,str(scrolls[1].damage)+colorama.Fore.WHITE,"damage to"+colorama.Fore.RED,enemy.name)
                            time.sleep(2)
                            print(colorama.Fore.WHITE)

                        elif scroll_choice.lower() == "ice scroll" or scroll_choice.lower() == "ice" and player.inventory[2] > 0:
                            print("You use a"+colorama.Fore.CYAN, scrolls[2].name)
                            player.inventory[2] = player.inventory[2] - 1
                            see = 1
                            enemy.health = enemy.health - scrolls[2].damage
                            player.health = player.health + scrolls[2].block
                            print(colorama.Fore.WHITE)
                            print("You deal"+colorama.Fore.RED,str(scrolls[2].damage)+colorama.Fore.WHITE,"damage to"+colorama.Fore.RED,enemy.name)
                            print(colorama.Fore.WHITE)
                            print("And give yourself"+colorama.Fore.BLUE,str(scrolls[2].block)+colorama.Fore.WHITE,"health")
                            time.sleep(2)
                            print("")

                        elif scroll_choice.lower() == "plasma scroll" or scroll_choice.lower() == "plasma" and player.inventory[3] > 0:
                            print("You use a"+colorama.Fore.MAGENTA, scrolls[3].name)
                            player.inventory[3] = player.inventory[3] - 1
                            see = 1
                            enemy.health = enemy.health - scrolls[3].damage
                            player.health = player.health + scrolls[3].block
                            print(colorama.Fore.WHITE)
                            print("You deal"+colorama.Fore.RED,str(scrolls[3].damage)+colorama.Fore.WHITE,"damage to"+colorama.Fore.RED,enemy.name)
                            print(colorama.Fore.WHITE)
                            print("And give yourself"+colorama.Fore.BLUE,str(scrolls[3].block)+colorama.Fore.WHITE,"health")
                            time.sleep(2)
                            print("")

                        elif scroll_choice.lower() == "back":
                            see = 1

                        else:
                            print(colorama.Fore.WHITE)
                            print("Couldn't use that scroll try again")
                            time.sleep(2)
                    time.sleep(2)        
                    new_game_page()
                if enemy.health <= 0:
                    check = 1
                    
            else:#makes the player go again for not getting the right input
                print("Didn't understand that command try again")
                time.sleep(2)
                new_game_page()
        time.sleep(3)
        new_game_page()
    if player.health > 0:#gives the player a boost if they win 
        print("Easy win time to move on")
        print("")
        print("Collect your reward now")
    else:
        print("sadly you have died better luck next time")
    time.sleep(2)

def display_rewards(player):#displays the players rewards so that they know what they have 
    print(colorama.Fore.WHITE)
    print("You now have: ")
    print(colorama.Fore.YELLOW)
    print(player.gold,"Gold.")
    print(colorama.Fore.RED)
    print(player.blood,"Blood.")
    print(colorama.Fore.CYAN)
    print(player.diamond,"Diamonds.")
    print(colorama.Fore.GREEN)
    print("Scrolls (Grass, Fire, Ice, Plasma)")
    print("("+str(player.inventory[0])+","
        ,str(player.inventory[1])+","
        ,str(player.inventory[2])+","
        ,str(player.inventory[3])+")")

    time.sleep(3)
    new_game_page()


def pick_enemy(level, enemies):
    max = len(enemies[level]) - 1
    choice = random.randint(0, max)
    return(enemies[level][choice])

def give_reward(rechoice, player):#gives the player their reward when completing a conflict 
    if rechoice == "nothing":#gives nothing
        print(colorama.Fore.WHITE)
        print("You got nothing from this encounter")
        display_rewards(player)#displays the players rewards so they know what they have 

    elif rechoice == "gold":#
        print(colorama.Fore.YELLOW)
        amount = random.randint(20,70)
        if player.number == 1:
            print("You get",str(amount + 20),"gold from this encounter")
            player.gold = player.gold + amount +20
            display_rewards(player)
        else:
            print("You get",str(amount),"gold from this encounter")
            player.gold = player.gold + amount
            display_rewards(player)
    
    elif rechoice == "blood":
        print(colorama.Fore.RED)
        amount = random.randint(15,55)
        if player.number == 1:
            print("You get",str(amount+15),"blood from this encounter")
            player.blood = player.blood + amount+15
            display_rewards(player)
        else:
            print("You get",str(amount),"blood from this encounter")
            player.blood = player.blood + amount
            display_rewards(player)
    
    elif rechoice == "diamonds":
        print(colorama.Fore.CYAN)
        amount = random.randint(10,25)
        if player.number == 1:
            print("You get",str(amount+10),"diamonds from this encounter")
            player.diamond = player.diamond + amount
            display_rewards(player)
        else:
            print("You get",str(amount+10),"diamonds from this encounter")
            player.diamond = player.diamond + amount
            display_rewards(player)
        
    else:#if the reaward is a scroll player will get a random scroll 
        print(colorama.Fore.GREEN)
        print("you get a scroll")
        print("")
        ran_scroll = random.randint(0,100)
        if ran_scroll <= 40:#Grass scroll is the most common 40% of scrolls will be grass
            player.inventory[0] = player.inventory[0] + 1
            print("A Grass Scroll has now been added")
        elif ran_scroll <= 70:#fire scroll is second in commonality 30% of scrolls will be fire scrolls
            player.inventory[1] = player.inventory[1] + 1
            print("A Fire Scroll has now been added")
        elif ran_scroll <=90:#ice scolls have a 20% chance of being gotten adds to inventory if randomly picked
            player.inventory[2] = player.inventory[2] + 1
            print("A Ice Scroll has now been added")
        else:
            player.inventory[3] = player.inventory[3] + 1
            print("A Plasma Scroll has now been added")#gives a plasma scroll if the random number is greater than 90
        display_rewards(player)
    

def conflict(player, level, enemies, scrolls):
    rewardchoice1 = make_a_path()
    rewardchoice2 = make_a_path()
    rewardchoice3 = make_a_path()
    check = 0
    while check == 0:
        print(colorama.Fore.BLUE+"Choose a reward for this next conflict (by number)")
        print(colorama.Fore.WHITE)
        display_path(rewardchoice1, 1)#display path 1
        print("")
        display_path(rewardchoice2, 2)#dispaly path 2
        print("")
        display_path(rewardchoice3, 3)#diplay path 3
        print(colorama.Fore.WHITE)
        print("")
        choice = input("Pick the numbered path you will take: ")#asks for input 
        if choice == "1" or choice == "2" or choice == "3":
            check = 1
        else:
            new_game_page()
            print(colorama.Fore.BLUE+"Couldn't understand which path")#gets the player to choose a path again if the code cant undersat what they inputed
            time.sleep(1)
            print(colorama.Fore.WHITE)
            new_game_page()
    enemy = pick_enemy(level, enemies)
    fight_rand_num = random.randint(0, 10)
    new_game_page()
    if fight_rand_num <= 7:#there is a random instace where the player doesn't have to fight to get a reward this is it 
        combat(player, enemy, scrolls)
    else:
        print("there seems to be noone here easy win")


    if choice == "1" and player.health > 0:
        give_reward(rewardchoice1, player)
    elif choice == "2" and player.health >  0:
        give_reward(rewardchoice2, player)
    elif choice == "3" and player.health > 0:
        give_reward(rewardchoice3, player)
    else:
        new_game_page()#if the player dies they do not get a reward they must beat the conflict to get a reward
        print("Sorry no reward you hvae died")
        display_rewards(player)



def boss_conflict(player, boss, scrolls):#the start of a conflict made it a fuction becasue it means it can be used multiple times
    rewardchoice1 = make_a_path()
    rewardchoice2 = make_a_path()
    rewardchoice3 = make_a_path()
    check = 0
    while check == 0:#makes sure that the player chooses a correct path before moving on 
        print(colorama.Fore.BLUE+"Choose a reward for this next conflict (by number)")#choose a conflict path by inputting which way the player wants to go
        print(colorama.Fore.WHITE)
        display_path(rewardchoice1, 1)
        print("")
        display_path(rewardchoice2, 2)
        print("")
        display_path(rewardchoice3, 3)
        print(colorama.Fore.WHITE)
        print("")
        choice = input("Pick the numbered path you will take: ")#collects input and tests it if able to be true then player moves on 
        if choice == "1" or choice == "2" or choice == "3":
            check = 1
        else:
            new_game_page()
            print(colorama.Fore.BLUE+"Couldn't understand which path")
            time.sleep(1)
            print(colorama.Fore.WHITE)
            new_game_page()
    enemy = boss
    new_game_page()
    combat(player, enemy, scrolls)

    #gives the right reward for which path they chose at the start of the fight
    if choice == "1" and player.health > 0:
        give_reward(rewardchoice1, player)
    elif choice == "2" and player.health > 0:
        give_reward(rewardchoice2, player)
    elif choice == "3" and player.health > 0:
        give_reward(rewardchoice3, player)
    else:
        new_game_page()
        print("sorry you have died")
        display_rewards(player)

def make_a_path(): #makes the avaible options at that start of a conflict to say weather it is what reward 
    randchoice = random.randint(1,100)
    reward = ""
    if randchoice <= 30:
        reward = "nothing" #WHITE
    elif randchoice <= 60:
        reward = "gold" #YELLOW
    elif randchoice <= 80:
        reward = "blood" #RED
    elif randchoice <= 95:
        reward = "diamonds" #CYAN
    else:
        reward = "scroll" #GREEN

    return(reward)
    
def display_path(rechoice, number):#gets the rewards and displays it properly with the correct colour
    if rechoice == "nothing":
        print(colorama.Fore.WHITE+str(number)+"."+colorama.Fore.WHITE,str(rechoice))
    elif rechoice == "gold":
        print(colorama.Fore.WHITE+str(number)+"."+colorama.Fore.YELLOW,str(rechoice))
    elif rechoice == "blood":
        print(colorama.Fore.WHITE+str(number)+"."+colorama.Fore.RED,str(rechoice))
    elif rechoice == "diamonds":
        print(colorama.Fore.WHITE+str(number)+"."+colorama.Fore.CYAN,str(rechoice))
    else:
        print(colorama.Fore.WHITE+str(number)+"."+colorama.Fore.GREEN,str(rechoice))




#makes the heros and add them to there respective list if they are a enemy or a boss
fullenemies = add_enemies()
bosses = fullenemies[0]
enemies = fullenemies[1]

fullheros = generate_heros()
hero_goblin = fullheros[0]
hero_archer = fullheros[1]
hero_knight = fullheros[2]
hero_god = fullheros[3]

scrolls = generate_scrolls()

merchants = generate_merchants()

#start here
# player = choose_starter_hero(hero_goblin, hero_archer, hero_knight)



runs = 1



while 1 == 1:
    check = 0
    while check == 0:
        new_game_page()
        print(colorama.Fore.BLUE+"Welcome to Face The Fantasy")
        print("")
        print(colorama.Fore.CYAN+"1. Start New Game")
        print("")
        print(colorama.Fore.RED+"2. Exit")
        print("")
        print(colorama.Fore.MAGENTA+"3. Easy: (Run to test game without the hardness 2 conflicts per level for the first run)")
        print("")
        print(colorama.Fore.WHITE)
        pick = input("What do you want: ")
        if pick == "1" or pick.lower() == "start":
            new_game_page()
            choose_starter_hero(hero_goblin, hero_archer, hero_knight)
            time.sleep(2)
            new_game_page()
            level = 0 
            conflict_numeber = 1
            if player.number == 1:
                runs = 10
            elif player.number == 2:
                runs = 9
            else:
                runs = 11
            health = player.health
            while level < 1 and player.health >0:
                while conflict_numeber <= runs and player.health >0:
                    conflict(player, level, enemies, scrolls)
                    conflict_numeber = conflict_numeber + 1
                
                if player.health > 0:
                    new_game_page()
                    print("time for a boss fight")
                    time.sleep(3)
                    print("")
                    boss_conflict(player, bosses[level], scrolls)
                        
                    level = level + 1
            
            print(colorama.Fore.WHITE)
            if player.health < 0:
                print("Its sad to see that you died but now you can upgrade and get better and go for another run")
            else:
                print("Congrats on the run win but it seems that all those guys that you killed their brothers have taken their place")
            player.health = health
            return_back = 0
            while return_back == 0:
                level = 0 
                conflict_numeber = 1
                if player.number == 1:
                    runs = 10
                elif player.number == 2:
                    runs = 9
                else:
                    runs = 11

                new_game_page()
                print(colorama.Fore.MAGENTA)
                print("Welcome to the hub")
                print("")
                print("Right now you have",player.name,player.charactertype, "with a health of", str(player.health), 
                        "dealing", str(player.damage),"damage and can do", str(player.block), "block")
                print("")
                print("What would you like to do (by number)")
                print("")
                print("1. Go on another run")
                print("")
                print("2. Trade")
                print("")
                print("3. Change Character")
                print("")
                print("4. Back to main menu")
                print("")
                print(colorama.Fore.BLUE)
                decision = input("Make a choice: ")
                if decision == "1":
                    health = player.health
                    while level < 5 and player.health > 0:
                        while conflict_numeber <= runs and player.health >0:
                            conflict(player, level, enemies, scrolls)
                            conflict_numeber = conflict_numeber + 1
                        
                        new_game_page()
                        print("time for a boss fight")
                        time.sleep(3)
                        print("")
                        boss_conflict(player, bosses[level], scrolls)
                            
                        level = level + 1
                    player.health = health


                elif decision == "2":
                    merchant = merchants[random.randint(0,len(merchants)-1)]
                    out = 0
                    while out == 0:
                        new_game_page()
                        print("You enter the trading center and find", merchant.name)
                        print("")
                        print("1. He will incease the intail health for this hero by 20 for", str(merchant.trade1),"gold")
                        print("")
                        print("2. He will give you + 10 damage for this hero for", str(merchant.trade2),"blood")
                        print("")
                        print("3. He will give you + 15 block for this hero for", str(merchant.trade3),"diamonds")
                        print("")
                        print("4. He will give you a random scroll for", str(merchant.trade4),"diamonds")
                        print("")
                        print("")
                        make = input("'Make a trade?' he asks or do you (leave): ")
                        new_game_page()
                        if make == "1" and player.gold >= merchant.trade1:
                            player.health = player.health + 20
                            print("You get 20 more health")
                            player.gold = player.gold - merchant.trade1
                            if player.number == 1:
                                hero_goblin.health = player.health
                            elif player.number == 2:
                                hero_archer.health == player.health
                            elif player.number == 3:
                                hero_knight.health == player.health
                            else:
                                hero_god.health == player.health

                        elif make == "2" and player.blood >= merchant.trade2:
                            player.damage = player.damage + 10
                            print("You do 10 more damage")
                            player.blood = player.blood - merchant.trade2
                            if player.number == 1:
                                hero_goblin.damage = player.damage
                            elif player.number == 2:
                                hero_archer.damage == player.damage
                            elif player.number == 3:
                                hero_knight.damage == player.damage
                            else:
                                hero_god.damage == player.damage

                        elif make == "3" and player.diamond >= merchant.trade3:
                            player.block = player.block + 15
                            print("You get 15 block")
                            player.diamond = player.diamond - merchant.trade3
                            if player.number == 1:
                                hero_goblin.block = player.block
                            elif player.number == 2:
                                hero_archer.block == player.block
                            elif player.number == 3:
                                hero_knight.block == player.block
                            else:
                                hero_god.block == player.block

                        elif make == "4" and player.diamond >= merchant.trade4:
                            player.diamond = player.diamond - merchant.trade3
                            print(colorama.Fore.GREEN)
                            print("you get a scroll")
                            print("")
                            ran_scroll = random.randint(0,100)
                            if ran_scroll <= 40:
                                player.inventory[0] = player.inventory[0] + 1
                                print("A Grass Scroll has now been added")
                            elif ran_scroll <= 70:
                                player.inventory[1] = player.inventory[1] + 1
                                print("A Fire Scroll has now been added")
                            elif ran_scroll <=90:
                                player.inventory[2] = player.inventory[2] + 1
                                print("A Ice Scroll has now been added")
                            else:
                                player.inventory[3] = player.inventory[3] + 1
                                print("A Plasma Scroll has now been added")
                            display_rewards(player)   

                        elif make.lower() == "leave":
                            out = 1                            
                        else:
                            print("")
                            print("cant do this")
                            time.sleep(1)

                elif decision == "3":
                    gold = player.gold
                    blood = player.blood
                    diamond = player.diamond
                    inventory = player.inventory
                    player = choose_starter_hero(hero_goblin, hero_archer, hero_knight)
                    player.gold = gold
                    player.blood = blood
                    player.diamond = diamond
                    player.inventory = inventory
                elif decision == "4":
                    print("Back to menu:")
                    return_back = 1
                else:
                    print("")
                    print("unable to understand that request try again")
                    time.sleep(1)


        elif pick == "2" or pick.lower() == "exit":
            print("Exiting in:")
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
            time.sleep(1)
            exit()

        elif pick == "3" or pick.lower() == "easy":
            new_game_page()
            print("It seems like you have god as your hero")
            print("")
            print("This must be an easy run for you then")
            time.sleep(2)
            new_game_page()
            runs = 2
            player = hero_god
            level = 0 
            conflict_numeber = 1
            health = player.health
            while level < 5 and player.health >0:
                while conflict_numeber <= runs and player.health >0:
                    conflict(player, level, enemies, scrolls)
                    conflict_numeber = conflict_numeber + 1
                
                if player.health > 0:
                    new_game_page()
                    print("time for a boss fight")
                    time.sleep(3)
                    print("")
                    boss_conflict(player, bosses[level], scrolls)
                        
                    level = level + 1
            
            print(colorama.Fore.WHITE)
            if player.health < 0:
                print("Its sad to see that you died but now you can upgrade and get better and go for another run")
            else:
                print("Congrats on the run win but it seems that all those guys that you killed their brothers have taken their place")
            player.health = health
            return_back = 0
            while return_back == 0:
                level = 0 
                conflict_numeber = 1
                if player.number == 1:
                    runs = 10
                elif player.number == 2:
                    runs = 9
                else:
                    runs = 11

                new_game_page()
                print(colorama.Fore.MAGENTA)
                print("Welcome to the hub")
                print("")
                print("Right now you have",player.name,player.charactertype, "with a health of", str(player.health), 
                        "dealing", str(player.damage),"damage and can do", str(player.block), "block")
                print("")
                print("What would you like to do (by number)")
                print("")
                print("1. Go on another run")
                print("")
                print("2. Trade")
                print("")
                print("3. Change Character")
                print("")
                print("4. Back to main menu")
                print("")
                print(colorama.Fore.BLUE)
                decision = input("Make a choice: ")
                if decision == "1":
                    health = player.health
                    while level < 5 and player.health > 0:
                        while conflict_numeber <= runs and player.health >0:
                            conflict(player, level, enemies, scrolls)
                            conflict_numeber = conflict_numeber + 1
                        
                        new_game_page()
                        print("time for a boss fight")
                        time.sleep(3)
                        print("")
                        boss_conflict(player, bosses[level], scrolls)
                            
                        level = level + 1
                    player.health = health


                elif decision == "2":
                    merchant = merchants[random.randint(0,len(merchants)-1)]
                    out = 0
                    while out == 0:
                        new_game_page()
                        print("You enter the trading center and find", merchant.name)
                        print("")
                        print("1. He will incease the intail health for this hero by 20 for", str(merchant.trade1),"gold")
                        print("")
                        print("2. He will give you + 10 damage for this hero for", str(merchant.trade2),"blood")
                        print("")
                        print("3. He will give you + 15 block for this hero for", str(merchant.trade3),"diamonds")
                        print("")
                        print("4. He will give you a random scroll for", str(merchant.trade4),"diamonds")
                        print("")
                        print("")
                        make = input("'Make a trade?' he asks or do you (leave): ")
                        new_game_page()
                        if make == "1" and player.gold >= merchant.trade1:
                            player.health = player.health + 20
                            print("You get 20 more health")
                            player.gold = player.gold - merchant.trade1
                            if player.number == 1:
                                hero_goblin.health = player.health
                            elif player.number == 2:
                                hero_archer.health == player.health
                            elif player.number == 3:
                                hero_knight.health == player.health
                            else:
                                hero_god.health == player.health

                        elif make == "2" and player.blood >= merchant.trade2:
                            player.damage = player.damage + 10
                            print("You do 10 more damage")
                            player.blood = player.blood - merchant.trade2
                            if player.number == 1:
                                hero_goblin.damage = player.damage
                            elif player.number == 2:
                                hero_archer.damage == player.damage
                            elif player.number == 3:
                                hero_knight.damage == player.damage
                            else:
                                hero_god.damage == player.damage

                        elif make == "3" and player.diamond >= merchant.trade3:
                            player.block = player.block + 15
                            print("You get 15 block")
                            player.diamond = player.diamond - merchant.trade3
                            if player.number == 1:
                                hero_goblin.block = player.block
                            elif player.number == 2:
                                hero_archer.block == player.block
                            elif player.number == 3:
                                hero_knight.block == player.block
                            else:
                                hero_god.block == player.block

                        elif make == "4" and player.diamond >= merchant.trade4:
                            player.diamond = player.diamond - merchant.trade3
                            print(colorama.Fore.GREEN)
                            print("you get a scroll")
                            print("")
                            ran_scroll = random.randint(0,100)
                            if ran_scroll <= 40:
                                player.inventory[0] = player.inventory[0] + 1
                                print("A Grass Scroll has now been added")
                            elif ran_scroll <= 70:
                                player.inventory[1] = player.inventory[1] + 1
                                print("A Fire Scroll has now been added")
                            elif ran_scroll <=90:
                                player.inventory[2] = player.inventory[2] + 1
                                print("A Ice Scroll has now been added")
                            else:
                                player.inventory[3] = player.inventory[3] + 1
                                print("A Plasma Scroll has now been added")
                            display_rewards(player)   

                        elif make.lower() == "leave":
                            out = 1                            
                        else:
                            print("")
                            print("cant do this")
                            time.sleep(1)

                elif decision == "3":
                    gold = player.gold
                    blood = player.blood
                    diamond = player.diamond
                    inventory = player.inventory
                    player = choose_starter_hero(hero_goblin, hero_archer, hero_knight)
                    player.gold = gold
                    player.blood = blood
                    player.diamond = diamond
                    player.inventory = inventory
                elif decision == "4":
                    print("Back to menu:")
                    return_back = 1
                else:
                    print("")
                    print("unable to understand that request try again")
                    time.sleep(1)



        else:
            print("")
            print("Couldn't understand your request try again")
            time.sleep(2)