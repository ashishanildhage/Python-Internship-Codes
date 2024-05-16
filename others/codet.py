# a store has different category of products as shown:
item_no=[101,102,103,104]
item_name=["Milk","Cheese","Ghee","Bread"]
price=[42,50,500,40]
stock=[10,20,15,16]
user_input=[item_no,stock]
# calculate total price with float in precision 1
#Quantity left after purchase 
# if qty less than entered stock then display stock not available

inum=int(input("Enter the number : "))
q=int(input("Enter the quantity : "))
try:
    index=item_no.index(inum)
    name,price,cstock=item_name[index],price[index],stock[index]#use cstock instead of stock because current stock is a int not a list so
    if q<=cstock:
        total_price=q*price
        rem_stock=cstock-q        
        stock[index]=rem_stock
        print(f"price = {total_price}\nstock = {rem_stock}\n")
    else:
        print("quantity high")
except Exception as e:
    print(e)
    print("wrong item number")        



