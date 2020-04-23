import csv
class staff:
    def __init__(self,salary=0):

         self.salary=salary

    def print_details(self):
        tr1="yes"
        while(tr1=="yes"):
            with open("staff.csv", "r") as csv_file:

                data1 = csv.reader(csv_file)

                staff_name1 = input("enter the staff name to search:>")

                for i in data1:
                    if (i[1] == staff_name1):
                        print("staff id:> ", i[0])
                        print("staff name:> ", i[1])
                        print("staff address:> ", i[2])
                        print("staff mobile number:> ", i[3])
                        print("staff date of birth:> ", i[4])
                        print("staff designation:> ", i[5])
                        if (i[5] == "salesperson"):
                            self.salary = 20000
                        elif (i[5] == "clerk"):
                            self.salary = 30000
                        elif (i[5] == "manager"):
                            self.salary = 35000

                print("staff salary", self.salary)
            tr1=input("do you want to continue?")
