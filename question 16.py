print("Stone Paper Scissor Cut Game - First to score 5 wins!")

score_a = 0
score_b = 0

while score_a < 5 and score_b < 5:
    a = input("Player A: ").capitalize().strip()
    b = input("Player B: ").capitalize().strip()

    if a not in ["Stone", "Paper", "Scissor"] or b not in ["Stone", "Paper", "Scissor"]:
        print("Invalid input. Use Stone, Paper, or Scissor.\n")
        continue

    if a == b:
        result = "DRAW"
    elif (a == "Stone" and b == "Scissor") or \
         (a == "Paper" and b == "Stone") or \
         (a == "Scissor" and b == "Paper"):
        result = "Player A wins"
        score_a += 1
    else:
        result = "Player B wins"
        score_b += 1

    print("Result:", result)
    print("Score - Player A:", score_a, "| Player B:", score_b, "\n")

print("Game Over!")
if score_a == 5:
    print("Player A wins the game!")
else:
    print("Player B wins the game!")
