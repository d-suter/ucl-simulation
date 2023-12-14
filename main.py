import json
import random
from collections import defaultdict

def read_teams(file_path):
    with open(file_path, 'r') as file:
        teams_data = json.load(file)
    return teams_data

def get_match_probability(team1_ranking, team2_ranking):
    k = 0.065
    rating_diff = team2_ranking - team1_ranking
    odds = pow(10, k * rating_diff)
    prob = odds / (1 + odds)
    return prob

def simulate_match(team1, team2):
    team1_prob = get_match_probability(team1['world_ranking'], team2['world_ranking'])
    winner = team1 if random.random() < team1_prob else team2
    return winner

def initial_draw(teams_data):
    first_placed_teams = [team['1st'] for team in teams_data.values()]
    second_placed_teams = [team['2nd'] for team in teams_data.values()]
    matches = []

    for _ in range(100):
        random.shuffle(first_placed_teams)
        random.shuffle(second_placed_teams)
        temp_second_placed = second_placed_teams.copy()

        for team1 in first_placed_teams:
            possible_opponents = [team for team in temp_second_placed if team['country'] != team1['country'] and team['group'] != team1['group']]
            if possible_opponents:
                team2 = random.choice(possible_opponents)
                matches.append((team1, team2))
                temp_second_placed.remove(team2)
            else:
                matches = []
                break

        if matches:
            break

    return matches


def knockout_round(matches, progress_tracker, round_name):
    winners = []
    for match in matches:
        winner = simulate_match(match[0], match[1])
        winners.append(winner)
        progress_tracker[winner['name']][round_name] += 1
    return winners

def main():
    teams_data = read_teams('teams.json')
    progress_tracker = defaultdict(lambda: defaultdict(int))

    for _ in range(10000000):
        matches = initial_draw(teams_data)
        side_a_winners = knockout_round(matches[:4], progress_tracker, "quarter_finals")
        side_b_winners = knockout_round(matches[4:], progress_tracker, "quarter_finals")
        side_a_semi_finals_winner = simulate_match(side_a_winners[0], side_a_winners[1])
        side_b_semi_finals_winner = simulate_match(side_b_winners[0], side_b_winners[1])
        progress_tracker[side_a_semi_finals_winner['name']]['semi_finals'] += 1
        progress_tracker[side_b_semi_finals_winner['name']]['semi_finals'] += 1
        
        final_winner = simulate_match(side_a_semi_finals_winner, side_b_semi_finals_winner)
        progress_tracker[side_a_semi_finals_winner['name']]['finals'] += 1
        progress_tracker[side_b_semi_finals_winner['name']]['finals'] += 1
        progress_tracker[final_winner['name']]['win'] += 1

    for team in progress_tracker:
        for stage in progress_tracker[team]:
            progress_tracker[team][stage] = (progress_tracker[team][stage] / 10000000) * 100

    sorted_teams_by_win = sorted(progress_tracker.items(), key=lambda x: x[1]['win'], reverse=True)
    sorted_progress_tracker = {team: stages for team, stages in sorted_teams_by_win}

    with open('analysis.json', 'w') as file:
        json.dump(sorted_progress_tracker, file, indent=4)

if __name__ == "__main__":
    main()
