prices = [100, 50, 200]
quantities = [2, 5, 1]

discount = 10
tax = 5

subtotal = 0

for i in range(len(prices)):
    subtotal += prices[i] * quantities[i]

discount_amount = subtotal * discount / 100
amount = subtotal - discount_amount

tax_amount = amount * tax / 100

total = amount + tax_amount

print("Subtotal:", subtotal)
print("Discount:", discount_amount)
print("Tax:", tax_amount)
print("Total Cost:", total)
