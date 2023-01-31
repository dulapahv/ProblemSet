my.Binomial <- function(x, n, p) {
  # Set the scientific notation precision threshold to 30
  options(scipen = 30)

  # Save x value later for coloring the selected bar graph
  selected <- x

  # Create a vector of the x values
  x <- 0:n

  # Create a vector of the y values
  # Can also use built-in dbinom(x, n, p) function to calculate
  y <- (factorial(n) / (factorial(x) * factorial(n - x))) * (p ^ x) * ((1 - p) ^ (n - x))

  # Loop through the x values and print the probability for each one
  for (i in seq_along(x)) {
    cat("P(X = ", x[i], ") = ", y[i], "\n", sep = "")
  }

  # Calculate the mean, variance and standard deviation
  mean <- n * p
  variance <- n * p * (1 - p)
  sd <- sqrt(variance)

  # Print the mean, variance and standard deviation
  cat("Mean:", mean, "\nVariance:", variance, "\nStandard Deviation:", sd, "\n")

  # Plot the y values as a bar chart and highlight the selected x value
  barplot(y, names.arg = x, col = ifelse(x == selected, "#fa9398", "#219796"), xlab = "x", ylab = "P(X=x)")
}

my.Binomial(2, 4, 0.1)
