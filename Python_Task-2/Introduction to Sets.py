from __future__ import division

def average(array):
    # your code goes here
    array = list(array)
    array = set(array)
    array = list(array)
    avg = sum(array) / len(array)
    return round(avg,3)

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print result