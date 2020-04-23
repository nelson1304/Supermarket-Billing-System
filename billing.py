import csv
class product1:
    def __init__(self,total=0,product1="",quantity=0):
        self.total=total
        self.product1=product1
        self.quantity=quantity
    def buy_product(self):
        tr3="yes"
        quantity=0
        while(tr3=="yes"):
            with open("product.csv","r") as csv_file:
                data=csv.reader(csv_file)

                self.product1=input("enter the product to buy:>")
                for i in data:
                    if  self.product1 in i[1]:
                       if(int(i[3])>0):
                         self.quantity=int(input("enter the quantity:>"))
                         self.total+=int(i[2])*self.quantity

            tr3=input("do you want to continue?")
        else:
            print("total amount is:>", self.total)
            discount=int(input("enter the discount percentage:>"))
            grand_total=(self.total * discount) / 100
            print("The remaining amount is:>",self.total-grand_total)

