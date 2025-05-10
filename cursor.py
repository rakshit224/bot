with open("example.txt", "w") as file:
    file.write("Hello, World!\nThis is Python file handling.")

# Reading file and showing cursor positions
with open("example.txt", "r") as file:
    print("Initial Cursor Position:", file.tell())  # Should be 0
    
    content = file.read(5)  # Read first 5 characters
    print("Read Content:", content)
    
    print("Cursor Position After Read:", file.tell())  # Should be 5
    
    file.seek(0)  # Move cursor back to the beginning
    print("Cursor Position After seek(0):", file.tell())  # Should be 0
    
    full_content = file.read()
    print("Full File Content:\n", full_content)
    
    print("Cursor Position at End of File:", file.tell())  # Should be at EOF
with open("example.txt", "r") as file:
    file.seek(7)  # Move cursor to the 7th byte
    print("\nReading after seek(7):", file.read(5)) 
with open("example.txt", "rb") as file:  # Open in binary mode for relative seeking
    file.seek(-10, 2)  # Move 10 bytes before the end of file
    print("\nLast 10 characters of the file:", file.read().decode())  
