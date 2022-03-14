import random

li = ['python', 'java', 'kotlin', 'javascript']
print("H A N G M A N")

def menu():
    menu_choice = input('Type "play" to play the game, "exit" to quit:')
    if menu_choice == "play":
        play()
    if menu_choice == "exit":
        exit()

def play():
    data = random.choice(li)
    data_list = list(data)
    line_data = "-" * len(data)
    line_guess = []
    i = 0
    while True:
        print()
        print(line_data)
        answer = input("Input a letter: ")

        if len(answer) > 1:
            print("You should input a single letter")
            continue
        if "-" in answer:
            print("Please enter a lowercase English letter")
            continue

        if answer in line_data:
            print("You've already guessed this letter")
            continue

        if answer in line_guess:
            print("You've already guessed this letter")
            continue

        if answer.isalpha() is not True:
            print("Please enter a lowercase English letter")
            continue


        if answer.lower() == answer.upper():
            print("Please enter a lowercase English letter")
            continue

        if answer == answer.upper():
            print("Please enter a lowercase English letter")
            continue


        if answer in data:
            for vv in data_list:
                if vv == answer:
                    index_element = data_list.index(answer)
                    data_list[index_element] = "*"
                    line_data = line_data[:index_element] + answer + line_data[index_element + 1:]

        else:
            print("That letter doesn't appear in the word")
            line_guess.append(answer)
            i += 1

        if line_data == data:
            print(data)
            print("You guessed the word!")
            print("You survived!")
            menu()
            break

        if i == 8:
            print("You lost!")
            menu()
            break

menu()
