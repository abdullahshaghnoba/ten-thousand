

############################################### full code ##############################################################


# from game_logic import GameLogic

# dice_roller=GameLogic.roll_dice
# def play(roller=GameLogic.roll_dice,max_round=40):
#     """
#     play ten thousand game 
#     arguments : roller = roll dice method from game logic if run in this module or mock roller from flo if run from tests 
#                 max_round= maximum allowed number of rounds  
#     """
#     global dice_roller
#     dice_roller=roller

#     choice=invite_to_play()
#     if choice=="y":
#         start_game(max_round)
#     else:
#         decline_game()
#         """
#         print welcom and as if you want to play or not
#         """
# def invite_to_play():
#      print("Welcome to Ten Thousand")
#      print("(y)es to play or (n)o to decline") 
#      choice=input("> ")    
#      return choice

# """
# starts the game Arguments: num_rounds =maximum allowed number of rounds
# and calls do_round function
# """
# def start_game(num_rounds):
#     round_num=1
#     max_round=num_rounds
#     total_points=0
#     while round_num<max_round:
#         round_result=do_round(round_num)
#         if round_result==-1:
#             break
#         print(f"You banked {round_result} points in round {round_num}")
#         total_points+=round_result
#         print(f"Total score is {total_points} points")
#         round_num+=1
#     print(f"Thanks for playing. You earned {total_points} points")  
# """
# starts the round Arguments: round_num=the number of the current round
# calls do_roll function and calculates the score for the rolled dices
# """
# def do_round(round_num):
#     print(f"Starting round {round_num}")
#     num_dice=6
#     unbanked_points=0
#     while True:
#         roll = do_roll(num_dice)
#         if GameLogic.calculate_score(roll)==0:
#             zilch()
#             return 0
#         keepers = confirm_keepers(roll)
#         if len(keepers) == 0:
#             return -1
#         unbanked_points+= GameLogic.calculate_score(keepers)
#         num_dice-=len(keepers)
#         if num_dice==0:
#             num_dice=6
#         print(f"You have {unbanked_points} unbanked points and {num_dice} dice remaining")
#         print("(r)oll again, (b)ank your points or (q)uit:")
#         roll_bank_or_quit = input("> ")  
#         if roll_bank_or_quit == "q":
#             return -1
#         elif roll_bank_or_quit == "b":
#             return unbanked_points
# """
# starts when the score is 0 and prints the below massege
# """
# def zilch():
#     print("****************************************")
#     print("**         Zilch!!! Round over        **")        
#     print("****************************************")   
# """
# takes the input dices to keep and calls  validate_keepers function
# then returns deferent values deppending on the input and the validate function returned value
# """
# def confirm_keepers(roll):
#     while True:
#         print("Enter dice to keep, or (q)uit:")
#         keep_or_quit = input("> ")
#         if keep_or_quit == "q":
#             return tuple()
#         keepers = convert_keepers(keep_or_quit)
#         if GameLogic.validate_keepers(roll,keepers):
#             return keepers
#         else:
#             print("Cheater!!! Or Possibly made a typo...")
#             formated_roll =format_roll(roll)
#             print(formated_roll)
# """
# puts the kept dices in the needed format 
# """               
# def convert_keepers(keeper_string):
#     values = [int(value) for value in keeper_string if value.isdigit()]
#     return tuple(values)
# """
# makes a roll deppending on the number of dices from the argument
# """
# def do_roll(num_dice):
#     print(f"Rolling {num_dice} dice...")
#     roll = dice_roller(num_dice)
#     formated_roll = format_roll(roll)
#     print(formated_roll)
#     return roll



# """
# puts the roll in the needed format
# """
# def format_roll(roll):
#     values_as_strings = [str(value) for value in roll]
#     formated_roll = " ".join(values_as_strings)
#     return f"*** {formated_roll} ***"
# """
# ends the game if the input is q
# """
# def decline_game(): 
#     print("OK. Maybe another time")

