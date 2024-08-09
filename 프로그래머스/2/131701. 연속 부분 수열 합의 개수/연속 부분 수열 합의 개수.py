def solution(elements):
    n = len(elements)
    extended_elements = elements * 2
    sum_set = set()

    for length in range(1, n + 1):
        for start in range(n):
            sum_set.add(sum(extended_elements[start:start + length]))

    return len(sum_set)