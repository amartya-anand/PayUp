event = input("What was the event? ")
cost = float(input("How much did it cost? "))
service_charge = int(
    input("What was the service charge on the bill? ").strip("%"))
group_size = int(input("How many people were there in total? "))
# grand_total = 330
# total_per_person = 110


service_charge_total = cost * service_charge / 100

grand_total = cost + service_charge_total

total_per_person = grand_total / group_size

print("Welcome to the PayUp!")
print()
print(f"Here's the breakdown for dinner at Fantastic Pizza")
print(f"Cost of the event is:{cost: .2f}")
print(f"Service charge of the event is: {service_charge_total}")
print(f"For a group size of : {group_size}")
print(f"Grand total of the event : {grand_total: .2f}")
print(f"The cost per person is: {total_per_person: .2f}")
