import json
import random
import re
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set

DATA_DIR = Path(__file__).resolve().parent
HIGHSCORE_FILE = DATA_DIR / "hangman_highscores.json"

WORD_BANK = [
    "algorithm",
    "microcontroller",
    "equilibrium",
    "cryptography",
    "photosynthesis",
    "bioluminescence",
    "subterranean",
    "metamorphosis",
    "antidisestablishmentarianism",
    "rendezvous",
    "symphony",
    "neuroscience",
    "catastrophic",
    "philosophy",
    "telecommunication",
    "quantification",
    "architecture",
    "bibliophile",
    "entrepreneur",
    "topography",
]

ASCII_STATE = [
    "\n\n\n\n\n\n",
    "\n\n\n\n\n____\n",
    " |\n |\n |\n |\n_|___\n",
    " ____\n |  |\n |\n |\n_|___\n",
    " ____\n |  |\n |  O\n |\n_|___\n",
    " ____\n |  |\n |  O\n |  |\n_|___\n",
    " ____\n |  |\n |  O\n | /|\\\n_|___\n",
    " ____\n |  |\n |  O\n | /|\\\n | / \\\n_|___\n",
]


class Difficulty(Enum):
    EASY = (12, 0.5)
    MEDIUM = (9, 0.75)
    HARD = (6, 0.9)

    def __init__(self, lives: int, reveal_ratio: float) -> None:
        self.lives = lives
        self.reveal_ratio = reveal_ratio

    @classmethod
    def from_choice(cls, choice: str) -> "Difficulty":
        normalized = choice.strip().lower()
        if normalized.startswith("e"):
            return cls.EASY
        if normalized.startswith("m"):
            return cls.MEDIUM
        return cls.HARD


@dataclass
class HangmanStats:
    wins: int = 0
    losses: int = 0
    streak: int = 0
    best_streak: int = 0

    def update(self, won: bool) -> None:
        if won:
            self.wins += 1
            self.streak += 1
            self.best_streak = max(self.best_streak, self.streak)
        else:
            self.losses += 1
            self.streak = 0


@dataclass
class HangmanGame:
    word: str
    difficulty: Difficulty
    guessed_letters: Set[str] = field(default_factory=set)
    incorrect_guesses: Set[str] = field(default_factory=set)
    lives_remaining: int = field(init=False)

    def __post_init__(self) -> None:
        self.lives_remaining = self.difficulty.lives

    @property
    def revealed_pattern(self) -> str:
        return " ".join(ch if ch in self.guessed_letters else "_" for ch in self.word)

    @property
    def is_won(self) -> bool:
        return all(ch in self.guessed_letters for ch in self.word)

    @property
    def is_lost(self) -> bool:
        return self.lives_remaining <= 0

    @property
    def score(self) -> int:
        base = len(self.word) * 50
        penalty = len(self.incorrect_guesses) * 10
        bonus = max(0, self.lives_remaining * 15)
        return max(0, base + bonus - penalty)

    def guess(self, char: str) -> str:
        char = char.lower()
        if not self._valid_guess(char):
            return "INVALID"

        if char in self.guessed_letters or char in self.incorrect_guesses:
            return "REPEATED"

        if char in self.word:
            self.guessed_letters.add(char)
            return "CORRECT"

        self.incorrect_guesses.add(char)
        self.lives_remaining -= 1
        return "INCORRECT"

    def _valid_guess(self, char: str) -> bool:
        return bool(re.fullmatch(r"[a-z]", char))

    def hint(self) -> Optional[str]:
        unrevealed = [ch for ch in set(
            self.word) if ch not in self.guessed_letters]
        if not unrevealed:
            return None
        next_letter = sorted(
            unrevealed, key=lambda c: self.word.count(c), reverse=True)[0]
        self.guessed_letters.add(next_letter)
        self.lives_remaining = max(1, self.lives_remaining - 2)
        return next_letter

    def display(self) -> str:
        state_index = min(len(ASCII_STATE) - 1, len(ASCII_STATE) -
                          1 - self.lives_remaining + self.difficulty.lives)
        return "\n".join([ASCII_STATE[state_index], f"Word: {self.revealed_pattern}", f"Lives: {self.lives_remaining}", f"Incorrect: {', '.join(sorted(self.incorrect_guesses)) if self.incorrect_guesses else 'None'}"])


def load_stats() -> Dict[str, HangmanStats]:
    if not HIGHSCORE_FILE.exists():
        return {}
    try:
        raw = json.loads(HIGHSCORE_FILE.read_text(encoding="utf-8"))
        return {key: HangmanStats(**value) for key, value in raw.items()}
    except (json.JSONDecodeError, TypeError):
        return {}


def save_stats(stats: Dict[str, HangmanStats]) -> None:
    HIGHSCORE_FILE.write_text(
        json.dumps({key: data.__dict__ for key,
                   data in stats.items()}, indent=2),
        encoding="utf-8",
    )


def choose_word(difficulty: Difficulty) -> str:
    word_pool = [word for word in WORD_BANK if len(word) >= {
        Difficulty.EASY: 6, Difficulty.MEDIUM: 8, Difficulty.HARD: 10}[difficulty]]
    return random.choice(word_pool)


def select_difficulty() -> Difficulty:
    while True:
        choice = input("Choose difficulty [Easy / Medium / Hard]: ").strip()
        if not choice:
            continue
        try:
            return Difficulty.from_choice(choice)
        except ValueError:
            print("Please choose Easy, Medium, or Hard.")


def request_guess() -> str:
    while True:
        raw = input("Guess a letter or enter '?' for a hint: ").strip().lower()
        if raw == "?":
            return raw
        if len(raw) == 1 and raw.isalpha():
            return raw
        print("Enter exactly one alphabetical character, or '?' for a hint.")


def main() -> None:
    stats = load_stats()
    player_name = input(
        "Enter your name for the scoreboard: ").strip() or "Player"
    difficulty = select_difficulty()
    word = choose_word(difficulty)
    game = HangmanGame(word=word, difficulty=difficulty)

    print("\nStarting advanced Hangman! Guess all letters before you run out of lives. Learn from wrong guesses and use hints wisely.")

    while not (game.is_won or game.is_lost):
        print("\n" + game.display())
        choice = request_guess()
        if choice == "?":
            hint_letter = game.hint()
            if hint_letter:
                print(f"Hint used! Revealed letter: {hint_letter.upper()}")
            else:
                print("No hint available; word already fully revealed.")
            continue

        result = game.guess(choice)
        if result == "INVALID":
            print("Invalid input: only letters are allowed.")
        elif result == "REPEATED":
            print("You already tried that letter.")
        elif result == "CORRECT":
            print(f"Nice! The letter '{choice.upper()}' is in the word.")
        else:
            print(f"Oops! '{choice.upper()}' is not in the word.")

    print("\n" + game.display())
    if game.is_won:
        print(
            f"\nCONGRATULATIONS! You guessed the word '{word.upper()}' and scored {game.score} points.")
    else:
        print(f"\nGAME OVER! The correct word was '{word.upper()}'.")

    player_stats = stats.setdefault(player_name, HangmanStats())
    player_stats.update(game.is_won)
    save_stats(stats)

    print(f"\n{player_name}'s record: {player_stats.wins} wins, {player_stats.losses} losses, best streak {player_stats.best_streak}.")


if __name__ == "__main__":
    main()
