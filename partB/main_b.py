from game import Game

game = Game()
print(game.rules_for("rock"))
print(game.rules_for("paper"))
print(game.rules_for("banana"))
print(game.play("scissors", "paper"))
print(game.rules_for("scissors"))
print(f"Score: {game.score()}")
