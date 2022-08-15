# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
x = list(map(float,input().split()))
y = list(map(float,input().split()))

mu_x = sum(x) / n
mu_y = sum(y) / n
sd_x = (sum([(i - mu_x)**2 for i in x]) / n)**0.5
sd_y = (sum([(i - mu_y)**2 for i in y]) / n)**0.5

cov = sum([(x[i] - mu_x) * (y[i] - mu_y) for i in range(n)])
p_corr_coef = cov / (n * sd_x * sd_y)

print(round(p_corr_coef,3))