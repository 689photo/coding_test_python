def solution(numbers, k):
    numbers = (numbers*2)[::2]
    return numbers[(k % len(numbers) - 1)]