## Derelicts 2.0
## Original "Zork" exercise refactored to use functions.
## Discontinued due to useless structuring.
## Uses codefinder.py for a minigame.

# ver. X

# added reset for illegal commands
# texts done
# library vault game implemented
# basic map done


from sys import exit
from codefinder import *

prompt = "> "
clues = 0

def choose():
    ch = input("> ")
    return ch

def invalid():
    print("No idea what that means.")

def die(why):
    print("GAME OVER\n")
    print(why)
    exit(0)

def wait():
    x = input("Press enter to continue...")

# .oO   LOCATIONS     Oo.

# ------factory

def factory():
    print("You find yourself in the old factory. Rows upon rows of derelict machinery and a metal catwalk overlooking it all. It might be worthwhile to search the place, or to get a better view from the catwalk.")
    
    choice = choose()
    
    if choice == "search":
       fac_floor()

    elif choice == "catwalk":
        fac_catwalk()
     
    elif choice == "back":
        print("You decide to leave the factory for now and head back to the street.")
        xroads()
        
    else:
        invalid()
        factory()

def fac_catwalk():
    print("You very carefully ascend the rusted stairs. After several nerve-racking moments, you reach the catwalk\n.")
    print("From this vantage point, you can see the entire hall. You see nothing of note, but at least sketch a simple floor plan.\n")
    print("YOU GAIN 1 CLUE!")
    print("There are several doors on the far end of the catwalk. The only other way is back down.")
    
    choice = choose()
    
    if choice == "doors":
        fac_offices()
    
    elif choice == "back":
        print("You decide not to risk it and head back down.")
        print("This time, your luck runs out. The ancient stairway gives way under your weight and you tumble to your death.")
        die("You fell from a catwalk in the old factory.")
        
    else:
        invalid()
        fac_catwalk()
        
def fac_floor():
    print("You can only guess what all these machines used to do back in their day. The metal hulks are silent now, and will stay so until rust finally eats them all.\n")
    print("Despite all your effort, you only find dust and a couple of old parts. Just as you are going to turn away, you notice something under an old boiler.\n")
    print("There is a wooden box under the massive machine, almost as if supporting it. You could probably pry it loose.")
        
    choice = choose()
    
    if choice == "pry":
        print("As you heave against your crowbar, suddenly, something snaps. With a deafening metal screech, the world goes black.")
        die("You were crushed to pulp by several tons of rusted steel.")
    
    elif choice == "back":
        print("Seeing the state the boiler is in, you decide to avoid the collapsing structure.")
        factory()
    
    else:
        invalid()
        fac_floor()

def fac_offices():
    print("There are three doors here. These must have been offices of the various clerks working here, maybe there is something worth reading inside...")
    print("Search door number one, two or three, or leave the offices be?\n")
    
    choice = choose()
    
    if choice == "one":
        print("This is a small room with a collapsed desk in the centre.  A layer of assorted garbage covers the floor. You rummage in it for a while, but find nothing useful and decide to leave.")
        wait()
        fac_offices()
    
    elif choice == "two":
        print("This is a large office, with a thick layer of mold on the floor that must once have been a carpet.")
        print("A gleaming sword, neatly arranged in a rack close to the door, immediately catches your eye.")
        print("Only after clutching it in your fist do you realize the blade is cursed. A miasma of madness engulfs your mind.\n")
        die("You went insane because of the blade's curse and still roam the City to this day, claiming more victims for it.")
    
    elif choice == "three":
        print("The third office is relatively well-preserved. The massive bookcase on the east wall immediately catches your eye.")
        print("Your instincts were right! Among the sorry masses of moldy leather and paper pulp, you find a near-intact volume.")
        print("As far as you can tell, it details the workings of some infernal engine or other. You know the right people will tear your arms off to get it.")
        print("YOU GAIN 5 CLUES!")
        print("You stash the thick volume away and can almost hear the coins ringing. Now to get it out of here...")
        wait()
        fac_offices()
    
    elif choice == "back":
        print("You carefully walk back to the staircase. Surely, some stupid offices have nothing interesting in them.")
        fac_catwalk()

    else:
        invalid()
        fac_offices()


# ------ library 
      
def library():
    print("This used to be some kind of public library. You are sure most of the books are either destroyed or long since stolen, but who knows...")
    print("You can either explore the hall, or descend to the vaults. Perhaps they haven't been broken in yet.\n")
    
    choice = choose()
    
    if choice == "hall":
        lib_hall()
        
    elif choice == "vault":
        lib_vault()
        
    elif choice == "back":
        print("You decide against exploring the building. It is almost certainly picked clean and probably dangerous. You head back to the crossroads.")
        xroads()
    
    else:
        invalid()
        library()

