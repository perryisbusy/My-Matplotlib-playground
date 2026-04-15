import random

def get_computer_choice():
    """Return a random choice for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])

def get_player_choice():
    """Get valid player input."""
    shortcuts = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
    while True:
        choice = input("Enter your choice (r/rock, p/paper, s/scissors): ").lower().strip()
        if choice in shortcuts:
            return shortcuts[choice]
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        print("Invalid choice. Please enter 'rock', 'paper', or 'scissors' (or r, p, s).")

def determine_winner(player, computer):
    """Determine the winner of a single round."""
    if player == computer:
        return "tie"
    
    winning_combinations = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    
    if winning_combinations[player] == computer:
        return "player"
    else:
        return "computer"

def display_round_result(player_choice, computer_choice, result):
    """Display the result of a single round."""
    print(f"\nYou chose: {player_choice.upper()}")
    print(f"Computer chose: {computer_choice.upper()}")
    
    if result == "tie":
        print("It's a TIE!")
    elif result == "player":
        print("🎉 You WIN this round!")
    else:
        print("💻 Computer wins this round.")

def play_game():
    """Main game loop."""
    player_score = 0
    computer_score = 0
    round_number = 0
    
    print("=" * 50)
    print("Welcome to Rock, Paper, Scissors!")
    print("=" * 50)
    
    while True:
        round_number += 1
        print(f"\n--- Round {round_number} ---")
        
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(player_choice, computer_choice)
        
        display_round_result(player_choice, computer_choice, result)
        
        if result == "player":
            player_score += 1
        elif result == "computer":
            computer_score += 1
        
        print(f"\nScore - You: {player_score} | Computer: {computer_score}")
        
        play_again = input("\nDo you want to play another round? (yes/no): ").lower().strip()
        if play_again not in ['yes', 'y']:
            break
    
    # Display final results
    print("\n" + "=" * 50)
    print("GAME OVER!")
    print("=" * 50)
    print(f"Final Score - You: {player_score} | Computer: {computer_score}")
    
    if player_score > computer_score:
        print("🏆 Congratulations! You won the game!")
    elif computer_score > player_score:
        print("😢 The computer won the game.")
    else:
        print("🤝 The game ended in a tie!")
    print("=" * 50)

if __name__ == "__main__":
    play_game()
