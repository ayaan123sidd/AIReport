def calculate_passing_probability(score):
    if score > 80:
        return 0.9 + ((score - 80) / 20) * 0.1 
    elif score >= 50:
        return 0.7 + ((score - 50) / 30) * 0.2
    elif score >= 30:
        return 0.5 + ((score - 30) / 20) * 0.2
    elif score >= 25:
        return 0.3 + ((score - 25) / 5) * 0.2  
    elif score >= 10:
        return 0.1 + ((score - 10) / 15) * 0.2 
    else:
        return (score / 10) * 0.1 

scores = [95, 75, 65, 35, 25,78.0,9]
probabilities = [calculate_passing_probability(score) for score in scores]

for score, probability in zip(scores, probabilities):
    print(f"Score: {score}% -> Passing Probability: {probability:.2f}")
