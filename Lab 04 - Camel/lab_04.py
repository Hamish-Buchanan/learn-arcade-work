"""
The Sword Thief's Journey is a text based adventure game where the player makes their way to the rebel base. The player
must stay ahead of the royal guard who, if they catch up, will kill the player. They also must manage their resources so
as not to succumb to upkeep issues. They will also have to fight off chance encounters along the way.
"""

import random

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

def hunger_check():
    if hunger == 0:
        print("You feel full")
    elif hunger <= 3:
        print("You're peckish")
    elif hunger <= 5:
        print("You're hungry")
    elif hunger <= 7:
        print("You're famished")
    else:
        print("You're hunger is unbearable")

def health_check():
    if hp == 50:
        print("You're unhurt")
    elif hp >= 35:
        print("You have a few scrapes and brusies")
    elif hp >= 25:
        print("You're pretty injured")
    elif hp >= 10:
        print("You're seriously hurt")
    else:
        print("You're on the verge of death")

def thirst_check():
    if thirst <= 3:
        print("You're not thirsty")
    elif thirst <= 5:
        print("You're thirsty")
    elif thirst <= 7:
        print("You're parched")
    else:
        print("You are feeling very dehydrated")

def horse_check():
    if horse_tiredness == 0:
        print("Your horse seems like it's raring to go!")
    elif horse_tiredness <= 3:
        print("Your horse is happy")
    elif horse_tiredness <= 5:
        print("Your horse seems a little tired")
    elif horse_tiredness <= 7:
        print("Your horse is panting heavily")
    else:
        print("Your horse looks extremely tired")

def dead_check():
    if hunger >= 10:
        print("You collapse unconscious, never to awaken. You've starved to death")
        return True
    elif thirst >= 10:
        print("Your throat as dry as you eye your horses saliva wistfully...")
        print("You stumble towards the horse, unsteady on your feet. You stumble and fall over.")
        print("Your consciousness fades. You've died of thirst")
        return True
    elif horse_tiredness >= 10:
        print("Your horse, already moving slowly stumbles under your weight.")
        print("You urge it on, tapping your spurs on the open wounds at it's side.")
        print("It falls over, with you on it, and you tumble to the ground.")
        print("You run away from the animal, from the guards. But without the horse you're too slow.")
        print("You hear the sound of cantering hooves and turn, just in time to see an arrow whizz by.")
        print("The next doesn't miss. You loo at it embedded in your chest. Another strikes your head.")
        print("It all goes black")
        return True
    elif distance_traveled - guard_distance_traveled <= 0:
        print("You hear shouts behind you. 'There he is!' the guards cry.")
        print("You look, to see a muscular knight galloping towards you, axe in hand.")
        print("You go to pull your blade, but an arrow strikes your shoulder and it falls to the ground with a clatter")
        print("Terrified you turn back once more, to see the axe looming above your head. Then nothing.")
    elif distance_traveled >= 250:
        print("You slow down as a handsome young man waves you over.")
        print(player_name + " you've made it! Come. We've much to discuss.")
        print("And with that, the sword thief's journey ends and the legend of " + player_name + " begins")
        return True
    else :
        if hunger > 7:
            print("Your hunger is unbearable")
        if thirst > 7:
            print("You are feeling very dehydrated")
        if hp < 10:
            print("You're on the verge of death")
        if horse_tiredness > 7:
            print("Your horse looks extremely tired. It's skin is raw where your stirrups touch it.")
        return False

