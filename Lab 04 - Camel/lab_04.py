"""
The Sword Theif's Journey is a text based adventure game where the player makes their way to the rebel base. The player
must stay ahead of the royal guard who, if they catch up, will kill the player. They also must manage their resources so
as not to succumb to upkeep issues. They will also have to fight off chance encounters along the way.
"""

def get_valid_string_input(prompt):
    valid = False
    while not valid:
        string = input(prompt).lower()
        if string.isalpha() and len(string) >= 3:
            valid = True
        else:
            print("Try again, I'm looking for something made for only letters three or more letters long")
    return string

def get_action_input(prompt, valid_letters):
    valid = False
    while not valid:
        string = input(prompt).lower()
        if string.isalpha() and len(string) == 1:
            for letter in valid_letters:
                if letter == string:
                    valid = True
        else:
            print("Try again, your choices are :")
            print(*valid_letters, sep = " ")

    return string

def get_valid_number_input(prompt):
    valid = False
    while not valid:
        try:
            num = int(input(prompt))
            valid = True
        except :
            print("Try again, I'm looking for only integer numbers")
    return num

def print_intro():
    print("*************************************************************************")
    print("╭━━━━┳╮╱╱╱╱╱╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╭╮╭━━━━┳╮╱╱╱╱╱╱╭━╮╱╱╱╱╱╱╭╮")
    print("┃╭╮╭╮┃┃╱╱╱╱╱┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱┃┃┃╭╮╭╮┃┃╱╱╱╱╱╱┃╭╋╮╱╱╱╱╱┃┃")
    print("╰╯┃┃╰┫╰━┳━━╮┃╰━━┳╮╭╮╭┳━━┳━┳━╯┃╰╯┃┃╰┫╰━┳━━┳┳╯╰┫┣━━╮╱╱┃┣━━┳╮╭┳━┳━╮╭━━┳╮╱╭╮")
    print("╱╱┃┃╱┃╭╮┃┃━┫╰━━╮┃╰╯╰╯┃╭╮┃╭┫╭╮┃╱╱┃┃╱┃╭╮┃┃━╋╋╮╭┻┫━━┫╭╮┃┃╭╮┃┃┃┃╭┫╭╮┫┃━┫┃╱┃┃")
    print("╱╱┃┃╱┃┃┃┃┃━┫┃╰━╯┣╮╭╮╭┫╰╯┃┃┃╰╯┃╱╱┃┃╱┃┃┃┃┃━┫┃┃┃╱┣━━┃┃╰╯┃╰╯┃╰╯┃┃┃┃┃┃┃━┫╰━╯┃")
    print("╱╱╰╯╱╰╯╰┻━━╯╰━━━╯╰╯╰╯╰━━┻╯╰━━╯╱╱╰╯╱╰╯╰┻━━┻╯╰╯╱╰━━╯╰━━┻━━┻━━┻╯╰╯╰┻━━┻━╮╭╯")
    print("╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃")
    print("╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯")
    print("*************************************************************************")
    print()
    print("Welcome to The Sword Thief's Journey")
    print("In this text based adventure game you'll have to overcome many obsticales to reach the rebel hide out")
    print("before the royal guard catch and kill you. You'll need to manage your resources, like thirst, hungry energy")
    print("and health to make sure you're in a good enough condition to fight off 'obstacles' along the way.")
    input("Good luck adventurer. Press enter to continue.")
    print()

def steal_sword_start():
    print("You find yourself standing on barren rock, steep cliffs topped by large castle loom")
    print("You're not the only one here. A long line snakes it's way off behind you toward the dock.")
    print("Directly in front of you is a shining two-handed sword, glowing softly. It seems to be stuck in the rock.")
    print("A gruff looking guard is standing just to the left of the sword he looks both bored and angry.")
    no_cap_name = get_valid_string_input("Hey you, yeah you. What's yer name? ")
    player_name = no_cap_name[0].upper() + no_cap_name[1:]
    print("Well, " + player_name + " get yer head out of the clouds. Both hands. On the hilt. Just like everyone else.")
    print("You do as asked and give the weapon a tug, it slides out of the rock freely. The everyone is stunned.")
    print("A guard with a feather in his helmet is the fist to come to his senses.")
    print("\"Don't just stand there! Get him!\"")
    print("Things brings you to your senses, and you quickly begin to run toward the dock.")
    print("With the in your hand you feel strong and invigorated, putting distance between you and the guards.")
    print("As you reach the doc you see a ship pushing off from the doc. You increase your pace.")
    print("With a mighty leap your feet leave the doc and your hands wrap around the edge of the ship.")
    print("As you pull your self aboard you realize you're safe for now.")
    print("The next boat won't come until tomorrow morning, giving you a chance to put some distance between you.")
    print("As the sky darkens and the sun sets you sleep for the rest of the trip.")
    print("******************************************************************************************************")
    print("You arrive off the boat in a quaint little town. A man call you over.")
    print("\"You didn't hear this from me, but the rebel base is 250 miles south east of here.\"")
    print("\"Take this horse and sack of supplies. Get moving, The royal guard is coming and the king is NOT happy\"")
    print()
    return player_name

def day_actions():
    print("It's " + str(time) + " O'Clock")
    print("What do you do?")
    print("A. Eat something.")
    print("B. Have a drink.")
    print("C. Move ahead full speed")
    print("D. Move ahead medium speed")
    print("E. Take a break")
    print("F. Status check")
    print("Q. Give up")
    action_choice = get_action_input("What do you want to do? ", ["a", "b", "c", "d", "e", "f", "q"])
    if action_choice == 'q':
        print("You give up and enjoy the few hours you have before the guards catch up. They kill you.")
        return True

    elif action_choice == 'a':
        print("Add stuff here")

    elif action_choice == 'b':
        print("Add stuff here")

    elif action_choice == 'c':
        print("Add stuff here")

    elif action_choice == 'd':
        print("Add stuff here")

    elif action_choice == 'e':
        print("Add stuff here")

    elif action_choice == 'f':
        print("Add stuff here")



if __name__ == "__main__" :
    print_intro()
    global player_name, time, distance_traveled, guard_distance_traveled, thirst, hunger, horse_tiredness, food
    global food_in_bag, drinks_in_bottle
    player_name = steal_sword_start()
    time = 8
    thirst = 0
    hunger = 0
    horse_tiredness = 0
    food_in_bag = 3
    drinks_in_bottle = 3
    distance_traveled = 0
    guard_distance_traveled = -25

    dead = False
    while not dead:
        if time <= 19 and time >= 7 :
            dead = day_actions()
        print()