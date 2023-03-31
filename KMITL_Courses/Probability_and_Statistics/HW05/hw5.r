find_mean_variance <- function(x, Joint) {
    # y = Response time (nearest second)
    y <- c(1, 2, 3, 4)
    # marginal PDF fX(x) = summation of fXY(x,y)
    marginal_pdf <- apply(Joint, 2, sum)
    # conditional PDF fY|x(y) = fXY(x,y) / fX(x)
    conditional_pdf <- Joint[, x] / marginal_pdf[x]
    # calculate mean
    mean <- sum(y * conditional_pdf)
    # calculate variance
    var <- sum((y - mean)^2 * conditional_pdf)
    # print the mean and variance
    cat("E(Y|X =", x, ") =", mean, "\n")
    cat("V(Y|X =", x, ") =", var, "\n")
}

Joint <- matrix(c(0.01, 0.02, 0.25, 0.02, 0.03, 0.2, 0.02, 0.1, 0.05, 0.15, 0.1, 0.05), nrow = 4, ncol = 3, byrow = TRUE)

find_mean_variance(1, Joint)
find_mean_variance(2, Joint)
find_mean_variance(3, Joint)