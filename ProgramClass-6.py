class Banking:
    print("Welcome to VAVS-Bank")
    pino = int(input("Enter your pin "))
    mobno = input("Enter your mobile no:")
    def __init__(self):
        self.amt = 10000000
        self.pin = Banking.pino
        self.mob = Banking.mobno

    def Balenq(self):
        print("Avaliable Amount in your account",self.amt,"Rupees")

    def pinno(self,pinc):
        self.pih = pinc
        if self.pih == "YES":
            print("Chnage your Pin")
            mobno = int(input("Enter your old pin:"))
            if mobno == self.pin:
                nepin = int(input("Enter new pin:"))
                self.pin = nepin
                print("Congratulation Your Pin Changed")
            else:
                print("Wrong Pin ")          
                
                  
    def withdraw(self,wtdamt):
        if wtdamt != 00:
            self.wamt = wtdamt
            getmoney = (self.amt)-(self.wamt)
            print("Collect your Cash",self.wamt,"Avaliable Cash",getmoney)


        

Account = Banking()   
Account.Balenq()
pincha = input("Enter YES To Change and NO not to :")
Account.pinno(pincha)
Withdraw = int(input("Enter Amount to withdraw or press 00 to Skip:"))
Account.withdraw(Withdraw)


