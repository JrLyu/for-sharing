?dbinom

x <- seq(0, 100, by = 1)
y <- dbinom(x, 100, 0.6)
barplot(y)

y <- pbinom(x, 100, 0.6) > barplot(y)

# ======
# Say we are doing 10 flips with a fair coin -- i.e., p(head) = 0.5
# =====
## Probability of getting exactly 3 heads
dbinom(x = 3, size = 10, prob = 0.5) # 0.1171875

## Probability of getting 3 or fewer heads (CDF value)
pbinom(q = 3, size = 10, prob = 0.5) # 0.171875

## Which should match the sum/integral of the PMF/PDF from the lower bound of 
## the support to 3
dbinom(x = 0:3, size = 10, prob = 0.5) # [0.0009765625 0.0097656250 0.0439453125 0.1171875000]
sum(dbinom(x = 0:3, size = 10, prob = 0.5)) # 0.171875