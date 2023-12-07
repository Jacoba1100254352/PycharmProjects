# QUESTIONS 2-9
Transferred <- c(1, 0, 2, 0, 3, 1, 0, 1, 2, 0, 2, 0)
Broken <- c(16, 9, 17, 12, 22, 13, 8, 15, 19, 11, 19, 10)

airfreight.model <- lm(Broken~Transferred)
summary(airfreight.model)
airfreight_correlation_coefficient <- cor(Transferred, Broken)
print(airfreight_correlation_coefficient)

conf_interval <- confint(airfreight.model, level = 0.95)
print(conf_interval)

new_data <- data.frame(Transferred = 2)
prediction_interval <- predict(airfreight.model, newdata = new_data, interval = "prediction", level = 0.95)
print(prediction_interval)


# QUESTIONS 10-12
# Sample statistics
sample_mean <- 4.00
sample_sd <- 0.16
sample_size <- 64

# Calculate the standard error
standard_error <- sample_sd / sqrt(sample_size)

# Calculate the 95% confidence interval
error_margin <- qt(0.975, df = sample_size - 1) * standard_error
lower_ci <- sample_mean - error_margin
upper_ci <- sample_mean + error_margin

# 10-11
# Print the confidence interval
cat("95% Confidence Interval: (", lower_ci, ", ", upper_ci, ")\n")

# 12
# Required margin of error
target_error <- 0.02

# Z-score for a 90% confidence interval
z_score <- qnorm(0.95)

# Calculate the required sample size
required_sample_size <- ceiling((z_score * sample_sd / target_error)^2)

# Print the required sample size
cat("Required sample size for a 90% confidence interval: ", required_sample_size, "\n")


# QUESTIONS 13-15
data <- data.frame(
  Fertilizer = factor(rep(c("A", "B", "C"), each = 3)),
  Plot = factor(rep(1:3, times = 3)),
  Yield = c(327, 456, 273, 401, 546, 320, 304, 440, 235)
)

anova_result <- aov(Yield ~ Fertilizer, data = data)
print(summary(anova_result))

# QUESTIONS 16-19
recovery_data <- data.frame(
  A = factor(rep(c(-1, 1), each = 4, times = 2)),
  B = factor(rep(c(-1, 1), each = 2, times = 4)),
  C = factor(rep(c(-1, 1), times = 8)),
  Recovery = c(85, 91, 82, 85, 74, 76, 73, 76,
               89, 95, 82, 85, 77, 82, 74, 76)
)

model <- lm(Recovery ~ A * B * C, data = recovery_data)

anova_result <- anova(model)
print(anova_result)

# 16
print(model$coefficients["A1"])

# 17
print(model$coefficients["A1:B1:C1"])

# 18

# Attempt 2 at QUESTIONS 16-19
recovery_data <- read.csv("~/Downloads/2to3fac_1.csv")
recovery_data$A <- factor(recovery_data$A)
recovery_data$B <- factor(recovery_data$B)
recovery_data$C <- factor(recovery_data$C)
replicate_1_data <- recovery_data[, c("A", "B", "C", "Percent.Recovery.Replicate.1")]
replicate_2_data <- recovery_data[, c("A", "B", "C", "Percent.Recovery.Replicate.2")]
replicate_1_data <- recovery_data[, c("A", "B", "C", "Percent.Recovery.Replicate.1")]
names(replicate_1_data)[4] <- "Recovery"

replicate_2_data <- recovery_data[, c("A", "B", "C", "Percent.Recovery.Replicate.2")]
names(replicate_2_data)[4] <- "Recovery"

combined_data <- rbind(
  cbind(replicate_1_data, Replicate = 1),
  cbind(replicate_2_data, Replicate = 2)
)

recovery_model <- lm(Recovery ~ A * B * C, data = combined_data)
anova_result <- anova(recovery_model)
print(anova_result)
main_effect_A <- recovery_model$coefficients["A1"]
print(main_effect_A)
three_way_interaction <- recovery_model$coefficients["A1:B1:C1"]
print(three_way_interaction)
mse <- anova_result$`Mean Sq`["Residuals"]
print(mse)
additive_model_plausible <- all(anova_result$`Pr(>F)`[5:7] > 0.05)
print(additive_model_plausible)



# Attempt 3 at QUESTIONS 16-19
data <- read.table(text="A,B,C,PercentRecoveryReplicate1,PercentRecoveryReplicate2
-1,-1,-1,56.3,54.58
1,-1,-1,70.1,72.07
-1,1,-1,65.6,63.06
1,1,-1,80.2,78.08
-1,-1,1,50.3,48.59
1,-1,1,65.3,66
-1,1,1,60.53,59.05
1,1,1,70.63,69.68", sep=",", header=TRUE)

# Average the replicates
data$PercentRecovery <- rowMeans(data[, c("PercentRecoveryReplicate1", "PercentRecoveryReplicate2")])

# Perform ANOVA
model <- aov(PercentRecovery ~ A * B * C, data=data)
print(summary(model))
main_effect_A <- (mean(data[data$A == 1, "PercentRecovery"]) - mean(data[data$A == -1, "PercentRecovery"])) / 2
print(main_effect_A)





# Attempt 4 at QUESTIONS 16-19
print("LAST ATTEMPT")
# Read CSV data
csv_data <- "A,B,C,Percent_Recovery_Replicate_1,Percent_Recovery_Replicate_2
-1,-1,-1,56.3,54.58
1,-1,-1,70.1,72.07
-1,1,-1,65.6,63.06
1,1,-1,80.2,78.08
-1,-1,1,50.3,48.59
1,-1,1,65.3,66
-1,1,1,60.53,59.05
1,1,1,70.63,69.68"

data <- read.csv(text = csv_data, header = TRUE)

# Calculate the average percent recovery for each replicate
data$Avg_Percent_Recovery <- (data$Percent_Recovery_Replicate_1 + data$Percent_Recovery_Replicate_2) / 2

# Perform a 2^3 factorial ANOVA
model <- aov(Avg_Percent_Recovery ~ A * B * C, data = data)
print(model)

# Calculate main effect of A
A_effect <- mean(data$Avg_Percent_Recovery[data$A == 1]) - mean(data$Avg_Percent_Recovery[data$A == -1])

# Calculate three-way interaction effect
ABC_interaction <- coef(model)[8]

# Calculate the value of MSE
MSE <- summary(model)[[1]]$Mean[5]


# Check the additive model
model_additive <- aov(Avg_Percent_Recovery ~ A + B + C, data = data)
summary_additive <- summary(model_additive)
print(summary_additive)

# Calculate the p-value for each interaction term
p_AB <- summary_additive[[1]]$Pr[4]
p_AC <- summary_additive[[1]]$Pr[5]
p_BC <- summary_additive[[1]]$Pr[6]

additive_model_plausible <- p_AB > 0.05 & p_AC > 0.05 & p_BC > 0.05

print("Answers")
print(A_effect)
print(ABC_interaction)
print(MSE)
print(additive_model_plausible)




recovery_data <- read.csv("~/Downloads/2to3fac_1.csv")
print(recovery_data)
