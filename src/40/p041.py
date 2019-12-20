def is_prime_number(n):
    for i in range(2, n - 1):
        if n % i is 0:
            return False
    return True


user_input = int(input())
print(is_prime_number(user_input))
