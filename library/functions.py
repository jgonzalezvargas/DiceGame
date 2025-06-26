from random import randint
from library.print_messages import player_wins_game, print_play, player_wins

def roll_dice():
    return randint(1,6)

def is_loser(player_a_score, player_b_score, i, n):
    loser = min(player_a_score, player_b_score)
    winer = max(player_a_score, player_b_score)
    remaining_rounds = n - (i + 1)
    print("remainig rounds ", remaining_rounds)
    if loser + remaining_rounds < winer:
        return True
    return False

def decide_winner(player_a_score, player_b_score, i, n):
    winner = ''
    if player_a_score > player_b_score:
        winner = "A"
    elif player_a_score < player_b_score:
        winner = "B"
    else:
        print("Tie")
        winner = "AB"
    if i == n-1:    
        player_wins_game(winner)
        return winner 
    
    if is_loser(player_a_score, player_b_score, i, n):
        print(f"Player {winner} won best of {n}")
        return winner
    return ''

def play(player_a_score, player_b_score):
    _ = input("Roll the die")
    #player a plays
    player_a = roll_dice()
    #player b plays
    player_b = roll_dice()
    print_play('A', player_a)
    print_play('B', player_b)
    if player_b == player_a:
        print("Tie, roll again")
        player_a_score, player_b_score = play(player_a_score, player_b_score)
        return player_a_score, player_b_score
    
    if player_a > player_b:
        player_a_score += 1
        player_wins("A")
        
    else:
        player_b_score += 1
        player_wins("B")
    print(f"Scores: Player A: {player_a_score}, Player B: {player_b_score}")
    print()
        
    return player_a_score, player_b_score