#!/usr/bin/env python3

import sys
import math

def formula(u, o, x):
    return ((1 / (o * math.sqrt(2 * math.pi))) * math.exp(-((math.pow((x - u), 2)) / (2 * math.pow(o, 2)))))

def task_a(u, o):
    res = float(0)
    for i in range(0, 201):
        res = formula(u, o, i)
        print("%i %.5f" % (i, res), end='')
        print("")

def task_b(u, o, iqa):
    res = float(0)
    for i in range(0, iqa * 100):
        res = res + formula(u, o, i / 100)
    print("%.1f%% of people have an IQ inferior to %i" % (res, iqa))

def task_c(u, o, iqa, iqb):
    res = float(0)
    for i in range(iqa * 100, iqb * 100):
        res = res + formula(u, o, i / 100)
    print("%.1f%% of people have an IQ between %i and %i" % (res, iqa, iqb))

def is_arg_good(i, n, arg):
    try:
        int(i)
    except:
        print("Err: \"" + i + "\" has to be a Int")
        return 1
    if n == 4:
        if int(arg[3]) >= int(arg[4]):
            print("Err: \"" + i + "\" has to be smaller than IQ2")
            return 1
    if int(i) < 0 or int(i) > 200:
        print("Err: \"" + i + "\" has to be between 0 and 200")
        return 1
    return 0

if len(sys.argv) < 2 or len(sys.argv) > 5:
    print("Err: try -h for help")
    exit(84)
if sys.argv[1] == "-h":
    print('USAGE\n\t./205IQ µ s [IQ1] [IQ2]\n\nDESCRIPTION')
    print('\tµ\tmean')
    print('\ts\tstandard deviation')
    print('\tIQ1\tminimum IQ')
    print('\tIQ2\tmaximum IQ')
    exit(0)
elif len(sys.argv) >= 3 and len(sys.argv) <= 5:
    err = 0
    nbr = list()
    for i in range(1, len(sys.argv)):
        err = err + is_arg_good(sys.argv[i], i, sys.argv)
    if err != 0:
        exit(84)
    for i in range(1, len(sys.argv)):
        nbr.append(int(sys.argv[i]))
    if len(nbr) == 2:
        task_a(nbr[0], nbr[1])
    elif len(nbr) == 3:
        task_b(nbr[0], nbr[1], nbr[2])
    elif len(nbr) == 4:
        task_c(nbr[0], nbr[1], nbr[2], nbr[3])
    exit(0)
else:
    print("Err: try -h for help")
    exit(84)