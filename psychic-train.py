import keyboard
import random
import secrets


print("Using psychic powers I will predict the generator chose (0 or 1) ")

def print_green(text):
    print('\033[92m' + text + '\033[0m')

def print_red(text):
    print('\033[91m' + text + '\033[0m')

def on_key_press(event):
    if event.event_type == keyboard.KEY_DOWN:
        try:
            number_mind_thing = int(event.name)
            print("Using psychic powers I will predict the generator chose (0 or 1): ", number_mind_thing)
            guesses = {
                0: 0,
                1: 0
            }

            for _ in range(99):
                random_number = secrets.randbelow(2)
                #random_number = random.randint(0, 1)
                guesses[random_number] += 1

            print_statement = 'Zero: ' + str(guesses[0]) + ' One: '+ str(guesses[1]) + ' = '
            correct_answer = 3
            if guesses[0] > guesses[1]:
                correct_answer = 0
                print_statement += "0 had more guesses."
            elif guesses[1] > guesses[0]:
                correct_answer = 1
                print_statement += "1 had more guesses."
            else:
                print_statement += "Both 0 and 1 had an equal number of guesses."
            print(print_statement)
            if correct_answer == number_mind_thing:
                print_green('You are psychic!')
            else:
                print_red('You are not psychic')
        except ValueError:
            pass

keyboard.on_press(on_key_press)

# Keep the script running
keyboard.wait('esc')
