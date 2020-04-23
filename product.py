import csv
class product:
    def product_search(self):
        tr3="yes"
        while(tr3=="yes"):
            with open("product.csv", "r") as csv_file:
                data1 = csv.reader(csv_file)

                product_search = input("enter the product to search the quantity:>")

                for i in data1:
                    if (i[1] == product_search):
                        print("product quantity:>", i[3])

            tr3=input("do you want to continue?:>")

    def add_product(self):
            with open("product.csv", "a") as infile:
                data = csv.writer(infile)
                id = input("enter the product id:>")
                name = input('enter the product name:>')
                quantity = int(input("enter the quantity:>"))
                price = int(input("enter the price:>"))
                tup1 = (id, name, quantity, price)
                data.writerow(tup1)
                print("success!!!")

    def update_price(self):
        r = csv.reader(open('product.csv'))
        lines = list(r)
        search_product = input("enter the product to change price:>")
        for i in lines:
            if (i[1] == search_product):
                new_price = int(input("enter the new price:>"))
                i[2] = new_price
                print("success!!")
        writer = csv.writer(open('product.csv', 'w'))
        writer.writerows(lines)

    def update_quantity(self):
        r = csv.reader(open('product.csv'))
        lines = list(r)
        product = input("enter the product to change quantity:>")
        for i in lines:
            if (i[1] == "rice"):
                new_quantity = int(input("enter the new quantity:>"))
                i[3] = new_quantity
                print("success!!")
        writer = csv.writer(open('product.csv', 'w'))
        writer.writerows(lines)


