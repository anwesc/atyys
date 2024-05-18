import os
import random
import time

import pyautogui
import win32api
import win32con
import win32gui

"""
1394 19 2546 698    1152
                    679
x=2421, y=617       125		10.85%
                    81		11.92%
x=1968, y=528       578		48%
                    170		25%
"""


def random_num(a, b):
    return random.uniform(a, b)


def point_mouse_click(coordinate_point, offset, duration, click_time):
    print(duration)
    print(click_time)
    pyautogui.moveTo(coordinate_point['x'] + random_num(offset[0], offset[2]),
                     coordinate_point['y'] + random_num(offset[1], offset[3]), duration=duration)

    pyautogui.click(clicks=1, interval=click_time, duration=duration, button='left')


def main_yuling():
    num = 1
    while num <= total_num:
        print('第 %s 次挑战' % num)

        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        print(left, top, right, bottom)

        coordinate_point = {'x': right - ((right - left) * 0.1085),
                            'y': bottom - ((bottom - top) * 0.1192)
                            }

        print('挑战坐标：', coordinate_point)
        duration = random_num(0.15, 0.21)
        click_time = random_num(0.2, 0.32)
        point_offset = random_num(1, 3)
        start_time = time.time()
        # print(start_time)
        point_mouse_click(coordinate_point, [-12 + point_offset, -7 + point_offset,
                                             15 + point_offset, 8 + point_offset], duration, click_time)

        time.sleep(35)

        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        print(left, top, right, bottom)

        coordinate_point = {'x': right - ((right - left) * 0.48),
                            'y': bottom - ((bottom - top) * 0.25)
                            }
        print('结算坐标：', coordinate_point)
        duration = random_num(0.15, 0.25)
        click_time = random_num(0.2, 0.36)
        point_offset = random_num(2, 6)
        point_mouse_click(coordinate_point, [64 + point_offset, -5 + point_offset,
                                             100 + point_offset, 20 + point_offset], duration, click_time)
        end_time = time.time()
        # print(end_time)
        print(end_time - start_time)
        # click_time = random_num(0.2, 0.36)
        # pyautogui.click(clicks=1, interval=click_time, duration=duration, button='left')

        time.sleep(random_num(1, 2))
        pyautogui.PAUSE = random_num(0.8, 1.2)
        num += 1
    exit(0)


if __name__ == "__main__":
    # 根据窗口句柄获取窗口位置和大小
    hwnd = win32gui.FindWindow('Win32Window', "阴阳师-网易游戏")
    print(hwnd)
    # left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    # print(left, top, right, bottom)

    total_num = 100
    pyautogui.FAILSAFE = False
    pyautogui.PAUSE = 0.8
    main_yuling()
