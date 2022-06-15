import pyautogui

import sys
import time

pyautogui.FAILSAFE = False

def get_button(button):
    if button.lower() == "right":
        return "RIGHT"
    else:
        return "LEFT"

def extract_string(text):
    ret = []
    curr = ""
    string = False
    for c in text:
        if c.startswith('"'):
            string = True
            c = c[1:]
        if not string:
            ret.append(c)
        if string:
            curr += c + ' '
        if c.endswith('"'):
            string = False
            curr = curr[:-2]
            ret.append(curr)
            curr = ""
    return ret


def run(text):
    if '[INIT]' not in text or '[LOOP]' not in text:
        print("ERROR: Missing INIT or LOOP")
        sys.exit()
    init = text.split('[LOOP]')[0].replace('[INIT]', '')
    loop = text.split('[LOOP]')[1]
    parse(init)
    while True:
        try:
            parse(loop)
        except KeyboardInterrupt:
            sys.exit()


def parse(text):
    script = text.split('\n')
    for index, line in enumerate(script):
        if line.startswith('#') or line.strip() == '':
            continue
        keywords = line.split(' ')
        try:
            keywords[0] = keywords[0].lower()
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
            
            elif keywords[0] == 'type':
                text = extract_string(keywords)
                pyautogui.typewrite(text[1])
            
            elif keywords[0] == 'press':
                key = keywords[1]
                pyautogui.press(key)
            
            elif keywords[0] == 'hold':
                key = keywords[1]
                pyautogui.keyDown(key)

            elif keywords[0] == 'release':
                key = keywords[1]
                pyautogui.keyUp(key)

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
            run(text)
    else:
        while True:
            inp = input(">>> ")
            parse(inp)