cond_mean_var <- function(X, Joint){
  # Extract the marginal of X
  marginal_X <- rowSums(Joint)
  # Extract the marginal of Y
  marginal_Y <- colSums(Joint)
  # Extract the conditional probability of Y given X
  cond_prob <- Joint/marginal_X
  # Compute the Mean of Y given X
  cond_mean <- cond_prob %*% marginal_Y
  # Compute the variance of Y given X
  cond_var <- (cond_prob^2 %*% marginal_Y) - (cond_mean^2)
  # Print the results
  cat("Mean of Y given X =", X, "is", cond_mean[X],
  "and the variance is", cond_var[X], " \n")
}


Joint = matrix(c(0.01,0.02,0.25,0.02,0.03,0.20,0.02,0.10,0.05,0.15,0.10,0.05),nrow=4,ncol=3)


# Test function
cond_mean_var(1, Joint)