from random import randint


n_of_plays = 10

def roll_dice():
    return randint(1,6)

def print_play(player, value):
    print(f'Player {player}: {value}')

def decide_winner(player_a_score, player_b_score, i, n):
    winner = ''
    if i == n-1:
        if player_a_score > player_b_score:
            print("Player A wins")
            winner = "A"
            return winner
        elif player_a_score < player_b_score:
            print("Player B wins")
            winner = "B"
            return winner
        else:
            print("Tie")
            winner = "AB"
            return winner
    

def play(player_a_score, player_b_score):
    #player a plays
    player_a = roll_dice()
    #player b plays
    player_b = roll_dice()
    print_play('A', player_a)
    print_play('B', player_b)
    if player_b == player_a:
        print("Empate, tiran de nuevo")
        play()
    
    if player_a > player_b:
        player_a_score += 1
    else:
        player_b_score += 1
    




player_a_score, player_b_score= 0,0
for i in range(n_of_plays):
    play()