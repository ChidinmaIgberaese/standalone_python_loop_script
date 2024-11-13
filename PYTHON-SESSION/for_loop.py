# Below is a code example that uses a for loop to calculate the average score from a list of user scores

# List of user scores
user_scores = [85, 92, 78, 90, 88, 76, 95, 89]

# Calculate the total score
total_score = 0
for score in user_scores:
    total_score += score

# Display the total score
print(f"The total score is: {total_score}")

# Display the number of items in the list
num_items = len(user_scores)
print(f"The number of items in the list is: {num_items}")

# Calculate and display the average score
average_score = total_score / num_items
print(f"The average score is: {average_score}")
