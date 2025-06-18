def sellingStock_read():
    try:
        file = open("SellingStock.txt", "r")
        laptop_dictionary = {}
        laptop_ID = 1
        for line in file:
            line = line.replace("\n", "")
            line.split(",")
            laptop_dictionary.update({laptop_ID: line.split(",")})
            laptop_ID =laptop_ID + 1
        file.close()
        return laptop_dictionary
    except FileNotFoundError:
        print("There isn't any such file present at the moment. ")


# Takes the data from sellingStock and present it  in a tabular form:
def sellingStockTable():
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("S.N. LaptopName\tLaptopBrand\tPrice($)\tQuantity \tProcessor \tGraphics")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    file = open("SellingStock.txt", "r")
    a = 1
    for line in file:
        print(a,"\t"+line.replace(",","\t"))
        a += 1
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    file.close()
