import pandas as pd
import random

# Set random seed for reproducibility
random.seed(42)

# Number of samples
num_samples = 1000

# Define the questions and response options
questions = [
    "Little interest or pleasure in doing things",
    "Feeling down, depressed, or hopeless",
    "Trouble falling or staying asleep, or sleeping too much",
    "Feeling tired or having little energy",
    "Poor appetite or overeating",
    "Feeling bad about yourself — or that you are a failure or have let yourself or your family down",
    "Trouble concentrating on things, such as reading the newspaper or watching television",
    "Moving or speaking so slowly that other people could have noticed? Or the opposite — being so fidgety or restless that you have been moving around a lot more than usual?",
    "Thoughts that you would be better off dead or of hurting yourself in some way"
]

response_options = [0, 1, 2, 3]

# Create a list to store the data
data = []

# Generate synthetic data
for _ in range(num_samples):
    row = {question: random.choice(response_options) for question in questions}
    data.append(row)

# Create a DataFrame from the list
data_df = pd.DataFrame(data)

# Calculate the total score for each row
data_df["Total Score"] = data_df.sum(axis=1)

# Add interpretation based on the scoring rules
def interpret_score(score):
    if score <= 4:
        return "Minimal depression symptoms"
    elif score <= 9:
        return "Mild depression symptoms"
    elif score <= 14:
        return "Moderate depression symptoms"
    elif score <= 19:
        return "Moderately severe depression symptoms"
    else:
        return "Severe depression symptoms"

data_df["Interpretation"] = data_df["Total Score"].apply(interpret_score)

# Save the generated dataset to a CSV file
data_df.to_csv("depression_dataset.csv", index=False)
