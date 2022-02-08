def compare_guess_with_actual(guess, actual):
    if guess == actual:
        return True
    for i, letter in enumerate(guess):
        if letter == actual[i]:
            print("{} is in word and at right position".format(letter))
        elif letter in actual:
            print("{} is in word but at wrong position".format(letter))
        else:
            print("{} not does appear in word.".format(letter))
    return False
