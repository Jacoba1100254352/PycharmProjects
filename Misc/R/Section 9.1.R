# Provide data values #
Vertical<-c(8.3,7.2,6.9,7.3,8.7,8.7)
Arrow<-c(4.7,6.1,5.0,5.8,6.6,7.9)
FastT<-c(8.0,8.3,7.6,6.4,8.2,7.7)
dataset0<-data.frame(Vertical,Arrow,FastT)

# Reconstruct the data set #
dataset<-stack(dataset0)
names(dataset)<-c("Stiffness","Method")

# Graphical check of assumptions #
with(dataset, boxplot(Stiffness~Method))

# Obtain ANOVA table #
fit1<-lm(Stiffness~Method, data=dataset)
anova(fit1)

# Obtain CIs #
fit2<-lm(Stiffness~Method-1, data=dataset)
confint(fit2)

# If you need to find the means or variances #
with(dataset, tapply(Stiffness, Method, mean))
with(dataset, mean(Stiffness))
with(dataset, tapply(Stiffness, Method, var))

# If you know the value of a F statistic # 
# and want to find the p value #
pf(7.531,2,15,lower.tail=F)

# If you want to find the critical value #
qf(0.05,2,15,lower.tail=F)


###############################
# An example of no replicates #
###############################
Verti<-c(8.3)
Arr<-c(4.7)
Fast<-c(8.0)
eg0<-data.frame(Verti,Arr,Fast)

# Reconstruct the data set #
eg<-stack(eg0)
names(eg)<-c("Stiff","M")

# Graphical check of assumptions #
with(eg, boxplot(Stiff~M))

# Obtain ANOVA table #
model1<-lm(Stiff~M, data=eg)
anova(model1)
