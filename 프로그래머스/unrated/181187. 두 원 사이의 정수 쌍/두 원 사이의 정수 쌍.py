import math
def solution(r1, r2):
    answer = 0
    return dot_count_in_circle(r2) - dot_count_in_circle(r1) + dot_count_on_circle(r1)

def dot_count_in_circle(r):
    count = 0
    for i in range(r):
        count += int(math.sqrt(r ** 2 - i ** 2))
    return count * 4

def dot_count_on_circle(r):
    count = 0
    for i in range(r):
        if math.sqrt(r ** 2 - i ** 2) == int(math.sqrt(r ** 2 - i ** 2)):
            count += 1
    return count * 4