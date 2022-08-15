# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

x = float(input())
stu = float(input())
mu = stu * float(input())
sig = math.sqrt(stu) * float(input())

print(round(0.5*(1+math.erf((x - mu)/(sig * math.sqrt(2)))),4))