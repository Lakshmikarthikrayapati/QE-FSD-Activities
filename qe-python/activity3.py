p1 = input("player 1: rock,paper,scissor:")
p2 = input("player 2: rock,paper,scissor:")
if p1 == p2:
    print("Tie!")
elif p1 == 'rock' and p2 == 'scissor':
    print("player1 wins!")
elif p1 == 'rock' and p2 == 'paper':
    print("player2 wins!")
elif p1 == 'paper' and p2 == 'rock':
    print("player1 wins!")
elif p1 == 'scissor' and p2 == 'rock':
    print("player2 wins!")
else:
    print("player 2 wins!")