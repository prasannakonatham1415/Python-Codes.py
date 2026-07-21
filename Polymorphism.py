# Method Overloading(BUT PYTHON WONT SUPPORT THIS JUST FOR EXAMPLE)
class calc:
    def add(self,n1,n2):
        self.addition=self.n1+self.n2
        print(self.addition)
    def add(self,n1,n2,n3):
        self.addition=self.n1+self.n2+self.n3
        print(self.addition)
c1=calc()
c1.add()
c1.add()

# Method Overriding
class payment:
    def pay(self):
        print("Processing payment")
class creditcardpayment(payment):
    def pay(self):
        super().pay()
        print("Processing Credit Card Payment")
class UPIpayment(creditcardpayment):
    def pay(self):
        super().pay()
        print("Processing UPI Payment")
credit = creditcardpayment()
credit.pay()
UPI = UPIpayment()
UPI.pay() 
