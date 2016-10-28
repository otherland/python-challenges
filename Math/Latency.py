# Write a procedure, speed_fraction, which takes as its inputs the result of
# a traceroute (in ms) and distance (in km) between two points. It should
# return the speed the data travels as a decimal fraction of the speed of
# light.


def speed_fraction(time, distance):

    sol = 300000 # km per second
    solm = sol / 1000 # km per ms

    latency = distance/time # km per ms
    result = latency / solm
    return result * 2


print(speed_fraction(50,5000))
#>>> 0.666666666667

print(speed_fraction(50,10000))
#>>> 1.33333333333  # Any thoughts about this answer, or these inputs?