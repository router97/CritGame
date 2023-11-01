# CritGame


# IMPORTS
import random
import time
import json
import pygame
from data.enemy_class_module import Enemy, EnemyBoss
from data.player_class_module import Player
from data.variables import *
from data.constants import *
from data.functions import *
# # #


# IMAGES
icon = pygame.image.load("main/data/image/Walter White.jpg")
# # #


# INIT
pygame.init()
screen = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("CritGame")
pygame.display.set_icon(icon)
pygame.mixer.init()
# # #


# MUSIC
pygame.mixer.music.load("main/data/sounds/boss_loop.wav")
pygame.mixer.music.play(-1)
# # #


# SOUNDS
hit_sound = pygame.mixer.Sound("main/data/sounds/stick.wav")
death_sound = pygame.mixer.Sound("main/data/sounds/slash perc.wav")
# # #


# LOAD
with open("main/data/json/enemy.json", "r") as fl:
    enemies = Enemy.create_from_json(fl)
with open("main/data/json/shop.json", "r") as fl:
    json_shop = json.load(fl)
# # #


# VARIABLES
action = 'game start!'
font_button = pygame.font.SysFont('Comic Sans',35)
text_attack = font_button.render('ATTACK' , True , BLACK)
text_store = font_button.render('STORE' , True , BLACK)
open_store = False
clock = pygame.time.Clock()
playing = True
enemy = enemies[enemy_counter]
player = Player(player_health_base, player_damage_base, player_crit_chance_base, player_money_base)
# # #


# GAME LOOP
while playing:
    
    # # #
    clock.tick(FPS)
    screen.fill(DARK_PURPLE)
    mouse = pygame.mouse.get_pos()
    player.action = ''
    random_int = (random.randint(0, 10))
    # # #
    
    
    # BUTTONS
    
        # Store
    pygame.draw.rect(screen, WHITE,[WIDTH/2+150, HEIGHT-100, 140, 40])
    screen.blit(text_attack, (WIDTH/2+150, HEIGHT-100))
        # # #
    
        # Attack
    pygame.draw.rect(screen, WHITE,[WIDTH/2-300, HEIGHT-100, 140, 40])
    screen.blit(text_store, (WIDTH/2-300, HEIGHT-100))
        # # #
    
    # # #
    
    
    # HEALTH LINE
    pygame.draw.line(screen, GREEN, (10, 100) , (enemy.health/enemy.max_health*200, 100), 30)
    pygame.draw.line(screen, GREEN, (100, HEIGHT-100) , (player.health/player.max_health*240, HEIGHT-100), 15)
    # # #
    
    
    # TEXT
    text_enemy_health = font_button.render(f"{enemy.health}/{enemy.health}", True, RED)
    screen.blit(text_enemy_health, (10, 120))
    
    text_enemy_name = font_button.render(enemy.name, True , RED)
    screen.blit(text_enemy_name, (10, 50))
    
    text_player_health = font_button.render(f"HP={player.health}/{player.max_health}", True, BLACK)
    screen.blit(text_player_health, (100, HEIGHT-150))
    
    text_action = font_button.render(action, True, BLACK)
    screen.blit(text_action, (WIDTH/2-100, 500))
    
    text_money = font_button.render(f"G={player.money}", True, BLACK)
    screen.blit(text_money, (WIDTH/2+150, HEIGHT-150))
    # # #
    
    
    # MENU
    if open_store:
        pygame.draw.rect(screen, WHITE, [50, HEIGHT-500, WIDTH-100, 350])
    # # #
    
    
    # EVENT HANDLER
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if WIDTH/2+150 <= mouse[0] <= WIDTH/2+150+140 and HEIGHT-100 <= mouse[1] <= HEIGHT-100+40:
                
                player.action = 'attack'
                pygame.mixer.Sound.play(hit_sound)
                pygame.draw.rect(screen, GREEN, [WIDTH/2+150, HEIGHT-100, 140, 40])
                screen.blit(text_attack, (WIDTH/2+150+10, HEIGHT-100+4))

            elif WIDTH/2-300 <= mouse[0] <= WIDTH/2-300+140 and HEIGHT-100 <= mouse[1] <= HEIGHT-100+40:
                
                player.action = 'store'
                open_store = not open_store
                pygame.draw.rect(screen, GREEN, [WIDTH/2-300, HEIGHT-100, 140, 40])
                screen.blit(text_store, (WIDTH/2-300+20, HEIGHT-100+4))
    # # #
    
    
    # ATTACKS
    if player.action == 'attack':
        if random_int <= player.crit_chance:
            action = 'Hit'
            enemy.health = attack(enemy.health, player.damage)
        elif random_int in (5, 6, 7):
            action = 'CRITICAL HIT'
            enemy.health = crit_attack(enemy.health, player.damage)
    # # #
    
    
    # # #
    elif player.action[0:3] == 'buy':
        new_values = (buy(player_max_health, player_damage, crit_chance, player_health, player_money, player_max_health_base, player_damage_base))
        player_health, player_max_health, player_mana, player_max_mana, player_damage, crit_chance, player_money = new_values
    # # #
    
    
    # COUNTER ATTACK
    if random_int >= 8 and player.action not in ('s', ''):
        action = 'COUNTER ATTACK'
        player.health = counter_attack(player.health, enemy.damage)
    # # #
    
    
    # ROUND PROGRESSION
    if lose_check(player.health):
        action = '--- You lose! ---'
        playing = False
    elif enemy.health <= 0:
        action = '--- You win! ---'
        player.money, enemy_counter = win(enemy, player, enemy_counter, death_sound)
        if enemy_counter == len(enemies):
            playing = False
        else:
            enemy = enemies[enemy_counter]
    # # #
    
    
    # # #
    pygame.display.update()
    # # #
    
    
# # #