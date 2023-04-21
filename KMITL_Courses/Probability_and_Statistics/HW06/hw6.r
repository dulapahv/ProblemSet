x <- rnorm(1000, mean = 15, sd = 3)
y <- rchisq(1000, df = 4)

hist(x)
boxplot(x)
qqnorm(x)
qqline(x, col = "red", lwd = 2)

hist(y)
boxplot(y)
qqnorm(y)
qqline(y, col = "blue", lwd = 2)
