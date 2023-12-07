dataset <- c(6.72, 6.78, 6.82, 6.62, 6.66, 6.76, 6.72, 6.62, 6.73, 6.70,
             6.80, 6.78, 6.67, 6.64, 6.78, 6.74, 6.79, 6.72, 6.64, 6.68,
             6.77, 6.79, 6.66, 6.75, 6.77, 6.62, 6.77, 6.74, 6.69, 6.75)
summary <- summary(dataset)
ans3 <- sd(dataset)
ans4 <- var(dataset) # sd(dataset)^2

ans7 <- dbinom(5, 10, 0.2)
ans8 <- dbinom(0, 10, 0.2)
ans9 <- 1 - pbinom(4, 10, 0.2)
ans10 <- pbinom(5, 10, 0.2)
ans11 <- dbinom(10, 10, 0.2)
ans12 <- dpois(3, 7)
ans13 <- 1- ppois(0, 7)
ans14 <- ppois(3, 7)
ans15 <- ppois(3, 7) - dpois(0, 7)
q <- (71 - 72) / (8 / sqrt(36))
ans16 <- 1 - pnorm(q)
ans17 <- pnorm(74, 72, 4/3) - pnorm(70, 72, 4/3)
ans18 <- (70 - 72) / (8 / sqrt(36)) # z = (x - mu) / (sigma / sqrt(n))
ans19 <- qnorm((1-0.8)/2) * (8/sqrt(36)) + 72
ans20 <- qnorm(1 - (1-0.8)/2) * (8/sqrt(36)) + 72
ans21 <- pnorm(18, mean = 20, sd = 3)
ans22 <- 1 - pnorm(26, mean = 20, sd = 3)
ans23 <- pnorm(21, mean = 20, sd = 3) - pnorm(15, mean = 20, sd = 3)
ans24 <- 20 + qnorm(0.05) * 3
ans25 <- 20 + qnorm(0.95) * 3



