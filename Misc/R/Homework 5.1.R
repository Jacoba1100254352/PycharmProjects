ans1 <- qnorm(0.975) # 0.05/2 + 0.95 = 0.975
ans2 <- qnorm(0.99) # 0.02/2 + 0.98 = 0.99
ans3 <- qnorm(0.995) # 0.01/2 + 0.99 = 0.995
ans4 <- qnorm(0.9) # 0.1/2 + 0.8 = 0.9
ans5 <- pnorm(2.17) - (1-pnorm(2.17))
ans6 <- pnorm(3.28) - (1-pnorm(3.28))
sd <- 5.1 / sqrt(67)

mean <- 348.2
percent <- 0.90
zscore <- qnorm((1-percent)/2 + percent)
ans7 <- mean - zscore * sd
ans8 <- mean + zscore * sd
zscore <- qnorm(0.975)
ans9 <- mean - zscore * sd
ans10 <- mean + zscore * sd
zscore <- (348.2 - (347.5 + 348.9)/2) / sd
ans11 <- pnorm(zscore) - (1-pnorm(zscore))
sd <- 0.1
mean <- 1.56
percent <- 0.95
zscore <- qnorm((1-percent)/2 + percent)
ans12 <- mean - zscore * sd
ans13 <- mean + zscore * sd
zscore <- (348.2 - (347.5 + 348.9)/2) / sd
ans14 <- pnorm(zscore) - (1-pnorm(zscore))
