# Copyright is waived. No warranty is provided. Unrestricted use and modification is permitted.

import math


# f(x) = x
def linear(time, start, end):
    return start + ((end-start) * time)


# f(x) = x^2 * (3 - 2x)
def smooth(time, start, end):
    return start + ((end-start) * time * time * (3 - (2 * time)))


# f(x) = smooth(smooth(x))
def smooth2(time, start, end):
    return smooth(smooth(time, 0, 1), start, end)


# f(x) = smooth(smooth(smooth(x)))
def smooth3(time, start, end):
    return smooth(smooth(smooth(time, 0, 1), 0, 1), start, end)


# f(x) = sine(x * pi/2)
def sine_in(time, start, end):
    return start + ((end-start) * math.sin(time * math.pi/2))


# f(x) = 1 - cos(x * pi/2)
def sine_out(time, start, end):
    return start + ((end-start) * (1 - (math.cos(time * math.pi/2))))


# f(x) = 2x - x^2
def quadratic_in(time, start, end):
    return start + ((end-start) * ((2 * time) - (time * time)))


# f(x) = x^2
def quadratic_out(time, start, end):
    return start + ((end-start) * time * time)


# f(x) = 1 - (1-x)^3
def cubic_in(time, start, end):
    return start + ((end-start) * (1 - (1-time) * (1-time) * (1-time)))


# f(x) = x^3
def cubic_out(time, start, end):
    return start + ((end-start) * time * time * time)


# f(x) = sqrt(1 - (x-1)^2)
def circle_in(time, start, end):
    return start + ((end-start) * math.sqrt(1 - (time-1) * (time-1)))


# f(x) = 1 - sqrt(1 - x^2)
def circle_out(time, start, end):
    return start + ((end-start) * (1 - (math.sqrt(1 - (time * time)))))
