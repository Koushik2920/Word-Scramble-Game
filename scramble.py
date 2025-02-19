import random

def scramble_word(word):
    scrambled = list(word)
    random.shuffle(scrambled)
    return ''.join(scrambled)

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

if __name__ == "__main__":
    play_word_scramble_game()
