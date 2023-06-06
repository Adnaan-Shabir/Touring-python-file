import time
print("Welcome to our service portal \n Thank you for choosing us \n We are available in INDIA & America \n Press '1' for India \n Press '2' for America ")
user = int(input(" Enter your choice: "))

time.sleep(2)
if user == 1:
    print("Thank you for chosing India \n Kindly select the state you want to visit \n 1. Bangalore \n 2. Delhi \n 3. Jammu and Kashmir \n 4. Himachal Pradesh")
    user = int(input("Enter your choice: "))
    time.sleep(2)
    if user == 1:
        print("Wow... You have chosen Bangalore \n Now select your Hotel according to your convience: \n 1. Luxeroius hotel \n 2. Non- Luxerious Hotel")
        user =int(input("Enter your choice: "))
        if user == 1:
            print("Luxerious hotel details: \n * Total price 30,000/day \n * Breakfast is complementry \n * Wifi is available \n Attached pool.")
            days = int(input("How many days you want to stay: "))
            people = int(input("Total number of people: "))
            
            amount = 30000*days * people
            print("We also provide rental bikes with 300/day ")
            
            user = input("If you want type 'Y' if not type 'N' :")
            time.sleep(2)
            if user == "y":
                print(f"Your total amount for {days} days with bike is {amount+300}")
            else:
                print(f"Your total amount for {days} days is {amount}")
            
        elif user == 2:
            print("Non-Luxerious hotel details: \n * Total price 16,000/day \n ")
            days = int(input("How many days you want to stay: "))
            people = int(input("Total number of people: "))
            amount = 16000*days * people
            print("We also provide rental bikes with 300/day ")
            
            user = input("If you want type 'Y' if not type 'N' :")
            time.sleep(2)
            if user == "y":
                print(f"Your total amount for {days} days with bike is {amount+300}")
            else:
                print(f"Your total amount for {days} days is {amount}")
            
        else:
            print("Please choose valid option and try again")
            
        
    elif user == 2:
        print("Wow... You have chosen Delhi \n Now select your Hotel according to your convience: \n 1. Luxeroius hotel \n 2. Non- Luxerious Hotel")
        user =int(input("Enter your choice: "))
        if user == 1:
            print("Luxerious hotel details: \n * Total price 28,000/day \n * Breakfast is complementry \n * Wifi is available \n Attached pool.")
            days = int(input("How many days you want to stay: "))
            people = int(input("Total number of people: "))
            amount = 28000*days * people
            print("We also provide rental bikes with 300/day ")
            
            user = input("If you want type 'Y' if not type 'N' :")
            time.sleep(2)
            if user == "y":
                print(f"Your total amount for {days} days with bike  is {amount+300}")
            else:
                print(f"Your total amount for {days} days is {amount}")
            
        elif user == 2:
            print("Non-Luxerious hotel details: \n * Total price 15,000/day \n ")
            days = int(input("How many days you want to stay: "))
            people = int(input("Total number of people: "))
            amount = 15000*days * people
            print("We also provide rental bikes with 300/day ")
            
            user = input("If you want type 'Y' if not type 'N' :")
            time.sleep(2)
            if user == "y":
                print(f"Your total amount for {days} days with bike is {amount+300}")
            else:
                print(f"Your total amount for {days} days is {amount}")
            
        else:
            print("Please choose valid option and try again")
            
    elif user == 3:
        print("Wow... You have chosen Jammu and Kashmir \n Now select your Hotel according to your convience: \n 1. Luxeroius hotel \n 2. Non- Luxerious Hotel")
        user =int(input("Enter your choice: "))
        if user == 1:
            print("Luxerious hotel details: \n * Total price 35,000/day \n * Breakfast is complementry \n * Wifi is available \n Attached pool.")
            days = int(input("How many days you want to stay: "))
            people = int(input("Total number of people: "))
            amount = 35000*days * people
            
            print("We also provide rental bikes with 300/day ")
            
            user = input("If you want type 'Y' if not type 'N' :")
            time.sleep(2)
            if user == "y":
                print(f"Your total amount for {days} days with bike is {amount+300}")
            else:
                print(f"Your total amount for {days} days is {amount}")
            
        elif user == 2:
            print("Non-Luxerious hotel details: \n * Total price 19,000/day \n ")
            days = int(input("How many days you want to stay: "))
            people = int(input("Total number of people: "))
            amount = 19000*days * people
            b_amount = 300
            print("We also provide rental bikes with 300/day ")
            
            user = input("If you want type 'Y' if not type 'N' :")
            time.sleep(2)
            if user == "y":
                print(f"Your total amount for {days} days with bike is {amount+300}")
            else:
                print(f"Your total amount for {days} days is {amount}")
            
        else:
            print("Please choose valid option and try again")
            
    elif user == 4:
        print("Wow... You have chosen Himachal Pradesh \n Now select your Hotel according to your convience: \n 1. Luxeroius hotel \n 2. Non- Luxerious Hotel")
        user =int(input("Enter your choice: "))
        if user == 1:
            print("Luxerious hotel details: \n * Total price 28,000/day \n * Breakfast is complementry \n * Wifi is available \n Attached pool.")
            days = int(input("How many days you want to stay: "))
            people = int(input("Total number of people: "))
            amount = 18000*days * people
            
            print("We also provide rental bikes with 300/day ")
            
            user = input("If you want type 'Y' if not type 'N' :")
            time.sleep(2)
            if user == "y":
                print(f"Your total amount for {days} days with bike is {amount+300}")
            else:
                print(f"Your total amount for {days} days is {amount}")
            
        elif user == 2:
            print("Non-Luxerious hotel details: \n * Total price 15,000/day \n ")
            days = int(input("How many days you want to stay: "))
            people = int(input("Total number of people: "))
            amount = 5000*days * people
            
            print("We also provide rental bikes with 300/day ")
            
            user = input("If you want type 'Y' if not type 'N' :")
            time.sleep(2)
            if user == "y":
                print(f"Your total amount for {days} days with bike is {amount+300}")
            else:
                print(f"Your total amount for {days} days is {amount}")
            
        else:
            print("Please choose valid option and try again")

    else:
        print("Kindly choose valid option and try again.")
