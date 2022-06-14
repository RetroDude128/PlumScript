import pyautogui
import sys
import time

def parse(text):
    script = text.split('\n')
    for index, line in enumerate(script):
        if line.startswith('#'):
            continue
        keywords = line.split(' ')
        try:
            if keywords[0] == 'go':
                x, y = keywords[1].split(',')
                pyautogui.moveTo(int(x), int(y))
            elif keywords[0] == 'click':
                button = keywords[1]
                x, y = keywords[2].split(',')
                if button.lower() == "right":
                    button = "RIGHT"
                else:
                    button = "LEFT"
                pyautogui.click(int(x), int(y), button=button)
            elif keywords[0] == 'wait':
                time.sleep(float(keywords[1]))
        except IndexError:
            print(f"ERROR ({index + 1}): Not Enough Arguments")
        except Exception as e:
            print(f"ERROR ({index + 1}): {e}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            text = f.read()
            parse(text)