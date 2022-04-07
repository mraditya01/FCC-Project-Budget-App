import itertools
import math as m
class Category():

    def __init__(self, category):
        self.category = category
        self.Total = 0
        self.balance = 0
        self.ledger = {}
        self.n = 0
        self.spend = 0

    def deposit(self, amount1, name1=""):
        self.ledger[self.n] = {'description' : name1, 'amount' : amount1}
        self.balance += self.ledger[self.n]['amount']
        self.n += 1

    def withdraw(self, amount2, name2=""):
        if self.check_funds(amount2) == True:
            self.ledger[self.n] = {'description': name2, 'amount': -amount2}
            self.balance += -amount2
            self.spend += amount2
            self.n += 1
            return True
        else:
            return False

    def transfer(self, amount3, name3):
        if self.check_funds(amount3) == True:
          self.withdraw(amount3, f"Transfer to {name3.category}")
          name3.deposit(amount3, f"Transfer from {self.category}")
          return True
        else:
          return False

    def get_balance(self):
        return self.balance

    def check_funds(self, spend):
        if self.balance - spend >= 0:
            return True
        else:
            return False
    def name(self):
        return f"{self.category}"

    def __str__(self):
        self.stars = int((30-len(self.category))/2) * '*'
        name1 = f"{(self.stars)}{self.category}{(self.stars)}"
        for n in range(len(self.ledger)):
            self.spaces1 = int(30 - len(self.ledger[n]['description'][:23] if len(self.ledger[n]['description']) >= 23 else self.ledger[n]['description'])
                               - (len("{:.2f}".format(self.ledger[n]['amount'])))) * " "
            name1 += f"\n{self.ledger[n]['description'][:23] if len(self.ledger[n]['description']) >= 23 else self.ledger[n]['description']}" \
                     f"{self.spaces1}{self.ledger[n]['amount']:.2f}"
        name1 += f"\nTotal: {self.balance}"
        return name1


def create_spend_chart(categories):
    space=len(categories)*"   "
    dash=len(categories)*"---"
    b=[]
    a=[]
    c=[]
    o=[]
    circle=[]
    #Categories
    for n in range(len(categories)):
        a.append([i for i in categories[n].name()])
    #Percentage
    for n in range(len(categories)):
        b.append(categories[n].spend)
    bsum = sum(b)
    for n in range(len(categories)):
        b[n]=m.floor(b[n]/bsum*10)*10
        o.append(int(b[n]/10))
        circle.append((10-o[n])*' '+(o[n]+1)*'o')
        circle[n]=list(circle[n])
    #Percentage Visualization
    for n in range(100,-10,-10):
        if n==100:
            c.append(f"{n}|")
        elif n==0:
            c.append(f"  {n}|")
        else:
            c.append(f" {n}|")
    j = "Percentage spent by category\n"
    n=0
    for k in range(len(c)):
        j += f"{c[k]} {circle[n][k]}  {circle[n+1][k]}  {circle[n+2][k]}  \n"
    j += f"    -{dash}"
    for i in itertools.zip_longest(*a, fillvalue=" "):
        if any(m != " " for m in i):
            j += f"\n     {'  '.join(i)}  "
    return (f"{j}")
