# NITU SHARMA,202501100700201,ECE,B
import random
import time
min_limit = float(input("Enter minimum temperature limit: "))
max_limit = float(input("Enter maximum temperature limit: "))
print("\nMonitoring Temperature...\n")
while True:
    temperature = random.uniform(min_limit, max_limit)
    print("Current Temperature:", round(temperature,2))
    if temperature > max_limit:
        print("Alert: Temperature is too high")
    elif temperature < min_limit:
        print("Alert: Temperature is too low")
    else:
        print("Temperature is within acceptable limit")
    print("----------------------------")
    time.sleep(2)