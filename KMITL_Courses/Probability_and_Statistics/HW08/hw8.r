# Central Limit Theorem (CLT) Proof

# Setting a seed for reproducibility
set.seed(388)

# Creating an empty vector to store sample means
x.bar = numeric(3000)

# Generating a population with a chi-squared distribution
popu.x <- rchisq(n = 700, df = 4)

for (i in 1:3000) {
  # Taking a sample of size 80 with replacement
  samp.x = sample(popu.x, size = 80, replace = TRUE)
  # Calculating the mean of the sample and storing it in the vector
  x.bar[i] = mean(samp.x)
}

# Population distribution
hist(popu.x,
     main = "Population Distribution",
     xlab = "Value",
     ylab = "Frequency")

# Sampling distribution
hist(x.bar,
     main = "Sampling Distribution of the Mean",
     xlab = "Sample Mean",
     ylab = "Frequency")

# Rule1 proof
cat("Population mean:", mean(popu.x), "\n")
cat("Sample mean:", mean(x.bar), "\n")

# Rule2 proof
cat("Population standard deviation:", sd(popu.x), "\n")
cat("Standard error:", sd(popu.x) / sqrt(80), "\n")
cat("Sample standard deviation:", sd(x.bar), "\n")
