import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

lizard = '''
                                           ^      ^     ^
                                           ) '.   ) '.  ) '.   ^
                                     ^.   / _..;--"""""---..;  ) '.
                                )L   ) ';-""                 "-""--.._
                            )L_/..'-""                                ".
                   __...---"""                                     ()   "
        ___...---""                                        .             )
 .--""""                      .     ,                       )       _..-"
(_______________________d"".  "d   ,db_________..--".      /___r".""______
                        b,  L  P  ,d'               L     (  d'  ;  AZC
                         Y,  V   p'                 '.    'P" ,P'
                         .p      /                     b,      <_
                       _-"      <_                     "b        '-_
                    .-'   .       '-_                  d"     _.._  )
                  ."  _.-"d  d*-.._  )                d" d   b   ""
                   "-"   P' d'     ""                d" ,P P   b
                        d' P"                        ; d"  'Y, 'b
                       '_."                           "     'b._'
'''

spock = '''
⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⡀⠀⠀⠀⠀⢠⣶⣶⡄⠀⠀⠀
⠀⠀⠀⠀⠀⣀⣀⠀⢹⣿⣿⡇⠀⠀⠀⠀⣾⣿⣿⠃⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣿⣇⠈⣿⣿⣧⠀⠀⠀⢠⣿⣿⡏⠀⣰⣶⡄
⠀⠀⠀⠀⠘⣿⣿⣿⠀⢹⣿⣿⡀⠀⠀⣾⣿⣿⠃⢰⣿⣿⡇
⠀⠀⠀⠀⠀⢹⣿⣿⡆⠘⣿⣿⡇⠀⢠⣿⣿⡏⠀⣾⣿⣿⠁
⠀⠀⠀⠀⠀⠈⣿⣿⣿⠀⢹⣿⣧⣀⣾⣿⣿⣇⣸⣿⣿⣿⠀
⠀⠀⠀⠀⠀⠀⢻⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
⣴⣿⣿⣷⣤⡀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
⠻⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀
⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠛⠿⠿⠿⠿⠿⠿⠿⠿⠿⠟⠋⠀⠀⠀⠀

'''
computer_options = [rock, paper, scissors, lizard, spock]



# random_number = random.randint(1, 3)
#
# computer_choice = random.randint(1, 3)


print("Welcome to the Rock Paper Scissors Lizard spock game!")
print("What would you like to throw?")
user_input = input("Type r for rock, p for paper, s for scissors, l for lizard and sp for spock ")
if user_input == "r":
    print(rock)
elif user_input == "p":
    print(paper)
elif user_input == "s":
    print(scissors)
elif user_input == "l":
    print(lizard)
elif user_input == "sp":
    print(spock)
else:
    print("Please type r,p,s,l or sp")

computer_choice = random.choice(computer_options)

if computer_choice == computer_options[0]:
    print("Computer chose: " + rock)
elif computer_choice == computer_options[1]:
    print("Computer chose: " + paper)
elif computer_choice == computer_options[2]:
    print("Computer chose: " + scissors)
elif computer_choice == computer_options[3]:
    print("Computer chose: " + lizard)
elif computer_choice == computer_options[4]:
    print("Computer chose: " + spock)

if user_input == "r" and computer_choice == rock:
    print("It's a draw!")
elif user_input == "r" and computer_choice == paper:
    print("Paper beats Rock! You lose :( ")
elif user_input == "r" and computer_choice == scissors:
    print("Rock beats Scissors! You Win!")
elif user_input == "r" and computer_choice == lizard:
    print("Rock crushes Lizard ! You Win! :D ")
elif user_input == "r" and computer_choice == spock:
    print("spock vaporizes Rock! You Lose :( ")

if user_input == "p" and computer_choice == rock:
    print("Paper beats Rock! You Win!")
elif user_input == "p" and computer_choice == paper:
    print("It's a draw!")
elif user_input == "p" and computer_choice == scissors:
    print("Scissors beats Paper! You Lose :( :( ")
elif user_input == "p" and computer_choice == lizard:
    print("Lizard eats paper ! You Lose :(")
elif user_input == "p" and computer_choice == spock:
    print("Paper disproves spock! You Win! :D :D :D ")

if user_input == "s" and computer_choice == rock:
    print(" Rock beats Scissors! You lose :( ")
elif user_input == "s" and computer_choice == paper:
    print("Scissors beats Paper! You win!")
elif user_input == "s" and computer_choice == scissors:
    print("It's a draw!")
elif user_input == "s" and computer_choice == lizard:
    print("Scissors decapitates Lizard! You Win :D :D ")
elif user_input == "s" and computer_choice == spock:
    print("spocke smashes Scissors! You Lose :( ")

if user_input == "l" and computer_choice == rock:
    print("Rock crushes Lizard ! You Lose!! :( :( ")
elif user_input == "l" and computer_choice == paper:
    print("Lizard eats paper ! You Win! :D ")
elif user_input == "l" and computer_choice == scissors:
    print("Scissors decapitates Lizard! ! You Lose! :( ")
elif user_input == "l" and computer_choice == lizard:
    print("It's a draw!")
elif user_input == "l" and computer_choice == spock:
    print("Lizard poisons spock! You Win! :D" )

if user_input == "sp" and computer_choice == rock:
    print(" spock vaporizes Rock! You Win! :D :D :D ")
elif user_input == "sp" and computer_choice == paper:
    print("Paper disproves spock! You Lose! :( ")
elif user_input == "sp" and computer_choice == scissors:
    print("spock smashes Scissors! You Win! :D")
elif user_input == "sp" and computer_choice == lizard:
    print("Lizard poisons spock! You Lose! :( ")
elif user_input == "sp" and computer_choice == spock:
    print("It's a draw!")

#
# if computer_choice == 1:
#     print(rock)
# elif computer_choice == 2:
#     print(paper)
# elif computer_choice == 3:
#     print(scissors)
# print(computer_choice)
#
# if user_input == "r" and computer_choice == 1:
#     print("It's a draw!")
# elif user_input == "r" and computer_choice == 2:
#     print("Paper beats Rock! You lose :( ")
# elif user_input == "r" and computer_choice == 3:
#     print("Rock beats Scissors! You win!")
#
# if user_input == "p" and computer_choice == 1:
#     print("Paper beats Rock! You win!")
# elif user_input == "p" and computer_choice == 2:
#     print("It's a draw!")
# elif user_input == "p" and computer_choice == 3:
#     print("Scissors beats Paper! You lose :( :( ")
#
# if user_input == "s" and computer_choice == 1:
#     print(" Rock beats Scissors! You lose :( ")
# elif user_input == "s" and computer_choice == 2:
#     print("Scissors beats Paper! You win!")
# elif user_input == "s" and computer_choice == 3:
#     print("It's a draw!")


