import sys
import os
sys.path.append("..")
from models.tax_calc import reciept
from models.items import Item, food, medecins,books



class store:
    
    def __init__(self):
        self.shopped_items =[]
        
        # test input 1 from the description of the problem
        self.list1= [ 
           books(1,  False, "book",12.49),  
          Item(1 ,False,"music CD" , 14.99),
          food(1 ,False, "chocolate bar", 0.85)
               ]
        # test input 2 from the description of the problem
        self.list2 =[
        food(1,  True ,"box of chocolates",   10.00),
        Item(1 ,True, "bottle of perfume ",  47.50)
            ]
       
       # test input 3 from the description of the problem
        self.list3=[ 
        Item (1 ,True, "bottle of perfume" , 27.99),
        Item (1,False, "bottle of perfume" , 18.99),
        medecins(1, False, "packet of headache pills", 9.75),
        food(1 ,True,"box of  chocolates" , 11.25)
            ]
        
    
    
        """
        summry:
            cross-platform method to clean the console
        """
    def cls(self):
       
        os.system('cls' if os.name=='nt' else 'clear')
    
    
        
       
    def open_the_store(self):
        """
        summry:
            start the application and controll the flow of the program
        """

        self.store_is_open = True
        while(self.store_is_open):
            # App Intro
            print("**********Welcome to Itemis Store**********")
            print("The Store conians diffrent kind of goods.\n1- To display the former baskets please type 1 \n2- To buy new goods please type 2 \n3- list length \n3- Leave the store ")
            user_input= input("please enter your choice ")
            
            # take in the choice of the user
            if( int(user_input) ==1):
                print("write reciept for basket 1, 2 or 3 ?")
                user_input = input("please enter your choice ")
                if(int(user_input)==1):
                    self.cls()
                    reciept(self.list1)
                elif(int(user_input) ==2):
                    self.cls()
                    reciept(self.list2)
                elif(int(user_input) ==3):
                    self.cls()
                    reciept(self.list3)
                else:
                    print("invailed input ")

            elif( int(user_input) ==2):
                return_to_menu = False
                while(return_to_menu ==False):
                
                    imported = False
                    print("What do you wish to buy?")
                    print("1- Books \n2- Medecins \n3- Food \n4- Other Items ")
                    print("5- Would you like to to checkout and get the reciept? Please type 5 in such case \n6- Would you go back to main menu? please type 6")
                    
                    user_input = input("please enter your wished category ")
                    if(int(user_input) == 1):
                        self.take_user_input(books)
                        
                    elif(int(user_input) == 2):
                        self.take_user_input(medecins)
                    
                    elif(int(user_input) == 3):
                        self.take_user_input(food)
                    
                    elif(int(user_input) == 4):
                        self.take_user_input(Item)

                    elif(int(user_input) == 5):
                        if(len(self.shopped_items)>0):
                            reciept(self.shopped_items)
                        else:
                            print("**************\nYou have not purchased any item yet\n**************")
                        
                    elif(int(user_input) == 6):
                        return_to_menu = True
                        
        
            elif(int(user_input) == 3):
                print(len(self.shopped_items))
            
            elif(int(user_input) == 4):
                self.cls()
                print("thank you for visting the store\nHave a nice day \nBye")
                self.store_is_open = False
            
            else:
                self.cls()
                print("invailed input")

    
    
    
    
    
    def take_user_input(self, input_item):
        """
        summary:
            a method that take the input of the user and create the wished product 

        Args:
            input_item (class): Create The wished class  
        """
        
        self.cls()
        amount = int(input("Please enter the amount of the product ")) 
        name = input("Please enter the name of the product ")
        price= float(input("Please enter the price of the product "))
        print("if the item is imported please type 1 otherwise 2")
        input_imported= input("")
        if(int(input_imported) == 1):
            imported = True
        else:
            imported = False
                        
        self.shopped_items.append(input_item(amount,imported,name,price))
        print("The item is added to the shopping basket")
        print("\n")
    
    
    
    
   