#function to add a class
#parameters: a dictionary called schedule
#returns: a schedule with an added class

schedule = {} 

def add_class(schedule):
    A_Block = input("Enter A Block class name: ")
    B_Block = input ("Enter B Block class name: ")
    C_Block = input ("Enter C Block class name: ")
    D_Block = input ("Enter D Block class name: ")
    
    schedule ["A Block"] = A_Block
    schedule ["B Block"] = B_Block
    schedule ["C Block"] = C_Block
    schedule ["D Block"] = D_Block

    return schedule

#function to change a class
def change_class(schedule):

    change_A_Block = input (f"Enter the new class for A Block: ")
    change_B_Block = input (f"Enter the new class for B Block: ")
    change_C_Block = input (f"Enter the new class for C Block: ")
    change_D_Block = input (f"Enter the new class for D Block: ")

    schedule["A Block"]= change_A_Block
    schedule["B Block"]= change_B_Block
    schedule["C Block"]= change_C_Block
    schedule["D Block"]= change_D_Block

    return schedule
#function to drop (delet/pop) a class
def drop_class(schedule):

    remove_A_Block = input("do remove your A Block? (y/n)")
        if y then  .pop(A_Block)
    remove_B_Block = input("do remove your B Block? (y/n)")
        if y then  .pop(B_Block)
    remove_C_Block = input("do remove your C Block? (y/n)")
        if y then  .pop(C_Block)
    remove_D_Block = input("do remove your D Block? (y/n)")
        if y then  .pop(D_Block)

    return schedule

#main function
def main():
        print("Welcome to Mrs. Carroll's office.")
    user_choice = input("What would you like to do?").lower()
    valid_actions = ["add", "drop", "change"]
    while user_choice not in valid_actions:
        print("error. Please pick add, drop, or change.")
        user_choice = input("What would you like to do?").lower()
    if user_choice == "add":
        mod2 = add_class(mod2)

main()