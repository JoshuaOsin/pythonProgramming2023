def reverse_string(word):
    reverse = ""
    while len(word) > 0:
        reverse += word[len(word) - 1]
        word = word[:len(word) - 1]
    print(reverse)


reverse_string("Cydeo")


def evenNumbers(max):
    i = 2
    evens = ""
    while i <= max:
        evens += f"{i} "
        i += 2
    print(evens)


def oddNumbers(max):
    i = 1
    odds = ""
    while i <= max:
        odds += f"{i} "
        i += 2
    print(odds)


evenNumbers(100)
oddNumbers(100)
