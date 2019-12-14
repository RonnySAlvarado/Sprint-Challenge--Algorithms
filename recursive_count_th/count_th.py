'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # "abcthefthghith"
    # TBC
    # This gives me a good representation of what it looks like
    print(word[1:])
    count = 0
    if len(word) < 2:
        return 0

    elif word[0:2] == 'th':
        count += 1
        return count_th(word[1:]) + count

    else:
        return count_th(word[1:])


print(count_th('hellothesthingth'))
