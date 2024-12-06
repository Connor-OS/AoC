TEST = False
in_file = "./resources/day_5_test.txt" if TEST else "./resources/day_5.txt"


def file_lines():
    rules, orders = [section.splitlines() for section in open(in_file).read().split("\n\n")]

    rules = [[int(r) for r in rule.split("|")] for rule in rules]
    orders = [[int(o) for o in order.split(",")] for order in orders]
    # return sections
    return rules, orders


def apply_rule(order, rule):
    l, r = rule

    l_index = order.index(l) if l in order else -1
    r_index = order.index(r) if r in order else 10000000
    if l_index > r_index:
        return False
    return True


def apply_all_rules(order, rules):
    for rule in rules:
        if not apply_rule(order, rule):
            return False
    return True


def success(orders, rules):
    successful = [order for order in orders if apply_all_rules(order, rules)]
    unsuccessful = [order for order in orders if not apply_all_rules(order, rules)]

    return successful, unsuccessful


def question_1():
    """Answer to the first question of the day"""
    answer = 0
    rules, orders = file_lines()

    successful, _ = success(orders, rules)

    for s in successful:
        answer += s[int(len(s) / 2)]

    return answer


def fix_order(order, rule):
    l, r = rule

    l_index = order.index(l)
    r_index = order.index(r)

    r = order.pop(r_index)
    order.insert(l_index, r)
    return order


def question_2():
    """Answer to the second question of the day"""
    answer = 0
    rules, orders = file_lines()

    _, unsuccessful = success(orders, rules)

    for u in unsuccessful:
        while not apply_all_rules(u, rules):
            for r in rules:
                if not apply_rule(u, r):
                    u = fix_order(u, r)
        answer += u[int(len(u) / 2)]

    return answer


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")
