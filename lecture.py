filename = "table_of_5.txt"
with open(filename,'w') as file :
    file.write("="*30 + "\n")
    file.write(f"{"| multiplication table of 5":^28}|\n")
    file.write("="*30 + "\n")
    for i in range(1,11):
        file.write(f"| {'5':>3} X {i:<2} = {5* i:<3} | \n")

with open(filename,'r') as file :
    content = file.read()
    print(content)