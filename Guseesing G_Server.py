import socket
import random 

host = "192.168.68.105"
port = 7777
banner = """
== Guessing Game ==
Enter your guess:"""

def generate_random_int(low, high):
    return random.randint(low, high)

# initialize the socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)

print(f"server is listening in port {port}")
guessme = 0
conn = None
while True:
    if conn is None:
        print("waiting for connection..")
        conn, addr = s.accept()
        guessme = generate_random_int(1,100)
        print(f"new client: {addr[0]}")
        conn.sendall(banner.encode())
    else:
        client_input = conn.recv(1024)
        guess = int(client_input.decode().strip())
        print(f"User guess attempt: {guess}")
        if guess == guessme:
            conn.sendall(b"Correct Answer!")
            conn.close()
            conn = None
            continue
        elif guess > guessme:
            conn.sendall(b"Guess Lower!\nenter guess: ")
            continue
        elif guess < guessme:
            conn.sendall(b"Guess Higher!\nenter guess:")
            continue


