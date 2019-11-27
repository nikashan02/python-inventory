def mainMenu(): #Give user options to select from and redirects to other functions based on what is specified
    print("Welcome to the INVENTORY PROGRAM")
    print("")

    while True: #While loop keeps whole program in loop until option 8 is selected which breaks the loop
        print("Please choose from one of the options below:")
        print("")
        print("1. List current inventory")
        print("2. List/edit product detail ")
        print("3. Add new product ")
        print("4. Remove product ")
        print("5. Search")
        print("6. Receive product into stock ")
        print("7. Sale of product")
        print("8. Quit")
        print("")

        while True: #Error checks input for option selected
            try:
                option = int(input("What is your option: "))
                if option > 8 or option < 1:
                    a = 2/0
                break
            except:
                invalidEntry()
        
        if option == 1: #Runs listInv function if option 1 is selected
            print("")
            listInv()
            print("")
        
        elif option == 2: #Runs listInv and gives options for what the user can change
            print("")
            listInv()
            print("")
            productCode = getCode() #Gets product of the product the user wants to change

            print("")
            print("Would you like to:")
            print("")
            print("1. Change product name")
            print("2. Change quantity")
            print("3. Change total received")
            print("4. Change total sales")
            print("5. Quit this menu")
            print("")

            while True: #Error checks input
                try:
                    option2 = int(input("What is your option: "))
                    if option2 > 5 or option2 < 1:
                        a = 2/0
                    break
                except:
                    invalidEntry()
            
            #Runs editProduct with specified parameter for what the user wants to change
            if option2 == 1:            
                editProduct(1, productCode)
            
            elif option2 == 2:
                editProduct(2, productCode)
            
            elif option2 == 3:
                editProduct(3, productCode)
            
            elif option2 == 4:
                editProduct(4, productCode)
            
            else: #Prints blank line if user wants to exit out of the menu
                print("")
            
            if option2 == 1 or option2 == 2 or option2 == 3 or option2 == 4:
                print("")
                print("Inventory successfully updated")
                print("")
        
        elif option == 3: #Runs addProduct function if option 3 is selected
            addProduct()
            print("Inventory successfully updated")
            print("")
        
        elif option == 4: #Runs removeProduct function if option 4 is selected
            removeProduct()
        
        elif option == 5: #Runs search function if option 5 is selected
            search()
        
        elif option == 6: #Runs receive function if option 6 is selected
            receive()
        
        elif option == 7: #Runs sold function if option 7 is selected
            sold()

        else: #Breaks while loop and exits program if option 8 is selected
            print("")
            print("Thank you for using the INVENTORY PROGRAM")
            break

def invalidEntry(): #Function to print if an entry is invalid
    print("")
    print("INVALID ENTRY")
    print("")

