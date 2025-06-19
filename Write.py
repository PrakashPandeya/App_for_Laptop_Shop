from datetime import date
from Read import sellingStock_read

def bill(name,contact,current_address,orderFromCustomer,folder):
    today = date.today()
    billName =f"{name}_{today}.txt"
    billPath =f"{folder}/{billName}"
    totalAmount = 0
    ShippingCost = 0
    GrandtotalAmount = 0

    ShippingCost = input("Do you wish to get your laptop shipped to you? (Yes/No)")
    if ShippingCost=="Yes":
        GrandtotalAmount += 100
    else:
        print("\n")

    with open(billPath, "w") as p:
        p.write("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
        p.write("\t \t \t \t \t \t SiCaRiO Electronics  \t \t \t \n ")
        p.write("\t \t \t \t \t \t  Ghorahi,Dang \n ")
        p.write("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n\n")
        p.write("Bill Generation \n")
        p.write("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
        p.write(f"Name: {name}\n")
        p.write(f"Phone Number: {contact}\n")
        p.write(f"Address: {current_address}\n")
        p.write("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
        p.write(" LaptopBrandName   \tQuantity      \tUnit Cost($)    \tTotal Cost($) \n ")
        for order in orderFromCustomer:
            LaptopBrandName = order[0]
            Quantity = order[1]
            UnitCost = order[2]
            TotalCost = order[3]
            totalAmount += TotalCost

            p.write("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* \n")
            p.write(f"{LaptopBrandName} \t\t{Quantity} \t\t{UnitCost} \t\t{TotalCost} \n")
        p.write("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
        p.write(f"Grand Total($) = {totalAmount}\n")
        p.write("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
        p.write(f"Shipping cost($): {ShippingCost} \n")
        p.write(f"Cost without VAT($):{totalAmount}\n")
        p.write("VAT amount($): " + str(round((13 * totalAmount) / 100, 2))+"\n")
        p.write("Cost with VAT($):"+ str(round(totalAmount+(13*totalAmount)/100,2))+"\n")
        p.write("Grand Total($) : " + str(round(GrandtotalAmount + totalAmount + ((13 * totalAmount) / 100), 2)) + "\n\n")
        p.write(f"Thank you dear {name} for buying laptops from us. Dear {name}, Do visit us again!!\n")
        
def sellingStock_write(validlaptopID,decrement):
    laptop_dictionary = sellingStock_read()
    with open("SellingStock.txt", "w") as X:
        laptop_dictionary[validlaptopID][3] = decrement
        for key, value in laptop_dictionary.items():
            if key == validlaptopID:
                value[3] = decrement
            X.write(",".join(str(i) for i in value))
            X.write("\n")

def updatedsellingStock_write(changesinStock):
    laptop_dictionary = sellingStock_read()
    z = len(laptop_dictionary)+1
    for i in changesinStock:
        key = str(z)
        laptop_dictionary[key] = list(i)
        z +=1
        with open("SellingStock.txt", "w") as Y:
            for key, value in laptop_dictionary.items():
                Y.write(",".join(str(i) for i in value))
                Y.write("\n")


