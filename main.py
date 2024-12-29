import math
import time
import sys


# Constants
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 22
A_INCREMENT = 0.04
B_INCREMENT = 0.02
FRAME_DELAY = 0.03

# Global variables
A = 0.0
B = 0.0

# Initialize buffers
b = [' '] * (SCREEN_WIDTH * SCREEN_HEIGHT)
z = [0] * (SCREEN_WIDTH * SCREEN_HEIGHT)

def clear_screen():
    """Clear the terminal screen"""
    sys.stdout.write("\033[H")
    sys.stdout.flush()

def render_frame(b):
    """Render the current frame to the terminal"""
    for k in range(SCREEN_WIDTH * SCREEN_HEIGHT):
        sys.stdout.write(b[k])
        if k % SCREEN_WIDTH == SCREEN_WIDTH - 1:
            sys.stdout.write("\n")
    sys.stdout.flush()

def update_angles():
    """Update rotation angles for the next frame"""
    global A, B
    A = (A + A_INCREMENT) % (2 * math.pi)
    B = (B + B_INCREMENT) % (2 * math.pi)

def render_donut():
    global A, B, b, z

    b = [' '] * (SCREEN_WIDTH * SCREEN_HEIGHT)
    z = [0] * (SCREEN_WIDTH * SCREEN_HEIGHT)

    for j in range(0, 628, 7):  # j goes from 0 to 6.28 in steps of 0.07
        for i in range(0, 628, 2):  # i goes from 0 to 6.28 in steps of 0.02
            c = math.sin(i / 100)
            d = math.cos(j / 100)
            e = math.sin(A)
            f = math.sin(j / 100)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i / 100)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            x = int(40 + 30 * D * (l * h * m - t * n))
            y = int(12 + 15 * D * (l * h * n + t * m))
            o = x + SCREEN_WIDTH * y
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))

            if 0 <= y < SCREEN_HEIGHT and 0 <= x < SCREEN_WIDTH and D > z[o]:
                z[o] = D
                b[o] = ".,-~:;=!*#$@"[N if N > 0 else 0]

def main():
    try:
        while True:
            clear_screen()
            update_angles()
            render_donut()
            render_frame(b)
            time.sleep(FRAME_DELAY)
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main()
