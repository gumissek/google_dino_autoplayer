import time

import pyautogui
from PIL import Image
from selenium import webdriver

URL = 'https://elgoog.im/dinosaur-game/'
BG_COLOR_WHITE = (255, 255, 255)
OBSTACLE_COLOR = ''
GRAY = (82, 82, 82)
WHITE = (255, 255, 255)

def start():
    driver.get(URL)
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(3)

def is_white_bg() -> bool:
    im_bg = pyautogui.screenshot(region=(200, 950, 5, 5))
    im_bg.save('bg.jpg')
    img_bg = Image.open('bg.jpg')
    width_bg = img_bg.width
    height_bg = img_bg.height
    for x in range(width_bg):
        for y in range(height_bg):
            if img_bg.getpixel(xy=(x, y)) == BG_COLOR_WHITE:
                return True


def is_cactus_far():
    im_cac = pyautogui.screenshot(region=(610, 730, 30, 60))
    im_cac.save('cac1.jpg')
    img = Image.open('cac1.jpg')
    width = img.size[0]
    height = img.size[1]
    for x in range(width):
        for y in range(height):
            if img.getpixel(xy=(x, y)) == OBSTACLE_COLOR:
                return True


def is_cactus_close():
    im_cac = pyautogui.screenshot(region=(300, 730, 30, 60))
    im_cac.save('cac2.jpg')
    img = Image.open('cac2.jpg')
    width = img.size[0]
    height = img.size[1]
    for x in range(width):
        for y in range(height):
            if img.getpixel(xy=(x, y)) == OBSTACLE_COLOR:
                return True


def is_bird():
    im_bird = pyautogui.screenshot(region=(260, 630, 40, 40))
    im_bird.save('bird.jpg')
    img = Image.open('bird.jpg')
    width = img.width
    height = img.height
    for x in range(width):
        for y in range(height):
            if img.getpixel(xy=(x, y)) == OBSTACLE_COLOR:
                return True


def is_game_over():
    im = pyautogui.screenshot(region=(590, 620, 260, 35))
    im.save('game_over.jpg')
    img = Image.open('game_over.jpg')
    for x in range(img.width):
        for y in range(img.height):
            if img.getpixel(xy=(x, y)) == OBSTACLE_COLOR:
                return True


def is_obstacle():
    # im_cac = pyautogui.screenshot(region=(270, 740, 250, 100))
    im_cac = pyautogui.screenshot(region=(272, 740, 232, 100))
    im_cac.save('obs.jpg')
    img = Image.open('obs.jpg')
    width = img.size[0]
    height = img.size[1]
    for x in range(width):
        for y in range(height):
            if img.getpixel(xy=(x, y)) == OBSTACLE_COLOR:
                return True


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument('--start-maximized')
driver = webdriver.Chrome(options=chrome_options)

start()
game_is_on = True
while game_is_on:
    if is_white_bg():
        OBSTACLE_COLOR = GRAY
    else:
        OBSTACLE_COLOR = (171, 171, 171)

    if is_obstacle():
        pyautogui.press('space')

# mechanizm gry
# zrobic rzut ekranu w konkretnej pozycji i sprawdzic czy zawiera tam czarne pole
# sprawdzanie tla
