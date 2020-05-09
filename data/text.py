import pygame
from copy import deepcopy


def show_text(text, x, y, spacing, width_limit, font, surface, alpha=255, double=1, overflow='normal'):
    text += ' '
    if double == 2:
        x = int(x / 2)
        y = int(y / 2)
    original_x = x
    original_y = y
    current_word = ''
    if overflow == 'normal':
        for char in text:
            if char not in [' ', '\n']:
                try:
                    image = font[str(char)][1]
                    current_word += str(char)
                except KeyError:
                    pass
            else:
                word_total = 0
                for char2 in current_word:
                    word_total += font[char2][0]
                    word_total += spacing
                if word_total + x - original_x > width_limit:
                    x = original_x
                    y += font['Height']
                for char2 in current_word:
                    image = font[str(char2)][1]
                    image.set_alpha(alpha)
                    surface.blit(
                        pygame.transform.scale(image, (image.get_width() * double, image.get_height() * double)),
                        (x * double, y * double))
                    x += font[char2][0]
                    x += spacing
                if char == ' ':
                    x += font['A'][0]
                    x += spacing
                else:
                    x = original_x
                    y += font['Height']
                current_word = ''
            if x - original_x > width_limit:
                x = original_x
                y += font['Height']
        return x, y
    if overflow == 'cut all':
        for char in text:
            if char not in [' ', '\n']:
                try:
                    image = font[str(char)][1]
                    image.set_alpha(alpha)
                    surface.blit(
                        pygame.transform.scale(image, (image.get_width() * double, image.get_height() * double)),
                        (x * double, y * double))
                    x += font[str(char)][0]
                    x += spacing
                except KeyError:
                    pass
            else:
                if char == ' ':
                    x += font['A'][0]
                    x += spacing
                if char == '\n':
                    x = original_x
                    y += font['Height']
                current_word = ''
            if x - original_x > width_limit:
                x = original_x
                y += font['Height']
        return x, y


def generate_font(font_image, font_spacing_main, tile_size, tile_size_y, color):
    font_spacing = deepcopy(font_spacing_main)
    font_order = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                  'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', '-', ',', ':', '+', '\'', '!', '?',
                  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(', ')', '/', '_', '=', '\\', '[', ']', '*', '"',
                  '<', '>', ';', '%']
    font_image = pygame.image.load(font_image).convert()
    new_surf = pygame.Surface((font_image.get_width(), font_image.get_height())).convert()
    new_surf.fill(color)
    font_image.set_colorkey((0, 0, 0))
    new_surf.blit(font_image, (0, 0))
    font_image = new_surf.copy()
    font_image.set_colorkey((255, 255, 255))
    num = 0
    for char in font_order:
        font_image.set_clip(pygame.Rect(((tile_size + 1) * num), 0, tile_size, tile_size_y))
        character_image = font_image.subsurface(font_image.get_clip())
        font_spacing[char].append(character_image)
        num += 1
    font_spacing['Height'] = tile_size_y
    return font_spacing
