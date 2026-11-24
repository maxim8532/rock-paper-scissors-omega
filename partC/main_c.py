from game import Game

game = Game()
print(game.rules_for("rock"))
print(game.rules_for("spock"))
print(game.play("lizard", "spock"))
print(game.play("rock", "spock"))
print(game.play("scissors", "lizard"))
print(f"Score: {game.score()}")