# Enter your code here. Read input from STDIN. Print output to STDOUT
mu, sig = 500, 80

# sample mean distribution
muS, sigmaS = mu, sig/(100**0.5)

# confidence intervals of sample mean dist
A = mu - (1.96*sigmaS)
B = mu + (1.96*sigmaS)

print(round(A,2))
print(round(B,2))