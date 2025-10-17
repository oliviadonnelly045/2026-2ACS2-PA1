'''
Continuation of classwork, graded on completion/effort.

Write a small program that allows people to add, drop, and change their mod 2 schedule.
'''

mod1 = {
    "A Block": "",
    "B Block": "",
    "C Block": "",
    "E Block": ""
    }

mod2 = {
    "A Block": "",
    "B Block": "",
    "C Block": "",
    "E Block": ""
    }

mod3 = {
    "A Block": "",
    "B Block": "",
    "C Block": "",
    "E Block": ""
    }

mod4 = {
    "A Block": "",
    "B Block": "",
    "C Block": "",
    "E Block": ""
    }

mod5 = {
    "A Block": "",
    "B Block": "",
    "C Block": "",
    "E Block": ""
    }

mod6 = {
    "A Block": "",
    "B Block": "",
    "C Block": "",
    "E Block": ""
    }

mod7 = {
    "A Block": "",
    "B Block": "",
    "C Block": "",
    "E Block": ""
    }

D_Block = {
    "Fall": "",
    "Winter": "",
    "Spring" : ""
    }

full_schedule = [mod1, mod2, mod3, mod4, mod5, mod6, mod7, D_Block]

#parameters: a dictionary called schedule
#returns: a schedule with an added class
def add_class(schedule):
    schedule_add = input("What block would you like to add to (A,B,C,E)?").lower()
    valid_actions = ["a","b","c","e"]
    while schedule_add not in valid_actions:
        print("Error. Please pick A, B, C, or E.")
        schedule_add = input("What block would you like to add to (A,B,C,E)?").lower()
    if schedule_add == "a":
        schedule_A = input("Enter your A Block ").lower()
        schedule ["A Block"] = schedule_A
    elif schedule_add == "b":
        schedule_B = input("Enter your B Block ").lower()
        schedule ["B Block"] = schedule_B
    elif schedule_add == "c":
        schedule_C = input("Enter your C Block ").lower()
        schedule ["C Block"] = schedule_C
    elif schedule_add == "e":
        schedule_E = input("Enter your E Block ").lower()
        schedule ["E Block"] = schedule_E
    return schedule

#parameters: a dictionary called schedule
#returns: a schedule with a changed, preexisting class
def change_class(schedule):
    schedule_change = input("What block would you like to change to (A,B,C,E)?").lower()
    valid_actions = ["a","b","c","e"]
    while schedule_change not in valid_actions:
        print("Error. Please pick A, B, C, or E.")
        schedule_change = input("What block would you like to change to (A,B,C,E)?").lower()
    if schedule_change == "a":
        schedule_changeA = input (f"Enter the new class for A Block: ")
        schedule ["A Block"]= schedule_changeA
    elif schedule_change == "b":
        schedule_changeB = input (f"Enter the new class for B Block: ")
        schedule ["B Block"]= schedule_changeB
    elif schedule_change == "c":
        schedule_changeC = input (f"Enter the new class for C Block: ")
        schedule ["C Block"]= schedule_changeC
    elif schedule_change == "e":
        schedule_changeE = input (f"Enter the new class for E Block: ")
        schedule ["E Block"]= schedule_changeE
    return schedule

#parameters: a dictionary called schedule
#returns: a schedule with a removed class
def drop_class(schedule):
    schedule_drop = input("What block would you like to drop (A,B,C,E)?").lower()
    valid_actions = ["a","b","c","e"]
    while schedule_drop not in valid_actions:
        print("Error. Please pick A, B, C, or E.")
        schedule_drop = input("What block would you like to drop (A,B,C,E)?").lower()
    if schedule_drop == "a":
        schedule["A Block"] = ""
    elif schedule_drop == "b":
        schedule["B Block"] = ""
    elif schedule_drop == "c":
        schedule["C Block"] = ""
    elif schedule_drop == "e":
        schedule["E Block"] = ""
        return schedule


def add_dblock(dschedule):
    d_add = input ("What season would you like to add (fall, winter, spring)").lower()
    valid_actions = ["fall, winter, spring"]
    while d_add not in valid_actions:
        print("Error. Please pick fall, winter, or spring.")
        d_add = input ("What season would you like to add (fall, winter, spring)").lower()
    if d_add == "fall":
        d_addfall = input (f"Enter the class for your fall D Block: ")
        dschedule ["Fall"]= d_addfall
    elif d_add == "winter":
        d_addwinter = input (f"Enter the class for your winter D Block: ")
        dschedule ["Winter"]= d_addwinter
    elif d_add == "spring":
        d_addspring = input (f"Enter the class for your spring D Block: ")
        d_add ["Spring"]= d_addspring
    return dschedule

