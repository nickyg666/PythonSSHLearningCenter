# ==============================================
# 🌈 RAINBOW TURTLE - TERMINAL VERSION 🌈
# ==============================================
# Draw colorful ASCII art in your terminal!

import time
import sys

class TerminalTurtle:
    def __init__(self, width=80, height=40):
        self.width = width
        self.height = height
        self.canvas = [[' ' for _ in range(width)] for _ in range(height)]
        self.x = width // 2
        self.y = height // 2
        self.colors = {
            'red': '\033[31m',
            'green': '\033[32m',
            'yellow': '\033[33m',
            'blue': '\033[34m',
            'purple': '\033[35m',
            'cyan': '\033[36m',
            'white': '\033[37m',
            'reset': '\033[0m'
        }
        self.current_color = 'white'
    
    def color(self, color_name):
        if color_name in self.colors:
            self.current_color = color_name
    
    def put_char(self, char):
        if 0 <= self.x < self.width and 0 <= self.y < self.height:
            self.canvas[self.y][self.x] = (self.current_color, char)
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def draw_line(self, dx, dy, length, char='*'):
        for _ in range(length):
            self.put_char(char)
            self.move(dx, dy)
    
    def draw_circle(self, radius, char='@'):
        import math
        center_x, center_y = self.x, self.y
        for angle in range(0, 360, 5):
            rad = math.radians(angle)
            self.x = int(center_x + radius * math.cos(rad))
            self.y = int(center_y + radius * math.sin(rad))
            self.put_char(char)
    
    def display(self):
        print('\n' * 2)
        for row in self.canvas:
            line = ''
            for cell in row:
                if isinstance(cell, tuple):
                    color, char = cell
                    line += self.colors.get(color, '') + char + self.colors['reset']
                else:
                    line += cell
            print(line)
        print('\n')
    
    def clear(self):
        self.canvas = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        self.x = self.width // 2
        self.y = self.height // 2

# Step 1: Create our terminal turtle artist
artist = TerminalTurtle()

# Step 2: List of colors to use
colors = ["red", "green", "yellow", "blue", "purple", "cyan"]

print("🌈 Drawing a colorful flower with ASCII art!")
print("Please wait...\n")

# Step 3: Draw a colorful flower!
# We'll use a loop to repeat patterns
for i in range(36):
    # Pick a color from our list
    color = colors[i % len(colors)]
    
    # Set the pen color
    artist.color(color)
    
    # Draw one petal
    artist.draw_line(1, 0, 15, '>')
    artist.draw_line(0, 1, 7, 'v')
    artist.draw_line(-1, 0, 15, '<')
    artist.draw_line(1, 0, 7, '>')
    
    # Turn to next petal (approximate with position reset)
    artist.x = artist.width // 2
    artist.y = artist.height // 2
    
    # Move position slightly for each petal
    import math
    angle = i * 10
    rad = math.radians(angle)
    artist.x = int(artist.width // 2 + 10 * math.cos(rad))
    artist.y = int(artist.height // 2 + 10 * math.sin(rad))

# Draw center circle
artist.x = artist.width // 2
artist.y = artist.height // 2
artist.color("yellow")
artist.draw_circle(8, '@')

# Display the art
artist.display()

print("✨ Drawing complete!")
print("\n" + "=" * 60)
print("🎨 CREATE YOUR OWN ART! 🎨")
print("=" * 60)
print("TRY THIS:")
print("- Change the colors in the colors list!")
print("- Modify the character: '>' becomes '*' or '#'")
print("- Change the numbers to make different sizes!")
print("- Try artist.clear() to start over!")
print("=" * 60)
