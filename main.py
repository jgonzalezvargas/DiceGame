from library.functions import play, decide_winner

n_of_plays = 9

player_a_score, player_b_score= 0,0
for i in range(n_of_plays):
    print(f"Round {i + 1}")
    player_a_score, player_b_score = play(player_a_score, player_b_score)
    winner = decide_winner(player_a_score, player_b_score, i, n_of_plays)
    if winner != '' and (i+1 != n_of_plays):
        break
print(player_a_score, player_b_score)