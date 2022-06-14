import pyautogui
import sys

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
        except IndexError:
            print(f"ERROR ({index + 1}): Not Enough Arguments")
        except Exception as e:
            print(f"ERROR ({index + 1}): {e}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            text = f.read()
            parse(text)