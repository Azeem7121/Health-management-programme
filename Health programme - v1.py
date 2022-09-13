"""Health management system: In this exersice you have to make programme using file IO and create file for usernames
1 -Azeem khan, 2 -Amaanullah, 3 -Saad rizvi and ask user to {enter data or retrieve data} according to his name and
aad entry to (food and exersice) file as per user and similarly retrieve user data with datetime entry in []
automatically and enter data or retrieve data line wise """

"!!! Health management system !!!"

import datetime


def getdate():
    timestamp = datetime.datetime.now()
    return timestamp


d = str(getdate())
try:
    while 1:
        print()
        print("""Please select your option given below
                    1 - Enter data
                    2 - Retrieve data
                    3 - Quit
                    """)
        first_input = int(input(":- "))
        if first_input == 1:
            print("""Please select your name
                                1 - Azeem khan
                                2 - Amaanullah
                                3 - Saad rizvi
                                """)
            second_input = int(input(":- "))
            if second_input == 1:
                print("""Hello! Mr.Azeem khan
                    Sir please choose what you want to access:
                    1 - Food
                    2 - Exersice
                    """)
                third_input = int(input(":- "))
                if third_input == 1:
                    print("Mr.khan! please enter your data here:")
                    with open("azeemfood.txt", "a") as f:
                        f.write('[' + d + '] ')
                        f.write(input(":- ")+'\n')
                        print("Successfully Entered")
                elif third_input == 2:
                    print("Mr.khan! please enter your data here:")
                    with open("azeemexs.txt", "a") as f:
                        f.write('[' + d + '] ')
                        f.write(input(":- ") + '\n')
                        print("Successfully Entered")
            elif second_input == 2:
                print("""Hello! Mr.Amaanullah
                    Sir please choose what you want to access:
                    1 - Food
                    2 - Exersice
                    """)
                third_input = int(input(":- "))
                if third_input == 1:
                    print("Mr.Amaanullah! please enter your data here:")
                    with open("Amaanullahfood.txt", "a") as f:
                        f.write('[' + d + '] ')
                        f.write(input(":- ") + '\n')
                        print("Successfully Entered")
                elif third_input == 2:
                    print("Mr.Amaanullah! please enter your data here:")
                    with open("Amaanullahexs.txt", "a") as f:
                        f.write('[' + d + '] ')
                        f.write(input(":- ") + '\n')
                        print("Successfully Entered")
            elif second_input == 3:
                print("""Hello! Mr.Saad rizvi
                    Sir please choose what you want to access:
                    1 - Food
                    2 - Exersice
                    """)
                third_input = int(input(":- "))
                if third_input == 1:
                    print("Mr.Saad rizvi! please enter your data here:")
                    with open("saadfood.txt", "a") as f:
                        f.write('[' + d + '] ')
                        f.write(input(":- ") + '\n')
                        print("Successfully Entered")
                elif third_input == 2:
                    print("Mr.Saad rizvi! please enter your data here:")
                    with open("saadexs.txt", "a") as f:
                        f.write('[' + d + '] ')
                        f.write(input(":- ") + '\n')
                        print("Successfully Entered")
        elif first_input == 2:
            print("""Please select your name
                                            1 - Azeem khan
                                            2 - Amaanullah
                                            3 - Saad rizvi
                                            """)
            second_input = int(input(":- "))
            if second_input == 1:
                print("""Hello! Mr.Azeem khan
                                Sir please choose what you want to access:
                                1 - Food
                                2 - Exersice
                                """)
                third_input = int(input(":- "))
                if third_input == 1:
                    with open("azeemfood.txt") as f:
                        data = f.read()
                        print("Mr.khan! Here is your Food data:\n", data)
                elif third_input == 2:
                    with open("azeemexs.txt") as f:
                        data = f.read()
                        print("Mr.khan! Here is your Exersice data:\n", data)
            elif second_input == 2:
                print("""Hello! Mr.Amaanullah
                                Sir please choose what you want to access:
                                1 - Food
                                2 - Exersice
                                """)
                third_input = int(input(":- "))
                if third_input == 1:
                    with open("Amaanullahfood.txt") as f:
                        data = f.read()
                        print("Mr.Amaanullah! Here is your Food data:\n", data)
                elif third_input == 2:
                    with open("Amaanullahexs.txt") as f:
                        data = f.read()
                        print("Mr.Amaanullah! Here is your Exersice data:\n", data)
            elif second_input == 3:
                print("""Hello! Mr.Saad rizvi
                                Sir please choose what you want to access:
                                1 - Food
                                2 - Exersice
                                """)
                third_input = int(input(":- "))
                if third_input == 1:
                    with open("saadfood.txt") as f:
                        data = f.read()
                        print("Mr.Saad rizvi! Here is your Food data:\n", data)
                elif third_input == 2:
                    with open("saadexs.txt") as f:
                        data = f.read()
                        print("Mr.Saad rizvi! Here is your Exersice data:\n", data)
        elif first_input == 3:
            break
except Exception as e:
    print("Technical Error! Try Again")
    print(e)
