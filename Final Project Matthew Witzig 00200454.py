## Matthew Witzig
## 00200454
## Programming for IT: CIS-153-O1A
## 12/9/2020
## MEHVENTURE: THE REVENGE OF LORD BLARG
## In which we create a simple game where you take a generic fantasy hero and make them fight a generic fantasy monster
## Originally this was going to have a map, and I actually did get the map to render. But I couldn't figure out a way
## to make that interesting beyond just randomly wandering around the map until you bumped into the critter and getting
## the monster to a random spot was boring and fiddly so I decided to focus on the combat instead.
## Warning: I was tired and hungry when I wrote the comments, so expect some sass.
## Okay, a lot of sass.

## Combat here is simple: You have four stats: Health, Attack, Healing, and Defense
## Health is your total HP. If it reaches 0 you die
## Attack is your damage output.
## Healing is your ability to heal yourself after taking damage.
## Defense is your resistance to damage.
## Damage is calculated by rolling your Attack score and then subtracting the result of rolling the target's Defense score
## Everything is determined by rolls, with the score being the maximum result. Think of it as being a dWhatever dice
## After the player attacks the monster attacks back. Rinse, repeat, until somebody dies.

import random ## We put our trust in Random Number Jesus

def chooseplayerclass():  #Pick your class! Class warfare!  ... wait, not that kind of game.

    class fighter: #Beaty McBeatstick. Tough, but has crap damage and healing powers
        health = 100
        attack = 10
        healing = 5
        defense = 10
        description = "fighter"
        weapon = "sword"

    class rogue: #Sneaky McSneakerton. Kind of in the middle.
        health = 75
        attack = 15
        healing = 5
        defense = 7
        description = "rogue"
        weapon = "dagger"

    class wizard: #Youre a wizard, Harry
        health = 50
        attack = 20
        healing = 10
        defense = 5
        description = "wizard"
        weapon = "lightning bolt"

    class jedi: #Secret overpowered easter egg class
        health = 100
        attack = 40
        healing = 20
        defense = 20
        description = "Jedi Knight"
        weapon = "lightsaber"

    playerchoice = "dummy" #These are just placeholders, as I dont like leaving them undefined
    player = "moose"

    while True:
        playerchoice = input("What kind of hero do you want to fight? (Fighter, Rogue, Wizard)? ") #CHOOSE YOUR FIGHTER
        playerchoice = playerchoice.lower()
        if playerchoice in ["fighter","rogue","wizard","jedi"]:
            break
        else:
            print("Unrecognized class requested, please select one of Fighter, Rogue or Wizard.")

    if playerchoice in "fighter": #this should be obvious
        player = fighter()
    elif playerchoice in "rogue":
        player = rogue()
    elif playerchoice in "wizard":
        player = wizard()
    elif playerchoice in "jedi":
        player = jedi()

    return player #Player selected!

def choosemonsterclass(): #choose your monster!

    class goblin: #goblins are small. And weak. Yup. You're a real hero fighting this one.
        health = 25
        attack = 10
        defense = 5
        description = "Goblin"
        weapon = "sharp stick"

    class orc: #A big ol' orc. Which I guess are also technically goblins if you go by Tolkien and not Gygax.
        health = 50
        attack = 13
        defense = 7
        description = "Orc"
        weapon = "sword"

    class troll: #They have a cave troll
        health = 75
        attack = 15
        defense = 10
        description = "Troll"
        weapon = "club"

    class moose: #THE FURY OF THE FROZEN NORTH
        health = 250
        attack = 30
        defense = 20
        description = "Moose"
        weapon = "antlers"


    monster = "Man" #Like before in chooseplayerclass, these are placeholders
    monsterchoice = "Man"

    while True: #Moose are an easter egg, so I dont mention them.
        monsterchoice = input("What kind of monster do you want to fight? (Goblin, Orc or Troll)? ")
        monsterchoice = monsterchoice.lower()
        if monsterchoice in ["goblin","troll","orc","moose"]:
            break
        else:
            print("Unrecognized race requested, please select one of Goblin, Orc, or Troll.")

    if monsterchoice in "goblin": # Assigning the monster!
        monster = goblin()
    elif monsterchoice in "orc":
        monster = orc()
    elif monsterchoice in "troll":
        monster = troll()
    elif monsterchoice in "moose":
        monster = moose()

    return monster #And here we go!

