total_items = 0

print("Welcome to the grocery store!")

while True:
    item_quantity = int(input("Enter the quantity of the item (enter 0 to finish): "))
    
    if item_quantity == 0:
        break  # Exit the loop if the customer is done
    
    total_items += item_quantity

print(f"\nTotal number of items: {total_items}")

print("Thank you for shopping with us!")
    


