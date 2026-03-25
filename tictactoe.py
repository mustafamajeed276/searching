import random
import pickle
import os

BOARD_SIZE = 9
QFILE = "ttt_qtable.pkl"

class TicTacToeAI:
    def __init__(self, alpha=0.8, gamma=0.9, epsilon=0.6):
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q = {}

        if os.path.exists(QFILE):
            with open(QFILE, "rb") as f:
                self.q = pickle.load(f)

    def get_q(self, state, action):
        return self.q.get((state, action), 0.0)

    def choose_action(self, state, available):
        if random.random() < self.epsilon:
            return random.choice(available)

        qs = [self.get_q(state, a) for a in available]
        max_q = max(qs)
        best = [a for a, q in zip(available, qs) if q == max_q]
        return random.choice(best)

    def learn(self, state, action, reward, next_state, next_available):
        if state is None or action is None:
            return

        prev_q = self.get_q(state, action)
        future_q = max([self.get_q(next_state, a) for a in next_available], default=0)

        new_q = prev_q + self.alpha * (reward + self.gamma * future_q - prev_q)
        self.q[(state, action)] = new_q

    def decay_exploration(self):
        # Reduce randomness each game
        self.epsilon = max(0.05, self.epsilon * 0.85)

    def save(self):
        with open(QFILE, "wb") as f:
            pickle.dump(self.q, f)


class TicTacToe:
    wins = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]

    def __init__(self):
        self.board = [" "] * BOARD_SIZE

    def state(self):
        return "".join(self.board)

    def available(self):
        return [i for i,v in enumerate(self.board) if v == " "]

    def move(self, i, player):
        self.board[i] = player

    def winner(self):
        for a,b,c in self.wins:
            if self.board[a] == self.board[b] == self.board[c] != " ":
                return self.board[a]
        if " " not in self.board:
            return "draw"
        return None

    def display(self):
        b = self.board
        print(f"""
 {b[0]} | {b[1]} | {b[2]}
-----------
 {b[3]} | {b[4]} | {b[5]}
-----------
 {b[6]} | {b[7]} | {b[8]}
""")


def play():
    ai = TicTacToeAI()
    game_count = 0

    while True:
        game_count += 1
        print(f"\nGame #{game_count}")

        game = TicTacToe()
        last_state = None
        last_action = None

        while True:
            game.display()

            try:
                move = int(input("Choose position (0-8): "))
            except ValueError:
                print("Enter number 0-8")
                continue

            if move not in game.available():
                print("Invalid move")
                continue

            game.move(move, "X")

            result = game.winner()
            if result:
                game.display()

                if result == "X":
                    print("You win!")
                    ai.learn(last_state, last_action, -10, game.state(), [])
                elif result == "draw":
                    print("Draw!")
                    ai.learn(last_state, last_action, 2, game.state(), [])

                break

            state = game.state()
            action = ai.choose_action(state, game.available())
            game.move(action, "O")
            next_state = game.state()

            if last_state is not None:
                ai.learn(last_state, last_action, 0, state, game.available())

            last_state = state
            last_action = action

            result = game.winner()

            if result:
                game.display()

                if result == "O":
                    print("AI wins!")
                    ai.learn(state, action, 10, next_state, [])
                elif result == "draw":
                    print("Draw!")
                    ai.learn(state, action, 2, next_state, [])

                break

        ai.decay_exploration()
        ai.save()

        print(f"AI randomness (epsilon): {round(ai.epsilon,3)}")

        again = input("Play again? (y/n): ")
        if again.lower() != "y":
            break


if __name__ == "__main__":
    play()