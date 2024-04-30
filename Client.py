# Bermejo, Theodore Ross (Enhancing: Guessing Game)

# Note: Need Internet

import socket

# Host: Changeable, check IPConfig in the Command Line Interface
host = "192.168.212.253"
port = 7777

# Function: Play Game
def play_game():
    s = socket.socket()
    s.connect((host, port))

    # Receive: Banner name
    data = s.recv(1024)
    print("\n== Guessing Game (Enhanced) ==\n")

    # Print: Banner name
    print(data.decode().strip())

    # loop: While (Endless unless close)
    while True:
        # Get: User input
        user_input = input("Input: ").strip()
        s.sendall(user_input.encode())

        # Add: Spacing (after the input)
        print()

        # Reply: Receive
        reply = s.recv(1024).decode().strip()

        # Conditional: Reply's
        if "Correct" in reply:
            print(reply)
            break

        print(reply)
        continue

    # Close: Program
    s.close()

# Loop: While (Endless unless close)
while True:
    play_game() # If Yes and If No Break
    repeat = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if repeat != "yes":
        break

