## Matthew Witzig
## 00200454
## Programming for IT: CIS-153-O1A
## 12/21/2020
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

## Each monster you defeat gives you XP. As you level up you can boost your stats and get better, more overpowered weapons.
## Higher level monsters give better XP

## Credit for the core code goes to Keyfer Mathewson on Stackoverflow. I've expanded his code a lot, but the core concept and
## class structure is his.  https://stackoverflow.com/questions/14243831/python-fightsequence

import random ## We put our trust in Random Number Jesus

def chooseplayerclass():  #Pick your class! Class warfare!  ... wait, not that kind of game. A weapons are more balanced bonus to attack and defense, B weapons pure offense

    class fighter: #Beaty McBeatstick. Tough, but has crap damage and healing powers
        health = 100
        attack = 10
        healing = 5
        defense = 10
        xp = 0
        level = 1
        description = "fighter"
        weapon1a = "club"
        weapon1adesc = "You can get more with a kind word and a two-by-four than you can with a kind word alone."
        weapon1b = "nailbat"
        weapon1bdesc = "The classic weapon of angry mobs, the nailbat has not changed much since its invention in 1732 by Sir Henry Nailbat."
        weapon5a = "sword and shield"
        weapon5adesc = "The sword and board, traditional weapon of tanks everywhere."
        weapon5b = "greataxe"
        weapon5bdesc = "It's a big bloody axe. You feel angrier just holding it."
        weapon10a = "+1 sword"
        weapon10adesc = "There's a big '+1' emblazoned on the side of this blade and you somehow feel like it is slightly better in every way."
        weapon10b = "chainsaw"
        weapon10bdesc = "The chainsaw: mankind's ultimate anti-demon melee weapon. Rip and tear until it is done."

    class rogue: #Sneaky McSneakerton. Kind of in the middle.
        health = 75
        attack = 15
        healing = 7
        defense = 7
        xp = 0
        level = 1
        description = "rogue"
        weapon1a = "dagger"
        weapon1adesc = "It's too big to be a knife and too small to be a sword, so it must be a dagger."
        weapon1b = "slingshot"
        weapon1bdesc = "The slingshot is the traditional weapon of mischevious kids everywhere."
        weapon5a = "rapier"
        weapon5adesc = "You feel like Errol Flynn holding this rapier. Which is to say, cool and flashy."
        weapon5b = "longbow"
        weapon5bdesc = "Longbow is long. Try and put an arrow through another arrow!"
        weapon10a = "katana"
        weapon10adesc = "A katana can cut through a tank! It's true! I saw it on the internet!"
        weapon10b = "sniper rifle"
        weapon10bdesc = "The last thing you'll never see."

    class wizard: #Youre a wizard, Harry
        health = 50
        attack = 20
        healing = 10
        defense = 5
        xp = 0
        level = 1
        description = "wizard"
        weapon1a = "magic missile"
        weapon1adesc = "It makes little 'pew pew' sounds as it casts!"
        weapon1b = "angry sparkles"
        weapon1bdesc = "SO ANGRY. SO SPARKLY."
        weapon5a = "fireball"
        weapon5adesc = "Literally the only spell some wizards ever use."
        weapon5b = "lightning bolt"
        weapon5bdesc = "Zappier than a fireball."
        weapon10a = "meteor strike"
        weapon10adesc = "When you need to kill a bunch of dinosaurs or that dude with the dumb face, cast meteor strike."
        weapon10b = "gun"
        weapon10bdesc = "Cast .45 calibur to their face."

    class jedi: #Secret overpowered easter egg class
        health = 100
        attack = 40
        healing = 20
        defense = 20
        xp = 0
        level = 1
        description = "Jedi Knight"
        weapon1a = "lightsaber"
        weapon1adesc = "This is the weapon of a Jedi Knight. Not as clumsy or random as a blaster. An elegant weapon, for a more civilized age."
        weapon5a = "two lightsabers"
        weapon5adesc = "Now you're just showing off."
        weapon10a = "purple lightsaber"
        weapon10adesc = "I don't think you're cool enough to have Mr. Jackson's lightsaber."
        weapon1b = "lightsaber"
        weapon1bdesc = "This is the weapon of a Jedi Knight. Not as clumsy or random as a blaster. An elegant weapon, for a more civilized age."
        weapon5b = "two lightsabers"
        weapon5bdesc = "Now you're just showing off."
        weapon10b = "purple lightsaber"
        weapon10bdesc = "I don't think you're cool enough to have Mr. Jackson's lightsaber."

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

