# Section 9.3 Sample Code #

# If you haven't installed lsmeans package, 
# you can run the following code to acquire it. 
install.packages("lsmeans")
library(lsmeans)

# Please note that the following code is only for recreating
# the computed results in lesson 9.3 for the game example.
# It may not be proper for other cases. You might need to 
# modify the code in other cases.

fit<-lm(Time~factor(Scheme)*factor(Proximity),data=game)
anova(fit)
lsmeans(fit,"Scheme")
lsmeans(fit,"Proximity")
