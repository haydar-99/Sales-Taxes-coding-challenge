import sys
import unittest
sys.path.append("..")
from models.tax_calc import tax_calculator
from models.items import Item, food, medecins,books
class Unit_tests(unittest.TestCase):
    
    def setUp(self):
        self.list= [ 
                books(1,  False, "book",12.49),  
               Item(1 ,False,"music CD" , 14.99),
               food(1 ,False, "chocolate bar", 0.85)
                    ]
        
        self.list2 =[
                food(1,  True ,"box of chocolates",   10.00),
                Item(1 ,True, "bottle of perfume ",  47.50)
                    ]

        self.list3=[ 
                Item (1 ,True, "bottle of perfume" , 27.99),
                Item (1,False, "bottle of perfume" , 18.99),
                medecins(1, False, "packet of headache pills", 9.75),
                food(1 ,True,"box of  chocolates" , 11.25)
                    ]
    
    # testing the tax calculation, the rounding rule and the new price after the tax 
    def test_calculator(self): 
        #testing tax calculating in case it is exempted 
        price_after_tax, withdrawn_tax = tax_calculator(self.list[0])
        self.assertEqual(price_after_tax,12.49)
        
        #testing tax calculating and rounding up to 0.05 in case it is not exempted 
        price_after_tax, withdrawn_tax = tax_calculator(self.list[1])
        self.assertEqual(price_after_tax,16.49)
        
        #testing tax calculating and rounding up to 0.05 in case it is exempted  but imported
        price_after_tax, withdrawn_tax = tax_calculator(self.list2[0])
        self.assertEqual(price_after_tax,10.50)
        
        #testing tax calculating and rounding up to 0.05 in case it is not exempted but imported
        price_after_tax, withdrawn_tax = tax_calculator(self.list2[1])
        self.assertEqual(price_after_tax,54.65)
        
        
        
        
        
        
  
if __name__ == '__main__':
    unittest.main()