def lib_hall():
    print("This is the colossal main hall of the library. Once filled with literature, it now mostly contains mold, rubble and a motley collection of old tents and shelters.")
    print("There might be some scraps left in the remaining shelves. You could also peek inside the shelters or ascend to the gallery.")
    
    choice = choose()
    
    if choice == "shelters":
        print("You scurry through the shelters. You find what you would expect - a lot of nothing, some garbage, and... is that a spade? It is indeed!")
        print("FOUND SPADE!")
        print("And that's it. At least now you know the shelters are empty and most have been for months. You collect yourself and consider further options.")
        wait()
        lib_hall()
    
    elif choice == "shelves":
        print("There are a precious few shelves left and most of them are emptier than your stomach, which is saying something.")
        print("After an hour or so, you manage to find a couple of dull paperbacks, too ordinary for your predecessor to take.")
        print("YOU GAIN 2 CLUES!")
        print("Now, there is absolutely, positively nothing here. You scan the hall for other options.")
        wait()
        lib_hall()
    
    elif choice == "gallery":
        lib_gallery()
        
    elif choice == "back":
        print("Some of these shelters look to have been inhabited quite recently. You high-tail it out of here.")
        library()
    
    else:
        invalid()
        lib_hall()

def lib_gallery():
    print("You ascend to the gallery and see the decay of this library in full detail. So sad, really.")
    print("There seems to be a computer here, and it somehow works.")
    
    choice = choose()
    
    if choice == "computer":
        print("You turn the machine on and search it. One of the files yields the code for the library's vault: 5452.")
        wait()
        lib_gallery()
    
    elif choice == "back":
        print("You descend back to the hall.")
        lib_hall()
    
    else:
        invalid()
        lib_gallery()

def lib_vault():
    print("This is the library's vault. Whatever invaluable info is contained here, it is locked behind a massive steel door with a numpad.")
    
    choice = choose()
    
    if choice == "open":
        print("You see that the numpad has space for a 4-digit number. Time to start guessing...")
        
        game_result = codefinder()
        
        if game_result == True:
            print("With a muffled click, the lock slides open!")
            print("Inside the vault, there are scores upon scores of books. You shuffle around a while and then take a particularly interesting set of history books. Ka-ching.")
            print("YOU GAIN 6 CLUES!")
            print("Determined to return, you leave the vault and let the door lock itself behind you.")
            lib_vault()
            
        else:
            die("You were burned to a crisp by the vault's security flamethrower.")
        
    elif choice == "back":
        print("You decide not to tamper with the door and leave.")
        library()
    
    else:
        invalid()
        lib_vault()

# ------ precinct

def precinct():
    print("You enter the police station. Whatever lawmen might have once been here are long since gone.")
    print("You may try to explore the casefiles or look behind the reception. On the other side, a glass door says \"Sheriff's Office\".")
    
    choice = choose()
    
    if choice == "casefiles":
        print("You open a few of the casefile lockers at random. Unsurprisingly, there is nothing inside anymore.")
        wait()
        precinct()
        # die("missing casefiles game")
    
    elif choice == "reception":
        print("Behind the reception desk, you stumble upon an old album, neatly hidden under a plant pot. You take it for the historians to sort out.")
        print("YOU GAINED 3 CLUES!")
        wait()
        precinct()
        
    elif choice == "office":
        pre_office()
        
    elif choice == "back":
        print("The station is as boring in death as it was in life. You leave with a scoff.")
        xroads()
    
    else:
        invalid()
        precinct()

def pre_office():
    print("You approach the door to the office and find it is locked.")
    print("You could probably smash the glass door to pieces with your crowbar. You could also try to pick the lock.")
    
    choice = choose()
    
    if choice == "smash":
        print("The door shatters. A brief search of the office reveals a rusty, but functional shotgun!")
        print("YOU GOT A SHOTGUN!")
        precinct()
    
    elif choice == "pick":
        print("You start fiddling with the lock using your lockpick.")
        print("You get so distracted by this that you only notice the creeping ruinling when it is already too late.")
        print("The last thing you see are rows of sharp teeth, nearing your face at lightning speed.")
        die("You got eaten by a hungry ruinling.")
    
    elif choice == "back":
        print("You decide against breaking and entering in this case and look for other options.")
        precinct()
    
    else:
        invalid()
        precinct()


# ------ villa

