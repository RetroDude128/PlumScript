import pyautogui
import sys
import time

def get_button(button):
    if button.lower() == "right":
        return "RIGHT"
    else:
        return "LEFT"


def parse(text):
    script = text.split('\n')
    for index, line in enumerate(script):
        if line.startswith('#') or line.strip() == '':
            continue
        keywords = line.split(' ')
        try:
            if keywords[0] == 'go':
                x, y = keywords[1].split(',')
                pyautogui.moveTo(int(x), int(y))

            elif keywords[0] == 'click':
                button = get_button(keywords[1])
                x, y = keywords[2].split(',')
                pyautogui.click(int(x), int(y), button=button)

            elif keywords[0] == 'wait':
                time.sleep(float(keywords[1]))

            elif keywords[0] == 'mouse':
                button = get_button(keywords[1])
                if keywords[2] == 'down':
                    pyautogui.mouseDown(button=button)
                elif keywords[2] == 'up':
                    pyautogui.mouseUp(button=button)

            elif keywords[0] == 'drag':
                x1, y1 = keywords[1].split(',')
                x2, y2 = keywords[2].split(',')
                seconds = float(keywords[3])
                pyautogui.moveTo(int(x1), int(y1))
                pyautogui.moveTo(int(x2), int(y2), duration=seconds)

            elif keywords[0] == 'exit':
                sys.exit()

            else:
                print("Unknown command: " + keywords[0])

        except IndexError:
            print(f"ERROR ({index + 1}): Not Enough Arguments")

        except Exception as e:
            print(f"ERROR ({index + 1}): {e}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            text = f.read()
            parse(text)
    else:
        while True:
            inp = input(">>> ")
            parse(inp)