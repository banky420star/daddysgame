import random
import time
import os
import sys

class TextCarGame:
    def __init__(self):
        self.width = 20
        self.height = 15
        self.player_x = self.width // 2
        self.player_y = self.height - 2
        self.obstacles = []
        self.score = 0
        self.game_over = False
        self.speed = 0.1
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def draw_game(self):
        # Create the game board
        board = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        
        # Draw road boundaries
        for y in range(self.height):
            board[y][0] = '|'
            board[y][self.width-1] = '|'
            
        # Draw player car
        if 0 <= self.player_x < self.width and 0 <= self.player_y < self.height:
            board[self.player_y][self.player_x] = '🚗'
            
        # Draw obstacles
        for obstacle in self.obstacles:
            if 0 <= obstacle['x'] < self.width and 0 <= obstacle['y'] < self.height:
                board[obstacle['y']][obstacle['x']] = '🚙'
                
        # Draw the board
        print("\n" + "=" * (self.width + 4))
        for row in board:
            print("| " + "".join(row) + " |")
        print("=" * (self.width + 4))
        
        # Draw UI
        print(f"Score: {self.score}")
        print("Controls: A (left), D (right), Q (quit)")
        print("Avoid the red cars! 🚙")
        
    def spawn_obstacle(self):
        if random.random() < 0.3:  # 30% chance each frame
            x = random.randint(1, self.width - 2)
            self.obstacles.append({'x': x, 'y': 0})
            
    def update_obstacles(self):
        for obstacle in self.obstacles[:]:
            obstacle['y'] += 1
            if obstacle['y'] >= self.height:
                self.obstacles.remove(obstacle)
                self.score += 10
                
    def check_collisions(self):
        for obstacle in self.obstacles:
            if (obstacle['x'] == self.player_x and 
                obstacle['y'] == self.player_y):
                self.game_over = True
                
    def handle_input(self):
        if sys.platform == 'darwin':  # macOS
            import tty
            import termios
            import select
            
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                if select.select([sys.stdin], [], [], 0.1)[0]:
                    char = sys.stdin.read(1)
                    if char.lower() == 'a' and self.player_x > 1:
                        self.player_x -= 1
                    elif char.lower() == 'd' and self.player_x < self.width - 2:
                        self.player_x += 1
                    elif char.lower() == 'q':
                        return False
                return True
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        else:
            # For other platforms, use input() with timeout
            import threading
            import queue
            
            input_queue = queue.Queue()
            
            def get_input():
                try:
                    char = input().lower()
                    input_queue.put(char)
                except:
                    pass
                    
            input_thread = threading.Thread(target=get_input)
            input_thread.daemon = True
            input_thread.start()
            
            try:
                char = input_queue.get(timeout=0.1)
                if char == 'a' and self.player_x > 1:
                    self.player_x -= 1
                elif char == 'd' and self.player_x < self.width - 2:
                    self.player_x += 1
                elif char == 'q':
                    return False
            except queue.Empty:
                pass
            return True
            
    def show_game_over(self):
        self.clear_screen()
        print("\n" + "=" * 40)
        print("           GAME OVER!")
        print(f"         Final Score: {self.score}")
        print("=" * 40)
        print("Press Enter to play again or Q to quit...")
        
    def run(self):
        print("🚗 Welcome to Text Car Racing Game! 🚗")
        print("Press Enter to start...")
        input()
        
        while True:
            if self.game_over:
                self.show_game_over()
                choice = input().lower()
                if choice == 'q':
                    break
                else:
                    self.__init__()  # Reset game
                    continue
                    
            self.clear_screen()
            self.draw_game()
            
            # Handle input
            if not self.handle_input():
                break
                
            # Update game state
            self.spawn_obstacle()
            self.update_obstacles()
            self.check_collisions()
            
            time.sleep(self.speed)
            
        print("\nThanks for playing! 🏁")

if __name__ == "__main__":
    game = TextCarGame()
    game.run() 