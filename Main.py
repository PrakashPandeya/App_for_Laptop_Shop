from Operations import sellToCustomer
from Operations import purchaseFromManufacture

print("\n")
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print("\t \t \t SiCaRiO Electronics  \t \t \t ")
print("\t \t \t   Ghorahi,Dang \t \t \t ")
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

continue_Loop = True
while continue_Loop == True:
    print("\n")
    print("To explore our services please try the below mentioned options: ")
    print("\n")
    print("1. Press 1 to sale the laptop to the customer")
    print("2. Press 2 to purchase the laptop from the manufacturer")
    print("3. Press 3 to exit without buying")
    print("\n")

    user_Input = int(input("Please enter the above option to continue:"))
    print("\n")

    if user_Input == 1:
        sellToCustomer()
        break
    elif user_Input == 2:
        purchaseFromManufacture()
        break
    elif user_Input == 3:
        continue_Loop = False
        print("Thank you for exploring our electronics,Do visit us more in the future")
        print("\n")
    else:
        print("Please, Choose a correct option to continue")

    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

