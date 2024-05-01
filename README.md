The contents are the code for guessing game from server and client and the scoreboards
server

import socket
import random 

host = "192.168.68.105"
port = 7777
banner = """
== Guessing Game =="""
client_info = {}
def generate_random_int(low, high):
    return random.randint(low, high)
start = "You may start your guess"
# initialize the socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)

print(f"server is listening in port {port}")
guessme = 0
attemp = 0
conn = None
while True:
    if conn is None:
        print("waiting for connection..")
        conn, addr = s.accept()
        print(f"new client: {addr[0]}")
        conn.sendall(banner.encode())

        conn.sendall(b"Enter your name: ")
        client_name = conn.recv(1024).decode().strip()
        client_info[client_name] = {"attempts": 0, "difficulty": ""}
    else:
        client_input = conn.recv(1024)
        choice = int(client_input.decode().strip())
        if choice == 1:
            level = "Easy"
            guessme = generate_random_int(1,50)
            client_info[client_name]["difficulty"] = level
            conn.sendall(start.encode())
            while True:
                client_choice = conn.recv(1024)
                guess = int(client_choice.decode().strip())
                attemp +=1
                client_info[client_name]["attempts"] += 1
                if guess == guessme:
                    conn.sendall(b"Correct Answer!")
                    conn.close()
                    print(f"Numbers of Attempt for {client_name}: {attemp}")
                    print(client_info)
                    with open("Scorebooard.txt", "a") as file:
                        file.write(f"Name: {client_name}, Attempts: {client_info[client_name]['attempts']}, Difficulty: {client_info[client_name]['difficulty']}\n")
                    conn = None
                    break
                elif guess > guessme:
                    conn.sendall(b"Guess Lower!\nenter guess: ")
                    continue
                elif guess < guessme:
                    conn.sendall(b"Guess Higher!\nenter guess:")
                    continue
        elif choice == 2:
            level = "Medium"
            guessme = generate_random_int(1,100)
            client_info[client_name]["difficulty"] = level
            conn.sendall(start.encode())
            while True:
                client_choice = conn.recv(1024)
                guess = int(client_choice.decode().strip())
                attemp +=1
                client_info[client_name]["attempts"] += 1
                if guess == guessme:
                    conn.sendall(b"Correct Answer!")
                    conn.close()
                    print(f"Numbers of Attempt for {client_name}: {attemp}")
                    print(client_info)
                    with open("Scorebooard.txt", "a") as file:
                        file.write(f"Name: {client_name}, Attempts: {client_info[client_name]['attempts']}, Difficulty: {client_info[client_name]['difficulty']}\n")
                    conn = None
                    break
                elif guess > guessme:
                    conn.sendall(b"Guess Lower!\nenter guess: ")
                    continue
                elif guess < guessme:
                    conn.sendall(b"Guess Higher!\nenter guess:")
                    continue
        elif choice == 3:
            level = "Hard"
            guessme = generate_random_int(1,500)
            client_info[client_name]["difficulty"] = level
            conn.sendall(start.encode())
            while True:
                client_choice = conn.recv(1024)
                guess = int(client_choice.decode().strip())
                attemp += 1
                client_info[client_name]["attempts"] += 1
                if guess == guessme:
                    conn.sendall(b"Correct Answer!")
                    conn.close()
                    print(f"Numbers of Attempt for {client_name}: {attemp}")
                    print(client_info)
                    with open("Scorebooard.txt", "a") as file:
                        file.write(f"Name: {client_name}, Attempts: {client_info[client_name]['attempts']}, Difficulty: {client_info[client_name]['difficulty']}\n")
                    conn = None
                    break
                elif guess > guessme:
                    conn.sendall(b"Guess Lower!\nenter guess: ")
                    continue
                elif guess < guessme:
                    conn.sendall(b"Guess Higher!\nenter guess:")
                    continue


Client

import socket


host = "192.168.68.105"
port = 7777

s = socket.socket()
s.connect((host, port))

name = input("Enter your name: ")
s.sendall(name.encode())
# received the banner
data = s.recv(1024)
# print banner
print(data.decode().strip())
print("In What level do you wish to play? \n[1]Easy(1-50) \n[2]Medium(1-100) \n[3]Hard(1-500)")

while True:
    #let get our input from the user
    user_input = input("").strip()
    s.sendall(user_input.encode())
    reply = s.recv(1024).decode().strip()
    if "Correct" in reply:
        print(reply)
        break
    print(reply)
    continue
s.close()
