def solution(ingredient):
    answer, i = 0, 0
    amount = len(ingredient)
    while i < amount:
        if ingredient[i] == 1:
            i, answer, flag = ham(i+1, amount, ingredient, answer) # next indices
        else:
            i += 1
    return answer


def ham(s, max, ingredient, ans):
    hamburger = [2,3,1]
    if s >= max:
        return max, ans, 0

    original_s = s
    i = 0
    while i < 3:
        if s >= max:
            return max, ans, 0
        # Basic case
        if ingredient[s] == hamburger[i]:
            s += 1
            i += 1
        elif ingredient[s] == 1:
            s, ans, flag = ham(s+1, max, ingredient, ans)
            if not flag:
                return s, ans, 0
        else:
            return s, ans, 0

    return s, ans+1, 1