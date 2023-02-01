my.Binomial <- function(x, n, p) {
  # Set the scientific notation precision threshold to 30
  options(scipen = 30)

  # Create a sequence of x values from 0 to n
  x <- seq(0, n)

  # Calculate the probability for each x value
  x.fx <- dbinom(x, n, p)

  # Loop through the x values and print the probability for each one
  for (i in seq_along(x)) {
    cat("P(X = ", x[i], ") = ", x.fx[i], "\n", sep = "")
  }

  # Calculate the mean, variance and standard deviation
  EX <- sum(x * x.fx)
  Var <- sum((x ^ 2) * x.fx) - (EX ^ 2)
  SD <- sqrt(Var)

  # Print the mean, variance and standard deviation
  cat("Mean:", EX, "\nVariance:", Var, "\nStandard Deviation:", SD, "\n")

  # Plot the y values as a bar chart and highlight the selected x value
  barplot(x.fx, names.arg = x, col = "lightseagreen", xlab = "x", ylab = "P(X = x)")
}

my.Binomial(2, 4, 0.1)
