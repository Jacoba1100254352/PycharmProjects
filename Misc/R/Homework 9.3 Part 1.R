# Load the necessary libraries
library(readr)
library(dplyr)

# Set the file path
file_path <- "~/Downloads/_uY-dsuzCnbl.csv"

# Read the CSV file
data <- read_csv(file_path)

# Estimate the mean Sorption at each level of Concentration using dplyr
ans1_3_means <- data %>%
  group_by(Concentration) %>%
  summarise(Mean_Sorption = mean(Sorption))

# Display the estimated means
print(ans1_3_means)

# Estimate the mean Sorption at each treatment combination of Concentration and Ratio using dplyr
ans4_15_means <- data %>%
  group_by(Concentration, Ratio) %>%
  summarise(Mean_Sorption = mean(Sorption))

# Display the estimated means
print(ans4_15_means)
