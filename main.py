import login
import staff
import product
import billing

def main1():
    print("***LOGIN***")
    a=login.login()
    b=staff.staff()
    c=product.product()
    d=billing.product1()
    while(1):
        print("1.login 2.set password")
        a1=int(input("enter your choice:>"))

        if(a1==1):
            a.login1()
            break
        if(a1==2):
            a.setpassword()
            continue
        else:
           print("try again")

    while(1):
        print("1.staff details 2.product details 3.billing 4.exit")
        a2 = int(input("enter your choice:>"))

        if (a2 == 1):
            b.print_details()
            continue

        if (a2 == 2):
             while(1):
                print("1.product search")
                print("2.add product")
                print("3.update price")
                print("4.update quantity")
                print("5.quit")
                a3 = int(input('enter your choice:>'))
                if (a3 == 1):
                    c.product_search()
                    continue
                if (a3 == 2):
                    c.add_product()
                    continue
                if (a3 == 3):
                    c.update_price()
                    continue
                if (a3 == 4):
                    c.update_quantity()
                    continue
                if(a3== 5):
                    break
                else:
                    
                    continue
        if (a2 == 3):
            while(1):
                print("1.buy product")
                print('2.quit')
                a4 = int(input("enter your choice:>"))
                if (a4 == 1):
                    d.buy_product()
                    continue
                if(a4==2):
                    break
                else:
          
                    continue
        if(a2==4):
            quit()

        else:
            print("wrong choice")


main1()
