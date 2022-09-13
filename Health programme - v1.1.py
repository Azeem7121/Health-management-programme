"""Health management system: In this exersice you have to make programme using file IO and create file for usernames
1 -Azeem khan, 2 -Amaanullah, 3 -Saad rizvi and ask user to {enter data or retrieve data} according to his name and
aad entry to (food and exersice) file as per user and similarly retrieve user data with datetime entry in []
automatically and enter data or retrieve data line wise """

"!!! Health management system !!!"

import datetime


def getdate():
    timestamp = datetime.datetime.now()
    return timestamp


time = str(getdate())
a = (input("Please Enter Your Name:- ")).lower()
b = a.upper()
with open(a + "food.txt", "a") as f:
    print("...")
with open(a + "exersice.txt", "a") as f1:
    print("User Successfully Entered!")
    print()
try:
    while True:
        print("Welcome! " + b + ' |')
        print()
        print("""What you want to do:
        1 - Enter Your Data
        2 - Retrieve Your Data
        3 - Exit
        """)
        first = int(input())
        if first == 1:
            print("""What you want to Enter:
            1 - Food
            2 - Exersice
            3 - Exit
            """)
            second = int(input())
            if second == 1:
                fdata = input("Please Enter your data here: ")
                with open(a + "food.txt", "a") as f:
                    f.write("[" + time + "] " + fdata + '\n')
                    print("Successfully Submitted!")
                    print()
            elif second == 2:
                fdata = input("Please Enter your data here: ")
                with open(a + "exersice.txt", "a") as f:
                    f.write("[" + time + "] " + fdata + '\n')
                    print("Successfully Submitted!")
                    print()
            elif second == 3:
                break
            else:
                print("Please Enter Valid number!")
        elif first == 2:
            print("""What you want to Retrieve:
                    1 - Food Data
                    2 - Exersice Data
                    3 - Exit
                    """)
            third = int(input())
            if third == 1:
                with open(a + "food.txt") as g:
                    db = g.read()
                    print(db)
                    print("Successfully Retrieved!")
                    print()
            elif third == 2:
                with open(a + "exersice.txt") as g:
                    db = g.read()
                    print(db)
                    print("Successfully Retrieved!")
                    print()
            elif third == 3:
                break
            else:
                print("Please Enter Valid number!")
        elif first == 3:
            break
        else:
            print("Please Enter Valid number!")
except Exception as e:
    print("ERROR!", e, "Please Enter Valid number not letters")
