# 1
def number_1(starting_index, end_index):
    total = 0
    for k in range(starting_index, end_index+1):
        total += 2 * k

    return total


def number_2(start_index, end_index):
    total = 0
    for k in range(start_index, end_index + 1):
        total += k ** 3
    return total


def number_3(end_index, start_index=1):
    total = 1
    for k in range(start_index, end_index + 1):
        total *= k
    return total


def number_4(start_index, end_index):
    total = 1
    for k in range(start_index, end_index+1):
        total *= (4*(k**2)) / (4*(k**2) - 1)
    return total


def number_5(end_index, start_index=0):
    total = 0
    for k in range(start_index, end_index + 1):
        total += ((-1)**k) / ((2*k) + 1)
    return total


def binomial_coefficient(A, B):
    result = (number_3(A)) / (number_3(B) * (number_3(A-B)))
    return result


def find_bernoulli_number(n):
    if n == 0:
        return 1

    sub_result = 0
    for k in range(0, n):
        sub_result += binomial_coefficient(n+1, k) * find_bernoulli_number(k)

    return (-(1/(n+1))) * sub_result


def bernoulli_polynomial(n, x):
    total = 0
    for k in range(0, n + 1):
        total += binomial_coefficient(n, k) * \
            find_bernoulli_number(k) * (x ** (n - k))
    return total


def faulhabers_formula(power, end_index, start_index=0):
    n = power + 1
    total = (bernoulli_polynomial(n, end_index + 1) -
             find_bernoulli_number(n)) / n
    if start_index > 0:
        total -= (bernoulli_polynomial(n, start_index) -
                  find_bernoulli_number(n)) / n
    return total
