from tabulate import tabulate

# Define the events and their types
events = {
    "Trivia Quiz": "Academic",
    "Hackathon": "Academic",
    "Spelling Contest": "Academic",
    "Basketball": "Sporting",
    "5-a-side Football": "Sporting"
}

# Initialize an empty dictionary to store team scores
team_scores = {}

# Define a function to calculate the scores for each event
def calculate_event_scores(event_name):
    # Initialize an empty list to store the event scores
    event_scores = []
    print(f"\nEnter {event_name} scores for each team:")

    # Loop through each team and ask for their score for the event
    for i in range(1, 5):
        team_name = input(f"\nEnter team {i} name: ")
        score = int(input(f"Enter {event_name} score for {team_name}: "))
        event_scores.append((team_name, score))

    # Sort the event scores list in descending order
    sorted_scores = sorted(event_scores, key=lambda x: x[1], reverse=True)

    # Calculate the team scores based on the ranking and store in the team scores dictionary
    for i, (team_name, score) in enumerate(sorted_scores[:3]):
        if team_name not in team_scores:
            team_scores[team_name] = 0
        if i == 0:
            team_scores[team_name] += 3
        elif i == 1:
            team_scores[team_name] += 2
        else:
            team_scores[team_name] += 1

# Loop through each event and call the function to calculate the scores
for event_name, event_type in events.items():
    print(f"\n{event_name} ({event_type})")
    calculate_event_scores(event_name)

# Print the final team scores using tabulate
print("\nFinal Team Scores:")
table = []
for team_name, score in team_scores.items():
    table.append([team_name, score])
print(tabulate(table, headers=["Team", "Score"], tablefmt="grid"))

