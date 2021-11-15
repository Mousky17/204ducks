#!/usr/bin/python3

import sys
import operator
import math

def my_usage():
    print("USAGE")
    print("    ./204ducks a")
    print("\nDESCRIPTION")
    print("      a const")


def algo_average(result, time):
    return result * math.exp(-time) + (4 - 3 * result) * math.exp(time * -2) + (2 * result - 4) * math.exp(time * -4)

def average(result):
    f = float(0)
    time = float(0)
    while (time < 100):
        f = f + algo_average(result, time) * time * 0.001
        time = time + 0.001
    min = int(f)
    sec = math.ceil((f - min) * 60)
    print("Average return time: %dm %ds" %(min, sec))
    return f

def algo_deviation(result):
    f = float(0)
    time = float(0)
    while (time < 100):
        f = f + algo_average(result, time) * time * 0.001
        time = time + 0.001
    min = int(f)
    sec = math.ceil((f - min) * 60)
    return f

def deviation(result, max):
    f = float(0)
    time = float(0)
    while (time < 100):
        f = f + algo_average(result, time) * math.pow(time - max, 2)  * 0.001
        time = time + 0.001
    return math.sqrt(f)

def print_deviation(result):
    print("Standard deviation: %.3f" %(deviation(result, algo_deviation(result))))


def algo_time(result, time):
    return -result * math.exp(-time) - (4 - 3 * result) / 2 * math.exp(-2 * time) - (2 * result - 4) / 4 * math.exp(-4 * time)

def time_after(result):
    time = 0.0
    max = 0.50
    f = float(0)
    while (1):
        f = (algo_time(result, time / 60) - algo_time(result, 0))
        if (f >= max):
            break
        time = time + 0.01
    min = int(time) / 60
    sec = int(time) - (min * 60)
    print("Time after which %.d%% of the ducks are back: %dm %02ds" % (max * 100, min, sec))

def time_after_1(result):
    time = 0.0
    max = 0.99
    f = float(0)
    while (1):
        f = (algo_time(result, time / 60) - algo_time(result, 0))
        if (f >= max):
            break
        time = time + 0.01
    min = int(time) / 60
    sec = int(time) - (min * 60)
    print("Time after which %.d%% of the ducks are back: %dm %02ds" % (max * 100, min, sec))


def back(result):
    max = 1
    f = (algo_time(result, max) - algo_time(result, 0)) * 100
    print("Percentage of ducks back after 1 minute: %0.1f%%" %f)
     
def back_1(result):
    max = 2
    f = (algo_time(result, max) - algo_time(result, 0)) * 100
    print("Percentage of ducks back after 2 minute: %0.1f%%" %f)     

def ducks(result):
    average(result)
    print_deviation(result)
    time_after(result)
    time_after_1(result)
    back(result)
    back_1(result)
   


def my_main():
    if (len(sys.argv) > 2 or len(sys.argv) < 2):
        exit(84)
    else:
        try:
            if (sys.argv[1] == "-h"):
                my_usage()
                exit(0)
            a = float(sys.argv[1])
            if (a >= 0 and a <= 2.5):
                ducks(a)
                exit (0)
            else:
                exit (84)
        except ValueError:
            exit(84)


my_main()
    
