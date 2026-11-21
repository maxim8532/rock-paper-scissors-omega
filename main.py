from game import Game

game = Game()
print(game.play("rock", "scissors"))
print(game.play("paper", "scissors"))
print(game.play("paper", "paper"))
print(game.play("rock", "banana"))
print(game.play("paper", "rock"))
print(f"Score: {game.score()}")
