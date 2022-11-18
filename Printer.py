from time import sleep

my_chars = ['4', 'a', '9', 'd', '2', '7', 'h', '3', 'v', 'j', 'k', '5', 'm', 'x', 'o', '8', 'q', 'r', '0', 't', 'u',
            'i', '@', '#', "ù", "*", " $", "^", "µ", "+", "-", "/", "\\", "%", ".", "§", ";", ",", 'w', 'n', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', '1', 'K', 'L', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
            'W', 'X', 'Y', 'Z', 's', 'J', 'e', 'g', 'b', 'l', '6', 'f', 'p', 'c', ' ']
inp = input("enter your word: ")
output = list("")
for i in range(len(inp)):
    for j in my_chars:
        output.append(j)
        print(''.join(output))
        if j != inp[i]:
            output.pop()
        sleep(0.002)