def choosemonsterclass(level): #choose your monster!

    class goblin: #goblins are small. And weak. Yup. You're a real hero fighting this one.
        health = 25
        attack = 10
        defense = 5
        xp = 1
        level = 1
        description = "Goblin"
        weapon = "sharp stick"

    class orc: #A big ol' orc. Which I guess are also technically goblins if you go by Tolkien and not Gygax.
        health = 50
        attack = 13
        defense = 7
        xp = 5
        level = 1
        description = "Orc"
        weapon = "sword"

    class troll: #They have a cave troll
        health = 75
        attack = 15
        defense = 10
        xp = 10
        level = 1
        description = "Troll"
        weapon = "club"

    class gnoll: #It came from the grassy gnoll!
        health = 65
        attack = 15
        defense = 15
        xp = 15
        level = 3
        description = "Gnoll"
        weapon = "axe"

    class ogre: #Its a big ol' ogre.
        health = 100
        attack = 20
        defense = 7
        xp = 20
        level = 3
        description = "Ogre"
        weapon = "club"

    class treant: #I always knew trees were shady!
        health = 115
        attack = 15
        defense = 20
        xp = 25
        level = 3
        description = "Treant"
        weapon = "tree arms"

    class hydra: #seven heads are better than one!
        health = 100
        attack = 25
        defense = 15
        xp = 30
        level = 5
        description = "hydra"
        weapon = "fangs"

    class owlbear: #A wizard did it.
        health = 105
        attack = 27
        defense = 10
        xp = 35
        level = 5
        description = "Owlbear"
        weapon = "teeth and claws"

    class manticore: #Mash 'em all together and you get a manticore
        health = 125
        attack = 30
        defense = 10
        xp = 40
        level = 5
        description = "Manticore"
        weapon = "spines"

    class wyvern: #Like a dragon but with only two legs. Only big nerds know this. Or care.
        health = 120
        attack = 33
        defense = 15
        xp = 45
        level = 7
        description = "wyvern"
        weapon = "acid breath"

    class chimera: #Mash even more of them together and you get a chimera.
        health = 130
        attack = 35
        defense = 20
        xp = 50
        level = 7
        description = "Chimera"
        weapon = "flame breath"

    class golem: #STOMP STOMP STOMP
        health = 150
        attack = 28
        defense = 25
        xp = 55
        level = 7
        description = "Golem"
        weapon = "fist"

    class dragon: #Now you just need a dungeon to go with it
        health = 160
        attack = 40
        defense = 30
        xp = 60
        level = 9
        description = "dragon"
        weapon = "fiery breath"

    class colossus: #Stay out of its shadow
        health = 175
        attack = 35
        defense = 35
        xp = 65
        level = 9
        description = "Colossus"
        weapon = "big stomp"

    class threegoblins: #The deadliest of all!
        health = 75
        attack = 30
        defense = 15
        xp = 70
        level = 9
        description = "Three goblins in a trenchcoat"
        weapon = "small knives"

    class cthulhu: #IA IA FHTAGN This is the final boss!
        health = 250
        attack = 30
        defense = 20
        xp = 1000
        level = 10
        description = "Cthulhu"
        weapon = "tentacles"

    class moose: #THE FURY OF THE FROZEN NORTH
        health = 250
        attack = 30
        defense = 20
        xp = 1000
        level = 1
        description = "Moose"
        weapon = "antlers"


    monster = "Man" #Like before in chooseplayerclass, these are placeholders
    monsterchoice = "Man"

    print(level)

    if level == 10: #Bossfight time!
        monster = cthulhu()
        return monster

    while True: #Moose are an easter egg, so I dont mention them.
        print("Before you stands the doors to the different monster cages. You see signs for the following:")
        if level >= 1:
            print("Goblin, orc, or troll.")
        if level >= 3:
            print("Gnoll, ogre, or treant.")
        if level >= 5:
            print("Hydra, owlbear, or manticore.")
        if level >= 7:
            print("Wyvern, chimera, or golem.")
        if level >= 9:
            print("Dragon, colossus, or three goblins in a trenchcoat.")
        monsterchoice = input("Which kind of monster do you want to fight?")
        monsterchoice = monsterchoice.lower()
        if monsterchoice in ["goblin","troll","orc","gnoll","ogre","treant","hydra","owlbear","manticore","wyvern","chimera","golem","dragon","colossus","three goblins in a trenchcoat","moose"]:
            break
        else:
            print("Unrecognized race requested, please select a valid option.")

    if monsterchoice in "trenchcoat": # Assigning the monster!
        monster = threegoblins()
    elif monsterchoice in "goblin":
        monster = goblin()
    elif monsterchoice in "orc":
        monster = orc()
    elif monsterchoice in "troll":
        monster = troll()
    elif monsterchoice in "moose":
        monster = moose()
    elif monsterchoice in "gnoll":
        monster = gnoll()
    elif monsterchoice in "ogre":
        monster = ogre()
    elif monsterchoice in "treant":
        monster = treant()
    elif monsterchoice in "hydra":
        monster = hydra()
    elif monsterchoice in "owlbear":
        monster = owlbear()
    elif monsterchoice in "manticore":
        monster = manticore()
    elif monsterchoice in "wyvern":
        monster = wyvern()
    elif monsterchoice in "chimera":
        monster = chimera()
    elif monsterchoice in "golem":
        monster = golem()
    elif monsterchoice in "dragon":
        monster = dragon()
    elif monsterchoice in "colossus":
        monster = colossus()

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
print("As you defeat more powerful monsters, you gain XP and levels and become more powerful until")
print("you are ready to fight the FINAL BOSS")
print("Choose your doom!\n")