elif user ==2:
        print("Thank you for chosing America \n Kindly select the state you want to visit \n 1. Alaska \n 2. Florida \n 3. New York \n 4. Texas")
        user = int(input("Enter your choice: "))
    
        if user == 1:
            print("Wow... You have chosen Alaska \n Now select your Hotel according to your convience: \n 1. Luxeroius hotel \n 2. Non- Luxerious Hotel")
            user =int(input("Enter your choice: "))
            if user == 1:
                print("Luxerious hotel details: \n * Total price 30,000/day \n * Breakfast is complementry \n * Wifi is available \n Attached pool.")
                days = int(input("How many days you want to stay: "))
                people = int(input("Total number of people: "))
                
                amount = 30000*days * people
                print("We also provide rental bikes with 300/day ")
                
                user = input("If you want type 'Y' if not type 'N' :")
                time.sleep(2)
                if user == "y":
                    print(f"Your total amount for {days} days with bike is {amount+300}")
                else:
                    print(f"Your total amount for {days} days is {amount}")
                
            elif user == 2:
                print("Non-Luxerious hotel details: \n * Total price 16,000/day \n ")
                days = int(input("How many days you want to stay: "))
                people = int(input("Total number of people: "))
                amount = 16000*days * people
                print("We also provide rental bikes with 300/day ")
                
                user = input("If you want type 'Y' if not type 'N' :")
                time.sleep(2)
                if user == "y":
                    print(f"Your total amount for {days} days with bike is {amount+300}")
                else:
                    print(f"Your total amount for {days} days is {amount}")
                
            else:
                print("Please choose valid option and try again")
                
            
        elif user == 2:
            print("Wow... You have chosen Florida \n Now select your Hotel according to your convience: \n 1. Luxeroius hotel \n 2. Non- Luxerious Hotel")
            user =int(input("Enter your choice: "))
            if user == 1:
                print("Luxerious hotel details: \n * Total price 28,000/day \n * Breakfast is complementry \n * Wifi is available \n Attached pool.")
                days = int(input("How many days you want to stay: "))
                people = int(input("Total number of people: "))
                amount = 28000*days * people
                print("We also provide rental bikes with 300/day ")
                
                user = input("If you want type 'Y' if not type 'N' :")
                time.sleep(2)
                if user == "y":
                    print(f"Your total amount for {days} days with bike  is {amount+300}")
                else:
                    print(f"Your total amount for {days} days is {amount}")
                
            elif user == 2:
                print("Non-Luxerious hotel details: \n * Total price 15,000/day \n ")
                days = int(input("How many days you want to stay: "))
                people = int(input("Total number of people: "))
                amount = 15000*days * people
                print("We also provide rental bikes with 300/day ")
                
                user = input("If you want type 'Y' if not type 'N' :")
                time.sleep(2)
                if user == "y":
                    print(f"Your total amount for {days} days with bike is {amount+300}")
                else:
                    print(f"Your total amount for {days} days is {amount}")
                
            else:
                print("Please choose valid option and try again")
                
        elif user == 3:
            print("Wow... You have chosen New York \n Now select your Hotel according to your convience: \n 1. Luxeroius hotel \n 2. Non- Luxerious Hotel")
            user =int(input("Enter your choice: "))
            if user == 1:
                print("Luxerious hotel details: \n * Total price 35,000/day \n * Breakfast is complementry \n * Wifi is available \n Attached pool.")
                days = int(input("How many days you want to stay: "))
                people = int(input("Total number of people: "))
                amount = 35000*days * people
                
                print("We also provide rental bikes with 300/day ")
                
                user = input("If you want type 'Y' if not type 'N' :")
                time.sleep(2)
                if user == "y":
                    print(f"Your total amount for {days} days with bike is {amount+300}")
                else:
                    print(f"Your total amount for {days} days is {amount}")
                
            elif user == 2:
                print("Non-Luxerious hotel details: \n * Total price 19,000/day \n ")
                days = int(input("How many days you want to stay: "))
                people = int(input("Total number of people: "))
                amount = 19000*days * people
                b_amount = 300
                print("We also provide rental bikes with 300/day ")
                
                user = input("If you want type 'Y' if not type 'N' :")
                time.sleep(2)
                if user == "y":
                    print(f"Your total amount for {days} days with bike is {amount+300}")
                else:
                    print(f"Your total amount for {days} days is {amount}")
                
            else:
                print("Please choose valid option and try again")
                
        elif user == 4:
            print("Wow... You have chosen Texas \n Now select your Hotel according to your convience: \n 1. Luxeroius hotel \n 2. Non- Luxerious Hotel")
            user =int(input("Enter your choice: "))
            if user == 1:
                print("Luxerious hotel details: \n * Total price 28,000/day \n * Breakfast is complementry \n * Wifi is available \n Attached pool.")
                days = int(input("How many days you want to stay: "))
                people = int(input("Total number of people: "))
                amount = 18000*days * people
                
                print("We also provide rental bikes with 300/day ")
                
                user = input("If you want type 'Y' if not type 'N' :")
                time.sleep(2)
                if user == "y":
                    print(f"Your total amount for {days} days with bike is {amount+300}")
                else:
                    print(f"Your total amount for {days} days is {amount}")
                
            elif user == 2:
                print("Non-Luxerious hotel details: \n * Total price 15,000/day \n ")
                days = int(input("How many days you want to stay: "))
                people = int(input("Total number of people: "))
                amount = 5000*days * people
                
                print("We also provide rental bikes with 300/day ")
                
                user = input("If you want type 'Y' if not type 'N' :")
                time.sleep(2)
                if user == "y":
                    print(f"Your total amount for {days} days with bike is {amount+300}")
                else:
                    print(f"Your total amount for {days} days is {amount}")
                
            else:
                print("Please choose valid option and try again")
        
        else:
            print("Kindly choose valid option and try again.")
else:
    print("Kindly choose valid option and try again.")