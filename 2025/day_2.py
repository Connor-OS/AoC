TEST = False
in_file = "./resources/day_2_test.txt" if TEST else "./resources/day_2.txt"

# From the internet
def primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1


def check_invalid(ids):
    total = 0
    start, end = ids.split("-")
    start, end = int(start), int(end)
    for i in range(start, end+1):
        string = str(i)
        if len(string)%2 != 0:
            continue
        half = int(len(string)/2)
        if string[:half] == string[half:]:
            total += int(i)
    return total


def check_chunks(i: int):
    # only check splitting the number by prime factors
    p = primes()

    string = str(i)
    while (chunks := next(p)) <= len(string):
        if len(string) % chunks != 0:
            continue

        cut = int(len(string) / chunks)

        if len(set([string[j:j + cut] for j in range(0, len(string), cut)])) == 1:
            return int(i)
    return 0


def check_invalid_2(ids):
    total = 0
    start, end = ids.split("-")
    start, end = int(start), int(end)

    for i in range(start, end+1):
        total += check_chunks(i)
    return total

def question_1():
    """Answer to the first question of the day"""
    answer = 0
    with open(in_file) as f:
        ids = f.read().split(",")

    for id in ids:
        answer += check_invalid(id)

    return answer


def question_2():
    """Answer to the second question of the day"""
    answer = 0
    with open(in_file) as f:
        ids = f.read().split(",")

    for id in ids:
        answer += check_invalid_2(id)

    return answer


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")
