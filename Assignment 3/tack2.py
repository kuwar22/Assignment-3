from task1 import customer_booking
def ferry_service_total():
    total_price = 0
    print("\nservice item names and cost :")
    while True:
        item = input("service item name : ")
        if item.lower() == 'finish':
            break
        cost = input(f"cost for item{item}: $")
        if not cost.isdigit():
            print("invalid number for the cost.")
            continue
        
        cost = float(cost)  
        total_price += cost
    
    print(f"Total price: ${total_price:}")
ferry_service_total()