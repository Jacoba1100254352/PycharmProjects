if(!require(gmodels)){install.packages("gmodels")}
library(gmodels)


###   Set 1   ###
times <- c(56, 40, 42, 65, 48, 59, 57, 63, 59, 49, 62, 50, 48, 52, 61, 54, 60)

# Calculate the sample mean and standard deviation
sample_mean <- mean(times)
sample_sd <- sd(times)

# Perform the one-sample t-test
H0_mean <- 59
t_test <- t.test(times, alternative = "less", mu = H0_mean)

# Calculate the critical point for the 10% level
alpha <- 0.10
df <- length(times) - 1
critical_point <- qt(alpha, df)

# Calculate the two-sided 90% confidence interval
conf_level <- 0.90
conf_interval <- t.test(times, conf.level = conf_level)$conf.int
print("CI 1")
ci (times, conf.level =conf_level)

# Output the results
print("ANSWER SET 1")
t_test
t_test$statistic
t_test$p.value
critical_point
conf_interval

print("From Page")
x1 <- c(56,40,42,65,48,59,57,63,59,49,62,50,48,52,61,54,60)
t.test(x1, alternative = "less", mu = 59, conf.level = 0.90)


###   Set 2   ###
print("ANSWER SET 2")
# Input the data
fish_oil <- c(8, 12, 9, 14, 2, 0, 0, 7)
standard_oil <- c(-6, 0, 1, 2, -3, -4, 2)

# Perform the two-sample t-test
t_test <- t.test(fish_oil, standard_oil, conf.level = conf_level)

# Calculate the 98% confidence interval for the difference in means
conf_level <- 0.98
conf_interval <- t.test(fish_oil, standard_oil, conf.level = conf_level)$conf.int

print("CI 2")
t.test(fish_oil, standard_oil, alternative = "two.sided", paired = FALSE, var.equal =FALSE, conf.level = conf_level)

# Perform an F-test to compare the variances
f_test <- var.test(fish_oil, standard_oil)

# Output the results
t_test$statistic
t_test$p.value
conf_interval
f_test$statistic
f_test$p.value


###   Set 3   ###
print("ANSWER SET 3")
# Input the data
before_diet <- c(209, 211, 205, 197, 238, 240, 222, 216, 219)
after_diet <- c(199, 208, 197, 203, 240, 229, 212, 217, 203)

# Calculate the differences in cholesterol levels
differences <- before_diet - after_diet

# Perform a paired t-test
t_test <- t.test(differences, alternative = "greater", mu = 0)

# Output the results
t_test$statistic
t_test$p.value

t.test(before_diet, after_diet, alternative = "greater", paired = TRUE)

###   Set 4   ###
print("ANSWER SET 4")
# Input the data
low <- c(7.6, 6.8, 5.8, 6.6, 7.7, 6.0)
moderate <- c(8.1, 9.4, 7.8, 8.9, 8.7, 7.1)
high <- c(8.5, 9.7, 10.1, 7.8, 9.6, 9.5)

# Perform one-way ANOVA
data <- c(low, moderate, high)
groups <- factor(rep(c("low", "moderate", "high"), c(length(low), length(moderate), length(high))))
anova_result <- aov(data ~ groups)

# Fill in the ANOVA table
anova_table <- summary(anova_result)
df_firms <- anova_table[[1]]["groups", "Df"]
df_error <- anova_table[[1]]["Residuals", "Df"]
df_total <- df_firms + df_error
ss_firms <- anova_table[[1]]["groups", "Sum Sq"]
ss_error <- anova_table[[1]]["Residuals", "Sum Sq"]
ss_total <- ss_firms + ss_error
ms_firms <- anova_table[[1]]["groups", "Mean Sq"]
ms_error <- anova_table[[1]]["Residuals", "Mean Sq"]
f_value <- anova_table[[1]]["groups", "F value"]
p_value <- anova_table[[1]]["groups", "Pr(>F)"]

# Calculate the 95% confidence intervals for each level of expenditures
conf_level <- 0.95
conf_interval_low <- t.test(low, conf.level = conf_level)$conf.int
conf_interval_moderate <- t.test(moderate, conf.level = conf_level)$conf.int
conf_interval_high <- t.test(high, conf.level = conf_level)$conf.int

print("CI 2")
ci (low, conf.level =conf_level)
ci (moderate, conf.level =conf_level)
ci (high, conf.level =conf_level)

# Output the results
df_firms
df_error
df_total
ss_error
f_value
p_value
conf_interval_low
conf_interval_moderate
conf_interval_high

# Perform Tukey's HSD test, Q30
tukey_result <- TukeyHSD(anova_result)

# Output the results
tukey_result


###   Set 5   ###
print("ANSWER SET 5")
# Input the data
fertilizer <- factor(rep(c("Low", "Medium", "High"), each = 9))
zone <- factor(rep(c("Southern", "Central", "Northern"), 9))
sap_production <- c(76.2, 80.4, 74.2, 79.4, 87.9, 86.9, 84.5, 85.2, 80.1,
                    87, 95.1, 93, 98.2, 94.7, 96.2, 88.4, 90.4, 92.2,
                    84.2, 87.5, 83.1, 90.3, 89.9, 93.2, 81.4, 84.7, 82.2)

# Perform two-way ANOVA
data <- data.frame(fertilizer, zone, sap_production)
anova_result <- aov(sap_production ~ fertilizer * zone, data)

# Calculate main effects
main_effects <- model.tables(anova_result, type = "effects")
main_effects

# Fill in the ANOVA table
anova_table <- summary(anova_result)
MSE <- anova_table[[1]]["Residuals", "Mean Sq"]
MS_fertilizer <- anova_table[[1]]["fertilizer", "Mean Sq"]
MS_interaction <- anova_table[[1]]["fertilizer:zone", "Mean Sq"]

# Test the hypothesis
test_statistic <- anova_table[[1]]["fertilizer", "F value"]
p_value <- anova_table[[1]]["fertilizer", "Pr(>F)"]

# Output the results
print("Effects")
main_effects
print("MSE")
MSE
MS_fertilizer
MS_interaction
test_statistic
p_value
