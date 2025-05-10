with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a file handling example.\n")
with open("example.txt", "a") as file:
    file.write("Appending a new line.\n")
with open("example.txt", "r") as file:
    content = file.read()
    print("\n--- Reading Full File ---")
    print(content)
print("\n--- Reading Line by Line ---")
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  #Removes new line characters.
with open("example.txt", "r") as file:
    lines = file.readlines()
    print("\n--- Using readlines() ---")
    print(lines)
lines_to_write = ["First Line\n", "Second Line\n", "Third Line\n"]
with open("example.txt", "w") as file:
    file.writelines(lines_to_write)

with open("example.txt", "r") as file:
    print("\n--- Final Content of File ---")
    print(file.read())
