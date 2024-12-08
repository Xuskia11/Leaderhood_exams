import math

def Flooring_sum(lists):
    return sum(math.floor(i) for i in lists if i > 0)

print(Flooring_sum([-1.5, 2.7, -3.3, 4.8]))