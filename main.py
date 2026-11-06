import pygame
import random
import sys
 
pygame.init()
WIDTH, HEIGHT = 1200, 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gold Hunter Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 30)
 
robot_img = pygame.transform.scale(pygame.image.load("robot.png"), (50, 50))
coin_img = pygame.transform.scale(pygame.image.load("coin.png"), (40, 40))
monster_img = pygame.transform.scale(pygame.image.load("monster.png"), (50, 50))
door_img = pygame.transform.scale(pygame.image.load("door.png"), (60, 60))
 
 
robot_pos = pygame.Rect(100, 100, 50, 50)
robot_dir = [0, 0]
coin_pos = pygame.Rect(random.randint(50, WIDTH - 90), random.randint(50, HEIGHT - 90), 40, 40)
door_pos = pygame.Rect(random.randint(50, WIDTH - 90), random.randint(50, HEIGHT - 90), 60, 60)
monsters = []
score = 0
game_over = False
game_won = False
show_coin = True
monster_speed = 3
 
 
EASY, MEDIUM, HARD = 2, 4, 6
NAVY_GREY = (60, 60, 80)
 
def draw_start_menu():
    screen.fill(NAVY_GREY)
    welcome = font.render("Welcome to Gold Hunter Game!", True, (0, 255, 255))
    start = font.render("Choose difficulty:", True, (255, 255, 255))
    easy = font.render("1 - Easy", True, (0, 255, 0))
    medium = font.render("2 - Medium", True, (255, 165, 0))
    hard = font.render("3 - Hard", True, (255, 0, 0))
 
    screen.blit(welcome, (WIDTH//2 - welcome.get_width()//2, 100))
    screen.blit(start, (WIDTH//2 - start.get_width()//2, 200))
    screen.blit(easy, (WIDTH//2 - easy.get_width()//2, 260))
    screen.blit(medium, (WIDTH//2 - medium.get_width()//2, 300))
    screen.blit(hard, (WIDTH//2 - hard.get_width()//2, 340))
    pygame.display.flip()
 
def setup_difficulty(monster_count):
    global monsters, monster_speed
    speed = {EASY: 2, MEDIUM: 3, HARD: 4}[monster_count]
    monster_speed = speed
    monsters = [
        {"rect": pygame.Rect(random.randint(50, WIDTH - 100), random.randint(50, HEIGHT - 100), 50, 50),
         "dir": [random.choice([-speed, speed]), random.choice([-speed, speed])]} for _ in range(monster_count)
    ]
 
def draw_game():
    screen.fill(NAVY_GREY)
    pygame.draw.rect(screen, (200, 0, 0), (0, 0, WIDTH, 10))
    pygame.draw.rect(screen, (200, 0, 0), (0, 0, 10, HEIGHT))
    pygame.draw.rect(screen, (200, 0, 0), (0, HEIGHT - 10, WIDTH, 10))
    pygame.draw.rect(screen, (200, 0, 0), (WIDTH - 10, 0, 10, HEIGHT))
    screen.blit(robot_img, robot_pos)
    if show_coin:
        screen.blit(coin_img, coin_pos)
    for m in monsters:
        screen.blit(monster_img, m["rect"])
    if score >= 10:
        screen.blit(door_img, door_pos)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
 
def move_robot():
    global robot_pos
    next_pos = robot_pos.move(robot_dir[0], robot_dir[1])
    if next_pos.left >= 10 and next_pos.right <= WIDTH - 10 and next_pos.top >= 10 and next_pos.bottom <= HEIGHT - 10:
        robot_pos = next_pos
 
def move_monsters():
    for m in monsters:
        m["rect"].x += m["dir"][0]
        m["rect"].y += m["dir"][1]
        if m["rect"].left <= 10 or m["rect"].right >= WIDTH - 10:
            m["dir"][0] *= -1
        if m["rect"].top <= 10 or m["rect"].bottom >= HEIGHT - 10:
            m["dir"][1] *= -1
 
def check_collisions():
    global score, coin_pos, game_over, game_won, show_coin
    if show_coin and robot_pos.colliderect(coin_pos):
        score += 1
        if score < 10:
            coin_pos.x = random.randint(50, WIDTH - 90)
            coin_pos.y = random.randint(50, HEIGHT - 90)
        else:
            show_coin = False
    for m in monsters:
        if robot_pos.colliderect(m["rect"]):
            game_over = True
    if score >= 10 and robot_pos.colliderect(door_pos):
        game_won = True
 
def draw_buttons():
    restart_btn = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 40, 200, 50)
    exit_btn = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 110, 200, 50)
    pygame.draw.rect(screen, (70, 70, 70), restart_btn)
    pygame.draw.rect(screen, (70, 70, 70), exit_btn)
    restart_text = font.render("Restart", True, (255, 255, 255))
    exit_text = font.render("Exit", True, (255, 255, 255))
    screen.blit(restart_text, (restart_btn.x + 50, restart_btn.y + 10))
    screen.blit(exit_text, (exit_btn.x + 70, exit_btn.y + 10))
    return restart_btn, exit_btn
 
def show_end_screen(message):
    screen.fill(NAVY_GREY)
    text = font.render(message, True, (255, 0, 0))
    final = font.render(f"Final Score: {score}", True, (255, 255, 255))
    screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2 - 80))
    screen.blit(final, (WIDTH // 2 - 120, HEIGHT // 2 - 40))
    restart_btn, exit_btn = draw_buttons()
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_btn.collidepoint(event.pos):
                    reset_game()
                    return
                elif exit_btn.collidepoint(event.pos):
                    pygame.quit(); sys.exit()
 
def reset_game():
    global robot_pos, coin_pos, monsters, door_pos, score, game_over, game_won, robot_dir, show_coin
    robot_pos.x, robot_pos.y = 100, 100
    robot_dir = [0, 0]
    coin_pos.x, coin_pos.y = random.randint(50, WIDTH - 90), random.randint(50, HEIGHT - 90)
    door_pos.x, door_pos.y = random.randint(50, WIDTH - 90), random.randint(50, HEIGHT - 90)
    score = 0
    game_over = False
    game_won = False
    show_coin = True
    main()
 
def main_game():
    global robot_dir, game_over, game_won
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    robot_dir = [-5, 0]
                elif event.key == pygame.K_RIGHT:
                    robot_dir = [5, 0]
                elif event.key == pygame.K_UP:
                    robot_dir = [0, -5]
                elif event.key == pygame.K_DOWN:
                    robot_dir = [0, 5]
        if not game_over and not game_won:
            move_robot()
            move_monsters()
            check_collisions()
            draw_game()
        elif game_over:
            show_end_screen("Game Over!")
            break
        elif game_won:
            show_end_screen("You Win!")
            break
        pygame.display.flip()
        clock.tick(60)
 
def main():
    while True:
        draw_start_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    setup_difficulty(EASY)
                    main_game()
                    return
                elif event.key == pygame.K_2:
                    setup_difficulty(MEDIUM)
                    main_game()
                    return
                elif event.key == pygame.K_3:
                    setup_difficulty(HARD)
                    main_game()
                    return
 
if __name__ == "__main__":
    main()
 