from datetime import datetime

import data.entities as e
import data.text as text
import math
import os
import pygame
import random
import socket
import sys
import time
import json

from pygame.locals import *

# Окно и всякие ненужные константы
mainClock = pygame.time.Clock()

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.set_num_channels(32)
pygame.display.set_caption('Название потом придумаем')
window_width = 720
window_height = 405
screen = pygame.display.set_mode((window_width, window_height), 0, 32)
display = pygame.Surface((240, 135))


# Шрифт
def get_text_width(text, spacing):
    global font_dat
    width = 0
    for char in text:
        if char in font_dat:
            width += font_dat[char][0] + spacing
        elif char == ' ':
            width += font_dat['A'][0] + spacing
    return width


def paused():
    global current_level, entities, message_queue, level_messages

    pause = True
    timer = 0

    paused_text = pygame.image.load('data/images/paused_text.png').convert()
    paused_text.set_colorkey((255, 255, 255))

    plashka = pygame.image.load('data/images/plashka.png').convert()
    plashka.set_colorkey((255, 255, 255))

    n = 0
    py = 44
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause = False
                if event.key == pygame.K_q:
                    terminate()
                if event.key == pygame.K_w:
                    n -= 1
                if event.key == pygame.K_s:
                    n += 1
                if event.key == pygame.K_SPACE:
                    if n == 0:
                        pause = False
                    elif n == 1:
                        for entity in entities:
                            if entity.type not in ['player']:
                                entity.entity_data['health'] = 0

                        with open("save.json", "w") as data:
                            data.write(json.dumps({"current_level": current_level}, ensure_ascii=False))

                        pause = False
                        fade_in = 10
                        message_queue = [level_messages[current_level], 0, 0]
                        current_level = 0
                        load_level(entities, current_level)

                        if fade_in > 0:
                            fade_in -= 1
                            black_surf = pygame.Surface((240, 135))
                            black_surf.set_alpha(int(255 * fade_in / 10))
                            display.blit(black_surf, (0, 0))
                    elif n == 2:
                        terminate()

        if n == 0:
            py = 44
            continue_text = pygame.image.load('data/images/continue_text_2.png').convert()
            continue_text.set_colorkey((255, 255, 255))
            main_menu_text = pygame.image.load('data/images/main_menu_text_1.png').convert()
            main_menu_text.set_colorkey((255, 255, 255))
            exit_text = pygame.image.load('data/images/exit_text_1.png').convert()
            exit_text.set_colorkey((255, 255, 255))
        elif n == 1:
            py = 59
            continue_text = pygame.image.load('data/images/continue_text_1.png').convert()
            continue_text.set_colorkey((255, 255, 255))
            main_menu_text = pygame.image.load('data/images/main_menu_text_2.png').convert()
            main_menu_text.set_colorkey((255, 255, 255))
            exit_text = pygame.image.load('data/images/exit_text_1.png').convert()
            exit_text.set_colorkey((255, 255, 255))
        elif n == 2:
            py = 74
            continue_text = pygame.image.load('data/images/continue_text_1.png').convert()
            continue_text.set_colorkey((255, 255, 255))
            main_menu_text = pygame.image.load('data/images/main_menu_text_1.png').convert()
            main_menu_text.set_colorkey((255, 255, 255))
            exit_text = pygame.image.load('data/images/exit_text_2.png').convert()
            exit_text.set_colorkey((255, 255, 255))
        elif n > 2:
            n = 0
        elif n < 0:
            n = 2

        timer += 1
        if timer > 20:
            timer = 20
        black_surf_text = pygame.Surface((240, 135))
        black_surf_text.fill(pygame.color.Color(20, 12, 28))
        black_surf_text.set_alpha(int(timer * 12.75))
        display.blit(black_surf_text, (0, 0))

        display.blit(paused_text, (5, 10))

        display.blit(plashka, (0, py))

        display.blit(continue_text, (5, 45))
        display.blit(main_menu_text, (5, 60))
        display.blit(exit_text, (5, 75))

        pygame.display.update()
        screen.blit(pygame.transform.scale(display, (window_width, window_height)), (0, 0))
        mainClock.tick(60)


def terminate():
    pygame.quit()
    sys.exit()


font_dat = {'A': [3], 'B': [3], 'C': [3], 'D': [3], 'E': [3], 'F': [3], 'G': [3], 'H': [3], 'I': [3], 'J': [3],
            'K': [3], 'L': [3], 'M': [5], 'N': [3], 'O': [3], 'P': [3], 'Q': [3], 'R': [3], 'S': [3], 'T': [3],
            'U': [3], 'V': [3], 'W': [5], 'X': [3], 'Y': [3], 'Z': [3],
            'a': [3], 'b': [3], 'c': [3], 'd': [3], 'e': [3], 'f': [3], 'g': [3], 'h': [3], 'i': [1], 'j': [2],
            'k': [3], 'l': [3], 'm': [5], 'n': [3], 'o': [3], 'p': [3], 'q': [3], 'r': [2], 's': [3], 't': [3],
            'u': [3], 'v': [3], 'w': [5], 'x': [3], 'y': [3], 'z': [3],
            '.': [1], '-': [3], ',': [2], ':': [1], '+': [3], '\'': [1], '!': [1], '?': [3],
            '0': [3], '1': [3], '2': [3], '3': [3], '4': [3], '5': [3], '6': [3], '7': [3], '8': [3], '9': [3],
            '(': [2], ')': [2], '/': [3], '_': [5], '=': [3], '\\': [3], '[': [2], ']': [2], '*': [3], '"': [3],
            '<': [3], '>': [3], ';': [1], '%': [5]}

font_white = text.generate_font('data/font/small_font.png', font_dat, 5, 8, (248, 248, 248))
font_gold = text.generate_font('data/font/small_font.png', font_dat, 5, 8, (247, 172, 55))
font_brown = text.generate_font('data/font/small_font.png', font_dat, 5, 8, (70, 33, 31))
font_blue = text.generate_font('data/font/small_font.png', font_dat, 5, 8, (15, 77, 163))
# Картиночки враговБ игрока, окружения
heart_img = pygame.image.load('data/images/heart.png').convert()
heart_img.set_colorkey((255, 255, 255))
background_img = pygame.image.load('data/images/background.png').convert()
cast_marker_img = pygame.image.load('data/images/cast_marker.png').convert()
cast_marker_img.set_colorkey((255, 255, 255))
health_bar_img = pygame.image.load('data/images/health_bar.png').convert()
health_bar_img.set_colorkey((255, 255, 255))
text_box_img = pygame.image.load('data/images/text_box.png').convert()
text_box_img.set_colorkey((255, 255, 255))
next_arrow_img = pygame.image.load('data/images/arrow.png').convert()
next_arrow_img.set_colorkey((255, 255, 255))
projectile_img = pygame.image.load('data/images/projectile.png').convert()
projectile_img.set_colorkey((255, 255, 255))
mana_bar_img = pygame.image.load('data/images/mana_bar.png').convert()
mana_bar_img.set_colorkey((255, 255, 255))
scroll_img = pygame.image.load('data/images/scroll.png').convert()
scroll_img.set_colorkey((255, 255, 255))
rock_img = pygame.image.load('data/images/rock.png').convert()
rock_img.set_colorkey((255, 255, 255))
scarlet_img = pygame.image.load('data/images/boss_portraits/scarlet.png').convert()
scarlet_img.set_colorkey((255, 255, 255))
jamician_img = pygame.image.load('data/images/boss_portraits/jamician.png').convert()
jamician_img.set_colorkey((255, 255, 255))
boss_portraits = {'scarlet': scarlet_img, 'jamician': jamician_img}
boss_bar_img = pygame.image.load('data/images/boss_bar.png').convert()
boss_bar_img.set_colorkey((255, 255, 255))

