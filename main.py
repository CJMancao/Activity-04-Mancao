import show

while True:

    print("1. Show shiba \n2. choose a jpg file")
    choice = int(input("Choice: "))
    
    if choice == 1:
        show.displayshiba()
        break

    elif choice == 2:
        show.userinput()
        break
    
    else:
        print("Invalid Input...")