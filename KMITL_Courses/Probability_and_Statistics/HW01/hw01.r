# Function to find the probability of getting "Head" when flip a coin
# n times.

coinflip <- function(n) {
    coin <- c(0, 1)  # Create a vector of 0 (tail) and 1 (head)
    coin <- sample(coin, n, replace = TRUE)  # Randomly sample n times

    # Count the frequency of 1 (Head) in the vector
    # then divide it by number of trials n.
    prob <- sum(coin == 1) / n

    cat("Number of trials:", n, "\nProbability of getting 'Head':", prob,
    "\nThe difference from 0.5:", abs(0.5 - prob), "\n")
}

coinflip(1000)
coinflip(100000)
coinflip(1000000)