import random 

# conditions true, player wins
# r > s, s> p, p> r
def player_wins(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True


def game():
    # choosing
    user = input("'r' for rock, 'p' for paper, 's' for scissors: ").lower()
    pc = random.choice(['r', 's', 'p'])

    choices = f'You gave {user}, and PC gave {pc}'
    
    # deciding results
    if user == pc:
        return f"{choices}, It's a tie :/"
    if player_wins(user, pc):
        return f"{choices}, You won :)"
    return f"{choices}, You Lost :("
    


print(game())
