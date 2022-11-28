import pyautogui

PAGES = int(input())
pyautogui.sleep(2)

next_btn = pyautogui.locateOnScreen('auto/next.png', confidence=0.9)


for page in range(PAGES):
    file_name = f'auto/pages/deep_dive_javascript/{page}.png'
    img = pyautogui.screenshot(file_name, region=(800, 120, 1030, 1330))
    pyautogui.click(next_btn)
    pyautogui.sleep(0.5)


