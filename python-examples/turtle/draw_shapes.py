# ==============================================
# 🐢 TERMINAL TURTLE DRAWING FUN! 🐢
# ==============================================
# Learn to draw cool ASCII art with Python!

import sys

class TerminalTurtle:
    def __init__(self, width=80, height=40):
        self.width = width
        self.height = height
        self.canvas = [[' ' for _ in range(width)] for _ in range(height)]
        self.x = width // 2
        self.y = height // 2
        self.pen_down = True
    
    def penup(self):
        self.pen_down = False
    
    def pendown(self):
        self.pen_down = True
    
    def put_char(self, char):
        if self.pen_down and 0 <= self.x < self.width and 0 <= self.y < self.height:
            self.canvas[self.y][self.x] = char
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def forward(self, distance, char='*'):
        import math
        direction = getattr(self, 'direction', 0)
        rad = math.radians(direction)
        dx = int(distance * math.cos(rad))
        dy = int(distance * math.sin(rad))
        
        for _ in range(abs(max(abs(dx), abs(dy))) or 1):
            if dx != 0:
                step_x = 1 if dx > 0 else -1
                self.put_char(char)
                self.x += step_x
                dx -= step_x
            if dy != 0:
                step_y = 1 if dy > 0 else -1
                self.put_char(char)
                self.y += step_y
                dy -= step_y
    
    def right(self, angle):
        self.direction = getattr(self, 'direction', 0) + angle
    
    def left(self, angle):
        self.direction = getattr(self, 'direction', 0) - angle
    
    def goto(self, x, y):
        self.x = x
        self.y = y
    
    def circle(self, radius, char='@'):
        import math
        center_x, center_y = self.x, self.y
        for angle in range(0, 360, 8):
            rad = math.radians(angle)
            self.x = int(center_x + radius * math.cos(rad))
            self.y = int(center_y + radius * math.sin(rad))
            self.put_char(char)
    
    def display(self):
        print('\n' * 2)
        print(' ' * 20 + "🎨 YOUR DRAWING 🎨\n")
        for row in self.canvas:
            print(''.join(row))
        print('\n')
    
    def clear(self):
        self.canvas = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        self.x = self.width // 2
        self.y = self.height // 2

# Step 1: Make our turtle
pen = TerminalTurtle()

# Step 2: Initialize direction
pen.direction = 0

print("🐢 Drawing shapes with ASCII art!")
print("Drawing: SQUARE, CIRCLE, TRIANGLE\n")

# Step 3: Draw a SQUARE
# A square has 4 sides, each line turns 90 degrees
for i in range(4):
    pen.forward(25, '#')
    pen.right(90)

# Step 4: Move to new spot without drawing
pen.penup()
pen.goto(40, 30)
pen.pendown()

# Step 5: Draw a CIRCLE
pen.circle(8, 'O')

# Step 6: Move again
pen.penup()
pen.goto(10, 10)
pen.pendown()

# Step 7: Draw a TRIANGLE
# Triangle has 3 sides, each turn is 120 degrees
for i in range(3):
    pen.forward(25, '+')
    pen.left(120)

# Display the art
pen.display()

print("✨ Drawing complete!")
print("\n" + "=" * 60)
print("🎨 TRY CHANGING THIS! 🎨")
print("=" * 60)
print("IDEAS:")
print("- Change forward(25) to forward(35) for bigger shapes")
print("- Change the characters: '#' becomes '@' or '*'")
print("- Draw more shapes!")
print("- Use pen.goto(x, y) to move to new spots!")
print("=" * 60)
