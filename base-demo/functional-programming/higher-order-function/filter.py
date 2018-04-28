def is_odd(n):
    return n % 2 == 1


my_list = [1, 2, 3, 5, 6, 8, 4, 5]
print('odd filter', my_list, '=', list(filter(is_odd, my_list)))


def is_palindrome(n):
    if n < 10:
        return True
    check_length = int(len(str(n)) / 2)
    # print(str(n)[:check_length], str(n)[check_length + 1:])
    if str(n)[:check_length] == str(n)[check_length + 1:]:
        return True
    return False


is_palindrome(122)


def palindromes():
    n = 0
    while True:
        if is_palindrome(n):
            yield n
        n = n + 1


output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
