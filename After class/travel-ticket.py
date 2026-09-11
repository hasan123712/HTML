# ================================
# MY TRAVEL TICKET COUNTER
# ================================
 
# PART 1 - TYPES OF DATA
 
passenger_name = "Bob"        # str - text
destination = "Connecticut"             # str - text
ticket_price = 950.5           # float - decimal number
number_of_tickets = 3           # int - whole number
is_available = True             # bool - True or False
 
print("Passenger Name:", passenger_name)
print("Destination:", destination)
print("Ticket Price: $", ticket_price)
print("Number of Tickets:", number_of_tickets)
print("Tickets Available?", is_available)
 
print(type(passenger_name))
print(type(destination))
print(type(ticket_price))
print(type(number_of_tickets))
print(type(is_available))
 
#  - ARITHMETIC OPERATORS
 
total_cost = ticket_price * number_of_tickets
discount = 250
final_cost = total_cost - discount
 
print("\nTotal Cost: $", total_cost)
print("Discount: $", discount)
print("Final Cost: $", final_cost)
 
print("Double Ticket Price: $", ticket_price * 3)
print("Ticket Price After $200 Increase: $", ticket_price + 200)
print("Half Ticket Price: $", ticket_price / 2)
 
# COMPARISON OPERATORS
 
print("\nIs ticket price under $50,000?", ticket_price < 1650)
print("Are more than 7 tickets booked?", number_of_tickets > 3)
print("Is destination Connecticut?", destination == "Connecticut")
print("Is final cost more than $60,000?", final_cost > 3000)
 
# STRING OPERATIONS
 
travel_message = passenger_name + " is travelling to " + destination + "."
print("\nTravel Message:", travel_message)
 
print("Destination in uppercase:", destination.upper())
print("Passenger name in lowercase:", passenger_name.lower())
print("First letter of destination:", destination[0])
print("Length of passenger name:", len(passenger_name))
 
# PART 5 - SWAPPING VALUES
 
morning_ticket_price = 1000
evening_ticket_price = 1650
 
print("\nBefore Swapping:")
print("Morning Ticket Price: $", morning_ticket_price)
print("Evening Ticket Price: $", evening_ticket_price)
 
morning_ticket_price, evening_ticket_price = evening_ticket_price, morning_ticket_price
 
print("\nAfter Swapping:")
print("Morning Ticket Price: $", morning_ticket_price)
print("Evening Ticket Price: $", evening_ticket_price)
 
# FINAL SUMMARY
 
print("\n================================")
print("TICKET SUMMARY")
print("================================")
print("Passenger:", passenger_name)
print("Destination:", destination)
print("Tickets Booked:", number_of_tickets)
print("Final Amount to Pay: $", final_cost)
print("Booking Confirmed?", is_available)