def day_actions():
    global player_name, time, distance_traveled, guard_distance_traveled, thirst, hunger, horse_tiredness
    global food_in_bag, drinks_in_bottle, hp, atk, defence
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
        if hunger > 0 and food_in_bag > 0:
            print("You eat some food from your bag")
            food_in_bag -= 1
            if hunger >= 5:
                hunger -= 5
            else:
                hunger = 0
            hunger_check()
        elif not hunger > 0:
            print("You're too full to eat anymore")
        else:
            print("You don't have any food left")

    elif action_choice == 'b':
        if thirst > 0 and drinks_in_bottle > 0:
            print("You drink from your bottle")
            drinks_in_bottle -= 1
            thirst = 0
            thirst_check()
        elif not thirst > 0:
            print("You don't feel thirsty right now")
        else:
            print("You don't have any water left")

    elif action_choice == 'c':
        num_hours = get_valid_number_input("For how many hours? ")
        if time + num_hours > 24:
            time = time + num_hours - 24
        else:
            time += num_hours
        print("You push your horse to go as fast as it can!")
        new_dist = 0
        guard_dist = 0
        for i in range(num_hours):
            horse_tiredness += random.randint(1, 2)
            new_dist += random.randint(7, 12)
            guard_dist += random.randint(6, 10)
            hunger += random.random()/4*3
            thirst += random.random()
        distance_traveled = distance_traveled + new_dist
        guard_distance_traveled = guard_distance_traveled + guard_dist
        if dead_check():
            return True
        print("You've traveled " + str(new_dist) + " miles")
        print("The guards traveled " + str(guard_dist) + " miles")
        if guard_distance_traveled <= 0:
            print("The guards are far behind you")
        else:
            print("The guards seem to be " + str(distance_traveled - guard_distance_traveled) + " miles behind you")

    elif action_choice == 'd':
        num_hours = get_valid_number_input("For how many hours? ")
        if time + num_hours > 24:
            time = time + num_hours - 24
        else:
            time += num_hours
        print("You set off at a steady pace")
        new_dist = 0
        guard_dist = 0
        for i in range(num_hours):
            horse_tiredness += random.randint(1, 2)
            new_dist += random.randint(5, 8)
            guard_dist += random.randint(6, 10)
            hunger += random.random() / 4 * 3
            thirst += random.random()
        distance_traveled = distance_traveled + new_dist
        guard_distance_traveled = guard_distance_traveled + guard_dist
        if dead_check():
            return True
        print("You've traveled " + str(new_dist) + " miles")
        print("The guards traveled " + str(guard_dist) + " miles")
        if guard_distance_traveled <= 0:
            print("The guards are far behind you")
        else:
            print("The guards seem to be " + str(distance_traveled - guard_distance_traveled) + " miles behind you")

    elif action_choice == 'e':
        num_hours = get_valid_number_input("For how many hours? ")
        if time + num_hours > 24:
            time = time + num_hours - 24
        else:
            time += num_hours
        print("You tie up your horse in a field with lush grass and doze off")
        guard_dist = 0
        for i in range(num_hours):
            horse_tiredness -= random.randint(2, 3)
            guard_dist += random.randint(6, 10)
            hp += random.randint(4,8)
            hunger += random.random() / 3
            thirst += random.random() / 2
        if hp > 50 : hp = 50
        guard_distance_traveled = guard_distance_traveled + guard_dist
        if dead_check():
            return True
        horse_check()
        print("The guards traveled " + str(guard_dist) + " miles")
        if guard_distance_traveled <= 0:
            print("The guards are far behind you")
        else:
            print("The guards seem to be " + str(distance_traveled - guard_distance_traveled) + " miles behind you")

    elif action_choice == 'f':
        print("You do a stock take : ")
        health_check()
        hunger_check()
        thirst_check()
        horse_check()
        print("You have " + str(food_in_bag) + " pieces of food in your bag")
        print("You have " + str(drinks_in_bottle) + " drinks left in your bag")
        print("You have traveled around " + str(distance_traveled) + " miles")
        if guard_distance_traveled <= 0:
            print("The guards are far behind you")
        else:
            print("The guards seem to be " + str(distance_traveled - guard_distance_traveled) + " miles behind you")
    if time >= 20:
        print("The sun has set and the moon rises into the sky. The guards have turned in for the night.")
        print("You hear the eerie cries of monsters in the dark. Traveling will be more dangerous now.")

