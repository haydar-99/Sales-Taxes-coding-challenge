class Item:
  def __init__(self, amount , imported, name, price):
    self.name:str = name
    self.amount:int = amount
    self.name:str = name
    # if(imported):
    #     self.imported = "imported" 
    # else:
    #      self.imported = ""
    self.imported:bool = imported
    ##imported? this.imported="imported": this.imported="";
    self.price:float = self.amount * price
    self.exempt = False

  def DescripeItem(self):
            print(f"{self.amount} {self.imported} {self.name} at {self.price}")
    
  def get_Name(self):
      return self.name if self.imported == False else f"imported {self.name}"
      
        


class medecins(Item):
    def __init__(self, amount, imported, name, price):
        super().__init__(amount, imported, name, price)
        self.exempt = True
    
        
class food(Item):
    def __init__(self, amount, imported, name, price):
        super().__init__(amount, imported, name, price)
        self.exempt = True
    

class books(Item):
    def __init__(self, amount, imported, name, price):
        super().__init__(amount, imported, name, price)
        self.exempt = True
    