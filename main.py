while True:
    i = float(input("Enter a number : "))
    i = i**(1/2)
    print(f"Your square root number is: {i}")
    check = str(input("Do you want to quit or start again? enter Y to restart or another key to end: "))
    if check in ["y", "Y"]:
        continue
    else:
        print("Goodbye!")
        exit()
