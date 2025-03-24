import pygame
import random

# Initialize Pygame and mixer for sound
pygame.init()
pygame.mixer.init()

# Screen settings
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Plane Crash")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (0, 180, 255)
BUTTON_HOVER_COLOR = (0, 150, 220)

# Load images
bird_img = pygame.image.load("bird.png")
pipe_img = pygame.image.load("pipe.png")
bg_img = pygame.image.load("bg2.jpg")
explosion_img = pygame.image.load("ex3.png")

# Resize images
bird_img = pygame.transform.scale(bird_img, (40, 30))
pipe_img = pygame.transform.scale(pipe_img, (70, 400))
bg_img = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
pipe_img_flipped = pygame.transform.flip(pipe_img, False, True)  # Rotated upper pipe
explosion_img = pygame.transform.scale(
    explosion_img, (50, 50)
)  # Adjust size of explosion

# Load sound
game_over_sound = pygame.mixer.Sound("audio2.mp3")

# Bird settings
bird_x, bird_y = 50, SCREEN_HEIGHT // 2
bird_width, bird_height = bird_img.get_width(), bird_img.get_height()
bird_velocity = 0
gravity = 0.3
jump_strength = -5

# Pipe settings
pipe_gap = 90
pipe_velocity = -3

# Score settings
score = 0
highest_score = 0

# List of pipes
pipes = []

# Button settings
button_rect = pygame.Rect(0, 0, 120, 40)  # Define the button_rect outside the function


# Function to create pipes with random heights
def create_pipe():
    height = random.randint(150, SCREEN_HEIGHT - pipe_gap - 100)
    pipe_top = pygame.Rect(
        SCREEN_WIDTH,
        height - pipe_gap - pipe_img.get_height(),
        pipe_img.get_width(),
        pipe_img.get_height(),
    )
    pipe_bottom = pygame.Rect(
        SCREEN_WIDTH, height, pipe_img.get_width(), SCREEN_HEIGHT - height
    )
    return pipe_top, pipe_bottom, height


# Function to move the bird
def move_bird():
    global bird_y, bird_velocity
    bird_velocity += gravity
    bird_y += bird_velocity


# Function to check for collisions using masks
def check_collision():
    bird_mask = pygame.mask.from_surface(bird_img)
    for pipe_top, pipe_bottom, _ in pipes:
        top_mask = pygame.mask.from_surface(pipe_img_flipped)
        bottom_mask = pygame.mask.from_surface(pipe_img)

        top_offset = (pipe_top.x - bird_x, pipe_top.y - bird_y)
        bottom_offset = (pipe_bottom.x - bird_x, pipe_bottom.y - bird_y)

        if bird_mask.overlap(top_mask, top_offset) or bird_mask.overlap(
            bottom_mask, bottom_offset
        ):
            return True

    if bird_y <= 0 or bird_y >= SCREEN_HEIGHT - bird_height:
        return True

    return False


# Function to show the explosion at the collision point
def show_explosion():
    screen.blit(explosion_img, (bird_x, bird_y))
    pygame.display.flip()
    pygame.time.delay(500)  # Display explosion for 0.5 seconds


# Function to show the game over popup
def show_game_over_popup():
    global highest_score, score
    if score > highest_score:
        highest_score = score

    # Draw popup background
    popup_rect = pygame.Rect(50, 150, SCREEN_WIDTH - 100, 300)
    pygame.draw.rect(screen, BLACK, popup_rect)
    pygame.draw.rect(screen, WHITE, popup_rect, 5)

    font = pygame.font.Font(None, 36)
    game_over_text = font.render("Game Over", True, WHITE)
    score_text = font.render(f"Score: {score}", True, WHITE)
    high_score_text = font.render(f"Highest Score: {highest_score}", True, WHITE)

    # Update button position to be inside popup
    button_rect.center = (popup_rect.centerx, popup_rect.y + 240)

    # Button text and color
    button_font = pygame.font.Font(None, 32)
    button_text = button_font.render("Play Again", True, WHITE)

    # Draw text
    screen.blit(
        game_over_text,
        (popup_rect.centerx - game_over_text.get_width() // 2, popup_rect.y + 20),
    )
    screen.blit(
        score_text,
        (popup_rect.centerx - score_text.get_width() // 2, popup_rect.y + 80),
    )
    screen.blit(
        high_score_text,
        (popup_rect.centerx - high_score_text.get_width() // 2, popup_rect.y + 140),
    )

    # Draw button with hover effect
    mouse_pos = pygame.mouse.get_pos()
    if button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, BUTTON_HOVER_COLOR, button_rect)
    else:
        pygame.draw.rect(screen, BUTTON_COLOR, button_rect)

    screen.blit(
        button_text,
        (button_rect.centerx - button_text.get_width() // 2, button_rect.y + 5),
    )
    pygame.display.flip()


# Function to render the score
def render_score():
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (SCREEN_WIDTH - score_text.get_width() - 10, 10))


# Main game loop
running = True
game_over = False
clock = pygame.time.Clock()
pipe_timer = 0

while running:
    screen.blit(bg_img, (0, 0))  # Fixed background image

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                bird_velocity = jump_strength
            if event.key == pygame.K_r and game_over:
                game_over = False
                bird_y = SCREEN_HEIGHT // 2
                bird_velocity = 0
                pipes = []
                score = 0
                pipe_timer = 0
        if event.type == pygame.MOUSEBUTTONDOWN and game_over:
            if button_rect.collidepoint(event.pos):
                game_over = False
                bird_y = SCREEN_HEIGHT // 2
                bird_velocity = 0
                pipes = []
                score = 0
                pipe_timer = 0

    if not game_over:
        move_bird()
        bird_rect = pygame.Rect(bird_x, bird_y, bird_width, bird_height)
        screen.blit(bird_img, (bird_x, bird_y))

        pipe_timer += 1
        if pipe_timer > 90:
            pipes.append(create_pipe())
            pipe_timer = 0
            score += 1

        for pipe_top, pipe_bottom, _ in pipes:
            pipe_top.x += pipe_velocity
            pipe_bottom.x += pipe_velocity
            screen.blit(pipe_img_flipped, (pipe_top.x, pipe_top.y))
            screen.blit(pipe_img, (pipe_bottom.x, pipe_bottom.y))

        pipes = [pipe for pipe in pipes if pipe[0].x > -pipe_img.get_width()]

        if check_collision():
            game_over = True
            game_over_sound.play()
            show_explosion()  # Show explosion before game-over popup
            show_game_over_popup()

        # Render the real-time score in the top-right corner
        render_score()
    else:
        show_game_over_popup()

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
