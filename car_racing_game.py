import pygame
import random
import sys
import os

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
YELLOW = (255, 255, 0)

# Game settings
PLAYER_SPEED = 5
OBSTACLE_SPEED = 3
ROAD_SPEED = 2

class PlayerCar:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 60
        self.speed = PLAYER_SPEED
        self.color = BLUE
        
    def draw(self, screen):
        # Draw car body
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        # Draw car details
        pygame.draw.rect(screen, BLACK, (self.x + 5, self.y + 10, 30, 40))
        pygame.draw.rect(screen, WHITE, (self.x + 10, self.y + 15, 20, 30))
        # Draw wheels
        pygame.draw.rect(screen, BLACK, (self.x - 5, self.y + 5, 10, 15))
        pygame.draw.rect(screen, BLACK, (self.x + 35, self.y + 5, 10, 15))
        pygame.draw.rect(screen, BLACK, (self.x - 5, self.y + 40, 10, 15))
        pygame.draw.rect(screen, BLACK, (self.x + 35, self.y + 40, 10, 15))
        
    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 150:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < SCREEN_WIDTH - 190:
            self.x += self.speed
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < SCREEN_HEIGHT - self.height:
            self.y += self.speed
            
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 60
        self.speed = OBSTACLE_SPEED
        self.color = RED
        
    def draw(self, screen):
        # Draw obstacle car
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        # Draw car details
        pygame.draw.rect(screen, BLACK, (self.x + 5, self.y + 10, 30, 40))
        pygame.draw.rect(screen, WHITE, (self.x + 10, self.y + 15, 20, 30))
        # Draw wheels
        pygame.draw.rect(screen, BLACK, (self.x - 5, self.y + 5, 10, 15))
        pygame.draw.rect(screen, BLACK, (self.x + 35, self.y + 5, 10, 15))
        pygame.draw.rect(screen, BLACK, (self.x - 5, self.y + 40, 10, 15))
        pygame.draw.rect(screen, BLACK, (self.x + 35, self.y + 40, 10, 15))
        
    def move(self):
        self.y += self.speed
        
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
        
    def is_off_screen(self):
        return self.y > SCREEN_HEIGHT

class Road:
    def __init__(self):
        self.y = 0
        self.speed = ROAD_SPEED
        self.lane_width = 200
        self.lane_center = SCREEN_WIDTH // 2
        
    def draw(self, screen):
        # Draw road background
        pygame.draw.rect(screen, GRAY, (150, 0, 500, SCREEN_HEIGHT))
        
        # Draw lane markings
        for i in range(0, SCREEN_HEIGHT, 50):
            pygame.draw.rect(screen, YELLOW, (self.lane_center - 2, i + self.y, 4, 30))
            
        # Draw road edges
        pygame.draw.rect(screen, WHITE, (150, 0, 5, SCREEN_HEIGHT))
        pygame.draw.rect(screen, WHITE, (645, 0, 5, SCREEN_HEIGHT))
        
    def move(self):
        self.y += self.speed
        if self.y >= 50:
            self.y = 0

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Car Racing Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.big_font = pygame.font.Font(None, 72)
        
        self.reset_game()
        
    def reset_game(self):
        self.player = PlayerCar(SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT - 100)
        self.obstacles = []
        self.road = Road()
        self.score = 0
        self.game_over = False
        self.paused = False
        
    def spawn_obstacle(self):
        if random.random() < 0.02:  # 2% chance each frame
            lane_positions = [200, 400, 600]  # Three lanes
            x = random.choice(lane_positions)
            obstacle = Obstacle(x, -60)
            self.obstacles.append(obstacle)
            
    def update_obstacles(self):
        for obstacle in self.obstacles[:]:
            obstacle.move()
            if obstacle.is_off_screen():
                self.obstacles.remove(obstacle)
                self.score += 10
                
    def check_collisions(self):
        player_rect = self.player.get_rect()
        for obstacle in self.obstacles:
            if player_rect.colliderect(obstacle.get_rect()):
                self.game_over = True
                
    def draw_ui(self):
        # Draw score
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        # Draw instructions
        instructions = [
            "Use Arrow Keys to move",
            "Avoid red cars",
            "Press P to pause",
            "Press R to restart"
        ]
        
        for i, instruction in enumerate(instructions):
            text = self.font.render(instruction, True, WHITE)
            self.screen.blit(text, (10, 40 + i * 25))
            
    def draw_game_over(self):
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        # Game over text
        game_over_text = self.big_font.render("GAME OVER", True, RED)
        score_text = self.font.render(f"Final Score: {self.score}", True, WHITE)
        restart_text = self.font.render("Press R to restart or Q to quit", True, WHITE)
        
        self.screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, 200))
        self.screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 280))
        self.screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, 320))
        
    def draw_pause(self):
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        # Pause text
        pause_text = self.big_font.render("PAUSED", True, YELLOW)
        resume_text = self.font.render("Press P to resume", True, WHITE)
        
        self.screen.blit(pause_text, (SCREEN_WIDTH // 2 - pause_text.get_width() // 2, 250))
        self.screen.blit(resume_text, (SCREEN_WIDTH // 2 - resume_text.get_width() // 2, 320))
        
    def run(self):
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.reset_game()
                    elif event.key == pygame.K_q and self.game_over:
                        running = False
                    elif event.key == pygame.K_p:
                        self.paused = not self.paused
                        
            if not self.paused and not self.game_over:
                # Update game state
                keys = pygame.key.get_pressed()
                self.player.move(keys)
                self.road.move()
                self.spawn_obstacle()
                self.update_obstacles()
                self.check_collisions()
                
            # Draw everything
            self.screen.fill(GREEN)  # Background
            self.road.draw(self.screen)
            self.player.draw(self.screen)
            
            for obstacle in self.obstacles:
                obstacle.draw(self.screen)
                
            self.draw_ui()
            
            if self.game_over:
                self.draw_game_over()
            elif self.paused:
                self.draw_pause()
                
            pygame.display.flip()
            self.clock.tick(FPS)
            
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run() 