player = chooseplayerclass() #CHOOSE YOUR FIGHTER
weapon = "butt"

print("Choose your weapon! The ",player.weapon1a,"is a versatile weapon, while the ",player.weapon1b,"gives more raw power. Choose wisely!")
print(player.weapon1a.upper())
print(player.weapon1adesc)
print("\n", player.weapon1b.upper())
print(player.weapon1bdesc)

attmult = 1.0
defmult = 1.0

while True:
    weapon = input("CHOOSE YOUR WEAPON!")

    if weapon.lower() in player.weapon1a: ##choice A gives a smaller boost to attack and defense, B gives a big boost to attack
        attmult = 1.1
        defmult = 1.1
    elif weapon.lower() in player.weapon1b:
        attmult = 1.2
        defmult = 1.0

    if weapon.lower() in [player.weapon1a, player.weapon1b]:
        break
    else:
        print("Pick a valid weapon.")

encounter = 1
game = 1
turn = 'player'
while game == 1:

    if (player.xp >= 10) and (player.level < 2): ## This is a SUPER sloppy way to do this, I know. But in my defense, I'm tired.
        while True:
            advance = input("You leveled up! You are now level 2! Do you want to boost your health, attack, defense, or healing?")
            advance = advance.lower()
            if advance in 'health':
                player.health = player.health + 5
            elif advance in 'attack':
                player.attack = player.attack + 5
            elif advance in 'defense':
                player.defense = player.defense + 5
            elif advance in 'healing':
                player.healing = player.healing + 5

            if advance in ['health','attack','defense''healing']:
                player.level = 2
                break
            else:
                print("Input a valid entry.")

    if (player.xp >= 25) and (player.level < 3): ## This is a SUPER sloppy way to do this, I know. But in my defense, I'm tired.
        while True:
            advance = input("You leveled up! You are now level 3! You've unlocked new monsters to fight! Do you want to boost your health, attack, defense, or healing?")
            advance = advance.lower()
            if advance in 'health':
                player.health = player.health + 5
            elif advance in 'attack':
                player.attack = player.attack + 5
            elif advance in 'defense':
                player.defense = player.defense + 5
            elif advance in 'healing':
                player.healing = player.healing + 5

            if advance in ['health','attack','defense''healing']:
                player.level = 3
                break
            else:
                print("Input a valid entry.")

    elif (player.xp >= 50) and (player.level < 4): ## This is a SUPER sloppy way to do this, I know. But in my defense, I'm tired.
        while True:
            advance = input("You leveled up! You are now level 4! Do you want to boost your health, attack, defense, or healing?")
            advance = advance.lower()
            if advance in 'health':
                player.health = player.health + 5
            elif advance in 'attack':
                player.attack = player.attack + 5
            elif advance in 'defense':
                player.defense = player.defense + 5
            elif advance in 'healing':
                player.healing = player.healing + 5

            if advance in ['health','attack','defense''healing']:
                player.level = 4
                break
            else:
                print("Input a valid entry.")

    elif (player.xp >= 75) and (player.level < 5): ## This is a SUPER sloppy way to do this, I know. But in my defense, I'm tired.
        while True:
            advance = input("You leveled up! You are now level 5! You get new monsters to fight and a new weapon! Do you want to boost your health, attack, defense, or healing?")
            advance = advance.lower()
            if advance in 'health':
                player.health = player.health + 5
            elif advance in 'attack':
                player.attack = player.attack + 5
            elif advance in 'defense':
                player.defense = player.defense + 5
            elif advance in 'healing':
                player.healing = player.healing + 5

            if advance in ['health','attack','defense''healing']:
                print("Choose your weapon! The ",player.weapon5a,"is a versatile weapon, while the ",player.weapon5b,"gives more raw power. Choose wisely!")
                print(player.weapon5a.upper())
                print(player.weapon5adesc)
                print("\n", player.weapon5b.upper())
                print(player.weapon5bdesc)
                while True:
                    weapon = input("CHOOSE YOUR WEAPON!")
                    if weapon.lower() in player.weapon5a: ##Now we're cooking with gas!
                        attmult = 1.25
                        defmult = 1.25
                    elif weapon.lower() in player.weapon5b:
                        attmult = 1.5
                        defmult = 1

                    if weapon.lower() in [player.weapon5a, player.weapon5b]:
                        break
                    else:
                       print("Pick a valid weapon.")
                player.level = 5
                break
            else:
                print("Input a valid entry")

    elif (player.xp >= 125) and (player.level < 6): ## This is a SUPER sloppy way to do this, I know. But in my defense, I'm tired.
        while True:
            advance = input("You leveled up! You are now level 6! Do you want to boost your health, attack, defense, or healing?")
            advance = advance.lower()
            if advance in 'health':
                player.health = player.health + 5
            elif advance in 'attack':
                player.attack = player.attack + 5
            elif advance in 'defense':
                player.defense = player.defense + 5
            elif advance in 'healing':
                player.healing = player.healing + 5

            if advance in ['health','attack','defense''healing']:
                player.level = 6
                break
            else:
                print("Input a valid entry.")

    elif (player.xp >= 175) and (player.level < 7): ## This is a SUPER sloppy way to do this, I know. But in my defense, I'm tired.
        while True:
            advance = input("You leveled up! You are now level 7! There are new monsters to fight! Do you want to boost your health, attack, defense, or healing?")
            advance = advance.lower()
            if advance in 'health':
                player.health = player.health + 5
            elif advance in 'attack':
                player.attack = player.attack + 5
            elif advance in 'defense':
                player.defense = player.defense + 5
            elif advance in 'healing':
                player.healing = player.healing + 5

            if advance in ['health','attack','defense''healing']:
                player.level = 7
                break
            else:
                print("Input a valid entry.")

    elif (player.xp >= 250) and (player.level < 8): ## This is a SUPER sloppy way to do this, I know. But in my defense, I'm tired.
        while True:
            advance = input("You leveled up! You are now level 8! Do you want to boost your health, attack, defense, or healing?")
            advance = advance.lower()
            if advance in 'health':
                player.health = player.health + 5
            elif advance in 'attack':
                player.attack = player.attack + 5
            elif advance in 'defense':
                player.defense = player.defense + 5
            elif advance in 'healing':
                player.healing = player.healing + 5

            if advance in ['health','attack','defense''healing']:
                player.level = 8
                break
            else:
                print("Input a valid entry.")

    elif (player.xp >= 400) and (player.level < 9): ## This is a SUPER sloppy way to do this, I know. But in my defense, I'm tired.
        while True:
            advance = input("You leveled up! You are now level 9! You've unlocked new monsters to fight! Do you want to boost your health, attack, defense, or healing?")
            advance = advance.lower()
            if advance in 'health':
                player.health = player.health + 5
            elif advance in 'attack':
                player.attack = player.attack + 5
            elif advance in 'defense':
                player.defense = player.defense + 5
            elif advance in 'healing':
                player.healing = player.healing + 5

            if advance in ['health','attack','defense''healing']:
                player.level = 9
                break
            else:
                print("Input a valid entry.")

    elif (player.xp >= 600) and (player.level < 10): ## This is a SUPER sloppy way to do this, I know. But in my defense, I'm tired.
        while True:
            advance = input("You are now level 10! You have a new weapon and the final enemy is before you! Do you want to boost your health, attack, defense, or healing?")
            advance = advance.lower()
            if advance in 'health':
                player.health = player.health + 5
            elif advance in 'attack':
                player.attack = player.attack + 5
            elif advance in 'defense':
                player.defense = player.defense + 5
            elif advance in 'healing':
                player.healing = player.healing + 5

            if advance in ['health','attack','defense''healing']:
                print("Choose your weapon! The ",player.weapon10a,"is a versatile weapon, while the ",player.weapon10b,"gives more raw power. Choose wisely!")
                print(player.weapon10a.upper())
                print(player.weapon10adesc)
                print("\n", player.weapon10b.upper())
                print(player.weapon10bdesc)
                while True:
                    weapon = input("CHOOSE YOUR WEAPON!")
                    if weapon.lower() in player.weapon10a: ##Now we're cooking with gas!
                        attmult = 1.5
                        defmult = 1.5
                    elif weapon.lower() in player.weapon10b:
                        attmult = 2.0
                        defmult = 1

                    if weapon.lower() in [player.weapon10a, player.weapon10b]:
                        break
                    else:
                       print("Pick a valid weapon.")
                player.level = 10
                break
            else:
                print("Input a valid entry")

    armor = player.defense #armor is a stat so that I know the player's baseline armor if they choose to take a Defend action and to deal with the weapon multiplier
    sword = player.attack #sword is so that the baseline attack evens out despite the weapon multiplier
    monster = choosemonsterclass(player.level) #CHOOSE YOUR ENEMY

    print("You are a mighty", player.description,"who fights with a powerful", weapon.lower(),"!")
    print("But what's this? An evil",monster.description, "stands before you!")
    print("Have at thee!") #That's the entire plot.

    while encounter == 1:
        if turn == 'player':
            player.defense = round(armor * defmult) ## RandInt doesn't like non-integers, which happens with this, so we round it off
            player.attack = round(sword * attmult)
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
                        print("You hit the ", monster.description, "with your", weapon, "for", damage, "damage, reducing its HP to", monster.health)
                        if monster.health <= 0: #A winner is you!
                            print("The ", monster.description, "goes down!  You're a winner!")
                            player.xp = player.xp + monster.xp
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

    if turn in 'loser':
        game = 0
        break
    elif turn in 'winner':
        if monster.description in "Cthulhu":
            print("You have defeated the DREAD CTHULHU! And you did it without a boat! You are the champion! Your feats are legend!")
            game = 0
            break
        yesno = input("Do you want to advance to the next round?")
        if yesno.lower() in 'y':
            turn = 'player'
            encounter = 1
        elif yesno.lower() in 'n':
            game = 0
            break

input("\nGAME OVER. Press Enter to exit.")

## And that's it! I do wish I could have implemented the map, as I spent a while on it, but it was too fiddly on top of the rest of this.
