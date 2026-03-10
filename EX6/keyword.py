items = []
keyword = "STOP"
print(f"Enter elements (type '{keyword}' to finish):")
while True:
    user_input = input("Enter element: ")
    if user_input.upper() == keyword:
        break
    items.append(user_input)
result_tuple = tuple(items)
print("\nFinal Tuple:", result_tuple)
