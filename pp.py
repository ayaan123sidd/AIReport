import numpy as np

def logistic_function(x, L, x0, k, lower_limit=0):
   
    return lower_limit + (L - lower_limit) / (1 + np.exp(-k * (x - x0)))

def passing_probability(score):
    
    if score==100:
        return 1.00
    elif score > 80:
        return logistic_function(score, 0.98, 80, 0.28, 0.8)  # L=1, x0=80, k=0.3, lower_limit=0.9
    elif 50 <= score <= 80:
        return logistic_function(score, 0.8, 70, 0.01)  # L=0.7, x0=65, k=0.1
    elif 30 <= score < 50:
        return logistic_function(score, 0.5, 40, 0.1)  # L=0.5, x0=40, k=0.1
    else:
        return logistic_function(score, 0.2, 15, 0.1)  # L=0.2, x0=15, k=0.1

# Example usage:
mock_test_scores = [25, 35, 45, 55, 65, 75, 85, 100]
probabilities = [passing_probability(score) for score in mock_test_scores]
for score, prob in zip(mock_test_scores, probabilities):
    print(f"Mock test score: {score}%, Probability of passing: {prob:.2f}")