def change_dblock(dschedule):
    d_change = input ("What season would you like to change (fall, winter, spring)").lower()
    valid_actions = ["fall, winter, spring"]
    while d_change not in valid_actions:
        print("Error. Please pick fall, winter, or spring.")
        d_change = input ("What season would you like to change (fall, winter, spring)").lower()
    if d_change == "fall":
        d_changefall = input (f"Enter the new class for your fall D Block: ")
        dschedule ["Fall"]= d_changefall
    elif d_change == "winter":
        d_changewinter = input (f"Enter the new class for your winter D Block: ")
        dschedule ["Winter"]= d_changewinter
    elif d_change == "spring":
        d_changespring = input (f"Enter the new class for your spring D Block: ")
        dschedule ["Spring"]= d_changespring
    return dschedule


def drop_dblock(dschedule):
    d_drop = input ("What season would you like to drop (fall, winter, spring)").lower()
    valid_actions = ["fall, winter, spring"]
    while d_drop not in valid_actions:
        print("Error. Please pick fall, winter, or spring.")
        d_drop = input ("What season would you like to drop (fall, winter, spring)").lower()
    if d_drop == "fall":
        dschedule["Fall"] = ""
    elif d_drop == "winter":
        dschedule["Winter"] = ""
    elif d_drop == "spring":
        dschedule["Spring"] = ""
    return dschedule





#main function
def main():
    global mod1, mod2, mod3, mod4, mod5, mod6, mod7, D_Block
    print("Welcome to Mrs. Carroll's office.")
    dontstop = True
    while dontstop:
        user_option = input("What would you like to do? (edit or view) ").lower()
        valid_actions = ["edit", "view"]
        while user_option not in valid_actions:
            print("Error. Please pick edit or view.")
            user_option = input("What would you like to do? (edit or view) ").lower()
        if user_option == "edit":
            user_choice = input("What would you like to edit? (mod schedule or D Blocks)").lower()
            valid_actions = ["mod schedule","d blocks"]
            while user_choice not in valid_actions:
                print("Error. Please pick mod schedule or D Blocks.")
                user_choice = input("What would you like to do?").lower()
        
            if user_choice == "mod schedule":
                mod_choice = input("What mod would you like to edit?").lower()
                valid_actions = ["1", "2", "3", "4", "5", "6", "7"]
                edit_choice = input("What would you like to do? (add, drop, or change)").lower()
                valid_actions = ["add","drop","change"]
                while edit_choice not in valid_actions:
                    print("Error. Please pick add, drop, change, or exit.")
                    edit_choice = input("What would you like to do? (add, drop, or change)").lower()

                if mod_choice == "1":
                    if edit_choice == "add":
                        mod1 = add_class(mod1)
                    elif edit_choice == "change":
                        mod1 = change_class(mod1)
                    elif edit_choice == "drop":
                        mod1 = drop_class(mod1)
                elif mod_choice == "2":
                    if edit_choice == "add":
                        mod2 = add_class(mod2)
                    elif edit_choice == "change":
                        mod2 = change_class(mod2)
                    elif edit_choice == "drop":
                        mod2 = drop_class(mod2)
                elif mod_choice == "3":
                    if edit_choice == "add":
                        mod3 = add_class(mod3)
                    elif edit_choice == "change":
                        mod3 = change_class(mod3)
                    elif edit_choice == "drop":
                        mod3= drop_class(mod3)
                elif mod_choice == "4":
                    if edit_choice == "add":
                        mod4 = add_class(mod4)
                    elif edit_choice == "change":
                        mod4 = change_class(mod4)
                    elif edit_choice == "drop":
                        mod4 = drop_class(mod4)
                elif mod_choice == "5":
                    if edit_choice == "add":
                        mod5 = add_class(mod5)
                    elif edit_choice == "change":
                        mod5 = change_class(mod5)
                    elif edit_choice == "drop":
                        mod5 = drop_class(mod5)
                elif mod_choice == "6":
                    if edit_choice == "add":
                        mod6 = add_class(mod6)
                    elif edit_choice == "change":
                        mod6 = change_class(mod6)
                    elif edit_choice == "drop":
                        mod6 = drop_class(mod6)
                elif mod_choice == "7":
                    if edit_choice == "add":
                        mod7 = add_class(mod7)
                    elif edit_choice == "change":
                        mod7 = change_class(mod7)
                    elif edit_choice == "drop":
                        mod7 = drop_class(mod7)
            elif user_choice == "d blocks":
                edit_dchoice = input("What would you like to do? (add, drop, or change) ").lower()
                valid_actions = ["add","drop","change"]
                if edit_dchoice == "add":
                    D_Block = add_dblock(D_Block)
                elif edit_dchoice == "drop":
                    D_Block = drop_dblock(D_Block)
                elif edit_dchoice == "change":
                    D_Block = change_dblock(D_Block)
        
            ask = input("Would you like to keep going (yes/no) ")
            if ask == "no":
                dontstop = False

        elif user_option == "view":
            for mod in full_schedule:
                for block in mod:
                    print(f"{block}")
                print ("_"*50)

    print("Thanks for stopping by!")

main()
