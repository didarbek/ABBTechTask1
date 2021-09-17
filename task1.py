#####  TASK 1 #######

# There are many cars parked in a parking lot. The parking lot is a straight line with a parking spot for every meter.
# There are n cars currently parked and a roofer wants to cover them with a roof. The requirement is that at least k cars are covered by the roof.
# Determine the minimum length of the roof that will cover k cars.

# I have solved this task using Python 3

def carParkingRoof(cars, k):
    cars.sort()
    length = len(cars)
    min_length = float('inf')
    for i in range(length-k+1):
        min_length = min(min_length, cars[i+k-1] - cars[i])
    return min_length+1

print(carParkingRoof([2, 10, 8, 17], 3))