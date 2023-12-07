x <- c(3.32, 2.53, 3.45, 2.38, 3.01)

#Sample statistics
xbar <- mean(x)  # sample mean
s <- sd(x)     # sample standard deviation
n <- length(x)       # sample size
alpha <- 0.05 # significance level

# Calculate the t-value
t <- qt(1-alpha/2, df=n-1)

# Calculate the margin of error
me <- t * s / sqrt(n)

# Calculate the confidence interval
ans1_2 <- c(xbar - me, xbar + me)

#Sample statistics
xbar <- mean(x)  # sample mean
s <- sd(x)     # sample standard deviation
n <- length(x)       # sample size
alpha <- 0.02 # significance level

# Calculate the t-value
t <- qt(1-alpha/2, df=n-1)

# Calculate the margin of error
me <- t * s / sqrt(n)

# Calculate the confidence interval
ans3_4 <- c(xbar - me, xbar + me)

#Sample statistics
xbar <- 6.59635  # sample mean
s <- 0.11213     # sample standard deviation
n <- 10       # sample size
alpha <- 0.01 # significance level

# Calculate the t-value
t <- qt(1-alpha/2, df=n-1)

# Calculate the margin of error
me <- t * s / sqrt(n)

# Calculate the confidence interval
ans12_13 <- c(xbar - me, xbar + me)

# Sample statistics
xbar <- 13  # sample mean
s <- 2     # sample standard deviation
n <- 15       # sample size
alpha <- 0.01 # significance level

# Calculate the t-value
t <- qt(1-alpha/2, df=n-1)

# Calculate the margin of error
me <- t * s / sqrt(n)

# Calculate the confidence interval
ans14_15 <- c(xbar - me, xbar + me)

# Sample statistics
xbar <- 2.64  # sample mean
s <- 1.02     # sample standard deviation
n <- 15       # sample size
alpha <- 0.05 # significance level

# Calculate the t-value
t <- qt(1-alpha/2, df=n-1)

# Calculate the margin of error
me <- t * s / sqrt(n)

# Calculate the confidence interval
ans16_17 <- c(xbar - me, xbar + me)