def night_actions():
    global player_name, time, distance_traveled, guard_distance_traveled, thirst, hunger, horse_tiredness
    global food_in_bag, drinks_in_bottle, hp, atk, defence
    print("It's " + str(time) + " O'Clock")
    print("What do you do?")
    print("A. Eat something.")
    print("B. Have a drink.")
    print("C. Move ahead full speed")
    print("D. Move ahead medium speed")
    print("E. Sleep for the night")
    print("F. Status check")
    print("Q. Give up")
    action_choice = get_action_input("What do you want to do? ", ["a", "b", "c", "d", "e", "f", "q"])
    if action_choice == 'q':
        print("You give up and enjoy the few hours you have before the guards catch up. They kill you.")
        return True

    elif action_choice == 'a':
        if hunger > 0 and food_in_bag > 0:
            print("You eat some food from your bag")
            food_in_bag -= 1
            if hunger >= 5:
                hunger -= 5
            else:
                hunger = 0
            hunger_check()
        elif not hunger > 0:
            print("You're too full to eat anymore")
        else:
            print("You don't have any food left")

    elif action_choice == 'b':
        if thirst > 0 and drinks_in_bottle > 0:
            print("You drink from your bottle")
            drinks_in_bottle -= 1
            thirst = 0
            thirst_check()
        elif not thirst > 0:
            print("You don't feel thirsty right now")
        else:
            print("You don't have any water left")

    elif action_choice == 'c':
        num_hours = get_valid_number_input("For how many hours? ")
        if time + num_hours > 24:
            time = time + num_hours - 24
        else:
            time += num_hours
        print("You push your horse to go as fast as it can!")
        new_dist = 0
        for i in range(num_hours):
            horse_tiredness += random.randint(1, 2)
            new_dist += random.randint(6, 10)
            hunger += random.random()/4*3
            thirst += random.random()
        distance_traveled = distance_traveled + new_dist
        if dead_check():
            return True
        print("You've traveled " + str(new_dist) + " miles")
        print("The guards slept")
        if guard_distance_traveled <= 0:
            print("The guards are far behind you")
        else:
            print("The guards seem to be " + str(distance_traveled - guard_distance_traveled) + " miles behind you")

    elif action_choice == 'd':
        num_hours = get_valid_number_input("For how many hours? ")
        if time + num_hours > 24:
            time = time + num_hours - 24
        else:
            time += num_hours
        print("You set off at a steady pace")
        new_dist = 0
        for i in range(num_hours):
            horse_tiredness += random.randint(1, 2)
            new_dist += random.randint(3, 7)
            hunger += random.random() / 4 * 3
            thirst += random.random()
        distance_traveled = distance_traveled + new_dist
        if dead_check():
            return True
        print("You've traveled " + str(new_dist) + " miles")
        print("The guards slept")
        if guard_distance_traveled <= 0:
            print("The guards are far behind you")
        else:
            print("The guards seem to be " + str(distance_traveled - guard_distance_traveled) + " miles behind you")

    elif action_choice == 'e':
        if time >= 19:
            time_slept = (time-24)*-1 + 7
        else:
            time_slept = 7-time
        time = 7
        horse_tiredness -= 1.5*time_slept
        if horse_tiredness < 0: horse_tiredness = 0
        hunger += random.random() / 4 * 3
        thirst += random.random()
        hp += 3*time_slept
        if hp > 50: hp = 50
        print("You set up camp for the night. You tie up your horse and nod off.")
        if dead_check():
            return True

    elif action_choice == 'f':
        print("You do a stock take : ")
        health_check()
        hunger_check()
        thirst_check()
        horse_check()
        print("You have " + str(food_in_bag) + " pieces of food in your bag")
        print("You have " + str(drinks_in_bottle) + " drinks left in your bag")
        print("You have traveled around " + str(distance_traveled) + " miles")
        if guard_distance_traveled <= 0:
            print("The guards are far behind you")
        else:
            print("The guards seem to be " + str(distance_traveled - guard_distance_traveled) + " miles behind you")


if __name__ == "__main__" :
    print_intro()
    global player_name, time, distance_traveled, guard_distance_traveled, thirst, hunger, horse_tiredness
    global food_in_bag, drinks_in_bottle, hp, atk, defence
    player_name = steal_sword_start()
    time = 8
    thirst = 0
    hunger = 0
    horse_tiredness = 0
    food_in_bag = 3
    drinks_in_bottle = 3
    distance_traveled = 0
    guard_distance_traveled = -25
    hp = 50
    atk = 5
    defence = 8
    dead = False
    while not dead:
        if time <= 19 and time >= 7 :
            dead = day_actions()
        else:
            dead = night_actions()
        print()