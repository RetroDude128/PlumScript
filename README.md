# PlumScript
A language for writing scripts for simulation keyboard and mouse inputs.

# Syntax
- `mouse {left/right} down` holds the left/right mouse button down
- `mouse {left/right} up` releases the left/right mouse button
- `go {x},{y}` moves the mouse to the x,y coordinates
- `click {left/right} {x},{y}` clicks the left/right mouse button at the x,y coordinates
- `drag {x1},{y1} {x2},{y2}` drags the mouse cursor from x1,y1 to x2,y2
- `wait {seconds}` waits for the specified number of seconds