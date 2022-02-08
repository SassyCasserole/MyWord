from word_gen import generate_words
from input import get_user_input
from compare import compare_guess_with_actual

if __name__ == '__main__':
    words = generate_words()
    actual = words[0]
    print(actual)
    MAX_GUESSES = 5
    for i in range(0, MAX_GUESSES):
        user_input = get_user_input()
        if compare_guess_with_actual(user_input, actual):
            print("SUCCESS! Word is {}.".format(actual))
            exit(0)
    else:
        print("Failure! Actual word is {}".format(actual))

