# * Displaying information
from random import random
import random
# print([1, 2, 3])
# print([4, 5, 6])
# print([7, 8, 9])


# def display(row1, row2, row3):
#    print(row1)
#    print(row2)
#    print(row3)


# row1 = [' ', ' ', ' ']
# row2 = [' ', ' ', ' ']
# row3 = [' ', ' ', ' ']

# display(row1, row2, row3)

# row2[1] = 'X'

# display(row1, row2, row3)

# * Accepting User Input

# input('Please enter a value: ')

# result = input('Enter a value: ')
# result_int = int(result)
# print(type(result_int))
# print(type(2.3))

# ?-----------------

# position_index = int(input('Choose an index position: '))

# print('--->', row2[position_index])


# * Validation User Input

# def user_choice():
#    choice = input('Please enter a number (0-10) : ')
#    return choice

# print(user_choice())

# ! робимо перевірку що введене значення дійсно число і що воно не виходе за межі діапазону 0-10

# def user_choice():
#    choice = 'WRONG'
#    acceptable_range = range(0, 10)
#    within_range = False
# TWO CONDITIONS TO CHECK
# DIGIT OR WITHIN_RANGE== False
#    while choice.isdigit() == False or within_range == False:

#        choice = input('Please enter a number (0-10) : ')
#        # DOGIT CHECK
#        if choice.isdigit() == False:
#            print('Sorry that is not a digit')
# RANGE CHECK
#        if choice.isdigit() == True:
#            if int(choice) in acceptable_range:
#                within_range = True
#            else:
#                print('Sorry you are out of acceptable range 0-10')
#                within_range = False

#    return choice


# print(user_choice())

# * Simple User Interaction

#game_list = [0, 1, 2]


#def display_game(game_list):
#    print('Here is current list: ')
#    print(game_list)


#display_game(game_list)


#def position_choice():

#    choice = 'wrong'

#    while choice not in ['0', '1', '2']:

#        choice=input('Pick a position (0, 1, 2): ')

#        if choice not in ['0', '1', '2']:
#            print('Sorry, invalid choice! ')

#    return int(choice)

#position_choice()



#def replacement_choice(game_list, position):

#    user_placement = input('Type a string to place at position:')

#    game_list[position] = user_placement

#    return game_list

#replacement_choice(game_list, 1)


#def gameon_choice():

#    choice = 'wrong'

#    while choice not in ['Y', 'N']:

#        choice=input('Keep playing? (Y or N) : ')

#        if choice not in ['Y', 'N']:
#            print('Sorry, I dont understand, please choose Y or N')

#    if choice == 'Y':
#        return True
#    else:
#        return False


#gameon_choice()


#game_on = True
#game_list = [0, 1, 2]

#while game_on:
#    display_game(game_list)
#    position = position_choice()
#    game_list = replacement_choice(game_list, position)
#    display_game(game_list)
#    game_on = gameon_choice()


# * First Milestone project

# ? cтворюємо дошку для гри



board = [' ']*10
def display_board(board):

    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-|-|-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-|-|-')
    print(board[1] + '|' + board[2] + '|' + board[3])
# board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(board)


def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
#player_input()
def place_marker(board, marker, position):
    board[position] = marker

# place_marker(board, '$', 6)
# display_board(board)


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal

#print(win_check(board,'X'))

def choose_first():
    if 0 == random.randint(0, 1):
        return 'Player 2'
    else:
        return 'Player 1'

#print(choose_first())


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')



