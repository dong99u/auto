import pyautogui

PAGES = int(input())
pyautogui.sleep(2)

for page in range(PAGES):
    file_name = f'auto/pages/hongongjavascript/{page}.bmp'
    img = pyautogui.screenshot(file_name, region=(710, 93, 1117, 1500))
    pyautogui.press('right')
    pyautogui.sleep(0.5)