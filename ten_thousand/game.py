

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
            choice=cheater_function()
            if choice == "q":
                break

            dice_kept = [int(x) for x in choice]
            
            cheater=cheater_again(dice_roll,dice_kept,unpacked_tuple)
                    
            cheater_repet=False
            while cheater:
                choice=cheater_function()
                if choice == "q":
                    break
                elif choice!="q":
                    dice_kept = [int(x) for x in choice]
                    break
                elif not cheater_repet:
                        break
                else:
                    cheater_repet= cheater_again(dice_roll,dice_kept,unpacked_tuple)
            if choice=="q":
                break
            round_score = GameLogic.calculate_score(dice_kept)
            unbanked_score += round_score
            print(f"You have {unbanked_score} unbanked points and {num_of_dice - len(dice_kept)} dice remaining")

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
                num_of_dice -= len(dice_kept)
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
                    print("**         Zilch!!! Round over        **")        
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

def cheater_function():
    print("Enter dice to keep, or (q)uit:")
    choice = input("> ")
    return choice

def cheater_again(dice_roll,dice_kept,unpacked_tuple):
    cheater=False
    z=list(dice_roll)
    for x in dice_kept:
                if x not in z:
                    print("Cheater!!! Or Possibly made a typo...")
                    print("*** " + unpacked_tuple + " ***")
                    cheater=True
                    break
                else: 
                    z.remove(x)
    # quit_input=input("> ")
    return cheater                


if __name__=="__main__":
    play()


############################################################## trial and error code xd ######################################################
# from ten_thousand.game_logic import GameLogic
# # from game_logic import GameLogic

# roll_dice = GameLogic.roll_dice
# points_calculate = GameLogic.calculate_score

# def play (roller = GameLogic.roll_dice):
#     global roll_dice
#     roll_dice = roller
#     print("Welcome to Ten Thousand")
#     print("(y)es to play or (n)o to decline")
#     user_res= input('> ')
#     if user_res == "n":
#         quitter()
#     if user_res == 'y':
#         start_game()
                
# def quitter ():
#         return print('OK. Maybe another time') 
    

# def start_game(round_num=1,total=0,number_dices = 6):
        
#         user_choice = ''
        
#         first_roll = roll_dice(number_dices)
#         # zilch test
#         if points_calculate(first_roll) == 0:
#               print("ohhh ohhh ZILTCH you Lost your points.")
#               round_num+=1
#               points = 0
#               return start_game(round_num,total,number_dices=6)

#         unpacked_tuple = ''
#         for i in first_roll:
#             unpacked_tuple+= str(i)+' '
#         print(f'Starting round {round_num}')
#         print(f'Rolling {number_dices} dice...')
#         print("*** "+unpacked_tuple.strip()+' ***') 
#         print("Enter dice to keep, or (q)uit:")
#         user_choice = input('> ')
#         if user_choice == "q":
#               end_game(total)
#         else:
#               dice_to_keep = tuple(int(x) for x in user_choice)
#               roll_to_test_cheater = list(first_roll)
#               for i in dice_to_keep:
#                     if i not in roll_to_test_cheater:
#                           print("""********************************************\n********************************************\n***************  DON'T CHEAT  **************\n********************************************\n********************************************\n                TRY AGAIN   """)
#                         #   print("*** "+unpacked_tuple.strip()+' ***') 
#                         #   print("Enter dice to keep, or (q)uit:")
#                         #   user_choice = input('> ')
#                         #   dice_to_keep = tuple(int(x) for x in user_choice)
                          
#                           return start_game(round_num,total,number_dices=6)
                          
#                     index = roll_to_test_cheater.index(i)
#                     roll_to_test_cheater.pop(index)
                          
              
#               number_dices = number_dices - len(dice_to_keep)
#               points =  points_calculate(dice_to_keep)
#               print(f"You have {points} unbanked points and {number_dices} dice remaining")
#               print("(r)oll again, (b)ank your points or (q)uit:")     
#               user_choice = input('> ')
#               if user_choice == 'q':
#                     end_game(total)
#               elif user_choice == 'r':
#                     if number_dices > 0 :
#                         points += points
#                         start_game(round_num,total,number_dices)
#                     else:
#                           print('you ran out of dices new round will start\n you didnt bank yor points so you lost them')
#                           round_num+=1
#                           start_game(round_num,total,number_dices=6)  
#               elif user_choice == "b":
#                     bank_points(points,round_num,total)
                    
                                    

# def bank_points(points,round_num,total):
#       total = total + points
#       print(f"You banked {points} points in round {round_num}")
#       print(f"Total score is {total} points")
#       round_num += 1
#       start_game(round_num,total)       
        

# def end_game(total):
#       print(f"Thanks for playing. You earned {total} points")                   





# if __name__ == "__main__":
#     play()