## MAIN PROGRAM

## OBLIGATORY TEXT WALL
print("MEHVENTURE: THE REVENGE OF LORD BLARG") # Yeah, it's not Lord of the Rings here. Sue me, I'm tired.
print("\nA game of thrilling heroics and maniacally beating a monster over the head with a sharp object!")
print("\nYou are a hero! But not just any hero, a fighter, a rogue or a wizard hero!")
print("Fighters are very tough and hard to kill, but do the least damage.")
print("Rogues are in the middle, doing more damage than fighters but being tougher than wizards.")
print("Wizards are all about the damage, baby, but are made of spun glass.")
print("\nYou have been captured by the EVIL LORD BLARG and thrown into the fighting pit!")
print("You see three doors before you, each with a different monster to fight.")
print("Choose your doom!\n")

player = chooseplayerclass() #CHOOSE YOUR FIGHTER
monster = choosemonsterclass() #CHOOSE YOUR ENEMY

print("You are a mighty", player.description,"who fights with a powerful", player.weapon,"!")
print("But what's this? An evil",monster.description, "stands before you!")
print("Have at thee!") #That's the entire plot.

armor = player.defense #armor is a stat so that I know the player's baseline armor if they choose to take a Defend action
encounter = 1
turn = 'player'
while encounter == 1:
    if turn == 'player':
        player.defense = armor
        while True:
            action = input("What would you like to do (Attack/Defend/Heal)? ") #Murder/Dont Murder/Anti-Murder
            action = action.lower() #for my sanity
            if action in 'attack':
                damage = random.randint(0,player.attack) - random.randint(0,monster.defense) #SMACK
                if damage <= 0:
                    damage = 0
                    print("Your attack bounces off! The",monster.description, "laughs at your puny efforts!") # Weak!
                    turn = 'monster' # Monster's turn now
                else:
                    monster.health = monster.health - damage #The damage stat came out of me wanting to show the damage to the player
                    print("You hit the ", monster.description, "with your", player.weapon, "for", damage, "damage, reducing its HP to", monster.health)
                    if monster.health <= 0: #A winner is you!
                        print("The ", monster.description, "goes down!  You're a winner!")
                        encounter = 2
                        turn = 'winner'
                        break #Done!
                    else:
                        turn = 'monster' #Well its still up, so now it hits you
            elif action in 'defend': #If you defend instead, you boost your defense score for one turn. Which is kind of lame, and I don't like how I did this mechanic.
                damage = random.randint(1,player.defense)
                player.defense = player.defense + damage
                print("You brace yourself, briefly raising your defense by", damage, "!")
                turn = 'monster'
            elif action in 'heal': #Kind of like defend, this makes more sense in my head. Not really satisfied with how I implemented this.
                damage = random.randint(1,player.healing)
                player.health = player.health + damage
                print("You down a healing potion, raising your HP by", damage, "!")
                turn = 'monster'

            if action in ['attack', 'defend', 'heal']: ## Valid actions only
                break
            else:
                print("Input a valid action.")

    if turn == 'monster': ## Monster's turn!
        damage = random.randint(0,monster.attack) - random.randint(0,player.defense) ##Now to see how much the dice hate you today
        if damage <= 0:
            damage = 0
            print("The", monster.description, "misses you with its", monster.weapon,"! It should have tried harder!")
            turn = 'player'
        else:
            player.health = player.health - damage ## Owie
            print("The evil", monster.description, "hits you with its", monster.weapon, "doing", damage, "damage, reducing your HP to", player.health)

        if player.health <= 0: ## YOU LOSE AHAHAHA
            print("The", monster.description, "runs you through with its mighty", monster.weapon, "! Oh no!")
            encounter = 3
            turn = 'loser'
            break
        else:
            turn = 'player'

input("\nGAME OVER. Press Enter to exit.")

## And that's it! I do wish I could have implemented the map, as I spent a while on it, but it was too fiddly on top of the rest of this.
