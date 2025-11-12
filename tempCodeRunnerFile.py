while True:
    print("\n Menu:")
    print("1.Add")
    print("2.Substract")
    print("3.Multiply")
    print("4.Exit")

    choice = int(input("enter ypur choice:"))

    if choice ==4:
        print("exiting program")

        break
    elif choice not in (1,2,3):
             print("invalide choice.try again.")
        
             continue

    a = int(input("enter first number: "))
    b = int(input("enter second number: "))

    if choice ==1:
        print("result:", a + b)
    elif choice ==2:
        print("result:", a - b)
    elif choice ==3:
        print("result: ", a * b )