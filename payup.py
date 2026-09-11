event = "Dinner"
cost = 100
service_charge = 10
group_size = 5
grand_total = cost + service_charge
total_per_person = grand_total / group_size


print("Welcome to the PayUp!")
print()
print(f"Here's the breakdown for dinner at Fantastic Pizza")
print(f"Cost of the event is:{cost}")
print(f"Service charge of the event is: {service_charge}")
print(f"For a group size of : {group_size}")
print(f"Grand total of the event : {grand_total}")
print(f"The cost per person is: {total_per_person}")