def villa():
    print("This villa must have been magnificent back in its day. Now, it lies dead and emptier than your ex-girlfriend's heart... hopefully.")
    print("You may try the frontdoor, go around the backdoor or leave the husk undisturbed after all.")
    
    choice = choose()
    
    if choice == "frontdoor":
        vil_frontdoor()
    
    elif choice == "backdoor":
        print("The backdoor is smashed to splinters. As unsettling as that is, the way inside is clear.")
        vil_patio()
    
    elif choice == "back":
        print("Just as with your ex-girlfriend, you decide to leave the villa to its own devices and return to the crossroads.")
        xroads()
    
    else:
        invalid()
        villa()

def vil_frontdoor():
    print("The front door is boarded up. Luckily, some of the boards are rotten and will not withstand a determined assault.")
    print("You could pry them away carefully, or just bash the barricade like a madman.")
    
    choice = choose()
    
    if choice == "bash":
        print("You swing your crowbar around like a battleaxe and hit the boards. They are stronger than they seem!")
        print("After a few more disappointing swings, you utter a curse and stop. Violence, it seems, is not the answer.")
        wait()
        vil_frontdoor()
    
    elif choice == "pry":
        print("You carefully lodge the crowbar's beak between the planks and heave. The board comes loose with satisfying crackling.")
        print("After a while of this, you create an opening big enough to crawl through. Success!")
        vil_patio()
    
    elif choice == "back":
        print("This stinks of manual labor. No thanks, there are accessible buildings aplenty.")
        villa()
    
    else:
        invalid()
        vil_frontdoor()

def vil_patio():
    print("This is the patio - once opulent and imperial, now devastated by decades of disrepair.")
    print("There are a couple of framed photographs on the walls. Freeing them from their glass prisons, you stash them for the History Department.")
    print("YOU GAIN 2 CLUES!")
    print("A door seems to lead to a bedroom of some sort. A larder is down a set of stairs, while a magnificent spiral staircase leads to the tower.")
    
    choice = choose()
    
    if choice == "bedroom":
        print("The bedroom is devoid of anything interesting besides the wreck of a huge double bed. You are not feeling sleepy and turn back.")
        wait()
        vil_patio()
    
    elif choice == "tower":
        vil_tower()
    
    elif choice == "larder":
        print("You descend into the larder. Darkness envelops you as you continue further and further away from sunlight...")
        print("Too late did you realize that ruinlings typically nest underground. A sharp pain reminds you...")
        die("You stumbled into a ruinling nest and got devoured.")
    
    elif choice == "back":
        print("Something is not right about this lavish mansion. Trusting your gut, you leave.")
        villa()
    
    else:
        invalid()
        vil_patio()

def vil_tower():
    print("You ascend into the tower. Even though the topmost floor has long since crumbled, you can still catch a magnificent view of the City, such as it is.")
    print("You may just watch the sunset for a while, or attempt to sketch a rough map of the vicinity.")
    
    choice = choose()
    
    if choice == "sketch":
        print("You flip open your notebook and take note of several landmarks for your next expedition.")
        print("GAINED 3 CLUES!")
        vil_tower()
    
    elif choice == "look":
        print("As you turn, trying to catch a better view, you slip on a rock and fall from the tower to your death.")
        die("You fell from the villa's tower.")
    
    elif choice == "back":
        print("You know what, the view sucks anyway. You head back.")
        vil_patio()
    
    else:
        invalid()
        vil_tower()


# ------- crossroads / start

def xroads():
    print("You find yourself at a crossroads in one of the less traveled parts of the City.")
    print("To the north, you see an abandoned factory of some kind.")
    print("To the east, a splendid villa stands. Or what's left of it, anyway.")
    print("To the south, you may visit a police station. You don't expect anything worthwhile now, but then, barely anyone ever did.")
    print("To the west is an old library, a prime target both for you and your fellow scavengers.")
    
    choice = input(prompt)
    
    if "factory" in choice or "north" in choice:
        print("You head towards the old factory.\n")
        factory()
        
    elif "villa" in choice or "east" in choice:
        print("You decide to explore the villa.\n")
        villa()
        
    elif "precinct" in choice or "south" in choice:
        print("You turn your attention towards the cop station.\n")
        precinct()
        
    elif "library" in choice or "west" in choice:
        print("You start approaching the library carefully.\n")
        library()
     
    else:
        xroads()

print("\n\n\t\t\t\t DERELICTS 2.0")
print("You are a ruins explorer. Your task is to scavenge the Abandoned City for any useful information about its past.")
print("Type commands in lowercase only. The 'back' command will always take you back a step, unless, of course, you croak.")
print("Good luck!\n\n\n")


xroads()