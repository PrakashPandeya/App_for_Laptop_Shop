from Read import sellingStock_read, sellingStockTable
from Write import bill, updatedsellingStock_write, sellingStock_write


def sellToCustomer():
    """SellToCustomer function enables the owners to sell the laptops to various customers by aking the details from them."""

    folder = "Billings"
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("To continue purchasing please provide the below asked information: ")
    print("\n")
    name = input("Please enter your full name: ")
    contact = input("Please enter your phone number: ")
    current_address = input("Please enter your current address: ")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("\n")

    orderFromCustomer = []
    moreLaptops = True
    while moreLaptops == True:
        laptop_dictionary = sellingStock_read()
        sellingStockTable()  # if morelaptops is true then laptops of sellingStock are dispalyed:
        print("\n")

        # Valid laptop ID provided by the customer  is checked here
        while True:
            try:
                validlaptopID = int(input("Please provide the ID of the laptop you want to buy : "))
                print("\n")
                while validlaptopID not in laptop_dictionary:
                    print("Please use the valid laptop id to order")
                    print("\n")
                    sellingStockTable()

                    validlaptopID = int(input("Please provide the ID of the laptop you want to buy : "))
                    print("\n")
                break
            except ValueError:
                print("Please, put the above appropriate Serial Number(S.N) value to order laptops")

        # IF Valid laptop ID is provided then Valid laptop quantity is checked here:
        while True:
            try:
                orderQuantityByUser = int(input("Please provide the number of quantity of the laptop you want to buy:"))
                print("\n")
                getQuantityOfSelectedLaptop = laptop_dictionary[validlaptopID][3]
                while orderQuantityByUser <= 0 or orderQuantityByUser > int(getQuantityOfSelectedLaptop):
                    print(
                        "OOPs, The quantity of laptop you are looking for is not available in our shop.Please look again in the list")
                    print("\n")
                    orderQuantityByUser = int(
                        input("Please provide the number of quantity of the laptop you want to buy:"))
                break
            except ValueError:
                print("Your order quantity doesn't match to our available quantity")

        # Generating the total price of the laptop by getting name and price of it
        nameOfLaptop = laptop_dictionary[validlaptopID][0]
        priceOfLaptop = int(laptop_dictionary[validlaptopID][2])
        totalCost = orderQuantityByUser * priceOfLaptop

        # The list of order by customer is updated below:
        decrement = int(getQuantityOfSelectedLaptop) - orderQuantityByUser
        sellingStock_write(validlaptopID, decrement)
        orderFromCustomer.append((nameOfLaptop, orderQuantityByUser, priceOfLaptop, totalCost))

        # Confirming whether  the customer need to purchase more laptops or not. If yes continuing the loop:
        additionalLaptops = input("Would you like to purchase more laptops from us?(Yes/No):")
        if additionalLaptops == "Yes":
            moreLaptops = True
        else:
            print(" Thank you <3 \n")
            print("\n")
            break


    # Calling the functions that has been imported and assigning it to the parameter value.
    bill(name,contact,current_address,orderFromCustomer,folder)

    # Thanking the customer after loop ends and conveying the message that bill is  generated.
    print("Thank you for using our system!.")
    print("Your bill is being generated. Please view the respective folder to get your bill <3")


def purchaseFromManufacture():
    """ purchaseFromManufacture function enables the owners to purchase the laptops from manufacturers """

    folder = "Billings"

    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("To continue purchasing please provide the below asked information: ")
    print("\n")
    nameOfShop = input("Please enter your shop name: ")
    contactOfShop = input("Please enter your shop's phone number: ")
    current_addressOfShop = input("Please enter your shop's current address: ")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("\n")

    changesinStock = []
    orderFromCustomer = []
    moreLaptops = True
    while moreLaptops == True:
        nameOfLaptop = input("Please, enter laptop name that you want to purchase:")
        brandOfLaptop = input("Please, enter laptop brand that you want to purchase:")
        priceOfLaptop = int(input("Please, enter the laptop price that you want to purchase:"))
        quantityOfLaptop = int(input("Please, enter the laptop quantity that you want to purchase:"))
        processorOfLaptop = input("Please, enter the laptop processor that you want to purchase:")
        graphicsOfLaptop = input("Please, enter the  laptop graphics that you want to purchase:")

        changesinStock.append((nameOfLaptop,brandOfLaptop,priceOfLaptop,quantityOfLaptop,processorOfLaptop,graphicsOfLaptop))
        updatedsellingStock_write(changesinStock)

        totalCost = quantityOfLaptop * priceOfLaptop

        orderFromCustomer.append((nameOfLaptop,quantityOfLaptop,priceOfLaptop,totalCost))

        additionalLaptops = input("Would you like to purchase more laptops from us?(Yes/No):")
        if additionalLaptops == "Yes":
            moreLaptops = True
            continue
        else:
           print(" Thank you <3 \n")
           break

    #Calling the functions that is been imported and assigning it to the parameter value.
    bill(nameOfShop, contactOfShop, current_addressOfShop, orderFromCustomer, folder)

    #Thanking the customer after loop ends and conveying the message that bill is generated.
    print("Thank you for using our system!.")
    print("Your bill is being generated. Please view the respective folder to get your bill <3")
