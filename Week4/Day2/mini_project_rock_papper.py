import random

class Player:
    CHOICES = ["rock", "paper", "scissors"]

    def __init__(self, name: str):
        self.name = name
        self.score = 0

    def add_point(self):
        self.score += 1


class HumanPlayer(Player):
    def choose(self) -> str:
        while True:
            choice = input(f"👉 {self.name}, choose (rock, paper, scissors): ").strip().lower()
            if choice in self.CHOICES:
                return choice
            print("⚠️ Invalid choice. Try again.")


class ComputerPlayer(Player):
    def choose(self) -> str:
        choice = random.choice(self.CHOICES)
        print(f"🤖 {self.name} chose: {choice}")
        return choice


class GameEngine:
    RULES = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    def determine_winner(self, move1: str, move2: str) -> str:
        if move1 == move2:
            return "draw"
        elif self.RULES[move1] == move2:
            return "player1"
        else:
            return "player2"


class Game:
    def __init__(self):
        self.player = HumanPlayer("Player")
        self.computer = ComputerPlayer("Bot")
        self.engine = GameEngine()

    def play_round(self):
        print("\n--- NEW ROUND ---")
        p1_choice = self.player.choose()
        p2_choice = self.computer.choose()

        winner = self.engine.determine_winner(p1_choice, p2_choice)

        if winner == "draw":
            print("🤝 It's a draw!")
        elif winner == "player1":
            print(f"🎉 You win this round! {p1_choice.capitalize()} beats {p2_choice}.")
            self.player.add_point()
        else:
            print(f"❌ You lose this round. {p2_choice.capitalize()} beats {p1_choice}.")
            self.computer.add_point()

        print(f"📊 Current score -> {self.player.name}: {self.player.score} | {self.computer.name}: {self.computer.score}")

    def start(self):
        print("🎮 Welcome to Rock, Paper, Scissors!")
        
        while True:
            self.play_round()
            
            again = input("\nDo you want to play another round? (y/n): ").strip().lower()
            if again != 'y':
                print("\n🏁 Thanks for playing. Final score:")
                print(f"🏆 {self.player.name}: {self.player.score} | 🤖 {self.computer.name}: {self.computer.score}")
                break


if __name__ == "__main__":
    game = Game()
    game.start()