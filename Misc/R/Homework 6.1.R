xbar <- 0.595
mu <- 0.6
s <- 0.05
n <- 65

ans1 <- (xbar - mu) / (s / sqrt(n))
ans2 <- pt(ans1, df = n-1)
ans3 <- ans2*100

xbar <- 15.2
mu <- 15
s <- 1.8
n <- 87

ans5 <- (xbar - mu) / (s / sqrt(n))
ans6 <- (1-pt(ans5, df = n-1)) * 2 # pnorm(ans5, lower.tail = FALSE) * 2

xbar <- 73.2461
mu <- 73.6
s <- 2.3634
n <- 145
percent <- 0.99

ans10 <- pnorm(((xbar - mu) / (s / sqrt(n))))
ans11_12 <- xbar + c(-1,1) * qt((1-percent)/2 + percent, df = n-1) * (s / sqrt(n))

ans13 <- 1 - pnorm(2.24) # pval
ans15 <- 2 * (1 - pnorm(abs(2.24))) # pval

