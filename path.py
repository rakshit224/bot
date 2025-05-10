file_path = "C:\Users\LENOVO\OneDrive\Documents\cpp\filehandl.py"  # Windows Path
#file_path = "/home/user/Documents/example.txt"  # Linux/Mac Path
with open(file_path, "w") as file:
    file.write("This file is saved in a specific folder.")
print(f"File saved at: {file_path}")
