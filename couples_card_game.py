import random
import time
import os

class CouplesCardGame:
    def __init__(self):
        self.tiers = {
            "Beginner": {
                "questions": [
                    "What's your partner's favorite color?",
                    "What's your partner's favorite food?",
                    "What's your partner's favorite movie?",
                    "What's your partner's dream vacation destination?",
                    "What's your partner's favorite hobby?",
                    "What's your partner's favorite season?",
                    "What's your partner's favorite music genre?",
                    "What's your partner's favorite animal?",
                    "What's your partner's favorite drink?",
                    "What's your partner's favorite book?"
                ],
                "challenges": [
                    "Hold hands for 30 seconds",
                    "Give each other a compliment",
                    "Share a happy memory together",
                    "Tell each other what you appreciate most",
                    "Share your favorite thing about your partner",
                    "Give each other a hug",
                    "Share a goal you have together",
                    "Tell each other 'I love you'",
                    "Share something you're grateful for",
                    "Give each other a high five"
                ]
            },
            "Intermediate": {
                "questions": [
                    "What's your partner's biggest fear?",
                    "What's your partner's biggest dream?",
                    "What's your partner's most embarrassing moment?",
                    "What's your partner's favorite childhood memory?",
                    "What's your partner's biggest achievement?",
                    "What's your partner's favorite way to relax?",
                    "What's your partner's biggest pet peeve?",
                    "What's your partner's favorite way to spend a weekend?",
                    "What's your partner's biggest strength?",
                    "What's your partner's favorite way to show love?"
                ],
                "challenges": [
                    "Share a secret you've never told anyone",
                    "Tell each other what you'd change about yourselves",
                    "Share your biggest insecurity",
                    "Tell each other what you're most proud of",
                    "Share a time you felt most vulnerable",
                    "Tell each other what you're afraid of",
                    "Share your biggest regret",
                    "Tell each other what you're most excited about",
                    "Share a time you felt most loved",
                    "Tell each other what you're most grateful for"
                ]
            },
            "Advanced": {
                "questions": [
                    "What's your partner's deepest desire?",
                    "What's your partner's biggest regret in life?",
                    "What's your partner's biggest insecurity?",
                    "What's your partner's biggest fear about the future?",
                    "What's your partner's biggest dream for your relationship?",
                    "What's your partner's biggest challenge in life?",
                    "What's your partner's biggest strength in relationships?",
                    "What's your partner's biggest weakness?",
                    "What's your partner's biggest hope for the future?",
                    "What's your partner's biggest lesson learned in life?"
                ],
                "challenges": [
                    "Share your deepest fear about your relationship",
                    "Tell each other what you'd change about your relationship",
                    "Share your biggest relationship insecurity",
                    "Tell each other what you're most afraid of losing",
                    "Share your biggest relationship challenge",
                    "Tell each other what you're most grateful for in your relationship",
                    "Share your biggest relationship goal",
                    "Tell each other what you're most proud of in your relationship",
                    "Share your biggest relationship fear",
                    "Tell each other what you're most excited about in your future together"
                ]
            }
        }
        self.scores = {"Player 1": 0, "Player 2": 0}
        self.current_player = "Player 1"
        self.game_mode = "questions"  # or "challenges"
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def display_welcome(self):
        self.clear_screen()
        print("💕 Welcome to Couples Card Game! 💕")
        print("=" * 50)
        print("A turn-based game to strengthen your relationship")
        print("Choose your tier and answer questions or complete challenges")
        print("=" * 50)
        print()
        
    def choose_tier(self):
        print("Choose your tier:")
        print("1. Beginner - Easy questions and fun challenges")
        print("2. Intermediate - Deeper questions and meaningful challenges")
        print("3. Advanced - Intimate questions and relationship challenges")
        print()
        
        while True:
            choice = input("Enter your choice (1-3): ").strip()
            if choice == "1":
                return "Beginner"
            elif choice == "2":
                return "Intermediate"
            elif choice == "3":
                return "Advanced"
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
                
    def choose_mode(self):
        print("\nChoose game mode:")
        print("1. Questions - Answer questions about each other")
        print("2. Challenges - Complete relationship challenges")
        print("3. Mixed - Both questions and challenges")
        print()
        
        while True:
            choice = input("Enter your choice (1-3): ").strip()
            if choice == "1":
                return "questions"
            elif choice == "2":
                return "challenges"
            elif choice == "3":
                return "mixed"
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
                
    def get_card(self, tier, mode):
        if mode == "mixed":
            mode = random.choice(["questions", "challenges"])
            
        cards = self.tiers[tier][mode]
        return random.choice(cards), mode
        
    def display_card(self, card, mode, tier):
        self.clear_screen()
        print(f"🎴 {tier} Tier - {mode.title()} 🎴")
        print("=" * 50)
        print(f"Current Player: {self.current_player}")
        print(f"Score - Player 1: {self.scores['Player 1']} | Player 2: {self.scores['Player 2']}")
        print("=" * 50)
        print()
        
        if mode == "questions":
            print("❓ Question:")
            print(f"   {card}")
            print()
            print("Instructions:")
            print("- Answer the question about your partner")
            print("- Your partner will rate your answer (1-5 stars)")
            print("- 5 stars = 5 points, 4 stars = 4 points, etc.")
        else:
            print("🎯 Challenge:")
            print(f"   {card}")
            print()
            print("Instructions:")
            print("- Complete the challenge together")
            print("- Both players rate the experience (1-5 stars)")
            print("- Average rating = points for both players")
            
        print()
        input("Press Enter when ready to continue...")
        
    def get_rating(self):
        while True:
            try:
                rating = int(input("Rate the answer/challenge (1-5 stars): "))
                if 1 <= rating <= 5:
                    return rating
                else:
                    print("Please enter a number between 1 and 5.")
            except ValueError:
                print("Please enter a valid number.")
                
    def switch_player(self):
        self.current_player = "Player 2" if self.current_player == "Player 1" else "Player 1"
        
    def display_results(self):
        self.clear_screen()
        print("🏆 Game Results 🏆")
        print("=" * 30)
        print(f"Player 1: {self.scores['Player 1']} points")
        print(f"Player 2: {self.scores['Player 2']} points")
        print()
        
        if self.scores['Player 1'] > self.scores['Player 2']:
            print("🎉 Player 1 wins! 🎉")
        elif self.scores['Player 2'] > self.scores['Player 1']:
            print("🎉 Player 2 wins! 🎉")
        else:
            print("🤝 It's a tie! 🤝")
            
        print()
        print("💕 Remember: The real win is strengthening your relationship! 💕")
        
    def play_round(self, tier, mode):
        card, card_mode = self.get_card(tier, mode)
        self.display_card(card, card_mode, tier)
        
        if card_mode == "questions":
            print(f"\n{self.current_player}, answer the question...")
            input("Press Enter when you've answered...")
            
            print(f"\nPartner, rate {self.current_player}'s answer:")
            rating = self.get_rating()
            self.scores[self.current_player] += rating
            
            print(f"✅ {self.current_player} earned {rating} points!")
            
        else:  # challenges
            print(f"\nBoth players, complete the challenge together...")
            input("Press Enter when you've completed the challenge...")
            
            print(f"\n{self.current_player}, rate the experience:")
            rating1 = self.get_rating()
            
            print(f"\nPartner, rate the experience:")
            rating2 = self.get_rating()
            
            avg_rating = (rating1 + rating2) / 2
            self.scores['Player 1'] += avg_rating
            self.scores['Player 2'] += avg_rating
            
            print(f"✅ Both players earned {avg_rating:.1f} points!")
            
        self.switch_player()
        time.sleep(2)
        
    def run(self):
        self.display_welcome()
        
        # Get player names
        player1_name = input("Enter Player 1's name: ").strip() or "Player 1"
        player2_name = input("Enter Player 2's name: ").strip() or "Player 2"
        
        self.scores = {player1_name: 0, player2_name: 0}
        self.current_player = player1_name
        
        # Choose tier and mode
        tier = self.choose_tier()
        mode = self.choose_mode()
        
        # Get number of rounds
        while True:
            try:
                rounds = int(input("\nHow many rounds would you like to play? (1-10): "))
                if 1 <= rounds <= 10:
                    break
                else:
                    print("Please enter a number between 1 and 10.")
            except ValueError:
                print("Please enter a valid number.")
                
        print(f"\n🎮 Starting {rounds} rounds of {tier} tier {mode} mode!")
        print("Press Enter to begin...")
        input()
        
        # Play rounds
        for round_num in range(1, rounds + 1):
            print(f"\n🔄 Round {round_num}/{rounds}")
            self.play_round(tier, mode)
            
        # Display final results
        self.display_results()
        
        # Ask if they want to play again
        print("\nWould you like to play again? (y/n): ", end="")
        play_again = input().lower().strip()
        
        if play_again in ['y', 'yes']:
            self.__init__()
            self.run()
        else:
            print("\n💕 Thanks for playing! Keep strengthening your relationship! 💕")

if __name__ == "__main__":
    game = CouplesCardGame()
    game.run() 