# Анимации
animation_timings = {}
animation_database = {}

for anim in os.listdir('data/images/animations'):
    f = open('data/images/animations/' + anim + '/timings.txt', 'r')
    t = f.read()
    f.close()
    timings = t.split(';')
    n = 0
    for val in timings:
        timings[n] = int(val)
        n += 1
    animation_timings[anim] = timings.copy()
    images = []
    for i in range(len(timings)):
        img = pygame.image.load('data/images/animations/' + anim + '/' + anim + '_' + str(i) + '.png').convert()
        img.set_colorkey((255, 255, 255))
        images.append(img.copy())
    animation_database[anim] = images.copy()
# Загрузка звуков
eye_shoot_s = pygame.mixer.Sound('data/sfx/eye_shoot.wav')
fire_blast_s = pygame.mixer.Sound('data/sfx/fire_blast.wav')
hurt_s = pygame.mixer.Sound('data/sfx/hurt.wav')
jamician_atk_1_s = pygame.mixer.Sound('data/sfx/jamician_atk_1.wav')
jamician_atk_2_s = pygame.mixer.Sound('data/sfx/jamician_atk_2.wav')
scarlet_atk_1_s = pygame.mixer.Sound('data/sfx/scarlet_atk_1.wav')
scarlet_atk_2_s = pygame.mixer.Sound('data/sfx/scarlet_atk_2.wav')
maw_shoot_s = pygame.mixer.Sound('data/sfx/maw_shoot.wav')
meteor_crash_s = pygame.mixer.Sound('data/sfx/meteor_crash.wav')
new_spell_s = pygame.mixer.Sound('data/sfx/new_spell.wav')
protection_s = pygame.mixer.Sound('data/sfx/protection.wav')
text_next_s = pygame.mixer.Sound('data/sfx/text_next.wav')
wind_slash_s = pygame.mixer.Sound('data/sfx/wind_slash.wav')
mana_s = pygame.mixer.Sound('data/sfx/mana.wav')


# Функции
def minimum(num, num2):
    if num < num2:
        num = num2
    return num


def spell_str(spell_dat_spell):
    spell_string = ''
    for l in spell_dat_spell:
        spell_string += '['
        for point in l:
            spell_string += str(point[0]) + ',' + str(point[1]) + ','
        spell_string += '],'
    return spell_string


def setup_entity_data(entity_setup, entity_type):
    global entity_defaults, entity_offsets
    for value in entity_defaults[entity_type]:
        entity_setup.entity_data[value] = entity_defaults[entity_type][value]
    entity_setup.offset = entity_offsets[entity_type].copy()


def get_entity_angle(entity_1, entity_2):
    x1 = entity_1.x + int(entity_1.size_x / 2)
    y1 = entity_1.y + int(entity_1.size_y / 2)
    x2_get = entity_2.x + int(entity_2.size_x / 2)
    y2_get = entity_2.y + int(entity_2.size_y / 2)
    angle_get = math.atan((y2_get - y1) / (x2_get - x1))
    if x2_get < x1:
        angle_get += math.pi
    return angle_get


def swap_color(image_swap, old_c, new_c):
    image_swap.set_colorkey(old_c)
    surf = image_swap.copy()
    surf.fill(new_c)
    surf.blit(image_swap, (0, 0))
    surf.set_colorkey((255, 255, 255))
    return surf


def load_level(entities_load, current_level_load):
    global levels
    if current_level_load > 0:
        for ent in levels[current_level_load]:
            entities_load.append(
                e.Entity(ent[1], ent[2], entity_sizes[ent[0]][0], entity_sizes[ent[0]][1], ent[0]))
            if len(ent) == 4:
                entities_load[-1].entity_data[ent[3]] = 1


def text_screen(last_frame_text, screen_text):
    timer = 0
    going = True
    while going:
        display.blit(last_frame_text, (0, 0))
        timer += 1
        if timer > 20:
            timer = 20
        black_surf_text = pygame.Surface((240, 135))
        black_surf_text.set_alpha(int(timer * 12.75))
        display.blit(black_surf_text, (0, 0))
        text.show_text(screen_text, 120 - int(get_text_width(screen_text, 1) / 2), 60, 1, 9999, font_white, display,
                       alpha=int(timer * 12.75))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if screen_text == 'Vi sdohli. Press "r" to try again.':
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        going = False

        screen.blit(pygame.transform.scale(display, (window_width, window_height)), (0, 0))
        pygame.display.update()
        mainClock.tick(60)


