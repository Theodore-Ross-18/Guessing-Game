# Bermejo, Theodore Ross (Enhancing: Guessing Game)

import socket
import threading
import random
import json

# Host: Changeable, check IPConfig in the Command Line Interface
host = "192.168.212.253"
port = 7777
banner = """Enter your name:"""

# Dictionary: Store user data
user_data = {}
leaderboard = []

# Function: Load: User data from a file
def load_user_data():
    global user_data
    try:
        with open("user_data.json", "r") as file:
            data = file.read()
            if data:
                user_data = json.loads(data)
    except (FileNotFoundError, json.JSONDecodeError):
        pass

# Function: Save: User data to file
def save_user_data():
    with open("user_data.json", "w") as file:
        json.dump(user_data, file)

# Function: Difficulty
def generate_random_int(difficulty):

    if difficulty == 'easy':
        # The Guessing Number will not be higher than 50
        return random.randint(1, 50)
    
    elif difficulty == 'medium':
        # The Guessing Number will not be higher than 100
        return random.randint(1, 100)
    
    elif difficulty == 'hard':
        # The Guessing Number will not be higher than 500
        return random.randint(1, 500)

# Function: Handle Client
def handle_client(conn, addr):
    try:
        conn.sendall(banner.encode())
        player_name = conn.recv(1024).decode().strip()
        print(f"Player {player_name} connected.")
        conn.sendall(b"Choose difficulty level (easy, medium, hard):\n")
        difficulty = conn.recv(1024).decode().strip().lower()
        
        # Guessing Part: Endless Input until Correct
        while True:
            guessme = generate_random_int(difficulty)
            conn.sendall(b"Enter your guess:\n")
            tries = 0
            
            # Loop: While (Status)
            while True:
                try:
                    client_input = conn.recv(1024)

                    if not client_input:
                        print(f"Player {player_name} disconnected.")
                        save_user_data()
                        return  # Exit the function when the client disconnects
                    
                    guess = int(client_input.decode().strip())
                    tries += 1

                    # Score: Basis
                    if guess == guessme:

                        score = 1000 // tries
                        conn.sendall(f"Correct Answer! You won!\nYour score: {score}\n".encode())
                        user_data[player_name] = {'score': score, 'difficulty': difficulty}
                        leaderboard.append({'name': player_name, 'score': score, 'difficulty': difficulty})
                        save_user_data()
                        print(f"Player {player_name} guessed the correct number in {tries} tries!")
                        break
                    
                    # Guess: Lower or Higher (Hint)
                    elif guess > guessme:
                        conn.sendall(b"Guess Lower!\n")

                    elif guess < guessme:
                        conn.sendall(b"Guess Higher!\n")

                except ConnectionResetError:
                    print(f"Connection with player {player_name} forcibly closed by the remote host.")
                    save_user_data()
                    return  # Exit the function when the client disconnects

    except ConnectionAbortedError:
        print(f"Connection with player {player_name} aborted.")

    finally:
        conn.close()

# Function: Leaderboard
def display_leaderboard():
    global leaderboard
    print("\n== Leaderboard ==\n")
    for i, player in enumerate(sorted(leaderboard, key=lambda x: x['score'], reverse=True)):
        print(f"Rank {i+1}:")
        print(f"Name: {player['name']}")
        print(f"Score: {player['score']}")
        print(f"Difficulty: {player['difficulty']}\n")

# Initialize: Socket Object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)

load_user_data()
print(f"Server is listening on port {port}")

while True:
    conn, addr = s.accept()
    print(f"New connection from {addr}")
    client_thread = threading.Thread(target=handle_client, args=(conn, addr))
    client_thread.start()
    client_thread.join()  # Wait for the client thread to finish before displaying the leaderboard
    display_leaderboard()
