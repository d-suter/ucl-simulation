# UCL Simulation ⚽

This project simulates the knockout stages of the Champions League, starting from the round of 16, running the simulation 10 million times to calculate the probability of each team progressing through each round and ultimately winning the tournament.

## How it works:
- **Initial Draw**: Teams are divided into two pots: group winners (Pot 1) and runners-up (Pot 2). A draw is simulated ensuring teams from the same group or country do not face each other.
- **Match Simulation**: Each match outcome is determined by the world rankings of the teams involved, influenced by a factor `k`.
- **Progress Tracking**: As the simulation runs, each team's progress is recorded at each stage—quarter-finals, semi-finals, finals, and wins.
- **Probability Calculation**: The number of times a team reaches a stage is divided by the total simulations to calculate the percentage.
- **Sorting and Output**: Teams are sorted by their win percentage, and the data is output to `analysis.json`.

## The `k` Factor:
The `k` value in the `get_match_probability` function is a crucial parameter that affects the sensitivity of the match outcome to the ranking difference between teams. A lower `k` value results in a higher chance for upsets, while a higher `k` value increases the predictability in favor of higher-ranked teams.

## Results:
The results are displayed in `analysis.json`, showing the probabilities for each team. Win percentage for each team:
- Manchester City to win: `22.14201%`
- Real Madrid to win: `18.41769%`
- Bayern Munich to win: `16.87564%`
- Arsenal to win: `11.749080000000001%`
- Athletico Madrid to win: `7.986319999999999%`
- Inter Milano to win: `6.79437%`
- PSG to win: `4.36139%`
- Borussia Dortmund to win: `3.44318%`
- RB Leipzig to win: 3.41428`%`
- Barcelona to win: `2.20538%`
- Real Sociedad to win: `1.8589000000000002%`
- SSC Napoli to win: `0.37374999999999997%`
- PSV Eindhoven to win: `0.26029%`
- FC Porto to win: `0.11764%`
- Lazio to win: `7.999999999999999e-05%`
- FC Kobenhavn to win: `0%` 

The results provide insights into the likelihood of each team's success in the Champions League based on their current world rankings and the simulation model.

Global Rankings: https://theanalyst.com/eu/2023/09/who-are-the-best-football-team-in-the-world-opta-power-rankings/