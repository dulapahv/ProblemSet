wb <- rweibull(n = 500, shape = 4, scale = 3)
write.csv(data.frame(wb), file = "hw7.csv")