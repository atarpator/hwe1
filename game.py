import random
import re

WORDS = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']

def process_input(letter: str) -> (str, bool):
    valid = False
    letter = letter.lower()[0]
    if letter.isalpha():
        valid = True
    return letter, valid

def check_letter(word: str, letter: str) -> list:
    return [l.start() for l in re.finditer(letter, word)]

def check_win(word: str, guess: list) -> bool:
    if "".join(guess) == word:
        return True
    return False

if __name__ == '__main__':
    
    word = random.choice(WORDS)
    guess = ['_'] * len(word)
    penalty = 0
    
    print('--------------------------------------------')
    print('Игра "Виселица"')
    print('--------------------------------------------')
    print(' ')
    print('(Для выхода нажмите Enter или Ctr+C)')
    print(' ')
    print(f'Отгадайте слово из {len(word)} букв.')
    print('У вас есть право на 4 ошибки')
    print(' ')
    print(f"{' '.join(guess) }")
    print(' ')
    letter = input('Введите букву: ')

    while letter:
        letter, valid = process_input(letter)

        if valid:
            print(' ')
            print(f'Ваша буква: {letter}\n')
            indices = check_letter(word, letter)
            if indices:
                for i in indices:
                    guess[i] = letter
                    print('Такая буква в этом слове есть.')
                    print(f'Штрафных очков: {penalty}')
                    print(' ')
                if check_win(word, guess):
                    print('--------------------------------------------')
                    print(f"Это слово: { ' '.join(guess) }")
                    print(' ')
                    print('Правильно!')
                    print('Вы победили!')
                    break
            else:
                penalty += 1
                print('Такой буквы в этом слове нет.')
                print(f'Штрафных очков: {penalty}')
                print(' ')
                if penalty > 3:
                    print(' ')
                    print('Вы проиграли.')
                    break
                
        print(f"{ ' '.join(guess) }")
        print(' ')
        letter = input('Введите букву:')
        