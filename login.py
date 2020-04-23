import csv
class login:
    def setpassword(self):
        print("your default username and password is:> " "admin")
        print("do you want to change the username and password?")
        ans=input()
        if(ans=="yes" or ans=="Y"):
            r = csv.reader(open('login.csv'))
            lines = list(r)
            self.username1 = input("enter the username:>")
            self.password1 = input("enter the password:>")
            lines[1][0] = self.username1
            lines[1][1] = self.password1

            writer = csv.writer(open('login.csv', 'w'))
            writer.writerows(lines)

        else:
            exit()

    def login1(self):
        print("enter username and password to continue!!")
        tr="yes"
        while(tr=="yes"):
            username = input("enter username:>")
            password = input("enter password:>")
            r = csv.reader(open('login.csv'))
            lines = list(r)
            if(lines[1][0] == username and lines[1][1] == password):
                 print("welcome")
                 break
            else:
                print('wrong!!! try again')
                tr=input("do you want to try again?")