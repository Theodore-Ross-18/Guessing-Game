# Guessing-Game

An Enhance Guessing Game using Python Programming Language with the utilization of Sockets and additional features of the following:

1. user/client can repeat the game without disconnecting

2. user can choose difficulty based on the generated random number to guess

  a. easy (1-50)
  b. medium (1-100)
  c.hard (1-500)

3. the game implements a scoring mechanism based on the number of tries the user guesses the number to guess (less tries the better), and provide a leaderboard containing the name of the user and her/his score which is displayed after the user/client disconnects from the server.

4. persistence - the server should save the user's name, his/her score, and the last chosen difficulty (should default to easy) into a file and this file will be loaded/updated during leaderboard display and when the user set's the difficulty.

# Client Side Code Procedures:

1. Host and Port: The host IP address (host) and port number (port) are currently set to specific values. You may need to adjust these values based on your network configuration. The current values are placeholders (192.168.212.253 for host and 7777 for port).

2. Internet Connection: Since this game communicates over a network, you need an internet connection to run it. The client script connects to a server running on the specified host and port.

3. Server Implementation: This script is the client side of the game. It communicates with a server that should be running on the specified host and port. You need to ensure that the server is implemented and running. The server should expect and handle the client's requests and replies accordingly.

4. Game Logic on the Server Side: The server should implement the game logic, such as generating a random number for the player to guess, checking the correctness of the guess, and sending appropriate messages back to the client.

5. Input: The player interacts with the game by entering guesses through the input prompt. Ensure that the input mechanism works correctly and that the server can receive and process the input.

6. Output: The server sends messages back to the client to provide feedback on the guesses. Make sure the client can receive and display these messages correctly.

7. Looping: The script provides an option to play the game again after each round. You need to ensure that this loop works as intended and that the game restarts when the player chooses to play again.

8. Error Handling: Add error handling to deal with potential issues like connection errors, unexpected server responses, or invalid input from the user.

9. Banner: The server sends a banner message to the client upon connection. Ensure that the banner is appropriately formatted and informative.

10. Close Connection: The client closes the connection to the server after finishing the game. Ensure that the connection is closed properly to avoid resource leaks.

Note: This script utilizes the socket library, which is a standard Python library for socket programming, to establish communication between the client and the server over a network.

# Server Side Procedures:

1. Socket Programming: This script uses Python's socket module for networking. Ensure that Python's socket module is available and functional in your Python environment.

2. Threading: The script utilizes the threading module to handle multiple client connections concurrently. Make sure your Python environment supports threading.

3. JSON Module: It uses the json module to load and save user data to a JSON file (user_data.json). Ensure that the json module is available in your Python environment.

4. Host and Port: The server binds to a specific host IP address (host) and port number (port). Adjust these values as needed based on your network configuration.

5. Banner Message: The server sends a banner message to clients upon connection. You can customize this message as needed.

6. User Data Storage: User data is stored in a JSON file named user_data.json. Ensure that the script has read and write permissions to this file and that it exists in the script's directory.

7. Game Logic: The script implements the game logic, including generating a random number based on the chosen difficulty level, handling user guesses, and calculating scores.

8. Leaderboard: It maintains a leaderboard of player scores. Ensure that the leaderboard is displayed correctly and sorted by score.

9. Error Handling: Add appropriate error handling to deal with potential issues such as client disconnections, connection errors, file I/O errors, etc.

10. Client Interaction: Clients can connect to the server using a TCP socket and interact with the game by sending guesses and receiving feedback. Test the client-server interaction to ensure it works as expected.
