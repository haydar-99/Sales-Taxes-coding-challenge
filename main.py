from http.client import SWITCHING_PROTOCOLS


from models.tax_calc import reciept
from models.items import Item, food, medecins,books
 
list1= [ 
           books(1,  False, "book",12.49),  
          Item(1 ,False,"music CD" , 14.99),
          food(1 ,False, "chocolate bar", 0.85)
               ]
   
list2 =[
   food(1,  True ,"box of chocolates",   10.00),
   Item(1 ,True, "bottle of perfume ",  47.50)
       ]
list3=[ 
   Item (1 ,True, "bottle of perfume" , 27.99),
   Item (1,False, "bottle of perfume" , 18.99),
   medecins(1, False, "packet of headache pills", 9.75),
   food(1 ,True,"box of  chocolates" , 11.25)
       ]
basket = []
while(True):
    # App Intro
    print("Welcome to Itemis shop")
    print("The shop is big and conians diffrent kind of goods.")
    print("1- To display the former baskets please type 1 ")
    print("2- To buy new goods please type 2 ")
    print("3- list length ")
    user_input= input("please enter your choice ")
    
    # take in the choice of the user
    if( int(user_input) ==1):
        print("write reciept for basket 1, 2 or 3?")
        user_input = input("please enter your choice")
        if(int(user_input)==1):
            reciept(list1)
        elif(int(user_input) ==2):
            reciept(list2)
        elif(int(user_input) ==3):
            reciept(list3)
        else:
            print("invailed input ")

    if( int(user_input) ==2):
        return_to_menu = False
        while(return_to_menu ==False):
        
            imported = False
            print("What do you wish to buy?")
            print("1- Books \n2- Medecins \n3- Food \n4- Other Items ")
            print("- Would you like to to checkout and get the reciept? Please type 5 in such case \n- Would you go back to main menu? please type 6")
            
            user_input = input("please enter your wished category ")
            if(int(user_input) == 1):
                amount = int(input("Please enter the amount of the product ")) 
                name = input("Please enter the name of the product ")
                price= float(input("Please enter the price of the product "))
                print("if the item is imported please type 1 otherwise 2")
                input_imported= input("")
                if(int(input_imported) == 1):
                    imported = True
                else:
                    imported = False
                
                basket.append(books(amount,imported,name,price))
                
                print("\n")
                
            elif(int(user_input) == 2):
                amount = int(input("Please enter the amount of the product ")) 
                name = input("Please enter the name of the product ")
                price= float(input("Please enter the price of the product "))
                print("if the item is imported please type 1 otherwise 2")
                input_imported= input("")
                if(int(input_imported) == 1):
                    imported = True
                else:
                    imported = False
                
                basket.append(medecins(amount,imported,name,price))
                print("\n")
            
            elif(int(user_input) == 3):
                amount = int(input("Please enter the amount of the product ")) 
                name = input("Please enter the name of the product ")
                price= float(input("Please enter the price of the product "))
                print("if the item is imported please type 1 otherwise 2")
                input_imported= input("")
                if(int(input_imported) == 1):
                    imported = True
                else:
                    imported = False
                
                basket.append(food(amount,imported,name,price))
                print("\n")
            
            elif(int(user_input) == 4):
                amount = int(input("Please enter the amount of the product ")) 
                name = input("Please enter the name of the product ")
                price= float(input("Please enter the price of the product "))
                print("if the item is imported please type 1 otherwise 2")
                input_imported= input("")
                if(int(input_imported) == 1):
                    imported = True
                else:
                    imported = False
                
                basket.append(Item(amount,imported,name,price))
                print("\n")

            elif(int(user_input) == 5):
                reciept(basket)
                
            elif(int(user_input) == 6):
                return_to_menu = True
                
   
    elif(int(user_input) == 3):
        print(len(basket))