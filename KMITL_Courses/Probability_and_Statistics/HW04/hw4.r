my.empirical_rule_normal <- function(mu, sigma) {
    # generate 10 million normally distributed random numbers
    X <- rnorm(10000000, mu, sigma)
    # proportion of observations within 1 standard deviation of the mean
    SD.1 <- sum(abs(X - mu) < sigma) / length(X)
    # proportion of observations within 2 standard deviations of the mean
    SD.2 <- sum(abs(X - mu) < 2 * sigma) / length(X)
    # proportion of observations within 3 standard deviations of the mean
    SD.3 <- sum(abs(X - mu) < 3 * sigma) / length(X)
    cat("Area (probability) under curve for:",
        "\n68% interval =", SD.1,
        "\n95% interval =", SD.2,
        "\n99.7% interval =", SD.3)
}

my.empirical_rule_normal(0, 1)
