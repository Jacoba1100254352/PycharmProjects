ans1 <- qf(0.95, 7, 20)
ans2 <- qf(0.99, 2, 5)
ans3 <- 1 - pf(7.46, 5, 7) # p_value_one_tailed
ans4 <- 2 * ans3 # p_value_two_tailed
Day1 <- c(5.0, 4.8, 5.1, 5.1, 4.8, 5.1, 4.8, 4.8, 5.0, 5.2, 4.9, 4.9, 5.0)
Day2 <- c(5.8, 4.7, 4.7, 4.9, 5.1, 4.9, 5.4, 5.3, 5.3, 4.8, 5.7, 5.1, 5.7)
Day3 <- c(6.3, 4.7, 5.1, 5.9, 5.1, 5.9, 4.7, 6.0, 5.3, 4.9, 5.7, 5.3, 5.6)

var_test1 <- var.test(Day2, Day1, alternative = "greater", conf.level = 0.95)
ans6 <- var_test1$statistic
num_groups <- 3
num_observations <- length(Day1) + length(Day2) + length(Day3)

df1 <- num_groups - 1
df2 <- num_observations - num_groups

alpha <- 0.05
ans7 <- qf(1 - alpha, df1, df2, lower.tail = F)


BrandA <- c(34.36, 31.26, 37.36, 28.52, 33.14, 32.74, 34.34, 34.33, 30.95)
BrandB <- c(41.08, 38.22, 39.59, 38.82, 36.24, 37.73, 35.03, 39.22, 34.13, 34.33, 34.98, 29.64, 40.60)
ans9 <- abs(t.test(BrandA, BrandB, var.equal = TRUE)$statistic)

n1 <- length(BrandA)
n2 <- length(BrandB)
ans10 <- n1 + n2 - 2 # D. t20

var_test2 <- var.test(BrandA, BrandB, alternative = "two.sided", conf.level = 0.90)
ans11 <- var_test2$p.value

var_test3 <- var.test(Day3, Day2, alternative = "greater", conf.level = 0.95)
ans13 <- var_test3$statistic

ans14 <- var_test3$p.value
