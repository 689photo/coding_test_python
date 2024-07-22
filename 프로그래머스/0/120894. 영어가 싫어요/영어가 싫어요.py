def solution(numbers):
    num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for x, y in enumerate(num):
        if y in numbers:
            numbers = numbers.replace(y, str(x))
    
    return int(numbers)