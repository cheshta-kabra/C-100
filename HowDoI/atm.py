name=input('Enter you name')
age=int(input('Enter your Age'))
card_no=int(input('enter your card_no'))
initalbalance=50000
pin_no=int(input('enter your pin_no'))
withdrawl=int(input('enter the withdrawl amount'))
deposite=int(input('Enter he amount you want to deposite'))
callfunction=input('enter "CB" to ckeck balance , "WM" to withdrawl money and "DM" to deposite money  ')
class Atm(object):
    def __init__(self,name,age,card_no,initalbalance,pin_no,withdrawl,deposite,callfunction):
         self.name=name
         self.age=age
         self.card_no=card_no
         self.initalbalance=initalbalance
         self.pin_no=pin_no
         self.withdrawl=withdrawl
         self.deposite=deposite
         self.callfunction=callfunction
   
    def get_balanceWithdrawlDeposite(self):
        if (self.callfunction == "CB"):
            print('chequing account', self.initalbalance)
        elif (self.callfunction=="WM"):
            self.initalbalance=self.initalbalance-self.withdrawl
            print("Current Balance ", self.initalbalance)
        elif (self.callfunction=="DM"):
            self.initalbalance=self.initalbalance+self.deposite
            print("Current Balance ", self.initalbalance)
        else:
            print("please choose a correct option")
P1=Atm(name,age,card_no,initalbalance,pin_no,withdrawl,deposite,callfunction)
P1.get_balanceWithdrawlDeposite()