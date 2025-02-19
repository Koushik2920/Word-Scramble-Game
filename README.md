# Word-Scramble-Game
In this word puzzle game, the letters of a word are scrambled, and the player must guess the original word. The game includes multiple rounds with a predefined list of words. Points are awarded for each correct guess.
💾 Installation & Setup
Option 1: Clone the Repository (Recommended if on GitHub)
Open your terminal or command prompt.
Run the following command:

git clone https://github.com/yourusername/word-scramble-game.git
cd word-scramble-game
Option 2: Download the Script Manually
Click on word_scramble_game.py in the GitHub repository.
Click "Download" or copy the code into a new file called word_scramble_game.py.
Run the Game
After downloading, navigate to the script location and run:

python word_scramble_game.py
🎮 How to Play
The game displays a scrambled word selected from a predefined list.
You must guess the original word based on the scrambled letters.
If your guess is correct, you earn a point.
If your guess is incorrect, the correct word is displayed.
The game continues for multiple rounds, and your total score is displayed at the end.
You can choose to play again or exit after the game ends.
📝 Example Menu (Game Output)

Welcome to the Word Scramble Game!
Unscramble the letters to form a valid word.

Scrambled word: ptnohy
Your guess: python
Correct! Well done.

Scrambled word: rmgepoarmnig
Your guess: programming
Correct! Well done.

Scrambled word: tmcueorp
Your guess: random
Oops! The correct word was: computer.

Game Over! Your total score is: 2/3

Do you want to play again? (yes/no): no
Thank you for playing!
📜 Full Code for Word Scramble Game

import random

# Function to scramble the letters of a given word
def scramble_word(word):
    scrambled = list(word)
    random.shuffle(scrambled)
    return ''.join(scrambled)

# Main function to play the game
def play_word_scramble_game():
    words = ['python', 'computer', 'programming', 'puzzle', 'game', 'random', 'scramble']
    score = 0
    
    print("Welcome to the Word Scramble Game!")
    print("Unscramble the letters to form a valid word.")
    
    for word in words:
        scrambled_word = scramble_word(word)
        print(f"\nScrambled word: {scrambled_word}")
        
        user_guess = input("Your guess: ").lower()
        
        if user_guess == word:
            print("Correct! Well done.")
            score += 1
        else:
            print(f"Oops! The correct word was: {word}")
    
    print(f"\nGame Over! Your total score is: {score}/{len(words)}")
    
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        play_word_scramble_game()
    else:
        print("Thank you for playing!")

# Run the game
if __name__ == "__main__":
    play_word_scramble_game()
    
✨ Possible Enhancements
Different Difficulty Levels (Easy, Medium, Hard with more words)
Leaderboard System (Save high scores in a file)
Timed Mode (Limit time per guess)
GUI Version (Using tkinter or PyQt for a graphical interface)