###################
#  @staticmethod
#     def validate_keepers(roll, keepers):
#         remaining_dice = list(roll)
#         for keeper in keepers:
#             if keeper not in remaining_dice:
#                 return False
#             remaining_dice.remove(keeper)
#         return True  
############################# my code modifid #####################################
# from game_logic import GameLogic
from ten_thousand.game_logic import GameLogic

dice_roller = GameLogic.roll_dice

def play(roller=GameLogic.roll_dice):
    global dice_roller
    dice_roller = roller

    choice = invite_to_play()
    if choice == "y":
        score = start_game()
        print(f"Thanks for playing. You earned {score} points")
    else:
        decline_game()

def invite_to_play():
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    choice = input("> ")
    return choice

def start_game(max_round=40):
    round_num = 0
    total_score = 0
    choice=""

    while round_num < max_round:
        if choice=="q":
            break
        round_num += 1
        print(f"Starting round {round_num}")
        num_of_dice = 6
        print(f"Rolling {num_of_dice} dice...")
        dice_roll = dice_roller(num_of_dice)
        unpacked_tuple = ' '.join([str(x) for x in dice_roll])
        print("*** " + unpacked_tuple + " ***")

        round_score = 0
        unbanked_score = 0
        dice_kept = []
        while True:
            choice=ask_for_input()
            if choice == "q":
                break

            dice_kept = [int(x) for x in choice]
            
            cheater=cheater_function(dice_roll,dice_kept,unpacked_tuple)
            hot_check = GameLogic.get_scorers(dice_kept)

            if len(hot_check) == 6 and not cheater:

                choice = hot_dice_fun(dice_kept, unbanked_score)

            while cheater:
                choice=ask_for_input()
                if choice == "q":
                    break
                elif choice!="q":
                    dice_kept = [int(x) for x in choice]
                    cheater= cheater_function(dice_roll,dice_kept,unpacked_tuple)
                
                
            if choice=="q":
                break
            round_score = GameLogic.calculate_score(dice_kept)
            unbanked_score += round_score
            if len(dice_kept)!=6:
                num_of_dice-=len(dice_kept)
                print(f"You have {unbanked_score} unbanked points and {num_of_dice} dice remaining")

                print("(r)oll again, (b)ank your points or (q)uit:")
                choice = input("> ")
            if choice == "b":
                total_score += unbanked_score
                print(f"You banked {unbanked_score} points in round {round_num}")
                print(f"Total score is {total_score} points")
                unbanked_score = 0
                break
            elif choice == "q":
                break
            elif choice == "r":
                # num_of_dice -= len(dice_kept)
                if num_of_dice == 0:
                    break
                dice_roll = dice_roller(num_of_dice)
                unpacked_tuple = ' '.join([str(x) for x in dice_roll])
                print(f"Rolling {num_of_dice} dice...")
                print("*** " + unpacked_tuple + " ***")
                remaning_dices_score= GameLogic.calculate_score(dice_roll)
                if remaning_dices_score == 0:

                    unbanked_score = 0
                    print("****************************************")
                    print("**        Zilch!!! Round over         **")        
                    print("****************************************")
                    print(f"You banked 0 points in round {round_num}")
                    print("Total score is 0 points")
                    break
                dice_kept = []

        if choice == "q":
            break

    return total_score

def decline_game():
    print("OK. Maybe another time")

def ask_for_input():
    print("Enter dice to keep, or (q)uit:")
    choice = input("> ")    
    x = choice.replace(" ","")
    return x

def cheater_function(dice_roll,dice_kept,unpacked_tuple):
    cheater=False
    z=list(dice_roll)
    for x in dice_kept:
                if x not in z:
                    print("Cheater!!! Or possibly made a typo...")
                    print("*** " + unpacked_tuple + " ***")
                    cheater=True
                    break
                else: 
                    z.remove(x)
    # quit_input=input("> ")
    return cheater                

def hot_dice_fun(dice_kept, unbanked_score):
    round_score = GameLogic.calculate_score(dice_kept)
    unbanked_score += round_score
    num_of_dice = 6
    print(f"You have {unbanked_score} unbanked points and {num_of_dice} dice remaining")

    print("(r)oll again, (b)ank your points or (q)uit:")
    choice = input("> ")
    return choice
if __name__=="__main__":
    play()

