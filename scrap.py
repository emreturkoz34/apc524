import functions as F

numbers = [0, 1, 2, 3, 3, 4]

x = F.non_decreasing(numbers)
y = F.strictly_increasing(numbers)


print "Is this a non-decreasing set? :", x
print "Is the set monotonically increasing?: ", y;

