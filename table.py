num = int(input("enter the number you want to print the table of: "))
print(f"#"*30 + "\n")
print(f"{'the table of '+ str(num):^28}")
print(f"#"*30 + "\n")
for i in range(1,11):
    print(f'{num} X {i} = {num*i}')