def learn_spell(last_frame, spell_id):
    global spell_dat
    scroll_y = 135
    scroll_target_y = 0

    while True:
        display.blit(last_frame, (0, 0))

        scroll_y += (scroll_target_y - scroll_y) / 10
        if abs(scroll_target_y - scroll_y) < 0.5:
            scroll_y = scroll_target_y

        display.blit(scroll_img, (50, scroll_y))
        text.show_text('New spell learned!', 56, scroll_y + 16, 1, 128, font_brown, display)
        text.show_text(spell_id, 56, scroll_y + 32, 1, 128, font_brown, display)
        text.show_text('mana cost: ' + str(spell_dat[spell_id][2]) + '%', 56, scroll_y + 44, 1, 128, font_brown,
                       display)
        text.show_text(spell_dat[spell_id][3], 56, scroll_y + 54, 1, 128, font_brown, display)
        display.blit(spell_dat[spell_id][4], (88, scroll_y + 70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if scroll_y == 0:
                        scroll_target_y = 140

        screen.blit(pygame.transform.scale(display, (window_width, window_height)), (0, 0))
        pygame.display.update()
        mainClock.tick(60)

        if scroll_y > 135:
            break

timer = 0
# Инфа о врагах, спэллах
entity_defaults = {
    'player': {
        'speed': 1.4,
        'health': 3,
        'boss': -1,
        'hurt_timer': 0,
        'spawn_timer': 0
    },
    'dummy': {
        'speed': 0,
        'health': 3,
        'boss': 0,
        'hurt_timer': 0,
        'spawn_timer': 0
    },
    'eye': {
        'speed': 0,
        'health': 5,
        'boss': 0,
        'hurt_timer': 0,
        'cycle_timer': 0,
        'spawn_timer': 0
    },
    'maw': {
        'speed': 0.15,
        'health': 9,
        'boss': 0,
        'hurt_timer': 0,
        'cycle_timer': 0,
        'spawn_timer': 0
    },
    'mana': {
        'boss': -1,
        'hurt_timer': 0,
        'spawn_timer': 0,
        'health': 999999
    },
    'scarlet': {
        'boss': 1,
        'hurt_timer': 0,
        'spawn_timer': 0,
        'health': 25,
        'speed': 3,
        'cycle_timer': [0, 'idle'],
        'ghost_angle': 0
    },
    'jamician': {
        'boss': 1,
        'hurt_timer': 0,
        'spawn_timer': 0,
        'health': 50,
        'speed': 0,
        'cycle_timer': [0, 'idle'],
        'teleportation': 0
    }
}

entity_offsets = {
    'player': [-2, -1],
    'dummy': [-1, -2],
    'eye': [0, 0],
    'mana': [0, 0],
    'scarlet': [0, 0],
    'maw': [0, 0],
    'jamician': [0, 0]
}

entity_sizes = {
    'player': [6, 6],
    'dummy': [10, 26],
    'eye': [16, 16],
    'mana': [10, 10],
    'scarlet': [17, 22],
    'maw': [17, 18],
    'jamician': [16, 26]
}

spells = {
    spell_str([[[-1, 1], [0, 0]]]): 'Wind Slash',
    spell_str([[[0, 0], [1, 1]]]): 'Wind Slash',
    spell_str([[[0, 0], [1, -1]]]): 'Wind Slash',
    spell_str([[[-1, -1], [0, 0]]]): 'Wind Slash',
    spell_str([[[0, 0], [0, 1]], [[0, 1], [1, 0]], [[0, -1], [1, 0]], [[-1, 0], [0, -1]]]): 'Meteor Crash',
    spell_str([[[-1, 0], [0, 0]], [[-1, -1], [-1, 0]], [[-1, -1], [0, -1]], [[0, -1], [1, 0]]]): 'Fire Blast',
    spell_str([[[0, 0], [0, 1]], [[0, 1], [1, 0]], [[1, -1], [1, 0]]]): 'Protection'
}

spell_dat = {
    'Wind Slash': [15, 12, 20],  # radius, activation time, mana, desc, img
    'Meteor Crash': [30, 30, 60, 'Smash things with rocks!'],
    'Fire Blast': [15, 32, 35, 'Snipe things with fire!'],
    'Protection': [20, 120, 40, 'Protect yourself!']
}

for spell in spell_dat:
    try:
        img = pygame.image.load('data/images/spell_patterns/' + spell + '.png').convert()
        img.set_colorkey((255, 255, 255))
        spell_dat[spell].append(img)
    except:
        pass

level_messages = {
    1: ['Use WASD to move.',
        'Click the on or near the dummy and drag diagonally down and to the left to cast Wind Slash.'],
    2: ['Using spells takes mana. Collect blue orbs to get more.'],
    3: ['Some real enemies are here now.'],
    4: ['!Meteor Crash', 'There\'s more!'],
    5: ['The sorceress Scarlet wants to fight!'],
    6: ['!Fire Blast', 'Buuuuurrrrrn...'],
    7: ['Beware of the Maws.'],
    8: ['!Protection', 'Now you have a non-offensive spell!'],
    9: ['The Great Sorcerer, Jamician, wants to fight!']
}
# Инфа о уровнях
levels = {
    0: ['dummy', 300, 300],
    1: [
        ['dummy', 96, 60]
    ],
    2: [
        ['dummy', 60, 100],
        ['dummy', 132, 100],
    ],
    3: [
        ['eye', 70, 80],
        ['eye', 122, 80]
    ],
    4: [
        ['eye', 60, 40],
        ['eye', 132, 40],
        ['eye', 96, 80, 'rapid_fire']
    ],
    5: [
        ['scarlet', 96, 60]
    ],
    6: [
        ['eye', 10, 10],
        ['eye', 96, 60, 'rapid_fire'],
        ['eye', 214, 109]
    ],
    7: [
        ['maw', 70, 80],
        ['maw', 122, 80],
        ['eye', 10, 10],
        ['eye', 96, 60, 'rapid_fire'],
        ['eye', 214, 109]
    ],
    8: [
        ['maw', 10, 10],
        ['eye', 96, 60, 'rapid_fire'],
        ['maw', 214, 109],
        ['maw', 10, 109],
        ['maw', 214, 10]
    ],
    9: [
        ['jamician', 96, 60]
    ]
}
# Инициализация (её нет)
e.load_animations('data/images/entities/')
# Переменные
scroll = [0, 0]
true_scroll = [0, 0]
up = False
down = False
right = False
left = False
clicking = False
entities = [e.Entity(50, 50, 6, 6, 'player')]
player = entities[0]
current_level = -1
load_level(entities, current_level)

spell_hitboxes = []
active_spells = []
active_animations = []

projectiles = []

particles = []

mana_count = 0

fade_in = 0

mana = 100

no_mana = 0

damage_text = []  # [x, y, text, timer]

message_queue = [['Use WASD to move.',
                  'Click the on or near the dummy and drag diagonally down and to the left to cast Wind Slash.'], 0,
                 0]  # queue, y, timer

casting_spell = [False, [0, 0], [], 0, [0, 0]]  # active, location, line history, animation timer, last hit

last_frame = None
# Цикл щас начнётся
pygame.mixer.music.load('data/music/main.mp3')
pygame.mixer.music.play(-1)
# pygame.mixer.music.set_volume(1)

main_menu_background = pygame.image.load('data/images/main_menu_background.png').convert()
logo = pygame.image.load('data/images/logo.png').convert()
logo.set_colorkey((255, 255, 255))

press_img = pygame.image.load('data/images/press.png').convert()
press_img.set_colorkey((255, 255, 255))

knifes_img = pygame.image.load('data/images/knifes.png').convert()
knifes_img.set_colorkey((255, 255, 255))

while True:
    if current_level > 0:
        # Позиция иышки
        mx, my = pygame.mouse.get_pos()
        mx = int(mx / window_width * 240)
        my = int(my / window_height * 135)
        # Доступ к спэллам
        if current_level < 4:
            spell_access = ['Wind Slash']
        elif current_level < 6:
            spell_access = ['Wind Slash', 'Meteor Crash']
        elif current_level < 8:
            spell_access = ['Wind Slash', 'Meteor Crash', 'Fire Blast']
        else:
            spell_access = ['Wind Slash', 'Meteor Crash', 'Fire Blast', 'Protection']
        # Задний фон
        true_scroll[0] += (player.x - true_scroll[0] - 120) / 10
        true_scroll[1] += (player.y - true_scroll[1] - 68) / 10
        scroll = [int(true_scroll[0]), int(true_scroll[1])]
        display.fill((0, 0, 0))
        if scroll[1] > 5:
            scroll[1] = 5
        if scroll[1] < -69:
            scroll[1] = -69
        if scroll[0] < -62:
            scroll[0] = -62
        if scroll[0] > 67:
            scroll[0] = 67
        display.blit(background_img, (-scroll[0] - 62, -scroll[1] - 69))
        # Передвижение
        player_movement = [0, 0]
        if not casting_spell[0]:
            if up:
                player_movement[1] -= player.entity_data['speed']
            if down:
                player_movement[1] += player.entity_data['speed']
            if right:
                player_movement[0] += player.entity_data['speed']
            if left:
                player_movement[0] -= player.entity_data['speed']
        # Сортировка объектов класса энтити
        old_entities = entities.copy()
        entities = []
        while old_entities:
            highest = [None, 99999]
            n = 0
            for entity in old_entities:
                if entity.type == 'player':
                    b = 14
                else:
                    b = 0
                if entity.y + entity.size_y + b < highest[1]:
                    highest = [n, entity.y + entity.size_y + b]
                n += 1
            entities.append(old_entities[highest[0]])
            old_entities.pop(highest[0])
        # Энтити
        current_boss = [None, 0]

        r_list = []
        n = 0

        if mana_count < 20000:
            if current_level > 1:
                if random.randint(1, 1) == 1:
                    entities.append(e.Entity(random.randint(6, 230), random.randint(6, 125), 10, 10, 'mana'))

        mana_count = 0
        for entity in entities:
            hide = False
            if 'boss' not in entity.entity_data:
                setup_entity_data(entity, entity.type)
            if entity.entity_data['boss'] == 1:
                if not message_queue[0]:
                    entity.entity_data['spawn_timer'] += 1
            else:
                entity.entity_data['spawn_timer'] += 1
            if entity.entity_data['spawn_timer'] > 61:
                entity.entity_data['spawn_timer'] = 61
            if entity.type == 'player':
                if player_movement != [0, 0]:
                    entity.change_frame(1)
                if player_movement[1] > 0:
                    entity.set_action('walk_down')
                if player_movement[1] < 0:
                    entity.set_action('walk_up')
                if player_movement[0] > 0:
                    entity.set_action('walk_side')
                    entity.set_flip(False)
                if player_movement[0] < 0:
                    entity.set_action('walk_side')
                    entity.set_flip(True)
                entity.move(player_movement, [], [])
            if entity.type == 'jamician':
                current_boss = ['jamician', entity.entity_data['health'] / 50]
                entity.change_frame(1)
                if entity.entity_data['spawn_timer'] > 60:
                    if entity.entity_data['cycle_timer'][1] == 'idle':
                        if random.randint(1, 110) == 1:
                            if random.randint(1, 4) < 4:
                                entity.entity_data['cycle_timer'] = [27, 'attack_1']
                                entity.set_action('attack_1')
                            elif random.randint(1, 2) == 1:
                                entity.entity_data['cycle_timer'] = [30, 'teleport']
                                entity.set_action('idle')
                            else:
                                entity.entity_data['cycle_timer'] = [90, 'attack_2']
                                entity.set_action('attack_2')
                    if entity.entity_data['cycle_timer'][0] > 0:
                        entity.entity_data['cycle_timer'][0] -= 1
                        if entity.entity_data['cycle_timer'][0] == 0:
                            entity.entity_data['cycle_timer'][1] = 'idle'
                            entity.set_action('idle')
                    if entity.entity_data['cycle_timer'][1] == 'teleport':
                        if entity.entity_data['cycle_timer'][0] > 20:
                            if random.randint(1, 3) == 1:
                                hide = True
                        elif entity.entity_data['cycle_timer'][0] < 10:
                            if random.randint(1, 3) == 1:
                                hide = True
                        else:
                            hide = True
                        if entity.entity_data['cycle_timer'][0] == 15:
                            distance = random.randint(50, 100)
                            angle = math.radians(random.randint(0, 360))
                            entity_movement = [math.cos(angle) * distance, math.sin(angle) * distance]
                            entity.move(entity_movement, [], [])
                    if entity.action == 'attack_2':
                        if entity.entity_data['cycle_timer'][0] == 1:
                            jamician_atk_2_s.play()
                            for i in range(60):
                                projectiles.append([entity.get_center()[0], entity.get_center()[1], math.radians(i * 6),
                                                    random.randint(12, 15) / 30, 0])
                            for i in range(10):
                                particles.append(
                                    [entity.x - 2 + random.randint(0, 19),
                                     entity.y + entity.size_y - random.randint(0, 10),
                                     math.radians(270), random.randint(4, 7) / 10, random.randint(4, 7) / 10,
                                     random.randint(100, 200) / 1000, random.choice([(19, 178, 242), (65, 243, 252)])])
                    if entity.action == 'attack_1':
                        if entity.entity_data['cycle_timer'][0] == 1:
                            if random.randint(1, 4) == 1:
                                if len(entities) < 7:
                                    if random.randint(1, 2) == 1:
                                        entities.append(
                                            e.Entity(random.randint(0, 220), random.randint(0, 120), 16, 16, 'eye'))
                                    else:
                                        entities.append(
                                            e.Entity(random.randint(0, 220), random.randint(0, 120), 17, 18, 'maw'))

                            else:
                                jamician_atk_1_s.play()
                                for i in range(8):
                                    projectiles.append([entity.get_center()[0], entity.get_center()[1],
                                                        get_entity_angle(entity, player) + math.radians(
                                                            random.randint(0, 90) - 45), random.randint(5, 15) / 7, 0])

            if entity.type == 'scarlet':
                current_boss = ['scarlet', entity.entity_data['health'] / 25]
                entity.change_frame(1)
                if entity.entity_data['spawn_timer'] > 60:
                    if entity.entity_data['cycle_timer'][1] == 'idle':
                        if random.randint(1, 120) == 1:
                            if random.randint(1, 2) == 1:
                                entity.entity_data['cycle_timer'] = [120, 'attack_1']
                                entity.set_action('attack_1')
                            elif random.randint(1, 3) == 1:
                                entity.entity_data['cycle_timer'] = [180, 'attack_2']
                                entity.set_action('attack_2')
                                scarlet_atk_2_s.play()
                            else:
                                entity.entity_data['cycle_timer'] = [60, 'ghost']
                                entity.set_action('ghost')
                                entity.entity_data['ghost_angle'] = math.radians(random.randint(0, 360))
                    if entity.entity_data['cycle_timer'][0] > 0:
                        entity.entity_data['cycle_timer'][0] -= 1
                        if entity.entity_data['cycle_timer'][0] == 0:
                            entity.entity_data['cycle_timer'][1] = 'idle'
                            entity.set_action('idle')
                    if entity.action == 'attack_1':
                        if (entity.entity_data['cycle_timer'][0] + 20) % 30 == 0:
                            for i in range(10):
                                particles.append([entity.x + 14, entity.y + entity.size_y, math.radians(i * 18),
                                                  random.randint(5, 15) / 10, random.randint(0, 20) / 10,
                                                  random.randint(100, 200) / 1000,
                                                  random.choice([(38, 36, 58), (20, 16, 32)])])
                            if random.randint(1, 4) != 1:
                                scarlet_atk_1_s.play()
                                for i in range(3):
                                    projectiles.append([entity.get_center()[0], entity.get_center()[1],
                                                        get_entity_angle(entity, player) + math.radians(
                                                            random.randint(0, 60) - 30), random.randint(5, 15) / 10, 0])
                            elif len(entities) < 6:
                                entities.append(e.Entity(random.randint(0, 220), random.randint(0, 120), 16, 16, 'eye'))
                    if entity.action == 'ghost':
                        if entity.entity_data['cycle_timer'][0] < 20:
                            entity_movement = [
                                math.cos(entity.entity_data['ghost_angle']) * entity.entity_data['speed'],
                                math.sin(entity.entity_data['ghost_angle']) * entity.entity_data['speed']]
                            entity.move(entity_movement, [], [])
                            particles.append([entity.x + 9, entity.y + 11, math.radians(random.randint(0, 360)),
                                              random.randint(0, 20) / 100, random.randint(10, 20) / 10,
                                              random.randint(100, 200) / 1000,
                                              random.choice([(38, 36, 58), (20, 16, 32)])])
                            if entity.entity_data['cycle_timer'][0] == 1:
                                entity.entity_data['cycle_timer'] = [39, 'reverse_ghost']
                                entity.set_action('reverse_ghost')
                    if entity.action == 'attack_2':
                        entity.offset[0] = random.randint(0, 4) - 2
                        if entity.entity_data['cycle_timer'][0] % 3 == 0:
                            projectiles.append([entity.get_center()[0], entity.get_center()[1],
                                                math.radians(entity.entity_data['cycle_timer'][0] * 7),
                                                random.randint(5, 15) / 15, 0])
                            particles.append(
                                [entity.x - 6 + random.randint(0, 22), entity.y + entity.size_y + 3, math.pi * 3 / 2,
                                 random.randint(4, 12) / 10, random.randint(10, 20) / 10,
                                 random.randint(100, 200) / 1000,
                                 random.choice([(120, 31, 44), (53, 20, 40)])])
                    else:
                        entity.offset[0] = 0
            if entity.type == 'maw':
                if entity.entity_data['spawn_timer'] > 60:
                    entity.entity_data['cycle_timer'] -= 1
                    if entity.action not in ['attack', 'hurt']:
                        dif_x = player.x - entity.x
                        dif_y = player.y - entity.y
                        if math.sqrt(dif_x ** 2 + dif_y ** 2) > 40:
                            entity_movement = [dif_x / (abs(dif_x) + abs(dif_y)) * entity.entity_data['speed'],
                                               dif_y / (abs(dif_x) + abs(dif_y)) * entity.entity_data['speed']]
                            if entity_movement[1] < 0:
                                entity.set_action('move_up')
                            if entity_movement[1] > 0:
                                entity.set_action('move_down')
                            if entity_movement[0] > 0:
                                entity.set_flip(False)
                            if entity_movement[0] < 0:
                                entity.set_flip(True)
                            entity.move(entity_movement, [], [])
                        if entity.entity_data['cycle_timer'] <= 0:
                            if random.randint(1, 90) == 1:
                                entity.set_action('attack')
                                entity.entity_data['cycle_timer'] = 60
                                maw_shoot_s.play()
                                for i in range(12):
                                    projectiles.append([entity.get_center()[0], entity.get_center()[1],
                                                        math.radians(i * 60 + random.randint(0, 60)),
                                                        random.randint(30, 50) / 100, 0])
                                    particles.append([entity.get_center()[0], entity.get_center()[1],
                                                      math.radians(random.randint(0, 360)),
                                                      random.randint(20, 45) / 100, 0,
                                                      0.05, random.choice([(38, 36, 58), (20, 16, 32), (26, 69, 59)])])
                    elif entity.entity_data['cycle_timer'] == 1:
                        entity.entity_data['cycle_timer'] = 240
                        entity.set_action('idle')

            if entity.type == 'eye':
                if entity.entity_data['spawn_timer'] > 60:
                    entity.entity_data['cycle_timer'] += 1
                    m = 1
                    rot_offset = 0
                    if 'rapid_fire' in entity.entity_data:
                        m = 0.2
                        rot_offset = (random.randint(0, 150) - 75) / 300 * math.pi
                    if entity.entity_data['cycle_timer'] > int(200 * entity.entity_data['speed'] * m):
                        eye_shoot_s.play()
                        entity.entity_data['cycle_timer'] = 0
                        projectiles.append(
                            [entity.get_center()[0], entity.get_center()[1],
                             get_entity_angle(entity, player) + rot_offset,
                             random.randint(5, 8) / 10 * (m ** 0.5), 0])
                    if entity.entity_data['speed'] == 0:
                        entity.entity_data['speed'] = random.randint(3, 7) / 10
                        entity.entity_data['range'] = random.randint(60, 100)
                    dif_x = player.x - entity.x
                    dif_y = player.y - entity.y
                    if math.sqrt(dif_x ** 2 + dif_y ** 2) > entity.entity_data['range']:
                        entity_movement = [dif_x / (abs(dif_x) + abs(dif_y)) * entity.entity_data['speed'],
                                           dif_y / (abs(dif_x) + abs(dif_y)) * entity.entity_data['speed']]
                        if entity_movement[1] < 0:
                            entity.set_action('move_up')
                        if entity_movement[1] > 0:
                            entity.set_action('move_down')
                        if entity_movement[0] > 0:
                            entity.set_flip(False)
                        if entity_movement[0] < 0:
                            entity.set_flip(True)
                        entity.change_frame(1)
                        entity.move(entity_movement, [], [])
            if entity.type == 'mana':
                entity.change_frame(1)
                if entity.entity_data['spawn_timer'] > 42:
                    entity.set_action('main')
                mana_r = pygame.Rect(entity.x - 5, entity.y - 10, 20, 20)
                if mana_r.colliderect(player.obj.rect):
                    if entity.entity_data['health'] != 0:
                        mana_s.play()
                        entity.entity_data['health'] = 0
                        entity.entity_data['hurt_timer'] = 15
                        mana += 20
                        if mana > 100:
                            mana = 100
                mana_count += 1
            if entity.x < -2:
                entity.set_pos(-2, entity.y)
            if entity.x + entity.size_x > 238:
                entity.set_pos(238 - entity.size_x, entity.y)
            if entity.y < 0:
                entity.set_pos(entity.x, 0)
            if entity.y + entity.size_y > 133:
                entity.set_pos(entity.x, 133 - entity.size_y)
            if entity.type != 'mana':
                for spell in spell_hitboxes:
                    spell_r = pygame.Rect(spell[0] - spell_dat[spell[2]][0], spell[1] - spell_dat[spell[2]][0],
                                          spell_dat[spell[2]][0] * 2, spell_dat[spell[2]][0] * 2)
                    if entity.obj.rect.colliderect(spell_r):
                        if spell[2] == 'Protection':
                            if entity.type == 'player':
                                if entity.entity_data['health'] <= 0:
                                    if entity.entity_data['hurt_timer'] > 13:
                                        entity.entity_data['health'] = 1
                        dmg = None
                        if spell[2] == 'Wind Slash':
                            dmg = 1
                        if spell[2] == 'Meteor Crash':
                            dmg = 6
                        if spell[2] == 'Fire Blast':
                            if entity.entity_data['hurt_timer'] == 0:
                                if entity.type != 'player':
                                    dmg = 3
                        if dmg is not None:
                            if entity.type == 'player':
                                hurt_s.play()
                            entity.entity_data['health'] -= dmg
                            entity.entity_data['hurt_timer'] = 15
                            damage_text.append(
                                [entity.x + int(entity.size_x / 2) + random.randint(0, 2) - 1, entity.y - 15, str(dmg),
                                 0])
            if entity.entity_data['health'] <= 0:
                entity.alpha = int(entity.entity_data['hurt_timer'] / 15 * 255)
                if entity.entity_data['hurt_timer'] <= 0:
                    r_list.append(n)
            if entity.entity_data['hurt_timer'] > 0:
                entity.entity_data['hurt_timer'] -= 1
                if entity.type != 'mana':
                    entity.set_action('hurt')
            elif entity.action == 'hurt':
                entity.set_action('idle')
            if entity.entity_data['spawn_timer'] <= 60:
                entity.alpha = int(entity.entity_data['spawn_timer'] / 60 * 255)
            if not hide:
                entity.display(display, scroll)
            n += 1

        r_list.sort(reverse=True)
        for r in r_list:
            entities.pop(r)

        # Снаряды
        r_list = []
        n = 0
        for projectile in projectiles:  # [x,y,rotation,speed,age]
            projectile[0] += math.cos(projectile[2]) * projectile[3]
            projectile[1] += math.sin(projectile[2]) * projectile[3]
            projectile[4] += 1
            projectile_r = pygame.Rect(projectile[0] - 2, projectile[1] - 2, 3, 3)
            if player.obj.rect.colliderect(projectile_r):
                if player.entity_data['health'] > 0:
                    hurt_s.play()
                    player.entity_data['health'] -= 1
                    player.entity_data['hurt_timer'] = 15
                    damage_text.append(
                        [player.x + int(player.size_x / 2) + random.randint(0, 2) - 1, player.y - 15, str(1), 0])
                    r_list.append(n)
            if projectile[4] < 20:
                img = projectile_img.copy()
                img.set_alpha(int(projectile[4] * 12.75))
            else:
                img = projectile_img
            display.blit(img, (projectile[0] - 4 - scroll[0], projectile[1] - 4 - scroll[1]))
            if projectile[0] < -3:
                if n not in r_list:
                    r_list.append(n)
            if projectile[0] > 240:
                if n not in r_list:
                    r_list.append(n)
            if projectile[1] < 0:
                if n not in r_list:
                    r_list.append(n)
            if projectile[1] > 140:
                if n not in r_list:
                    r_list.append(n)
            n += 1

        r_list.sort(reverse=True)
        for r in r_list:
            projectiles.pop(r)

        # Партиклы
        r_list = []
        n = 0
        for particle in particles:  # [x, y, rot, speed, stage, decay_speed, color]
            particle[0] += math.cos(particle[2]) * particle[3]
            particle[1] += math.sin(particle[2]) * particle[3] * 0.6
            particle_img = animation_database['particle'][int(particle[4])].copy()
            particle_img = swap_color(particle_img, (20, 16, 32), particle[6])
            display.blit(particle_img, (particle[0] - 4 - scroll[0], particle[1] - 4 - scroll[1]))
            particle[4] += random.randint(1, 10) / 10 * particle[5]
            if particle[4] >= 6:
                r_list.append(n)
            n += 1

        r_list.sort(reverse=True)
        for r in r_list:
            particles.pop(r)

        # Активные анимации
        r_list = []
        n = 0
        for anim in active_animations:  # [x,y,id,frame,timer]
            anim[4] += 1
            if anim[4] >= animation_timings[anim[2]][anim[3]]:
                anim[3] += 1
                anim[4] = 0
            if anim[3] >= len(animation_timings[anim[2]]):
                r_list.append(n)
                n += 1
                continue
            display.blit(animation_database[anim[2]][anim[3]], (anim[0] - scroll[0], anim[1] - scroll[1]))
            n += 1

        r_list.sort(reverse=True)
        for r in r_list:
            active_animations.pop(r)
        # Управление заклинаниями
        r_list = []
        n = 0
        for spell in spell_hitboxes:  # [x, y, id, duration]
            spell[3] -= 1
            if spell[3] <= 0:
                r_list.append(n)
            n += 1
        r_list.sort(reverse=True)
        for r in r_list:
            spell_hitboxes.pop(r)
        # Показ уровня здоровья врагов
        for entity in entities:
            if entity.entity_data['boss'] == 0:
                if entity.entity_data['health'] > 0:
                    display.blit(health_bar_img,
                                 (entity.x + int(entity.size_x / 2) - 8 - scroll[0], entity.y - 7 - scroll[1]))
                    health_surf = pygame.Surface(
                        (
                        minimum(int(entity.entity_data['health'] / entity_defaults[entity.type]['health'] * 15), 1), 2))
                    health_surf.fill((196, 44, 54))
                    display.blit(health_surf,
                                 (entity.x + int(entity.size_x / 2) - 7 - scroll[0], entity.y - 6 - scroll[1]))
        # Текст получения дэмэджа
        r_list = []
        n = 0
        for text_obj in damage_text:
            alpha = 255 - int(text_obj[3] / 60 * 255)
            text.show_text(text_obj[2], text_obj[0] - int(get_text_width(text_obj[2], 1) / 2) - scroll[0] + 1,
                           text_obj[1] - scroll[1] - int(text_obj[3] / 4), 1, 9999, font_gold, display, alpha=alpha)
            text.show_text(text_obj[2], text_obj[0] - int(get_text_width(text_obj[2], 1) / 2) - scroll[0],
                           text_obj[1] - scroll[1] - 1 - int(text_obj[3] / 4), 1, 9999, font_white, display,
                           alpha=alpha)
            text_obj[3] += 1
            if text_obj[3] >= 60:
                r_list.append(n)
            n += 1

        r_list.sort(reverse=True)
        for r in r_list:
            damage_text.pop(r)
        # Кастование спэллов
        if not casting_spell[0]:
            if clicking:
                casting_spell = [True, [mx, my], [], 0, [0, 0]]
        elif not clicking:
            if casting_spell[3] >= 0:
                casting_spell[0] = False

        if casting_spell[0]:
            x = casting_spell[1][0]
            y = casting_spell[1][1]
            max_scale = 46
            t = abs(casting_spell[3])
            if t < 10:
                scale = max_scale / 10 * t
            else:
                scale = max_scale
            # pygame.draw.polygon(display,(196,44,54),[(x,y-scale),(x+scale*math.sin(math.radians(180-(t-10)*6)),y),(x,y+scale),(x+scale*math.sin(math.radians(180+(t-10)*6)),y)],1)
            pygame.draw.polygon(display, (255, 255, 255), [
                (x + math.cos(math.radians((t - 10) * 6)) * scale, y + math.sin(math.radians((t - 10) * 6)) * scale), (
                    x + math.cos(math.radians((t - 10) * 6 + 90)) * scale,
                    y + math.sin(math.radians((t - 10) * 6 + 90)) * scale), (
                    x + math.cos(math.radians((t - 10) * 6 + 180)) * scale,
                    y + math.sin(math.radians((t - 10) * 6 + 180)) * scale), (
                    x + math.cos(math.radians((t - 10) * 6 + 270)) * scale,
                    y + math.sin(math.radians((t - 10) * 6 + 270)) * scale)], 1)
            scale *= 1.3
            pygame.draw.polygon(display, (138, 206, 255), [
                (x + math.cos(math.radians((-t + 10) * 6)) * scale, y + math.sin(math.radians((-t + 10) * 6)) * scale),
                (
                    x + math.cos(math.radians((-t + 10) * 6 + 90)) * scale,
                    y + math.sin(math.radians((-t + 10) * 6 + 90)) * scale), (
                    x + math.cos(math.radians((-t + 10) * 6 + 180)) * scale,
                    y + math.sin(math.radians((-t + 10) * 6 + 180)) * scale), (
                    x + math.cos(math.radians((-t + 10) * 6 + 270)) * scale,
                    y + math.sin(math.radians((-t + 10) * 6 + 270)) * scale)], 1)
            casting_spell[3] += 1
            if casting_spell[3] > 70:
                casting_spell[3] = 10

            for y2 in range(3):
                for x2 in range(3):
                    display.blit(cast_marker_img, (
                        x + int((x2 - 1) * 14 * scale / max_scale) - 3, y + int((y2 - 1) * 14 * scale / max_scale) - 3))
                    marker_r = pygame.Rect(x + (x2 - 1) * 18 - 5, y + (y2 - 1) * 18 - 5, 11, 11)
                    if marker_r.collidepoint((mx, my)):
                        if casting_spell[3] >= 0:
                            if casting_spell[4] != [x2 - 1, y2 - 1]:
                                points = [casting_spell[4].copy(), [x2 - 1, y2 - 1]]
                                points.sort()
                                casting_spell[2].append(points)
                                casting_spell[4] = [x2 - 1, y2 - 1]
                                if spell_str(casting_spell[2]) in spells:
                                    if spells[spell_str(casting_spell[2])] in spell_access:
                                        casting_spell[3] = -10

            for line in casting_spell[2]:
                pygame.draw.line(display, (138, 206, 255), (x + line[0][0] * 18, y + line[0][1] * 18),
                                 (x + line[1][0] * 18, y + line[1][1] * 18), 3)

            if casting_spell[3] >= 0:
                pygame.draw.line(display, (138, 206, 255), (x + casting_spell[4][0] * 18, y + casting_spell[4][1] * 18),
                                 (mx, my), 3)

            if casting_spell[3] == -1:
                casting_spell[0] = False
                clicking = False
                spell_id = spells[spell_str(casting_spell[2])]
                if mana >= spell_dat[spell_id][2]:
                    mana -= spell_dat[spell_id][2]
                    active_spells.append([x + scroll[0], y + scroll[1], spell_id, spell_dat[spell_id][1]])
                    if spell_id == 'Fire Blast':
                        dif_x = mx + scroll[0] - (player.x + player.size_x / 2)
                        dif_y = my + scroll[1] - (player.y + player.size_y / 2)
                        active_spells[-1].append(math.atan2(dif_y, dif_x))
                        active_spells[-1][0] = player.x
                        active_spells[-1][1] = player.y
                else:
                    no_mana = 60
        # Коробочка с текстом
        if message_queue[0]:
            message_queue[1] += (-40 - message_queue[1]) / 10
            if abs(message_queue[1] + 40) < 0.5:
                message_queue[1] = -40
        else:
            message_queue[1] += (10 - message_queue[1]) / 10
        if message_queue[1] < 0:
            text_box_img.set_alpha(int(abs(message_queue[1]) / 40 * 165))
            display.blit(text_box_img, (0, 135 + message_queue[1]))
        if message_queue[1] == -40:
            message_queue[2] += 1
            if message_queue[0][0][0] == '!':
                up = False
                right = False
                left = False
                down = False
                new_spell_s.play()
                learn_spell(last_frame, message_queue[0][0][1:])
                message_queue[0].pop(0)
                message_queue[2] = 0
            text.show_text(message_queue[0][0][:int(message_queue[2])], 4, 102, 1, 232, font_white, display)
            if message_queue[2] - len(message_queue[0][0]) > 20:
                offset = 0
                if int(message_queue[2] / 20) % 3 == 0:
                    offset = 1
                display.blit(next_arrow_img, (226, 126 + offset))

        # Интерфэйс
        if player.entity_data["health"] >= 1:
            display.blit(heart_img, (4, 3))
        if player.entity_data["health"] >= 2:
            display.blit(heart_img, (15, 3))
        if player.entity_data["health"] >= 3:
            display.blit(heart_img, (26, 3))
        if current_level > 1:
            display.blit(mana_bar_img, (2, 14))
            mana_surf = pygame.Surface((mana, 3))
            mana_surf.fill((15, 77, 163))
            display.blit(mana_surf, (3, 15))
        else:
            mana = 100

        if current_boss[0] is not None:
            display.blit(boss_portraits[current_boss[0]], (190, 0))
            display.blit(boss_bar_img, (181, 46))
            if int(current_boss[1] * 50) > 0:
                health_surf = pygame.Surface((int(current_boss[1] * 50), 2))
                health_surf.fill((196, 44, 54))
                display.blit(health_surf, (189, 51))

        if no_mana > 0:
            no_mana -= 1
            text.show_text('Not enough mana!', 120 - int(get_text_width('Not enough mana!', 1) / 2), 60, 1, 9999,
                           font_blue,
                           display)

        # Конец или Смерть
        if (player.alpha < 10) and (player.entity_data['health'] <= 0):
            text_screen(last_frame, 'Vi sdohli. Press "r" to try again.')
            fade_in = 10
            entities = [e.Entity(50, 50, 6, 6, 'player')]
            player = entities[0]
            spell_hitboxes = []
            active_spells = []
            active_animations = []
            projectiles = []
            particles = []
            casting_spell = [False, [0, 0], [], 0, [0, 0]]
            mana = 100
            clicking = False
            message_queue = [level_messages[current_level], 0, 0]
            load_level(entities, current_level)
            up = False
            down = False
            right = False
            left = False

        if fade_in > 0:
            fade_in -= 1
            black_surf = pygame.Surface((240, 135))
            black_surf.set_alpha(int(255 * fade_in / 10))
            display.blit(black_surf, (0, 0))

        # Спэллы и их управление
        r_list = []
        n = 0
        for spell in active_spells:
            if spell[2] == 'Meteor Crash':
                display.blit(rock_img, (spell[0] + spell[3] * 3 - scroll[0] - 10, spell[1] - spell[3] * 7 - scroll[1]))
                for i in range(3):
                    particles.append([spell[0] + spell[3] * 3 + random.randint(0, 20) - 10,
                                      spell[1] - spell[3] * 7 + random.randint(0, 20) - 10,
                                      math.radians(84 + random.randint(0, 30)), 2, 0, 0.25, (120, 31, 44)])
            if spell[2] == 'Fire Blast':
                distance = (32 - spell[3]) * 5
                loc_x = spell[0] + math.cos(spell[4]) * distance
                loc_y = spell[1] + math.sin(spell[4]) * distance
                if (loc_x < -3) or (loc_x > 240) or (loc_y < 0) or (loc_y > 140):
                    spell[3] = 1
                else:
                    for i in range(2):
                        particles.append(
                            [loc_x, loc_y, spell[4] + math.radians(random.randint(0, 90) - 45),
                             random.randint(5, 20) / 10,
                             random.randint(100, 200) / 100, 0.4,
                             random.choice([(196, 44, 54), (229, 112, 40), (247, 172, 55)])])
                        spell_hitboxes.append([loc_x, loc_y, spell[2], 1])
            if spell[2] == 'Protection':
                if spell[3] % 24 == 0:
                    active_animations.append([spell[0] - spell_dat[spell[2]][0], spell[1] - spell_dat[spell[2]][0],
                                              spell[2].lower().replace(' ', '_'), 0, 0])
                if random.randint(1, 2) == 1:
                    particles.append(
                        [spell[0] - 20 + random.randint(0, 40), spell[1] - 10 + random.randint(0, 20), math.pi * 3 / 2,
                         random.randint(5, 20) / 30, random.randint(150, 250) / 100, 0.3,
                         random.choice([(247, 172, 55), (251, 223, 107)])])
            if spell[3] == spell_dat[spell[2]][1]:
                if spell[2] == 'Fire Blast':
                    fire_blast_s.play()
                if spell[2] in ['Wind Slash', 'Protection']:
                    if spell[2] == 'Protection':
                        spell_hitboxes.append([spell[0], spell[1], spell[2], 120])
                        protection_s.play()
                    else:
                        wind_slash_s.play()
                    active_animations.append([spell[0] - spell_dat[spell[2]][0], spell[1] - spell_dat[spell[2]][0],
                                              spell[2].lower().replace(' ', '_'), 0, 0])
            spell[3] -= 1
            if spell[3] <= 0:
                if spell[2] == 'Wind Slash':
                    spell_hitboxes.append([spell[0], spell[1], spell[2], 1])
                if spell[2] == 'Meteor Crash':
                    meteor_crash_s.play()
                    for i in range(30):
                        particles.append([spell[0] + spell[3] * 3 + random.randint(0, 20) - 10,
                                          spell[1] - spell[3] * 7 + random.randint(0, 20) - 10, math.radians(i * 12),
                                          random.randint(5, 10) / 10, 0, 0.2,
                                          random.choice([(120, 31, 44), (38, 36, 58)])])
                        if i % 2 == 0:
                            projectiles.append(
                                [spell[0], spell[1], math.radians(i * 12), random.randint(5, 20) / 10, 0])
                    spell_hitboxes.append([spell[0], spell[1], spell[2], 1])
                r_list.append(n)
            n += 1

        r_list.sort(reverse=True)
        for r in r_list:
            active_spells.pop(r)

        # Конец уровня
        enemy_count = 0
        for entity in entities:
            if entity.type not in ['mana', 'player']:
                enemy_count += 1
        if enemy_count == 0:
            current_level += 1
            if current_level == 10:
                text_screen(last_frame, 'Vi pobedili')
            message_queue = [level_messages[current_level], 0, 0]
            load_level(entities, current_level)

    else:
        pass
    # Эвенты кнопок
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if current_level > 0:
            if event.type == KEYDOWN:
                if event.key == K_d:
                    right = True
                if event.key == K_a:
                    left = True
                if event.key == K_w:
                    up = True
                if event.key == K_s:
                    down = True
                if event.key == pygame.K_ESCAPE:
                    paused()

            if event.type == KEYUP:
                if event.key == K_d:
                    right = False
                if event.key == K_a:
                    left = False
                if event.key == K_w:
                    up = False
                if event.key == K_s:
                    down = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if (message_queue[1] == -40) and (message_queue[2] - len(message_queue[0][0]) > 20):
                        message_queue[0].pop(0)
                        message_queue[2] = 0
                        text_next_s.play()
                    elif message_queue[1] >= 0:
                        clicking = True
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    clicking = False
        else:
            if event.type == KEYDOWN:
                if current_level == -1:
                    current_level = 0
                    c = 0
                else:
                    if event.key == pygame.K_w:
                        c -= 1
                    if event.key == pygame.K_s:
                        c += 1
                    if event.key == pygame.K_SPACE:
                        if c == 0:
                            current_level = 1
                            load_level(entities, current_level)
                        elif c == 1:
                            with open("save.json", "r") as save:
                                data = json.load(save)
                            current_level = data["current_level"]
                            load_level(entities, data["current_level"])
    if current_level in (-1, 0):
        if current_level == 0:
            if c == 0:
                new_game_img = pygame.image.load('data/images/new_game_text_2.png').convert()
                new_game_img.set_colorkey((255, 255, 255))
                exit_img = pygame.image.load('data/images/exit_text_4.png').convert()
                exit_img.set_colorkey((255, 255, 255))
                arena_img = pygame.image.load('data/images/arena_text_1.png').convert()
                arena_img.set_colorkey((255, 255, 255))
                continue_img = pygame.image.load('data/images/continue_text_4.png').convert()
                continue_img.set_colorkey((255, 255, 255))
                py = 78
            elif c == 1:
                new_game_img = pygame.image.load('data/images/new_game_text_1.png').convert()
                new_game_img.set_colorkey((255, 255, 255))
                exit_img = pygame.image.load('data/images/exit_text_4.png').convert()
                exit_img.set_colorkey((255, 255, 255))
                arena_img = pygame.image.load('data/images/arena_text_1.png').convert()
                arena_img.set_colorkey((255, 255, 255))
                continue_img = pygame.image.load('data/images/continue_text_3.png').convert()
                continue_img.set_colorkey((255, 255, 255))
                py = 88
            elif c == 2:
                new_game_img = pygame.image.load('data/images/new_game_text_1.png').convert()
                new_game_img.set_colorkey((255, 255, 255))
                exit_img = pygame.image.load('data/images/exit_text_4.png').convert()
                exit_img.set_colorkey((255, 255, 255))
                arena_img = pygame.image.load('data/images/arena_text_2.png').convert()
                arena_img.set_colorkey((255, 255, 255))
                continue_img = pygame.image.load('data/images/continue_text_4.png').convert()
                continue_img.set_colorkey((255, 255, 255))
                py = 100
            elif c == 3:
                new_game_img = pygame.image.load('data/images/new_game_text_1.png').convert()
                new_game_img.set_colorkey((255, 255, 255))
                exit_img = pygame.image.load('data/images/exit_text_3.png').convert()
                exit_img.set_colorkey((255, 255, 255))
                arena_img = pygame.image.load('data/images/arena_text_1.png').convert()
                arena_img.set_colorkey((255, 255, 255))
                continue_img = pygame.image.load('data/images/continue_text_4.png').convert()
                continue_img.set_colorkey((255, 255, 255))
                py = 114
            elif c > 2:
                c = 0
            elif c < 0:
                c = 2

        display.blit(main_menu_background, (0, 0))
        display.blit(logo, (27, 20))

        if current_level == -1:
            display.blit(press_img, (50, 115))
        else:
            display.blit(new_game_img, (95, 78))
            display.blit(continue_img, (98, 88))
            display.blit(arena_img, (106, 100))
            display.blit(exit_img, (110, 114))
            display.blit(knifes_img, (80, py))

    # Апдейты и всякая фигня
    screen.blit(pygame.transform.scale(display, (window_width, window_height)), (0, 0))
    pygame.display.update()
    mainClock.tick(60)
    last_frame = display.copy()
