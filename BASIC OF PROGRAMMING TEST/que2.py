total_messages = int(input("Enter total messages: "))
if total_messages <= 100:
    status = "Normal"
    active = total_messages
    compressed = 0
else:
    status = "Optimized"
    active = 100
    compressed = total_messages - 100
print(f"Status: {status}, Active: {active}, Compressed: {compressed}")
