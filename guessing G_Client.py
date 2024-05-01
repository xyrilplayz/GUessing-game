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