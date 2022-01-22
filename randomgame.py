import random
import sys

print('**** HELLO ****')

try:
    start = int(sys.argv[1])
    end = int(sys.argv[2])
except IndexError as err:
    print('Enter a range of numbers')
    raise err


def guess_the_number(user_guess_num, actual_answer):
    print(actual_answer)
    return actual_answer == user_guess_num


if __name__ == '__main__':
    while True:
        try:
            print("Guess the number: ")
            guessed_num = int(input())
            if start - 1 < guessed_num < end + 1:
                answer = random.randint(start, end)
                if guess_the_number(guessed_num, answer):
                    print("CONGRATULATIONS! YOU GUESSED IT...")
                    break
                else:
                    print('Try Again')
                    continue
            else:
                print(f"Enter a number between {first}~{last}")

        except ValueError:
            print('please enter a number')
            continue
