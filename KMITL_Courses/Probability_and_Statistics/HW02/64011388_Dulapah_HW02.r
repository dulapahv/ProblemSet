my.Pi <- function(n) {
    # Set the scientific notation precision threshold to 30
    options(scipen = 30)

    # Set the seed for reproducibility
    set.seed(388)

    # Generate n random numbers between 0 and 1
    x <- runif(n, min = 0, max = 1)
    y <- runif(n)

    # Calculate the distance from the origin
    r <- sqrt((x ^ 2) + (y ^ 2))

    # Calculate the number of random points that fall within the circle
    num.circle.dots <- sum(r <= 1)

    # Calculate the number of random points that fall within the square
    num.square.dots <- n

    # Calculate the ratio of the number of dots in the circle and the number
    # of dots in the square
    ratio <- num.circle.dots / num.square.dots

    # Calculate pi
    my.pi <- 4 * ratio

    plot(x, y, col = ifelse(r <= 1, "red", "blue"), asp = 1, pch = 20)
    cat("No. of dots:", n, "\nPi value:", my.pi, "\nDiff. from 3.14159:",
        abs(my.pi - 3.14159), "\n")
}

my.Pi(500000)
my.Pi(1000000)
my.Pi(3000000)
