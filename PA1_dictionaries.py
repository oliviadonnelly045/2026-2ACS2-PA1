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


#parameters: a dictionary called schedule
#returns: a schedule with an added class
def add_class(schedule):
    schedule_add = input("What block would you like to add to (A,B,C,E)?").lower()
    valid_actions = ["A","B","C","E"]
    while schedule_add not in valid_actions:
        print("Error. Please pick A, B, C, or E.")
        if schedule == "A":
            schedule_A = input("Enter your A Block").lower()
            mod1 ["A Block"] = schedule_A
        elif schedule == "B":
            schedule_B = input("Enter your B Block").lower()
            mod1 ["B Block"] = schedule_B
        elif schedule == "C":
            schedule_C = input("Enter your C Block").lower()
            mod1 ["C Block"] = schedule_C
        elif schedule == "E":
            schedule_E = input("Enter your E Block").lower()
            E_Block ["E Block"] = schedule_E
    return schedule

#parameters: a dictionary called schedule
#returns: a schedule with a changed, preexisting class
def change_class(schedule):
    schedule_change = input("What block would you like to change to (A,B,C,E)?").lower()
    valid_actions = ["A","B","C","E"]
    while schedule_change not in valid_actions:
        print("Error. Please pick A, B, C, or E.")
        if schedule_change == "A":
            schedule_changeA = input (f"Enter the new class for A Block: ")
            mod1 ["A Block"]= schedule_changeA
        elif schedule_change == "B":
            schedule_changeB = input (f"Enter the new class for B Block: ")
            mod1 ["B Block"]= schedule_changeB
        elif schedule_change == "C":
            schedule_changeC = input (f"Enter the new class for C Block: ")
            mod1 ["C Block"]= schedule_changeC
        elif schedule_change == "E":
            schedule_changeE = input (f"Enter the new class for E Block: ")
            mod1 ["E Block"]= schedule_changeE
    return schedule

#parameters: a dictionary called schedule
#returns: a schedule with a removed class
def drop_class(schedule):
  schedule_drop = input("What block would you like to drop (A,B,C,E)?").lower()
  valid_actions = ["A","B","C","E"]
  while mod1_drop not in valid_actions:
        print("Error. Please pick A, B, C, or E.")
        if schedule_drop == "A":
            mod1["A Block"] = ""
        elif schedule_drop == "B":
            mod1["B Block"] = ""
        elif schedule_drop == "C":
            mod1["C Block"] = ""
        elif schedule_drop == "E":
            mod1["E Block"] = ""
        return schedule

#main function
def main():
    print("Welcome to Mrs. Carroll's office.")
    user_choice = input("What would you like to edit?").lower()
    valid_actions = ["mod schedule","D Blocks"]
    while user_choice not in valid_actions:
        print("Error. Please pick add, drop, change, or exit.")
        user_choice = input("What would you like to do?").lower()
        if user_choice == "mod schedule":
            mod_choice = input("What mod would you like to edit?").lower()
            valid_actions = ["1", "2", "3", "4", "5", "6", "7"]
            while mod_choice not in valid_actions:
                print("Error. Please pick the mod number you would like to edit")
                mod_choice = input("What mod would you like to edit?").lower()

                if mod_choice == "1":
                    edit_choice = input("What would you like to do?").lower()
                    valid_actions = ["add","drop","change"]
                    while edit_choice not in valid_actions:
                        print("Error. Please pick add, drop, change, or exit.")
                    if edit_choice == "add":
                    
                    elif edit_choice == "change":

                    elif edit_choice == "drop": #FIX

                    
                    
                        
    return mod1






        
        valid_actions = ["add","drop","change","exit"]
    
    while user_choice != "exit":
        if user_choice == "add":
            mod2 = add_class(mod2)
        elif user_choice == "drop":
            mod2 = drop_class(mod2)
        else:
            mod2 = change_class(mod2)
        user_choice = input("Anything else? ")
        while user_choice not in valid_actions:
            print("Error. Please pick add, drop, change, or exit.")
            user_choice = input("Anything else? ").lower()
print("Thanks for stopping by!")

main()