def listInv(): #Prints inventory with a table format using the currentInv list
    longest = ""
    count = 0
    for item in currentInv: #Finds longest item in list
        if len(str(item)) > len(str(longest)):
            longest = item

    print("Code".ljust(5), "Name".ljust(len(longest)+1), "Qty".ljust(6), "Received".ljust(11)\
          , "Sold".ljust(10))
    print("")

    for i in range (len(currentInv)//5): #Specifies number of spaces from pervious column and prints
        print(str(currentInv[count]).ljust(5), str(currentInv[count+1]).ljust(len(longest)+1), \
              str(currentInv[count+2]).ljust(6), str(currentInv[count+3]).ljust(11), \
              str(currentInv[count+4]).ljust(10))
        count += 5

    print("")

def getCode(): #Gets input for product code
    while True: #Error checks input to make sure entered product code is valid and is in the list
            try:
                index = int(input("Enter the product code: "))
                if index not in currentInv[0::5]:
                    a = 2/0
                break
            except:
                invalidEntry()
    
    return index

def editProduct(change, code): #Passes in what the user wants to change and product code and gets user input
    count = 0
    if change == 1: #Changes product name with user input
        while True: #Error checks user input
            try:
                value = input("Enter a new product name: ")
                if value == "":
                    a = 2/0
                break
            except:
                invalidEntry()

        for index in currentInv[0::5]: #Finds product code in list and changes value
            if index == code:
                currentInv[count + 1] = value
                break
            count += 5

    elif change == 2: #Changes quantity with user input
        while True: #Error checks user input
            try:
                value = int(input("Enter the new quantity: "))
                if value < 0:
                    a = 2 / 0
                break
            except:
                invalidEntry()
    
        for index in currentInv[0::5]: #Finds product code in list and changes value
            if index == code:
                currentInv[count + 2] = value
                break
            count += 5

    elif change == 3: #Changes total recieved with user input
        while True: #Error checks user input
            try:
                value = int(input("Enter the new total received: "))
                if value < 0:
                    a = 2 / 0
                break
            except:
                invalidEntry()

        for index in currentInv[0::5]: #Finds product code in list and changes value
            if index == code:
                currentInv[count + 3] = value
                break
            count += 5

    elif change == 4: #Changes total sold with user input
        while True: #Error checks user input
            try:
                value = int(input("Enter the new total sold: "))
                if value < 0:
                    a = 2 / 0
                break
            except:
                invalidEntry()

        for index in currentInv[0::5]: #Finds product code in list and changes value
            if index == code:
                currentInv[count + 4] = value
                break
            count += 5

def addProduct(): #Adds a product using user input to the list, thus adding it to the inventory
    newCode = currentInv[len(currentInv) - 5] + 1 #Generates new product code for the new product
    print("")
    print("The product code for this product will be", newCode)
    print("")

    while True: #Error checks user input for product name, quantity, total received and total sold
        try:
            newName = input("Enter the new product name: ")
            if newName == "" or newName in currentInv:
                a = 2/0
            newQty = int(input("Enter the new quantity: "))
            if newQty < 0:
                a = 2/0
            newReceived = int(input("Enter the total received: "))
            if newReceived < 0:
                a = 2/0
            newSold = int(input("Enter the total sold: "))
            break
        except:
            invalidEntry()

    print("")
    #Appends values from user input into list
    currentInv.append(newCode)
    currentInv.append(newName)
    currentInv.append(newQty)
    currentInv.append(newReceived)
    currentInv.append(newSold)

def removeProduct(): #Removes product specified from user input from list
    print("")
    listInv() #Lists current inventory
    print("")

    while True: #Error checks user input for product and checks if user is sure that they would like to remove the product
        try:
            code = getCode()
            confirm = input("Are you sure you would like to remove the product? (y/n): ")
            if confirm != "y":
                if confirm != "n":
                    a = 2/0
            break
        except:
            invalidEntry()

    if confirm == "y": #Deletes product and next 4 elements in list (product name, quantity, total received and total sold)
        print("")
        count = 0
        for index in currentInv[0::5]:
            if index == code:
                for x in range (5):
                    del (currentInv[count])
                break
            count += 5

        print("Inventory successfully updated")
        print("")
    else: #Prints if user selects that they would not like to remove the product
        print("")
        print("Aborted")
        print("")

def search(): #Searches for search string specified from user input in list
    searchEntry = input("Enter a search string: ")
    while searchEntry == "": #Error checks search string
        invalidEntry()
        searchEntry = input("Enter a search string: ")
    print("")

    finds = 0
    findList = []
    count = 0
    newCount = 0
    for item in currentInv: #Searches through list and looks for search entry
        count += 1
        if str(item) == searchEntry: #Excecutes following code if search entry is found in list
            finds += 1
            mod = count % 5
            for x in range ((-1*mod), (-1*mod + 5)): #Appends values for each product matching search string to list
                    findList.append(currentInv[count+x])

    if finds > 0: #Prints number of hits
        print("")
        print("There were", finds, "hits:")
        print("")
        longest = ""
        for item in currentInv:
            if len(str(item)) > len(str(longest)):
                longest = item

        print("Code".ljust(5), "Name".ljust(len(longest) + 1), "Qty".ljust(6), "Received".ljust(11) \
              , "Sold".ljust(10))
        print("")
        #Prints the products found including the search string
        for item in findList[0::5]:
            print(str(item).ljust(5), str(findList[newCount + 1]).ljust(len(longest) + 1), \
                  str(findList[newCount + 2]).ljust(6),
                  str(findList[newCount + 3]).ljust(11), \
                  str(findList[newCount + 4]).ljust(10))
            newCount += 5
    else:
        print("")
        print("No results found")
    print("")

def receive(): #Increases total recieved value for specified product for specified amount from user input
    print("")
    listInv() #Prints current inventory
    print("")
    while True: #Error checks user inputted product code and amount the user wants to increase the total received by
        try:
            code = int(input("Enter product code: "))
            if code not in currentInv[0::5]:
                a = 2/0
            received = int(input("Enter the amount of stock received: "))
            if received < 0:
                a = 2/0
            break
        except:
            invalidEntry()

    count = 0
    for index in currentInv[0::5]: #Finds the specified product code and then goes to the 3 and 4 items for the product and increases them
        if index == code:
            currentInv[count + 2] += received
            currentInv[count + 3] += received
            break
        count += 5
    print(received, "of product received")
    print("")

def sold(): #Increases total sold value for specified product for specified amount from user input
    print("")
    listInv() #Prints current inventory
    print("")
    initialCount = 0
    while True: #Gets and error checks user input for product code and total sold
        try:
            code = int(input("Enter product code: "))                    
            if code not in currentInv[0::5]:
                a = 2 / 0
            sales = int(input("Enter the amount of stock sold: "))
            for index in currentInv[0::5]:
                if index == code:
                    if sales < 0 or currentInv[initialCount]-sales < 0:
                        a = 2 / 0
                initialCount += 5
            break
        except:
            invalidEntry()
    count = 0
    for index in currentInv[0::5]: #Decreases quantity by amount sold and increases total sold by amount specified
        if index == code:
            currentInv[count + 2] -= sales
            currentInv[count + 4] += sales
            break
        count += 5

    print(sales, "of product sold")
    print("")

# MAIN PROGRAM

#List with starting inventory
currentInv = [1, "apple", 400, 1650, 1250, 2, "toothbrush", 143, 450, 307, 3, "t-Shirt", 37, 100, 63, \
              4, "pen", 41, 200, 159, 5, "eraser", 39, 100, 61, 6, "USB-C charger", 91, 300, 209, \
              7, "keyboard", 8, 25, 17, 8, "monitor", 44, 55, 11, 9, "orange", 300, 1000, 700, \
              10, "car poster", 12, 30, 18]

mainMenu() #Runs main menu function which runs whole program