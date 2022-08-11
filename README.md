# PlumScript
A language for writing scripts for simulating keyboard and mouse inputs. Originally By StudiousGamer

# Syntax
## Basic
- `wait {seconds}` waits for the specified number of seconds
- `exit` stop the script
- `exec {python/os} {command**}` runs the specified command (python or cmd commands)

## Mouse
- `mouse {left/right} down` holds the left/right mouse button down
- `mouse {left/right} up` releases the left/right mouse button
- `go {x},{y}` moves the mouse to the x,y coordinates
- `click {left/right} {x},{y}` clicks the left/right mouse button at the x,y coordinates
- `drag {x1},{y1} {x2},{y2} {seconds}` drags the mouse cursor from x1,y1 to x2,y2 in specified seconds

## Keyboard
- `press {key}` presses the specified key
- `type {text}` types the specified text
- `hold {key}` holds the specified key down
- `release {key}` releases the specified key
