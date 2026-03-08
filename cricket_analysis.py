# Read number of players
n = int(input("Enter number of players: "))
total_strike_rate = 0
total_team_runs = 0
highest_scorer = ""
lowest_scorer = ""
highest_runs = 0
lowest_runs = None
# read player details
for i in range(1, n + 1):
    print(f"\nEnter details of player {i}")
    name = input("Player Name: ")
    runs = int(input("Runs Scored: "))
    balls = int(input("Balls Faced: "))

    # Calculate strike rate
    if balls > 0:
        strike_rate = (runs / balls) * 100
    else:
        strike_rate = 0

    total_strike_rate += strike_rate
    total_team_runs += runs

    # Highest scorer
    if runs > highest_runs:
        highest_runs = runs
        highest_scorer = name

    # Least scorer
    if lowest_runs is None or runs < lowest_runs:
        lowest_runs = runs
        lowest_scorer = name

    # Player classification
    if strike_rate >= 150:
        player_type = "Power Hitter"
    elif strike_rate >= 100:
        player_type = "Balanced Player"
    elif strike_rate >= 50:
        player_type = "Slow Scorer"
    else:
        player_type = "Defence Player"

    print("Strike Rate:", strike_rate)
    print("Player Category:", player_type)

# Team average strike rate
team_avg_strike_rate = total_strike_rate / n

# Team performance classification
if team_avg_strike_rate >= 150:
    team_performance = "Excellent"
elif team_avg_strike_rate >= 110:
    team_performance = "Good"
elif team_avg_strike_rate >= 80:
    team_performance = "Average"
else:
    team_performance = "Poor"

# Final Output
print("\n------ Team Performance Report ------")
print("Total Team Runs:", total_team_runs)
print("Highest Scorer:", highest_scorer, "(", highest_runs, "runs )")
print("Least Scorer:", lowest_scorer, "(", lowest_runs, "runs )")
print("Team Average Strike Rate:", team_avg_strike_rate)
print("Overall Team Performance:", team_performance)