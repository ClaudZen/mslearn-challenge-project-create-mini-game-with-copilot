import random

options = ['rock', 'paper', 'scissors']
options_continue = ['y', 'n']
results = {
    ('rock', 'paper'): 'Machine win',
    ('rock', 'scissors'): 'You win',
    ('paper', 'rock'): 'You win',
    ('paper', 'scissors'): 'Machine win',
    ('scissors', 'rock'): 'Machine win',
    ('scissors', 'paper'): 'You win',
}

def start_game():
    user_input = validate_input_option_game()
    print('You choose:', user_input)
    machine_input = random.choice(options)
    print('Machine choose:', machine_input)
    result = compare(user_input, machine_input)
    print(result)
    return result

# Make a function to compare user input and machine input and return winner, user or machine
def compare(user_input, machine_input):
    if user_input == machine_input:
        return 'Draw'
    else:
        return results[(user_input, machine_input)]
    
# Function that receives a user input if is not rock, paper or scissors, ask for a valid option and call the function again
def validate_input_option_game():
    print(f'Please choose {options[0]}, {options[1]} or {options[2]}')
    user_input = input().lower()
    if user_input not in options:
       return validate_input_option_game()
    return user_input
    
# Function that receives a user input if is not y or n, ask for a valid option and call the function again
def validate_input_play_again():
    # Ask user to play again
    print(f'Do you want to play again? {options_continue[0]}/{options_continue[1]}\n')
    option = input().lower()
    if option not in options_continue:
        print(f'Please choose {options_continue[0]} or {options_continue[1]}')
        return validate_input_play_again()
    
    return option


# Write 'Welcome rock-paper-scissors game' to the console
print('Welcome rock-paper-scissors game\n')

user_wins = 0
total_games = 0
start = options_continue[0]

while start == options_continue[0]:
    result = start_game()
    total_games += 1
    if result == 'You win':
        user_wins += 1
    start = validate_input_play_again()
    if start == options_continue[1]:
        print('Goodbye\n')
        print('Total games:', total_games)
        print('User wins:', user_wins)