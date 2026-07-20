# Monthly sales data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

sales = [120, 150, 180, 170, 200, 220,
         210, 250, 240, 260, 280, 300]

print("Monthly Sales Data")
print("--------------------------")

for month, sale in zip(months, sales):
    print(month, ":", sale)

print("\nLine Plot Representation")
for month, sale in zip(months, sales):
    print(month, "-" * (sale // 10))

print("\nBar Plot Representation")
for month, sale in zip(months, sales):
    print(f"{month:>3} | {'#' * (sale // 10)} ({sale})")
