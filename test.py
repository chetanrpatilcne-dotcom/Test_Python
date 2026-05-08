def array():
    num = [45,65,89,1,2,3,4,5]
    
    print("Print the array: ", len(num))
    print("Print the sorted elements: ", sorted(num))
    print("Print the first element: ", num[0])
    print("Print the maximum element: ", max(num))
    print("Print the minimum element: ", min(num))
    print("Print the sum of the elements: ", sum(num))
    print("Print the average of the elements: ", sum(num)/len(num))
    print("Print the reversed array: ", num[::-2])
    print("Print the sliced array: ", num[-3:])

    bin_number = [bin(n) for n in num]
    print("Print the binary representation of num ", bin_number)

    num2 = 577
    print("positive" if num2 > 0 else "negative" if num2 < 0 else "zero")
    print("give proper age" if num2 >= 100 else "Senior citizen" if num2 > 70 else "Adult" if num2 > 18 else "Child")

    Temprature = 33
    print("Hot" if Temprature > 35 else "Warm" if Temprature > 25 else "Cold")

    access_control = "Guest"
    print("Full access" if access_control == "Admin" else "Limited access" if access_control == "Guest" else "No access")

    result5 = input ("Enter your name: ")
    result2 = result5.count("t")
    result3 = result5.isdecimal()
    print(result3)




    text = input("enter your name: ")
    print("The length of the string", len(text))
    if len(text) > 12:
        print("The String is too long")
    elif not text.find(" ") == -1:
        print(f"your name shouldnt contain the spaces in the name")
    elif not text.isalpha():
        print("The string shouldnt have digits")
    else:
        print(f"Your name is: {text}")


array()

