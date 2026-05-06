# calculate selling price after discount

# for taking input 
mrp = float(input("Enter MRP: "))
discount = float(input("Enter discount percentage: "))

#  for Calculating discount amount
discount_amount = (mrp * discount) / 100

# Calculate final price
selling_price = mrp - discount_amount

# Display result
print("Discount Amount:", discount_amount)
print("Selling Price:", selling_price)



#output
#Enter MRP: 5000
#Enter discount percentage: 50
#Discount Amount: 2500.0
#Selling Price: 2500.0